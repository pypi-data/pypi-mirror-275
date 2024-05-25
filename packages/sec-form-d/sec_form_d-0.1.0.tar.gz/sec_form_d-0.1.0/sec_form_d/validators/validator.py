from typing import Optional, Union
from os import PathLike
import os

from bs4 import BeautifulSoup, Tag

from sec_form_d.exceptions import InvalidFormError
from sec_form_d.constants import SEC_FORM_D_TITLES
from sec_form_d.validators.html import _read_html_source
from sec_form_d.logger import set_up_logger

_FILE_TYPES = {".html", ".htm", ".xml"}

logger = set_up_logger(__name__)

class FormValidator:
    """
    Provides methods to validate the the file is an HTML file,
    and that it is also a Form D.

    Args:
        html_source (str | bytes | PathLike | BeautifulSoup): Either
            a string  containing HTML content, a string path, a path
            like object, or a BeautifulSoup instance.
    """
    def __init__(
        self,
        html_source: Union[str, bytes, PathLike, BeautifulSoup]
    ):
        self.html_source = html_source

    def validate_form(self, html: BeautifulSoup) -> Tag:
        """
        Accepts a BeautifulSoup instance, validates that the
        form is indeed a Form D, and returns the <body> tag.

        Args:
            html (BeautifulSoup): A BeautifulSoup instance.

        Returns:
            Tag: A Tag instance representing the <body> tag
                of the HTML file.
        """
        form_head: Optional[Tag] = html.find('head')

        # Each Form D must contain a <head> tag
        if form_head is not None:
            form_title: Optional[Tag] = form_head.find('title')

            # Each form D must also contain a <title> tag. If
            # the <title> tag can be found, then a variation of
            # the string 'SEC FORM D' must appear in the text
            # property of that tag
            if form_title is not None:
                if form_title.text.strip() in SEC_FORM_D_TITLES:

                    # If we can validate the <title>, then the <body>
                    # tag is found and returned
                    form_body: Optional[Tag] = html.find('body')
                    if form_body is not None:
                        return form_body
                
        raise InvalidFormError("html file passed is not a valid Form D")

    def validate_html(self) -> BeautifulSoup:
        """
        Processes and converts the HTML content passed into
        a BeautifulSoup instance.
        
        Returns:
            BeautifulSoup: A BeautifulSoup instance.
        """
        if isinstance(self.html_source, BeautifulSoup):
            return self.html_source
        
        # If a string or PathLike object is passed, it is either
        # a path to a file, or an HTML file that has been read in
        # as a string or bytes
        elif isinstance(self.html_source, (str, PathLike)):

            # If the object passed in is a file path
            if os.path.isfile(self.html_source):
                _, extension = os.path.splitext(os.path.abspath(self.html_source))
                if extension not in _FILE_TYPES:
                    logger.warning(
                        "extension of source file is not a recognized HTML/XML extension"
                    )

                # Read as bytes and return as a BeautifulSoup instance
                with open(self.html_source, mode='rb') as content:
                    return _read_html_source(html_content=content.read())
                
            # If a string representation of the HTML file
            # was passed
            else:
                return _read_html_source(html_content=self.html_source)
            
        # If a bytes representation of the HTML file was passed
        elif isinstance(self.html_source, bytes):
            return _read_html_source(html_content=self.html_source)
        
        # Raise a type error if an unexpected type was passed
        else:
            raise TypeError(
                f"{type(self.html_source)} is not a valid type for 'html_source'"
            )