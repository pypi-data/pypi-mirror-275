from typing import (
    Any,
    Dict,
    List,
    Tuple, 
    Type
)

from sec_form_d.constants import X_MARK
from sec_form_d.types.form import SectionSchemaType
from sec_form_d.utils import (
    detect_fields,
    serialize_field_names
)

class SchemaExtraction:
    """
    Extract and separate all fields from a pydantic model schema
    by field type. In addition, the field names are also extracted
    to be used in the processing of all form data elements

    Args:
        section (Type[SectionSchemaType]): A pydantic model schema type
            for a section appearing in the form.
    """
    def __init__(self, schema: Type[SectionSchemaType]):
        self._schema = schema

        # Parse section schema
        self.fields, self.boxes_single, self.boxes_multiple = detect_fields(
            section_schema=self._schema
        )

        # Generate field buckets
        self.box_names, self.box_field_names, self.all_field_names = self._generate_field_buckets()
        self.all_box_field_names: List[str] = self.box_names + self.box_field_names

    @property
    def serialized_single_box_names(self) -> Dict[str, Any]:
        """A seralized mapping of all single checkboxes appearing in section."""
        return serialize_field_names(fields=self.boxes_single)

    @property
    def serialized_field_names(self) -> Dict[str, Any]:
        """A seralized mapping of all non-checkbox data fields appearing in section."""
        return serialize_field_names(fields=self.fields)

    def _generate_field_buckets(self) -> Tuple[List[str], List[str], List[str]]:
        """
        A private method to extract all field names from all
        field types (fields and checkboxes) detected in the schema.
        """
        box_names: List[str] = []
        box_field_names: List[str] = []
        all_field_names: List[str] = []

        box_field_names.append(X_MARK)

        for check_box in self.boxes_single:
            all_field_names.append(check_box.field_name)

            box_field_names.append(check_box.field_name)

        for check_box in self.boxes_multiple:
            all_field_names.append(check_box.field_name)

            box_names.append(check_box.field_name)
            for field in check_box.fields:
                box_field_names.append(field.field_name)

        for field in self.fields:
            all_field_names.append(field.field_name)

        return (
            box_names, box_field_names, all_field_names
        )