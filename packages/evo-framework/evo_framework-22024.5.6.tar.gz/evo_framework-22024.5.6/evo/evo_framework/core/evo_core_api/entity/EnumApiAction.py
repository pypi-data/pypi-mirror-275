from enum import Enum

class EnumApiAction(Enum):
    NONE = 0
    ERROR = 1
    PROGRESS = 2
    PROGRESS_UPLOAD = 3
    PROGRESS_DOWNLOAD = 4
    PARTIAL = 5
    COMPLETE = 6