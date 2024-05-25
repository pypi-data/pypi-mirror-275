import inspect
from typing import (
    Any,
    Deque, 
    Dict, 
    List, 
    Tuple,
    Type,
    Union
)

from pydantic import BaseModel
from bs4 import Tag

from sec_form_d.types.form import SectionSchemaType
from sec_form_d.types.section import SectionTag
from sec_form_d.types.field import (
    CheckBoxMultipleType,
    CheckBoxSingleType,
    FieldType,
    FormCheckBox,
    FormCheckBoxMultiple,
    FormField
)

def serialize_field_names(
    fields: List[Union[CheckBoxSingleType, FieldType]]
) -> Dict[str, Any]:
    """
    Serializes a list of field type objects, to create a
    mapping from the field name to the attribute name.
    
    Args:
        fields (List[CheckBoxSingleType | FieldType]): A list
            of field type objects being either CheckBoxSingleType
            or FieldType.

    Returns:
        Dict[str, Any]: A dictionary representation of all field
            type objects appearing in the list.
    """
    return {
        field.field_name: field.attr_name for field in fields
    }


def serialize_fields(
    fields: List[Union[FormCheckBox, FormCheckBoxMultiple, FormField]]
) -> Dict[str, Any]:
    """
    Serializes a list of field structure objects.
    
    Args:
        fields (List[FormCheckBox | FormCheckBoxMultiple | FormField]):
            A list of field structure objects.

    Returns:
        Dict[str, Any]: A dictionary representation of all field
            structure objects appearing in the list.
    """
    return {
        k: v for field in fields for k, v in field.to_dict().items()
    }


def extract_text(element: Tag) -> List[str]:
    """
    Extract and clean all text from a bs4 Tag instance.

    Args:
        element (Tag): A bs4 Tag instance corresponding to an
            HTML element.

    Returns:
        List[str]: A list of strings corresponding to the text
            in an element.
    """
    return [
        i.strip() for i in element.get_text().split('\n') if i.strip()
    ]


def flush_header_waiting_room(queue: Deque) -> List[FormField]:
    """
    Pop all headers from header queue and fill with empty data.
    This is used only if there are headers with no data.

    Args:
        queue (Deque): The queue of headers that are waiting for data.

    Returns:
        List[FormField]: A list of FormField objects with
            headers but empty data.
    """
    patients: List[FormField] = []
    while queue:
        patient: str = queue.popleft()
        patients.append(
            FormField(name=patient, data=None)
        )
    return patients


def detect_fields(section_schema: Type[SectionSchemaType]) -> Tuple[
    List[FieldType],
    List[CheckBoxSingleType],
    List[CheckBoxMultipleType]
]:
    """
    Detects and separates all field types appearing in a section
    schema. These field types include FieldType, CheckBoxSingleType,
    and CheckBoxMultipleType.

    Args:
        section (Type[SectionSchemaType]): A pydantic model schema type
            for a section appearing in the form.

    Returns:
        Tuple[List[FieldType], List[CheckBoxSingleType], List[CheckBoxMultipleType]]:
            A tuple with three lists containing all types of fields from
            schema. The first has all the non-checkbox fields, the second
            has all the single checkboxes, and the third has all the
            multiple checkboxes.
    """
    data_fields: List[FieldType] = []
    check_boxes_single: List[CheckBoxSingleType] = []
    check_boxes_multiple: List[CheckBoxMultipleType] = []

    # Iterate through each field in section schema
    for attr, field_info in section_schema.model_fields.items():
        if not field_info.title:
            raise ValueError(
                "each field from a pydantic model schema must have a title"
            )
        
        if not field_info.is_required():
            raise ValueError(
                "each field from a pydantic model schema must be required field"
            )
        
        field_title = field_info.title
        field_annotation = field_info.annotation

        # If value is a single checkbox
        if field_annotation is bool:
            check_boxes_single.append(
                CheckBoxSingleType(
                    field_name=field_title, attr_name=attr
                )
            )

        # If value is a multiple checkbox
        elif (
            inspect.isclass(field_annotation) and
            issubclass(field_annotation, BaseModel)
        ):
            check_box_fields: List[str] = []
            check_box_fields.extend(
                detect_fields(section_schema=field_annotation)[1]
            )

            assert len(field_annotation.model_fields) == len(check_box_fields)
            
            check_boxes_multiple.append(
                CheckBoxMultipleType(
                    field_name=field_title,
                    attr_name=attr,
                    fields=check_box_fields
                )
            )
        else:
            data_fields.append(
                FieldType(field_name=field_title, attr_name=attr)
            )

    return (
        data_fields, check_boxes_single, check_boxes_multiple
    )


def extract_section_elements(
    html: Tag, section_tag: SectionTag
) -> Dict[str, List[Tuple[Tag, ...]]]:
    """
    Identify where the beginning and end of each section
    occurs. Once the beginning of a section is detected,
    then all following HTML elements up until the end are
    attributed to the section. Since there can be sub-sections,
    all elements are grouped into a tuple as Tag instances.

    A dictionary is returned where the keys are section names
    and the values are lists of tuples full of Tag instances.

    Args:
        html (Tag): A Tag instance representing the <body>
            element of the HTML file.
        section_tag (SectionTag): A SectionTag instance
            representing the HTML element that signifies
            the start of a section.

    Returns:
        Dict[str, List[Tuple[Tag, ...]]]: A dictionary that maps
            a section name to a list of tuples, each tuple
            consisting of bs4 Tag instances. Each Tag instance
            being an HTML element belonging to the section.
    """
    def is_section(element: Tag) -> bool:
        attr_list = element.get(section_tag.attr)
        return attr_list and section_tag.value in attr_list
    
    def tupleize(section_name: str, section_elements: dict) -> None:
        elements = section_elements[section_name]

        # Split up already parsed elements into tuple vs non-tuple
        tuples = [item for item in elements if isinstance(item, tuple)]
        non_tuples = [item for item in elements if not isinstance(item, tuple)]

        tupelized_non_tuples = tuple(non_tuples)
        section_elements.update(
            {section_name: tuples + [tupelized_non_tuples]}
        )

    section_name = None
    section_elements: Dict[str, List[Tuple[Tag, ...]]] = dict()

    # Iterate through each form HTML element and classify which
    # section it belongs to
    for element in html.children:
        if not isinstance(element, Tag):
            continue

        if is_section(element=element):
            section_name = element.text.strip()

            # If we encounter section for the first time
            if section_name not in section_elements:
                section_elements.update({section_name: []})

            # In rare cases, more than one issuer can be attached
            # to the form. Thus, we have some logic in place to group
            # all rogue elements into a tuple if we see a section for
            # the second time
            else:
                tupleize(
                    section_name=section_name,
                    section_elements=section_elements
                )

        elif section_name is not None:
            section_elements[section_name].append(element)

    # Once the entire extraction has occurred, we want
    # to ensure that all elements of each section have
    # been grouped in tuples. So we tupleize all rogue
    # elements in list
    for section_name in section_elements:
        tupleize(
            section_name=section_name, section_elements=section_elements
        )

    return section_elements