from abc import ABC, abstractmethod
from collections import deque
from typing import (
    Any,
    Deque,
    Dict,
    List,
    Optional,
    Tuple,
    Type
)

from pydantic import BaseModel
from bs4 import Tag

from sec_form_d.parsing.schema_extraction import SchemaExtraction
from sec_form_d.parsing.fields.base_fields import (
    BaseParsing,
    FormData
)
from sec_form_d.constants import (
    NONE, 
    X_MARK
)
from sec_form_d.enums import Tags
from sec_form_d.parsing.fields.checkboxes import (
    CheckBoxMultiple,
    CheckBoxMultipleDualAlternate,
    CheckBoxSingle
)
from sec_form_d.types.form import *
from sec_form_d.parsing.fields.data_fields import (
    FieldHeaderRowConsistent,
    FieldHeaderRowGrouped,
    FieldHeaderToRow
)
from sec_form_d.utils import (
    extract_text,
    serialize_fields
)

class BaseSection(ABC):
    """
    Abstract class for extracting and parsing all fields for
    each section for Form D. Handles extraction of text from all
    section-related HTML elements and parsing of the text to retrieve
    all relevant data fields.

    Args:
        name (str): The name of the section.
        section (Type[SectionType]): A pydantic model section type
            for a section appearing in the form.
        schema (Type[SectionSchemaType]): A pydantic model schema type
            for a section appearing in the form.
        sections (Dict[str, List[Tuple[Tag, ...]]]): A dictionary mapping
            from the name of the section to a list of tuples, each tuple
            consisting of bs4 Tag instances.
        filter_tags (List[Tags]): A list of Tags objects corresponding to
            HTML tag names to be filtered for when extracting text from
            section elements.
        split_section_tags (List[Tags]): A list of Tags objects corresponding
            to HTML tag names indicating where sub-sections end and begin.
        sub_section_merge (List[str]): A list of string field names serving
            as the primary key for each sub-section.
    """
    def __init__(
        self,
        name: str,
        section: Type[SectionType],
        schema: Type[SectionSchemaType],
        sections: Dict[str, List[Tuple[Tag, ...]]],
        filter_tags: List[Tags] = [],
        split_section_tags: List[Tags] = [],
        sub_section_merge: List[str] = []
    ):
        self._name = name
        self._section = section
        self._schema = schema
        self._sub_section_merge = sub_section_merge

        self._filter_tags: List[str] = [tag.value for tag in filter_tags]
        self._split_section_tags: List[str] = [
            tag.value for tag in split_section_tags
        ]

        # Retrieve elements corresponding with section
        self._section_text = self._extract_text(
            sections=sections.get(name)
        )

        # Extract fields from schema
        schema_extract = SchemaExtraction(schema=schema)

        self.section_args = {
            'schema': schema_extract
        }

    @abstractmethod
    def parse(self) -> SectionType:
        """Abstract method for running all parsing of fields."""
        pass

    def _remove_none_checkboxes(self, text: Tuple[str, ...]) -> List[str]:
        """
        """
        text_to_list: List[str] = list(text)
        for idx, text in enumerate(text_to_list[:]):
            if text == NONE:
                text_to_list.remove(text)

            if text == X_MARK and text_to_list[idx + 1] == NONE:
                text_to_list.remove(text)
        return text_to_list

    def _parse_fields(self, field_parsers: List[BaseParsing]) -> SectionType:
        """
        Iterate through all sections of text and parsers and extract
        all fields.

        Args:
            field_parsers (List[BaseParsing]): All parsers used to extract
                fields from a section.

        Returns:
            SectionType: A pydantic model for a section appearing in the form.
        """
        has_subsections = len(self._section_text) > 1
        do_sub_section = len(self._sub_section_merge) > 0
        if has_subsections and not do_sub_section:
            raise ValueError(
                "if there is a potential for sub-sections, "
                "the 'sub_section_merge' argument must be included"
            )
        section_fields: List[SectionSchemaType] = []

        # Iterate through each sub-section of text within section
        for text in self._section_text:
            section: Optional[SectionSchemaType] = None
            parsed_fields: List[Union[SectionSchemaType, FormData]] = []

            # Iterate through each parser and update fields
            for parser in field_parsers:
                text_to_list = self._remove_none_checkboxes(text=text)
                fields = parser.process(section_text=text_to_list)
                parsed_fields.extend(fields)

            if (
                do_sub_section and
                not all(isinstance(item, BaseModel) for item in parsed_fields)
            ) or not do_sub_section:
                serialized_fields: Dict[str, Any] = serialize_fields(fields=parsed_fields)
                section = self._schema.model_validate(fields=serialized_fields)
                section_fields.append(section)
            else:
                section_fields.extend(parsed_fields)

        if has_subsections or len(section_fields) > 1:
            fields_to_include = section_fields
        else:
            fields_to_include = section_fields[0]

        # Instantiate section type
        form_section = self._section(
            name=self._name, section=fields_to_include
        )
        
        form_section.sub_section_merge = self._sub_section_merge
        return form_section

    def _extract_text(
        self,
        sections: Optional[List[Tuple[Tag, ...]]]
    ) -> List[Tuple[str, ...]]:
        """
        Extracts text from all elements appearing within a section.
        The method accepts a list of tuples where each tuple contains
        Tag instances, and returns a list of tuples, where each tuple
        contains all text for that section.

        Args:
            sections (List[Tuple[Tag, ...]] | None): A list of tuples,
                each tuple containing Tag instances representing all
                HTML elements found in a given section.
 
        Returns:
            List[Tuple[str, ...]]: A list of tuples each containing all
                text extracted from every Tag instance appearing in the
                section. 
        """
        extracted_text: List[Tuple[str, ...]] = []
        
        def flush_and_extract(queue: Deque) -> None:
            """"""
            local_text: List[str] = []
            while queue:
                patient = queue.popleft()
                local_text.extend(extract_text(element=patient))

            if local_text:
                extracted_text.append(tuple(local_text))

        if sections is None:
            return extracted_text
        else:
            waiting_elements = deque([])
            for section in sections:

                if self._filter_tags:
                    section = *(
                        element for element in section
                        if element.name in self._filter_tags
                    ),
                
                for element in section:
                    if element.name in self._split_section_tags:
                        flush_and_extract(queue=waiting_elements)
                    else:
                        waiting_elements.append(element)
                
                flush_and_extract(queue=waiting_elements)
            return extracted_text


