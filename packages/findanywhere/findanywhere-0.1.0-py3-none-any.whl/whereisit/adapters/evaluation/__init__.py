from typing import Any

from whereisit.adapters.evaluation.string_distance import evaluate_by_similarity, evaluate_by_similarity_using
from whereisit.ports.evaluation import EvaluationAdapter
from whereisit.types.factory import FactoryMap

EVALUATION_FACTORIES: FactoryMap[EvaluationAdapter[Any]] = FactoryMap((evaluate_by_similarity_using,))
