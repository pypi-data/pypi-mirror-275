from typing import Dict, Type, Union
from os import PathLike

from bs4 import BeautifulSoup

from sec_form_d.validators.validator import FormValidator
from sec_form_d.utils import extract_section_elements
from sec_form_d.constants import SECTION_TAG
from sec_form_d.types.form import (
    FormD, 
    SectionType
)
from sec_form_d.parsing.sections import (
    BaseSection,
    SectionOneParser,
    SectionTwoParser,
    SectionThreeParser,
    SectionFourParser,
    SectionFiveParser,
    SectionSixParser,
    SectionSevenParser,
    SectionEightParser,
    SectionNineParser,
    SectionTenParser,
    SectionElevenParser,
    SectionTwelveParser,
    SectionThirteenParser,
    SectionFourteenParser,
    SectionFifteenParser,
    SectionSixteenParser,
    SectionSignatureParser
)

class FormDParser:
    """
    Drives all parsing of form D.

    Args:
        html_source (str | bytes | PathLike | BeautifulSoup): Either
            a string  containing HTML content, a string path, a path
            like object, or a BeautifulSoup instance.
    """
    def __init__(
        self, 
        html_source: Union[str, bytes, PathLike, BeautifulSoup]
    ):
        validator = FormValidator(html_source=html_source)
        
        self._html = validator.validate_html()
        self._html_body = validator.validate_form(html=self._html)
        
        # Extract section elements from HTML
        self._sections = extract_section_elements(
            html=self._html_body, section_tag=SECTION_TAG
        )

        self.section_args = {
            'sections': self._sections
        }

    def parse_form(self) -> FormD:
        """
        Executes parsing for each section existing in form and
        structures and returns results as a FormD instance.

        Returns:
            FormD: A FormD instance.
        """
        section_parsers: Dict[str, Type[BaseSection]] = {
            'section_one': SectionOneParser,
            'section_two': SectionTwoParser,
            'section_three': SectionThreeParser,
            'section_four': SectionFourParser,
            'section_five': SectionFiveParser,
            'section_six': SectionSixParser,
            'section_seven': SectionSevenParser,
            'section_eight': SectionEightParser,
            'section_nine': SectionNineParser,
            'section_ten': SectionTenParser,
            'section_eleven': SectionElevenParser,
            'section_twelve': SectionTwelveParser,
            'section_thirteen': SectionThirteenParser,
            'section_fourteen': SectionFourteenParser,
            'section_fifteen': SectionFifteenParser,
            'section_sixteen': SectionSixteenParser,
            'section_signature': SectionSignatureParser,
        }

        form_args: Dict[str, SectionType] = {
            arg: section(**self.section_args).parse()
            for arg, section in section_parsers.items()
        }

        return FormD(**form_args)