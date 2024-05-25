from typing import Dict, List

from tonic_textual.classes.common_api_responses.single_detection_result import (
    SingleDetectionResult,
)
from tonic_textual.enums.pii_state import PiiState


def filter_entities_by_config(
    entities: List[SingleDetectionResult],
    generator_config: Dict[str, PiiState],
    generator_default: PiiState,
) -> List[SingleDetectionResult]:
    filtered_entities = []
    for entity in entities:
        if entity["label"] in generator_config:
            if generator_config[entity["label"]] == PiiState.Off:
                continue
        elif generator_default == PiiState.Off:
            continue
        filtered_entities.append(entity)
    return filtered_entities
