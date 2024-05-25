from typing import (
    Any,
    Dict,
    List,
    Optional,
    Union
)

from pydantic import BaseModel

class AddedSection(BaseModel):
    """
    Representation of a sub-section that has been added.

    Args:
        section (Dict[str, Any]): A dictionary represenation
            of a section from Form D.
    """
    section: Dict[str, Any]
    

class RemovedSection(BaseModel):
    """
    Representation of a sub-section that has been removed.

    Args:
        section (Dict[str, Any]): A dictionary represenation
            of a section from Form D.
    """
    section: Dict[str, Any]


class Difference(BaseModel):
    """
    Representation of a difference between a previous and
    current version of the same section from Form D.

    Args:
        field_name (str): The name of the field.
        previous_value (str | int | bool | None): The value
            appearing in the previous section.
        current_value (str | int | bool | None): The value
            apearing in the current section.
    """
    field_name: str
    previous_value: Optional[Union[str, int, bool]]
    current_value: Optional[Union[str, int, bool]]


class SectionDifference(BaseModel):
    """
    A representation of all differences between a
    previous and current version of the same section.

    Args:
        section (Dict[str, Any]): A dictionary represenation
            of a section from Form D.
        differences (List[Difference]): A list of Difference
            objects each representing a difference between a
            previous and current version of the same section.
    """
    section: Dict[str, Any]
    differences: List[Difference]