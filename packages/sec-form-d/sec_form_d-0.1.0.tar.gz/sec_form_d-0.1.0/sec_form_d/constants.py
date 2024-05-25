from sec_form_d.types.section import SectionTag
from sec_form_d.enums import Attrs, Tags

# Text fields appearing in the form
NONE = 'None'
X_MARK = 'X'

# Strings appearing in numeric fields
NUMERIC_REPLACE = ['$', 'USD', ',']

# Text that appear in the <title> tag of a Form D
SEC_FORM_D_TITLES = {'SEC FORM D', 'SEC FORM D/A'}

# The HTML element indicating the beginning of a section
SECTION_TAG = SectionTag.from_enums(
    tag=Tags.PARAGRAPH, attr=Attrs.CLASS, value='SectionTitle'
)