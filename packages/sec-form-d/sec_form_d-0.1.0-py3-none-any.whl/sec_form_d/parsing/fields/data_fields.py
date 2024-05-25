from collections import deque
from typing import (
    Any, 
    Deque,
    Dict, 
    List, 
    Type
)

from sec_form_d.types.form import SectionSchemaType
from sec_form_d.types.field import FormField
from sec_form_d.parsing.schema_extraction import SchemaExtraction
from sec_form_d.parsing.fields.base_fields import BaseParsing
from sec_form_d.utils import (
    flush_header_waiting_room,
    serialize_fields
)

class FieldHeaderRowConsistent(BaseParsing):
    """
    Parsing for data fields appearing in a traditional
    tabular format within the form. First the headers
    are found, then each item in each row of data found
    after is linked to a header based on the position of
    the item in the row.
    
    Contains a single method to process all data fields
    included in the section.

    Args:
        schema (SchemaExtraction): An object containing all schema
            related variables after decomposition.
        section_schema (Type[SectionSchemaType]): A type of one of
            the seventeen section schemas.
    """
    def __init__(
        self,
        schema: SchemaExtraction,
        section_schema: Type[SectionSchemaType]
    ):
        super().__init__(schema=schema)
        self._section_schema = section_schema

    def process(self, section_text: List[str]) -> List[SectionSchemaType]:
        """
        Processing to extract all tabular formatted data
        fields from form. Methodology is to first find all the
        headers, then for every following row of data, each item
        is matched to a header based on the position within the
        row.

        Args:
            section_text (List[str]): A list of all text elements
                in section.

        Returns:
            List[SectionSchemaType]: A list of validated schema
                pydantic models containing the parsed data.
        """
        def pop_and_return(item: str) -> List[str]:
            section_text.remove(item)
            return item
        
        data_field_names: Dict[str, Any] = self.schema.serialized_field_names
        return_fields: List[SectionSchemaType] = []
        
        # Remove any text appearing before headers
        for idx, text in enumerate(section_text):
            if text in data_field_names:
                section_text = section_text[idx:]
                break

        # Filter for ordering of headers and remove from
        # section_text at same time
        headers = [
            pop_and_return(item=item) 
            for item in section_text[:] if item in data_field_names
        ]
        num_headers = len(headers)

        # Iterate through each item in the section text
        for idx, item in enumerate(section_text):
            self.append_to_fields(
                field=FormField(
                    name=data_field_names[headers[(idx % num_headers)]],
                    data=item
                )
            )
            
            if (idx % num_headers) + 1 == num_headers:
                serialized_fields: Dict[str, Any] = serialize_fields(
                    fields=self.flush_fields()
                )
                return_fields.append(
                    self._section_schema.model_validate(fields=serialized_fields)
                )

        return return_fields


class FieldHeaderRowGrouped(BaseParsing):
    """
    Parsing for data fields whose field and value are
    grouped together horizontally, in which the field
    appears on the left and the corresponding value
    just to the right. 
    
    Contains a single method to process all data fields
    included in the section.

    Args:
        schema (SchemaExtraction): An object containing all
            schema related variables after decomposition.
    """
    def __init__(
        self,
        schema: SchemaExtraction
    ):
        super().__init__(schema=schema)

    def process(self, section_text: List[str]) -> List[FormField]:
        """
        Processing to extract all horizontally grouped data
        fields from form. Methodology is to first find the
        field and then look for a corresponding non-null value
        appearing next.

        Args:
            section_text (List[str]): A list of all text elements
                in section.

        Returns:
            List[FormField]: A list of FormField objects with a
                field appearing in the section along with the
                corresponding data (if any).
        """
        data_field_names: Dict[str, Any] = self.schema.serialized_field_names

        # Iterate through each item in the section text
        section_text_length = len(section_text)
        for idx, item in enumerate(section_text):
            if item in data_field_names:
                next_idx = idx + 1

                # Ensure that there exists a next item in list
                if next_idx <= (section_text_length - 1):
                    next_item: str = section_text[next_idx]

                    # If text is not in fields to ignore then create a field
                    if next_item not in self.all_field_names:
                        self.append_to_fields(
                            field=FormField(
                                name=data_field_names[item], data=next_item
                            )
                        )
                        continue
                
                # Otherwise append an empty field
                self.append_to_fields(
                    field=FormField(name=data_field_names[item], data=None)
                )
        return self.flush_fields()


