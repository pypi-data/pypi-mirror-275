from typing import List, Tuple


from preql.core.enums import PurposeLineage
from preql.core.models import Concept, Function, AggregateWrapper, FilterItem
from preql.utility import unique


def resolve_function_parent_concepts(concept: Concept) -> List[Concept]:
    if not isinstance(concept.lineage, (Function, AggregateWrapper)):
        raise ValueError(f"Concept {concept} lineage is not function or aggregate")
    if concept.derivation == PurposeLineage.AGGREGATE:
        if concept.grain:
            return unique(
                concept.lineage.concept_arguments + concept.grain.components_copy,
                "address",
            )
        return concept.lineage.concept_arguments
    # TODO: handle basic lineage chains?

    return unique(concept.lineage.concept_arguments, "address")


def resolve_filter_parent_concepts(concept: Concept) -> Tuple[Concept, List[Concept]]:
    if not isinstance(concept.lineage, FilterItem):
        raise ValueError
    base = [concept.lineage.content]
    base += concept.lineage.where.concept_arguments
    return concept.lineage.content, unique(base, "address")


def concept_to_relevant_joins(concepts: list[Concept]) -> List[Concept]:
    addresses = [x.address for x in concepts]
    sub_props = [
        x.address
        for x in concepts
        if x.keys and all([key.address in addresses for key in x.keys])
    ]
    final = [c for c in concepts if c.address not in sub_props]
    return final