class SectionOneParser(BaseSection):
    """
    Parsing configuration for section one.
    
    Args:
        sections (List[Tuple[Tag, ...]]): A list of tuples,
            each tuple containing Tag instances representing all
            HTML elements found in a given section.
    """
    def __init__(self, sections: List[Tuple[Tag, ...]]):
        super().__init__(
            name="1. Issuer's Identity",
            section=SectionOne,
            schema=SectionOneSchema,
            sections=sections,
            sub_section_merge=['cik']
        )

    def parse(self) -> SectionOne:
        """
        Field parsing for section one.

        Returns:
            SectionOne: A pydantic model storing all parsed data
                for section one.
        """
        field_parsers = [
            FieldHeaderToRow(**self.section_args),
            CheckBoxMultiple(**self.section_args)
        ]

        return self._parse_fields(field_parsers=field_parsers)


class SectionTwoParser(BaseSection):
    """
    Parsing configuration for section two.
    
    Args:
        sections (List[Tuple[Tag, ...]]): A list of tuples,
            each tuple containing Tag instances representing all
            HTML elements found in a given section.
    """
    def __init__(self, sections: List[Tuple[Tag, ...]]):
        super().__init__(
            name="2. Principal Place of Business and Contact Information",
            section=SectionTwo,
            schema=SectionTwoSchema,
            sections=sections,
            sub_section_merge=['issuer_name']
        )

    def parse(self) -> SectionTwo:
        """
        Field parsing for section two.

        Returns:
            SectionTwo: A pydantic model storing all parsed data
                for section two.
        """
        field_parsers = [
            FieldHeaderToRow(**self.section_args)
        ]

        return self._parse_fields(field_parsers=field_parsers)
    

