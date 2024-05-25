from enum import Enum


class AssetInformationAssetKind(str, Enum):
    INSTANCE = "Instance"
    NOT_APPLICABLE = "NotApplicable"
    TYPE = "Type"

    def __str__(self) -> str:
        return str(self.value)
