from typing import IO
from pathlib import Path


class DataOpener:

    def __init__(self, filename: str):
        self.filename = filename

    def __enter__(self) -> IO:
        self.file_obj = open(Path(__file__).parent.resolve().joinpath('data', self.filename))
        return self.file_obj

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file_obj:
            self.file_obj.close()