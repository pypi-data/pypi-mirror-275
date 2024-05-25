from typing import Optional, Union
import re
from re import Match

from bs4 import BeautifulSoup
import charset_normalizer
from charset_normalizer import CharsetMatch

from sec_form_d.exceptions import HTMLConversionError

def __clean_encoding_match(encoding: str) -> str:
    """Standardize string encoding match found in HTML."""
    return encoding.lower().replace('_', '-')


def __detect_file_encoding(html_content: Union[bytes, str]) -> Optional[str]:
    """
    Private method to detect the encoding from HTML file.

    If a bytes object is passed then will try to detect
    encoding from the bytes. Otherwise, if a string is
    passed, then regex is used to search for the charset
    value contained in the <meta> tag.

    Args:
        html_content (bytes | str): A string or bytes representation
            of the HTML file.

    Returns:
        str | None: A string character encoding. Can return None
            if no encoding was detected or found.
    """
    if isinstance(html_content, bytes):
        encoding: Optional[CharsetMatch] = (
            charset_normalizer.from_bytes(html_content).best()
        )
        return encoding.encoding
    else:
        charset_match: Optional[Match] = re.search(
            r'<meta.*?charset=["\']?([\w-]+)', html_content, re.IGNORECASE
        )
        if charset_match is not None:
            encoding_match: str = charset_match.group(1)
            return __clean_encoding_match(encoding=encoding_match)
        else:
            return


def _read_html_source(html_content: Union[bytes, str]) -> BeautifulSoup:
    """
    Private method to convert a bytes or string object into
    a BeautifulSoup instance.

    Will detect the encoding of the object and then read in
    the content into a BeautifulSoup instance.

    Args:
        html_content (bytes | str): A string or bytes representation
            of the HTML file.

    Returns:
        BeautifulSoup: A BeautifulSoup instance.
    """
    encoding: Optional[str] = __detect_file_encoding(html_content=html_content)

    try:
        return BeautifulSoup(
            html_content, 'html.parser', from_encoding=encoding
        )
    except UnicodeDecodeError:
        raise HTMLConversionError(
            "issue occured when decoding source content"
        )
    except Exception:
        raise HTMLConversionError(
            "unexpected issue occured when converting source to HTML"
        )