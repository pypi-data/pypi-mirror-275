from typing import Any

from whereisit.adapters.source.text import load_text_source_using
from whereisit.adapters.source.tabular import load_tabular_source_using
from whereisit.ports.source import SourceAdapter
from whereisit.types.factory import FactoryMap

SOURCE_FACTORIES: FactoryMap[SourceAdapter[Any, Any, Any]] = FactoryMap(
    (load_text_source_using, load_tabular_source_using)
)