class SectionThreeParser(BaseSection):
    """
    Parsing configuration for section three.
    
    Args:
        sections (List[Tuple[Tag, ...]]): A list of tuples,
            each tuple containing Tag instances representing all
            HTML elements found in a given section.
    """
    def __init__(self, sections: List[Tuple[Tag, ...]]):
        super().__init__(
            name="3. Related Persons",
            section=SectionThree,
            schema=SectionThreeSchema,
            split_section_tags=[Tags.HR],
            sections=sections,
            sub_section_merge=['first_name', 'last_name']
        )

    def parse(self) -> SectionThree:
        """
        Field parsing for section three.

        Returns:
            SectionThree: A pydantic model storing all parsed data
                for section three.
        """
        field_parsers = [
            FieldHeaderToRow(**self.section_args),
            CheckBoxMultiple(**self.section_args)
        ]

        return self._parse_fields(field_parsers=field_parsers)
    

class SectionFourParser(BaseSection):
    """
    Parsing configuration for section four.
    
    Args:
        sections (List[Tuple[Tag, ...]]): A list of tuples,
            each tuple containing Tag instances representing all
            HTML elements found in a given section.
    """
    def __init__(self, sections: List[Tuple[Tag, ...]]):
        super().__init__(
            name="4. Industry Group",
            section=SectionFour,
            schema=SectionFourSchema,
            sections=sections
        )

    def parse(self) -> SectionFour:
        """
        Field parsing for section four.

        Returns:
            SectionFour: A pydantic model storing all parsed data
                for section four.
        """
        field_parsers = [
            CheckBoxSingle(**self.section_args),
            CheckBoxMultiple(**self.section_args)
        ]

        return self._parse_fields(field_parsers=field_parsers)
    

class SectionFiveParser(BaseSection):
    """
    Parsing configuration for section five.
    
    Args:
        sections (List[Tuple[Tag, ...]]): A list of tuples,
            each tuple containing Tag instances representing all
            HTML elements found in a given section.
    """
    def __init__(self, sections: List[Tuple[Tag, ...]]):
        super().__init__(
            name="5. Issuer Size",
            section=SectionFive,
            schema=SectionFiveSchema,
            sections=sections
        )

    def parse(self) -> SectionFive:
        """
        Field parsing for section five.

        Returns:
            SectionFive: A pydantic model storing all parsed data
                for section five.
        """
        field_parsers = [
            CheckBoxMultipleDualAlternate(**self.section_args),
            CheckBoxMultipleDualAlternate(**self.section_args, first=False)
        ]

        return self._parse_fields(field_parsers=field_parsers)
    

class SectionSixParser(BaseSection):
    """
    Parsing configuration for section six.
    
    Args:
        sections (List[Tuple[Tag, ...]]): A list of tuples,
            each tuple containing Tag instances representing all
            HTML elements found in a given section.
    """
    def __init__(self, sections: List[Tuple[Tag, ...]]):
        super().__init__(
            name="6. Federal Exemption(s) and Exclusion(s) Claimed (select all that apply)",
            section=SectionSix,
            schema=SectionSixSchema,
            sections=sections
        )

    def parse(self) -> SectionSix:
        """
        Field parsing for section six.

        Returns:
            SectionSix: A pydantic model storing all parsed data
                for section six.
        """
        field_parsers = [
            CheckBoxSingle(**self.section_args)
        ]

        return self._parse_fields(field_parsers=field_parsers)
    

class SectionSevenParser(BaseSection):
    """
    Parsing configuration for section seven.
    
    Args:
        sections (List[Tuple[Tag, ...]]): A list of tuples,
            each tuple containing Tag instances representing all
            HTML elements found in a given section.
    """
    def __init__(self, sections: List[Tuple[Tag, ...]]):
        super().__init__(
            name="7. Type of Filing",
            section=SectionSeven,
            schema=SectionSevenSchema,
            sections=sections
        )

    def parse(self) -> SectionSeven:
        """
        Field parsing for section seven.

        Returns:
            SectionSeven: A pydantic model storing all parsed data
                for section seven.
        """
        field_parsers = [
            FieldHeaderRowGrouped(**self.section_args),
            CheckBoxSingle(**self.section_args),
        ]

        return self._parse_fields(field_parsers=field_parsers)
    

