from enum import Enum


class PutSubmodelElementByPathSubmodelRepoLevel(str, Enum):
    DEEP = "deep"

    def __str__(self) -> str:
        return str(self.value)
