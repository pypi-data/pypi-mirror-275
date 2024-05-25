from enum import Enum

class Attrs(Enum):
    """Enum for HTML attributes."""
    CLASS = 'class'


class Tags(Enum):
    """Enum for HTML tags."""
    PARAGRAPH = 'p'
    HR = 'hr'
    TABLE = 'table'