from enum import Enum


class PatchSubmodelByIdValueOnlyLevel(str, Enum):
    CORE = "core"
    DEEP = "deep"

    def __str__(self) -> str:
        return str(self.value)
