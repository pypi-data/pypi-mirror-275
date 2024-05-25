from typing import (
    Any, 
    Dict, 
    List,
    Optional,
    Union
)

from sec_form_d.comparison.comparison_utils import is_empty_dictionary
from sec_form_d.types.form import (
    SectionDifferences,
    SectionType
)
from sec_form_d.types.diff import (
    AddedSection,
    Difference,
    RemovedSection,
    SectionDifference
)

DifferenceData = Union[Difference, RemovedSection, AddedSection]

class SectionComparison:
    """
    A class for comparing two instances of a SectionType type, each
    representing a section from different forms.

    This class is designed to facilitate the comparison of all fields
    between a section from a previous form and the same section from a
    current form. It converts each section into a dictionary for easier
    comparison of individual fields.

    Args:
        previous_section (SectionType): An instance of a SectionType
            containing all parsed fields for a section from the
            previous form.
        current_section (SectionType): An instance of a SectionType
            containing all parsed fields for a section from the
            current form.
    """
    def __init__(
        self, 
        previous_section: SectionType,
        current_section: SectionType
    ):
        self.previous_section = previous_section
        self.current_section = current_section

        # Turn each section dictionary into a dictionary
        self.previous_dict = SectionComparison.__standardize_model_dump(
            form_section=self.previous_section
        )
        self.current_dict = SectionComparison.__standardize_model_dump(
            form_section=self.current_section
        )

    @staticmethod
    def __standardize_model_dump(
        form_section: SectionType
    ) -> Union[Dict[str, Any], List[Dict[str, Any]]]:
        """
        A private static method to serialize the pydantic model whether
        it is a list of section objects or a singular section object. 
        """
        if isinstance(form_section.section, list):
            return [section.model_dump() for section in form_section.section]
        else:
            return form_section.section.model_dump()

    @staticmethod
    def __standardize_sub_sections(
        section: Union[Dict[str, Any], List[Dict[str, Any]]]
    ) -> List[Dict[str, Any]]:
        """
        A private static method to convert a singular pydantic model
        into a single element list for section comparisons that
        involve sub-sections.
        """
        return [section] if not isinstance(section, list) else section

    def field_difference_sub_section(self) -> SectionDifferences:
        """
        Find all differences for sub-sections within a section between
        the previous and current forms. Because there are sections that
        can have multiple sub-sections and the number can differ from
        previous to current form, we need to match each current sub-section
        with the corresponding previous sub-section.

        If we cannot find one, then we assume that sub-section has been
        added. We also do this with the previous sub-sections. If we cannot
        match a previous sub-section with a current one, then we assume
        that it has been removed.

        If there is a match found then we run the field_difference method
        to find all differences. All differences are then grouped into a
        SectionDifferences model.

        Returns:
            SectionDifferences: A pydantic model representing all added
                sections, removed sections, and differences between the
                the previous and current sections.
        """
        def generate_index_key(section: dict) -> str:
            return (
                '__'.join(
                    section[key] for key in self.current_section.sub_section_merge
                )
            )

        # Extract all sub-section fields
        previous_sub_sections: List[dict] = SectionComparison.__standardize_sub_sections(
            section=self.previous_dict
        )
        current_sub_sections: List[dict] = SectionComparison.__standardize_sub_sections(
            section=self.current_dict
        )

        # Ensure that primary keys have been specified
        if not self.current_section.sub_section_merge:
            raise ValueError(
                "there must be primary keys specified if sub-sections exist"
            )

        # Iterate through each current sub-section and then each
        # previous sub-section to find a match
        current_sections_matched: List[dict] = []
        previous_sections_matched: List[dict] = []

        # Create previous sectison index
        previous_section_index: Dict[str, Dict[str, Any]] = {
            generate_index_key(section=prev_section): prev_section
            for prev_section in previous_sub_sections
        }

        for cur_section in current_sub_sections[:]:
            index_key: str = generate_index_key(section=cur_section)
            previous_section_match: Optional[Dict[str, Any]] = (
                previous_section_index.get(index_key)
            )

            if previous_section_match is not None:
                current_sections_matched.append(cur_section)
                previous_sections_matched.append(previous_section_match)

                # Delete matched item from previous list
                previous_sub_sections.remove(previous_section_match)
                current_sub_sections.remove(cur_section)

        # Find all differences within matched sections
        differences: List[SectionDifference] = []
        for idx, _ in enumerate(current_sections_matched):
            previous_section_dict: Dict[str, Any] = previous_sections_matched[idx]
            current_section_dict: Dict[str, Any] = current_sections_matched[idx]

            # Find differences between sub-sections
            sub_section_differences: Optional[SectionDifference] = self.field_difference(
                prev_section=previous_section_dict,
                cur_section=current_section_dict
            )

            if sub_section_differences is not None:
                differences.append(sub_section_differences)
        
        # We are then left with any section that did not match in both current
        # and previous sub-section lists. Thus, these are all treated as new
        added_sections: List[AddedSection] = []
        removed_sections: List[RemovedSection] = []
        for section in current_sub_sections + previous_sub_sections:
            if not is_empty_dictionary(obj=section):
                if (
                    section in current_sub_sections and
                    section not in previous_sub_sections
                ):
                    added_sections.append(AddedSection(section=section))
                elif (
                    section in previous_sub_sections and
                    section not in current_sub_sections
                ):
                    removed_sections.append(RemovedSection(section=section))

        return SectionDifferences(
            section_name=self.current_section.name,
            differences=differences,
            added_sections=added_sections,
            removed_sections=removed_sections
        )

    @staticmethod
    def __field_difference(
        prev_dict: Dict[str, Any], cur_dict: Dict[str, Any]
    ) -> List[Difference]:
        """
        A private method which recursively finds all differences
        between two dictionaries.

        Args:
            prev_dict (Dict[str, Any]): A dictionary representing fields
                from the previous section.
            cur_dict (Dict[str, Any]): A dictionary representing fields
                from the current section.

        Returns
            List[Difference]: A list of Difference objects each representing
                a difference for a field for a specific section.
        """
        differences: List[Difference] = []

        # Iterate through each key in current dictionary and
        # compare current and previous values
        for key in cur_dict.keys():
            prev_value = prev_dict[key]
            cur_value = cur_dict[key]

            # If both values are dictionaries
            if isinstance(prev_value, dict) and isinstance(cur_value, dict):
                differences.extend(
                    SectionComparison.__field_difference(
                        prev_dict=prev_value, cur_dict=cur_value
                    )
                )

            # If both values are lists
            elif isinstance(prev_value, list) and isinstance(cur_value, list):
                for idx, _ in enumerate(prev_value):
                    differences.extend(
                        SectionComparison.__field_difference(
                            prev_dict=prev_value[idx], cur_dict=cur_value[idx]
                        )
                    )

            # If there is a difference between the values
            elif prev_value != cur_value:
                differences.append(
                    Difference(
                        field_name=key,
                        previous_value=prev_value,
                        current_value=cur_value
                    )
                )
        return differences

    def field_difference(
        self, prev_section: Dict[str, Any], cur_section: Dict[str, Any]
    ) -> Optional[SectionDifference]:
        """
        A method which runs a recursive method to find all
        differences between the previous and current sections.

        Args:
            prev_section (Dict[str, Any]): A dictionary representation of
                the previous section.
            cur_section (Dict[str, Any]): A dictionary representation of
                the current section.

        Returns:
            SectionDifference | None: A SectionDiffernce object representing
                all differences between the previous and current sections. Will
                return None if there were no differences found.
        """
        differences: List[Difference] = SectionComparison.__field_difference(
            prev_dict=prev_section, cur_dict=cur_section
        )

        if differences:
            return SectionDifference(
                section=cur_section, differences=differences
            )
        else:
            return