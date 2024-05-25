from abc import ABC, abstractmethod
from typing import Deque, List, Union
from collections import deque

from sec_form_d.parsing.schema_extraction import SchemaExtraction
from sec_form_d.constants import X_MARK
from sec_form_d.types.field import (
    FormCheckBox,
    FormCheckBoxMultiple,
    FormField
)

FormData = Union[FormCheckBox, FormCheckBoxMultiple, FormField]

class BaseParsing(ABC):
    """
    Abstract class for all field parser classes.

    Args:
        schema (SchemaExtraction): An object containing all schema
            related variables after decomposition.
    """
    def __init__(
        self,
        schema: SchemaExtraction
    ):
        self.schema = schema
        self.form_fields: Deque[FormData] = deque([])

        # Schema element breakdown
        self.fields = schema.fields
        self.boxes_single = schema.boxes_single
        self.boxes_multiple = schema.boxes_multiple

        # Schema field names breakdown
        self.box_names = schema.box_names
        self.box_field_names = schema.box_field_names
        self.all_box_field_names = schema.all_box_field_names
        self.all_field_names = schema.all_field_names

    @abstractmethod
    def process(self, section_text: List[str]) -> List[FormData]:
        """Abstract method to run processing for specific field type."""
        pass

    def append_to_fields(self, field: FormData) -> None:
        """
        Append a single field dataclass to queue.
        
        Args:
            field (FormData): A field dataclass with parsed data
                from section.
        """
        self.form_fields.append(field)

    def extend_fields(self, fields: List[FormData]) -> None:
        """
        Append multiple field dataclasses to queue.
        
        Args:
            field (List[FormData]): A list of field dataclasses with
                parsed data from section.
        """
        self.form_fields.extend(fields)

    def flush_fields(self) -> List[FormData]:
        """
        Flush all field dataclasses from queue.
        
        Returns:
            field (List[FormData]): A list of field dataclasses with
                parsed data from section.
        """
        fields = []
        while self.form_fields:
            field = self.form_fields.popleft()
            fields.append(field)
        return fields

    def check_box_status(self, idx: int, field_items: List[str]) -> bool:
        """
        Extracts the status of the checkbox (whether it has been
        checked or not). Then standardizes to be a boolean (True if
        checked and False if not) and returns the status.

        Args:
            idx (int): The index of the checkbox header within the
                list of all text elements in section.
            field_items (List[str]): The list of all text elements in section.

        Returns:
            bool: A boolean indicating whether the checkbox was checked.
        """
        prev_idx = idx - 1
        if prev_idx >= 0:
            prev_element = field_items[prev_idx]
            return prev_element == X_MARK
        else:
            return False