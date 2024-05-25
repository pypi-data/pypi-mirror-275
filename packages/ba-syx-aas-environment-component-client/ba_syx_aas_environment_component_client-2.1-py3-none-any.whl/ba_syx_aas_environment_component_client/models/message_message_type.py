from enum import Enum


class MessageMessageType(str, Enum):
    ERROR = "ERROR"
    EXCEPTION = "EXCEPTION"
    INFO = "INFO"
    WARNING = "WARNING"

    def __str__(self) -> str:
        return str(self.value)
