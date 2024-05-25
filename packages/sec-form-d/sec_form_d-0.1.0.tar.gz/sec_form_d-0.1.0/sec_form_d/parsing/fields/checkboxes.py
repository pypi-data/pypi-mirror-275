from typing import (
    Any,
    Dict, 
    List, 
    Optional
)

from sec_form_d.parsing.fields.base_fields import BaseParsing
from sec_form_d.parsing.schema_extraction import SchemaExtraction
from sec_form_d.types.field import (
    FormCheckBox,
    FormCheckBoxMultiple
)

class CheckBoxSingle(BaseParsing):
    """
    Parsing for single checkbox fields appearing in the
    form. Contains a single method to process all single
    checkboxes included in the section.

    Args:
        schema (SchemaExtraction): An object containing all schema
            related variables after decomposition.
    """
    def __init__(self, schema: SchemaExtraction):
        super().__init__(schema=schema)

    def process(self, section_text: List[str]) -> List[FormCheckBox]:
        """
        Processing to extract all single checkboxes from
        form. Methodology is to iterate through each checkbox
        from schema, and extract the "checked" status of each.

        Args:
            section_text (List[str]): A list of all text elements
                in section.

        Returns:
            List[FormCheckBox]: A list of FormCheckBox objects
                with a boolean status indicating whether the checkbox
                was "checked".
        """
        check_box_names: Dict[str, Any] = self.schema.serialized_single_box_names

        # Iterate through each item in section text
        for idx, item in enumerate(section_text):
            if item in check_box_names:

                # Extract checkbox status and append field
                data = self.check_box_status(idx=idx, field_items=section_text)
                self.append_to_fields(
                    field=FormCheckBox(name=check_box_names.get(item), data=data)
                )
        return self.flush_fields()
    

class CheckBoxMultiple(BaseParsing):
    """
    Parsing for multiple checkbox fields appearing in the
    form. Contains a single method to process all multiple
    checkboxes included in the section.
    
    Args:
        schema (SchemaExtraction): An object containing all schema
            related variables after decomposition.
    """
    def __init__(self, schema: SchemaExtraction):
        super().__init__(schema=schema)

    def process(self, section_text: List[str]) -> List[FormCheckBoxMultiple]:
        """
        Processing to extract all multiple checkboxes from
        form. Methodology is to iterate through each checkbox
        from schema, finding the start and end points of checkbox.
        Using these indices we extract only the checkbox data and
        extract status of each.

        Args:
            section_text (List[str]): A list of all text elements
                in section.

        Returns:
            List[FormCheckBoxMultiple]: A list of FormCheckBoxMultiple
                objects with a list of FormCheckBox objects each with a
                boolean status indicating whether the checkbox was "checked".
        """
        for check_box in self.boxes_multiple:
            check_box_items: List[str] = []
            start_idx = section_text.index(check_box.field_name)

            # Find end point of checkbox section
            end_text: Optional[str] = next(
                (
                    text for text in section_text[start_idx + 1:]
                    if text in self.all_field_names
                ), None
            )

            # Add relevant fields from HTML text to local items
            if end_text is not None:
                end_idx = section_text.index(end_text) + 1
                check_box_items.extend(section_text[start_idx:end_idx])
            else:
                check_box_items.extend(section_text[start_idx:])

            # If items found, create multiple checkbox dataclass
            if check_box_items:
                check_box_fields = [
                    FormCheckBox(
                        name=check_box.fields_mapping.get(item),
                        data=self.check_box_status(
                            idx=idx, field_items=check_box_items
                        )
                    )
                    for idx, item in enumerate(check_box_items)
                    if item in check_box.fields_mapping
                ]

                # Add all individual fields to multiple checkbox field
                self.append_to_fields(
                    field=FormCheckBoxMultiple(
                        name=check_box.attr_name, fields=check_box_fields
                    )
                )
        return self.flush_fields()
    

class CheckBoxMultipleDualAlternate(BaseParsing):
    """
    Parsing for multiple dual-alternate checkbox fields
    appearing in the form. Contains a single method to
    process all multiple dual-alternate checkboxes
    included in the section.

    Args:
        schema (SchemaExtraction): An object containing all schema
            related variables after decomposition.
        first (bool): A boolean indicating whether the field to
            extract is the first or second appearing.
    """
    def __init__(
        self,
        schema: SchemaExtraction,
        first: bool = True
    ):
        super().__init__(schema=schema)
        self._first = first

    def process(self, section_text: List[str]) -> List[FormCheckBoxMultiple]:
        """
        Processing to extract all multiple dual-alternate
        checkboxes from form. Methodology is to iterate through
        each checkbox from schema, in an alternating fashion and
        and extract status of each.

        Args:
            section_text (List[str]): A list of all text elements
                in section.

        Returns:
            List[FormCheckBoxMultiple]: A list of FormCheckBoxMultiple
                objects with a list of FormCheckBox objects each with a
                boolean status indicating whether the checkbox was "checked".
        """
        check_box_index = 0 if self._first else 1
        check_box = self.boxes_multiple[check_box_index]
        for field in check_box.fields:
            if self._first:
                index = section_text.index(field.field_name)
            else:
                all_indices = [
                    i for i, x in enumerate(section_text) if x == field.field_name
                ]
                index = all_indices[1] if len(all_indices) > 1 else all_indices[0]
                
            data = self.check_box_status(idx=index, field_items=section_text)
            self.append_to_fields(
                field=FormCheckBox(name=field.attr_name, data=data)
            )
        return [
            FormCheckBoxMultiple(
                name=check_box.attr_name, fields=self.flush_fields()
            )
        ]