# we are creating "entity" ie defining of return type of variables in dataingestion config

from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:      # this is not a normal class its dataclass
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path