class FieldHeaderToRow(BaseParsing):
    """
    Parsing for all data fields that are structured
    in a "header-to-row" format. This is where a field
    name will be in a row of headers and the corresponding
    value will appear in the next row. Thus, a data row
    will always following a header row.
    
    Contains a single method to process all data fields
    included in the section.

    Args:
        schema (SchemaExtraction): An object containing all schema
            related variables after decomposition.
    """
    def __init__(
        self, 
        schema: SchemaExtraction
    ):
        super().__init__(schema=schema)

    def process(self, section_text: List[str]) -> List[FormField]:
        """
        Processing to extract all data fields in a header-to-row
        format from form. Methodology is to iterate through each
        field appearing in a specific row, and then find the corresponding
        value in the following row based on the order in which
        the field names were found. 

        Args:
            section_text (List[str]): A list of all text elements
                in section.

        Returns:
            List[FormField]: A list of FormField objects with a
                field appearing in the section along with the
                corresponding data (if any).
        """
        def flush_headers(queue: Deque) -> None:
            if queue:
                headers = flush_header_waiting_room(queue=queue)
                self.extend_fields(fields=headers)

        do_last_header = False
        done_header = False
        waiting_text: Deque[str] = deque([])
        waiting_headers: Deque[str] = deque([])

        # Retrieve all field names to use in filtering
        data_field_names: Dict[str, Any] = self.schema.serialized_field_names

        # Iterate through each item in the section text
        for idx, item in enumerate(section_text):
            if item not in self.all_box_field_names:

                # Ensure item is in field names that are being searched
                if item in data_field_names:

                    # If previously there was no header but there are
                    # waiting headers this is an indication that there are
                    # empty fields, so we flush queue and append empty fields
                    if not do_last_header:
                        flush_headers(queue=waiting_headers)

                    waiting_headers.append(data_field_names[item])
                    do_last_header = True
                    if not done_header:
                        done_header = True

                # Ensure that we only append data if we have actually
                # encountered at least one header
                elif done_header:
                    next_idx = idx + 1
                    prev_idx = idx - 1

                    # If there is only one waiting header and the next element
                    # is not a field, it is an indication that there are multiple
                    # entries for the most recent header
                    if len(waiting_headers) == 1 and (
                        next_idx <= len(section_text) - 1 and
                        section_text[next_idx] not in self.all_field_names
                    ):
                        waiting_text.append(item)
                    else:
                        if waiting_headers:
                            header = waiting_headers.popleft()

                            # If text immediately follows a checkbox we know
                            # that it is junk text
                            if section_text[prev_idx] in self.box_field_names:
                                self.append_to_fields(
                                    field=FormField(name=header, data=None)
                                )

                            # If there is any waiting text we need to combine
                            # before appending field
                            elif waiting_text:
                                text: List[str] = []
                                while waiting_text:
                                    text.append(waiting_text.popleft())
                                text.append(item)
                                self.append_to_fields(
                                    field=FormField(
                                        name=header, data=';'.join(text)
                                    )
                                )

                            # Normal appending of field
                            else:
                                self.append_to_fields(
                                    field=FormField(name=header, data=item)
                                )
                    do_last_header = False

            # If we have extracted the number of fields that
            # we need, we can break
            if len(self.form_fields) == len(data_field_names):
                break

        # Flush all headers at the end if all fields are blank
        flush_headers(queue=waiting_headers)
        return self.flush_fields()