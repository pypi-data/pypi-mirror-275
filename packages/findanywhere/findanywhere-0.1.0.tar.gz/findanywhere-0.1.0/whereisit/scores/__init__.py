from whereisit.scores.deduction import average_score, create_average_score
from whereisit.types.factory import FactoryMap
from whereisit.types.similarity import DeduceScore

DEDUCTION_FACTORIES: FactoryMap[DeduceScore] = FactoryMap((create_average_score, ))

DEFAULT_DEDUCTION: str = create_average_score.name