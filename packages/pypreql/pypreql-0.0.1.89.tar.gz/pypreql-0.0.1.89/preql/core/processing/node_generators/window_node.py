from typing import List


from preql.core.models import Concept, WindowItem, Environment
from preql.utility import unique
from preql.core.processing.nodes import (
    WindowNode,
    StrategyNode,
)
from preql.core.processing.nodes import MergeNode

from preql.core.processing.nodes import (
    NodeJoin,
)
from preql.core.enums import JoinType
from preql.constants import logger
from preql.core.processing.utility import padding
from preql.core.processing.node_generators.common import concept_to_relevant_joins

LOGGER_PREFIX = "[GEN_WINDOW_NODE]"


def resolve_window_parent_concepts(concept: Concept) -> List[Concept]:
    if not isinstance(concept.lineage, WindowItem):
        raise ValueError
    base = [concept.lineage.content]
    if concept.lineage.over:
        base += concept.lineage.over
    if concept.lineage.order_by:
        for item in concept.lineage.order_by:
            base += [item.expr.output]
    return unique(base, "address")


def gen_window_node(
    concept: Concept,
    local_optional: list[Concept],
    environment: Environment,
    g,
    depth: int,
    source_concepts,
) -> WindowNode | MergeNode | None:
    parent_concepts = resolve_window_parent_concepts(concept)
    window_node = WindowNode(
        input_concepts=parent_concepts,
        output_concepts=[concept] + parent_concepts,
        environment=environment,
        g=g,
        parents=[
            source_concepts(
                mandatory_list=parent_concepts,
                environment=environment,
                g=g,
                depth=depth + 1,
            )
        ],
    )
    parents: list[StrategyNode] = [window_node]
    # if we have unsatisfied local optional, we need to enrich the window node
    if local_optional and not all(
        [
            x.address in [y.address for y in window_node.output_concepts]
            for x in local_optional
        ]
    ):
        enrich_node = source_concepts(  # this fetches the parent + join keys
            # to then connect to the rest of the query
            mandatory_list=parent_concepts + local_optional,
            environment=environment,
            g=g,
            depth=depth + 1,
        )
        if not enrich_node:
            logger.info(
                f"{padding(depth)}{LOGGER_PREFIX} Cannot generate window enrichment node for {concept} with optional {local_optional}"
            )
            return None
        parents.append(enrich_node)
    return MergeNode(
        input_concepts=[concept] + parent_concepts + local_optional,
        output_concepts=[concept] + parent_concepts + local_optional,
        environment=environment,
        g=g,
        parents=parents,
        node_joins=(
            [
                NodeJoin(
                    left_node=parents[-1],
                    right_node=parents[0],
                    concepts=concept_to_relevant_joins(parent_concepts),
                    filter_to_mutual=False,
                    join_type=JoinType.LEFT_OUTER,
                )
            ]
            if len(parents) == 2
            else []
        ),
    )