class SectionEightParser(BaseSection):
    """
    Parsing configuration for section eight.
    
    Args:
        sections (List[Tuple[Tag, ...]]): A list of tuples,
            each tuple containing Tag instances representing all
            HTML elements found in a given section.
    """
    def __init__(self, sections: List[Tuple[Tag, ...]]):
        super().__init__(
            name="8. Duration of Offering",
            section=SectionEight,
            schema=SectionEightSchema,
            sections=sections
        )

    def parse(self) -> SectionEight:
        """
        Field parsing for section eight.

        Returns:
            SectionEight: A pydantic model storing all parsed data
                for section eight.
        """
        field_parsers = [
            CheckBoxMultiple(**self.section_args)
        ]

        return self._parse_fields(field_parsers=field_parsers)
    

class SectionNineParser(BaseSection):
    """
    Parsing configuration for section nine.
    
    Args:
        sections (List[Tuple[Tag, ...]]): A list of tuples,
            each tuple containing Tag instances representing all
            HTML elements found in a given section.
    """
    def __init__(self, sections: List[Tuple[Tag, ...]]):
        super().__init__(
            name="9. Type(s) of Securities Offered (select all that apply)",
            section=SectionNine,
            schema=SectionNineSchema,
            sections=sections
        )

    def parse(self) -> SectionNine:
        """
        Field parsing for section nine.

        Returns:
            SectionNine: A pydantic model storing all parsed data
                for section nine.
        """
        field_parsers = [
            CheckBoxSingle(**self.section_args)
        ]

        return self._parse_fields(field_parsers=field_parsers)
    

class SectionTenParser(BaseSection):
    """
    Parsing configuration for section ten.
    
    Args:
        sections (List[Tuple[Tag, ...]]): A list of tuples,
            each tuple containing Tag instances representing all
            HTML elements found in a given section.
    """
    def __init__(self, sections: List[Tuple[Tag, ...]]):
        super().__init__(
            name="10. Business Combination Transaction",
            section=SectionTen,
            schema=SectionTenSchema,
            sections=sections
        )

    def parse(self) -> SectionTen:
        """
        Field parsing for section ten.

        Returns:
            SectionTen: A pydantic model storing all parsed data
                for section ten.
        """
        field_parsers = [
            FieldHeaderRowGrouped(**self.section_args),
            CheckBoxMultiple(**self.section_args)
        ]

        return self._parse_fields(field_parsers=field_parsers)
    

class SectionElevenParser(BaseSection):
    """
    Parsing configuration for section eleven.
    
    Args:
        sections (List[Tuple[Tag, ...]]): A list of tuples,
            each tuple containing Tag instances representing all
            HTML elements found in a given section.
    """
    def __init__(self, sections: List[Tuple[Tag, ...]]):
        super().__init__(
            name="11. Minimum Investment",
            section=SectionEleven,
            schema=SectionElevenSchema,
            sections=sections
        )

    def parse(self) -> SectionEleven:
        """
        Field parsing for section eleven.

        Returns:
            SectionEleven: A pydantic model storing all parsed data
                for section eleven.
        """
        field_parsers = [
            FieldHeaderRowGrouped(**self.section_args)
        ]

        return self._parse_fields(field_parsers=field_parsers)
    

class SectionTwelveParser(BaseSection):
    """
    Parsing configuration for section twelve.
    
    Args:
        sections (List[Tuple[Tag, ...]]): A list of tuples,
            each tuple containing Tag instances representing all
            HTML elements found in a given section.
    """
    def __init__(self, sections: List[Tuple[Tag, ...]]):
        super().__init__(
            name="12. Sales Compensation",
            section=SectionTwelve,
            schema=SectionTwelveSchema,
            split_section_tags=[Tags.HR],
            sections=sections,
            sub_section_merge=[
                'recipient',
                'recipient_crd',
                'broker_or_dealer',
                'broker_or_dealer_crd'
            ]
        )

    def parse(self) -> SectionTwelve:
        """
        Field parsing for section twelve.

        Returns:
            SectionTwelve: A pydantic model storing all parsed data
                for section twelve.
        """
        field_parsers = [
            FieldHeaderToRow(**self.section_args),
            CheckBoxSingle(**self.section_args),
            CheckBoxMultiple(**self.section_args)
        ]

        return self._parse_fields(field_parsers=field_parsers)
    

