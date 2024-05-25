from typing import Dict, List, Optional

from sec_form_d.comparison.difference import SectionComparison
from sec_form_d.types.diff import SectionDifference
from sec_form_d.types.form import (
    FormD,
    FormDDifferences,
    SectionDifferences,
    SectionType
)

def differences_by_form(
    current_form: FormD, previous_form: FormD
) -> FormDDifferences:
    """
    Detects all differences for each section between the previous
    and current forms. Returns a FormDDifferences instance with a
    similar structure than a FormD instance. 

    Args:
        current_form (FormD): A Form D instance for the current form.
        preivous_form (FormD): A Form D instance for the previous form.

    Returns:
        FormDDifferences: A FormDDifferences instance containing all
            differences for every section between the previous and
            current forms.
    """
    if (
        not isinstance(current_form, FormD) and
        not isinstance(previous_form, FormD)
    ):
        raise TypeError(
            "both form objects must both be a FormD instance"
        )
    form_differences: Dict[str, SectionDifferences] = dict()
    
    # Retrieve all attributes from each Form instance passed
    current_form_sections: Dict[str, SectionType] = current_form.__dict__
    previous_form_sections: Dict[str, SectionType] = previous_form.__dict__

    # Iterate through each section attribute in Form instance
    # and run difference function for each
    for form_attr, current_section in current_form_sections.items():
        previous_section: SectionType = previous_form_sections[form_attr]

        # Calculate all differences between both sections
        differences: SectionDifferences = differences_by_section(
            current_section=current_section,
            previous_section=previous_section
        )

        form_differences.update({form_attr: differences})

    return FormDDifferences(**form_differences)


def differences_by_section(
    current_section: SectionType,
    previous_section: SectionType
) -> SectionDifferences:
    """
    Detects all differences for a section from the previous
    form and the same section from the current form.
    
    Returns a SectionDifferences instance, a representation
    of all differences between a previous and current version
    of the same section.
    
    Args:
        current_section (SectionType): An instance of a SectionType
            containing all parsed fields for a section from the
            previous form.
        previous_section (SectionType): An instance of a SectionType
            containing all parsed fields for a section from the
            previous form.

    Returns:
        SectionDifferences: A SectionDifferences instance.
    """
    if (
        not isinstance(current_section, SectionType) and
        not isinstance(previous_section, SectionType)
    ):
        raise TypeError(
            "both section objects must be a SectionType instance"
        )

    if type(current_section) != type(previous_section):
        raise TypeError(
            "both section objects must be of the same type"
        )

    # Extract section from each list
    comparison = SectionComparison(
        previous_section=previous_section,
        current_section=current_section
    )

    if current_section.has_sub_sections or previous_section.has_sub_sections:
        differences: SectionDifferences = comparison.field_difference_sub_section()
        return differences
    else:
        differences_to_include: List[SectionDifference] = []

        differences: Optional[SectionDifference] = comparison.field_difference(
            prev_section=comparison.previous_dict,
            cur_section=comparison.current_dict
        )

        if differences is not None:
            differences_to_include.append(differences)

        return SectionDifferences(
            section_name=current_section.name,
            differences=differences_to_include
        )