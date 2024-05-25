from typing import (
    List, 
    Union
)

from pydantic import BaseModel, PrivateAttr

from sec_form_d.types.schema import *
from sec_form_d.types.diff import (
    AddedSection,
    Difference,
    RemovedSection,
    SectionDifference
)

class BaseSection(BaseModel):
    """
    Base class for a section appearing in a FormD instance.
    """
    name: str
    section: Union[BaseSchema, List[BaseSchema]]

    __sub_section_merge: List[str] = PrivateAttr(default_factory=list)

    @property
    def sub_section_merge(self) -> List[str]:
        """A list of string field names being the primary key a sub-section."""
        return self.__sub_section_merge
    
    @sub_section_merge.setter
    def sub_section_merge(self, sub_section_merge: List[str]) -> None:
        self.__sub_section_merge = sub_section_merge

    @property
    def has_sub_sections(self) -> bool:
        """Whether the section has sub-sections."""
        return isinstance(self.section, list)

    @property
    def number_sub_sections(self) -> int:
        """The number of sub-sections appearing in the section."""
        if self.has_sub_sections:
            return len(self.section)
        elif self.section is not None:
            return 1
        else:
            return 0


class SectionOne(BaseSection):
    """A representation of section one."""
    section: Union[List[SectionOneSchema], SectionOneSchema]


class SectionTwo(BaseSection):
    """A representation of section two."""
    section: Union[List[SectionTwoSchema], SectionTwoSchema]


class SectionThree(BaseSection):
    """A representation of section three."""
    section: Union[List[SectionThreeSchema], SectionThreeSchema]


class SectionFour(BaseSection):
    """A representation of section four."""
    section: SectionFourSchema


class SectionFive(BaseSection):
    """A representation of section five."""
    section: SectionFiveSchema


class SectionSix(BaseSection):
    """A representation of section six."""
    section: SectionSixSchema


class SectionSeven(BaseSection):
    """A representation of section seven."""
    section: SectionSevenSchema


class SectionEight(BaseSection):
    """A representation of section eight."""
    section: SectionEightSchema


class SectionNine(BaseSection):
    """A representation of section nine."""
    section: SectionNineSchema


class SectionTen(BaseSection):
    """A representation of section ten."""
    section: SectionTenSchema


class SectionEleven(BaseSection):
    """A representation of section eleven."""
    section: SectionElevenSchema


class SectionTwelve(BaseSection):
    """A representation of section twelve."""
    section: Union[List[SectionTwelveSchema], SectionTwelveSchema]


class SectionThirteen(BaseSection):
    """A representation of section thirteen."""
    section: SectionThirteenSchema


class SectionFourteen(BaseSection):
    """A representation of section fourteen."""
    section: SectionFourteenSchema


class SectionFifteen(BaseSection):
    """A representation of section fifteen."""
    section: SectionFifteenSchema


class SectionSixteen(BaseSection):
    """A representation of section sixteen."""
    section: SectionSixteenSchema


class SectionSignature(BaseSection):
    """A representation of the signature section."""
    section: Union[List[SectionSignatureSchema], SectionSignatureSchema]


class FormD(BaseModel):
    """
    A representation of a parsed Form D, containing fields extracted
    from all sections appearing in the form.
    """
    section_one: SectionOne
    section_two: SectionTwo
    section_three: SectionThree
    section_four: SectionFour
    section_five: SectionFive
    section_six: SectionSix
    section_seven: SectionSeven
    section_eight: SectionEight
    section_nine: SectionNine
    section_ten: SectionTen
    section_eleven: SectionEleven
    section_twelve: SectionTwelve
    section_thirteen: SectionThirteen
    section_fourteen: SectionFourteen
    section_fifteen: SectionFifteen
    section_sixteen: SectionSixteen
    section_signature: SectionSignature


class SectionDifferences(BaseModel):
    """
    Represents all differences found between a previous and
    current version of the same section from Form D

    Args:
        section_name (str): The name of the section.
        differences (List[SectionDifference]): All differences found,
            represented as a list of SectionDifference objects.
        added_sections (List[AddedSection]): All added, or completely new
            sections appearing in the current form. Represented as a list
            of AddedSection objects.
        removed_sections (List[RemovedSection]): All removed, or completely
            missing sections from the current form. Represented as a list
            of RemovedSection objects.
    """
    section_name: str
    differences: List[SectionDifference]
    added_sections: List[AddedSection] = []
    removed_sections: List[RemovedSection] = []

    def differences_by_field(self, field: str) -> List[SectionDifference]:
        """
        Find all differences for a specific field name from a section.

        Args:
            field (str): The name of the field.

        Returns:
            List[SectionDifference]: All differences found, represented
                as a list of SectionDifference objects.
        """
        section_differences: List[SectionDifference] = []

        # Iterate through each difference found
        for section_difference in self.differences:
            differences: List[Difference] = []

            # Iterate through each differnce within each
            # section difference.
            for difference in section_difference.differences:
                if difference.field_name == field:
                    differences.append(difference)
            
            # If there were any differences found for the
            # field specified, then append to list
            if differences:
                section_differences.append(
                    SectionDifference(
                        section=section_difference.section, differences=differences
                    )
                )

        return section_differences

    @property
    def number_differences(self) -> int:
        """The total number of differences."""
        number_differences = 0
        for section_difference in self.differences:
            for _ in section_difference.differences:
                number_differences += 1

        return number_differences
 
    @property
    def number_differing_sections(self) -> int:
        """
        The number of sections that had at least one difference. Even
        though this is a property for one section, there can be
        sub-sections. Thus this number can be greater than one.
        """
        return len(self.differences)

    @property
    def has_differences(self) -> bool:
        """Boolean indicating whether there were any differences for the section."""
        return not (not self.differences)
    
    @property
    def has_added_sections(self) -> bool:
        """Boolean indicating whether there were any added sections."""
        return not (not self.added_sections)
    
    @property
    def has_removed_sections(self) -> bool:
        """Boolean indicating whether there were any removed sections."""
        return not (not self.removed_sections)


class FormDDifferences(BaseModel):
    """"""
    section_one: SectionDifferences
    section_two: SectionDifferences
    section_three: SectionDifferences
    section_four: SectionDifferences
    section_five: SectionDifferences
    section_six: SectionDifferences
    section_seven: SectionDifferences
    section_eight: SectionDifferences
    section_nine: SectionDifferences
    section_ten: SectionDifferences
    section_eleven: SectionDifferences
    section_twelve: SectionDifferences
    section_thirteen: SectionDifferences
    section_fourteen: SectionDifferences
    section_fifteen: SectionDifferences
    section_sixteen: SectionDifferences
    section_signature: SectionDifferences


SectionType = Union[
    SectionOne,
    SectionTwo,
    SectionThree,
    SectionFour,
    SectionFive,
    SectionSix,
    SectionSeven,
    SectionEight,
    SectionNine,
    SectionTen,
    SectionEleven,
    SectionTwelve,
    SectionThirteen,
    SectionFourteen,
    SectionFifteen,
    SectionSixteen,
    SectionSignature
]


SectionSchemaType = Union[
    SectionOneSchema,
    SectionTwoSchema,
    SectionThreeSchema,
    SectionFourSchema,
    SectionFiveSchema,
    SectionSixSchema,
    SectionSevenSchema,
    SectionEightSchema,
    SectionNineSchema,
    SectionTenSchema,
    SectionElevenSchema,
    SectionTwelveSchema,
    SectionThirteenSchema,
    SectionFourteenSchema,
    SectionFifteenSchema,
    SectionSixteenSchema,
    SectionSignatureSchema
]