class SectionThirteenParser(BaseSection):
    """
    Parsing configuration for section thirteen.
    
    Args:
        sections (List[Tuple[Tag, ...]]): A list of tuples,
            each tuple containing Tag instances representing all
            HTML elements found in a given section.
    """
    def __init__(self, sections: List[Tuple[Tag, ...]]):
        super().__init__(
            name="13. Offering and Sales Amounts",
            section=SectionThirteen,
            schema=SectionThirteenSchema,
            sections=sections
        )

    def parse(self) -> SectionThirteen:
        """
        Field parsing for section thirteen.

        Returns:
            SectionThirteen: A pydantic model storing all parsed data
                for section thirteen.
        """
        field_parsers = [
            FieldHeaderRowGrouped(**self.section_args),
            CheckBoxMultiple(**self.section_args)
        ]

        return self._parse_fields(field_parsers=field_parsers)
    

class SectionFourteenParser(BaseSection):
    """
    Parsing configuration for section fourteen.
    
    Args:
        sections (List[Tuple[Tag, ...]]): A list of tuples,
            each tuple containing Tag instances representing all
            HTML elements found in a given section.
    """
    def __init__(self, sections: List[Tuple[Tag, ...]]):
        super().__init__(
            name="14. Investors",
            section=SectionFourteen,
            schema=SectionFourteenSchema,
            sections=sections
        )

    def parse(self) -> SectionFourteen:
        """
        Field parsing for section fourteen.

        Returns:
            SectionFourteen: A pydantic model storing all parsed data
                for section fourteen.
        """
        field_parsers = [
            FieldHeaderRowGrouped(**self.section_args)
        ]

        return self._parse_fields(field_parsers=field_parsers)
    

class SectionFifteenParser(BaseSection):
    """
    Parsing configuration for section fifteen.
    
    Args:
        sections (List[Tuple[Tag, ...]]): A list of tuples,
            each tuple containing Tag instances representing all
            HTML elements found in a given section.
    """
    def __init__(self, sections: List[Tuple[Tag, ...]]):
        super().__init__(
            name="15. Sales Commissions & Finder's Fees Expenses",
            section=SectionFifteen,
            schema=SectionFifteenSchema,
            sections=sections
        )

    def parse(self) -> SectionFifteen:
        """
        Field parsing for section fifteen.

        Returns:
            SectionFifteen: A pydantic model storing all parsed data
                for section fifteen.
        """
        field_parsers = [
            FieldHeaderRowGrouped(**self.section_args),
            CheckBoxMultiple(**self.section_args)
        ]

        return self._parse_fields(field_parsers=field_parsers)
    

class SectionSixteenParser(BaseSection):
    """
    Parsing configuration for section sixteen.
    
    Args:
        sections (List[Tuple[Tag, ...]]): A list of tuples,
            each tuple containing Tag instances representing all
            HTML elements found in a given section.
    """
    def __init__(self, sections: List[Tuple[Tag, ...]]):
        super().__init__(
            name="16. Use of Proceeds",
            section=SectionSixteen,
            schema=SectionSixteenSchema,
            sections=sections
        )

    def parse(self) -> SectionSixteen:
        """
        Field parsing for section sixteen.

        Returns:
            SectionSixteen: A pydantic model storing all parsed data
                for section sixteen.
        """
        field_parsers = [
            FieldHeaderRowGrouped(**self.section_args),
            CheckBoxMultiple(**self.section_args)
        ]

        return self._parse_fields(field_parsers=field_parsers)
    

class SectionSignatureParser(BaseSection):
    """
    Parsing configuration for the signature section.
    
    Args:
        sections (List[Tuple[Tag, ...]]): A list of tuples,
            each tuple containing Tag instances representing all
            HTML elements found in a given section.
    """
    def __init__(self, sections: List[Tuple[Tag, ...]]):
        super().__init__(
            name="Signature and Submission",
            section=SectionSignature,
            schema=SectionSignatureSchema,
            sections=sections,
            filter_tags=[Tags.TABLE],
            sub_section_merge=['issuer']
        )

    def parse(self) -> SectionSignature:
        """
        Field parsing for the signature section.

        Returns:
            SectionSignature: A pydantic model storing all parsed data
                for section signature.
        """
        field_parsers = [
            FieldHeaderRowConsistent(
                **self.section_args, section_schema=self._schema
            )
        ]

        return self._parse_fields(field_parsers=field_parsers)