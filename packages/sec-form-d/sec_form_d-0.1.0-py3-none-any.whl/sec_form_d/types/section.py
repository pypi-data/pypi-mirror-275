from dataclasses import dataclass

from sec_form_d.enums import Attrs, Tags

@dataclass
class SectionTag:
    """
    Information for an HTML element/tag.

    Args:
        tag (str): The name of the tag.
        attr (str): The name of the attribute.
        value (str): The attribute value.
    """
    tag: str
    attr: str
    value: str

    @classmethod
    def from_enums(
        cls, tag: Tags, attr: Attrs, value: str
    ) -> 'SectionTag':
        return cls(
            tag=tag.value, attr=attr.value, value=value
        )