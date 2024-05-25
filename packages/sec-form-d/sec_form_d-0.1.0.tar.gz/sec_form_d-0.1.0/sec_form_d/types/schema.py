from typing import (
    Any, 
    Dict,
    List,
    Optional,
    Set,
    Union
)

from pydantic import (
    BaseModel, 
    Field,
    field_validator,
    ValidationError
)

from sec_form_d.constants import NUMERIC_REPLACE
from sec_form_d.exceptions import InvalidSectionError

def _numeric_validation(number: Union[str, int]) -> Optional[Union[str, int]]:
    """
    Private function to validate a string representation of a numeric value
    in the form.
    """
    if isinstance(number, str):
        for string in NUMERIC_REPLACE:
            number = number.replace(string, '')
        
        if number:
            return number
        else:
            return
    else:
        return number


class BaseSchema(BaseModel):
    """
    Base pydantic model for all schemas.
    """
    def model_post_init(self, __context: Any) -> None:
        from sec_form_d.utils import detect_fields
        self.__fields, self.__single, self.__multiple = detect_fields(
            section_schema=type(self)
        )

    @property
    def number_checkboxes(self) -> int:
        """The number of checkboxes apearing in section."""
        return len(self.__single) + len(self.__multiple)

    @property
    def number_fields(self) -> int:
        """The number of non-checkbox fields apearing in section."""
        return len(self.__fields)

    @property
    def single_checkbox_attributes(self) -> Set[str]:
        """A set of all checkbox attribute names."""
        return {checkbox.attr_name for checkbox in self.__single}

    @property
    def multiple_checkbox_attributes(self) -> Set[str]:
        """A set of all multiple-checkbox attribute names."""
        return {checkbox.attr_name for checkbox in self.__multiple}

    @property
    def field_attributes(self) -> Set[str]:
        """A set of all non-checkbox field attribute names."""
        return {field.attr_name for field in self.__fields}

    @property
    def single_checkboxes(self) -> Union[Dict[str, Any], List[Dict[str, Any]]]:
        """A serialization of all single checkboxes from model."""
        return self.__retrieve_attributes(attributes=self.single_checkbox_attributes)

    @property
    def multiple_checkboxes(self) -> Union[Dict[str, Any], List[Dict[str, Any]]]:
        """A serialization of all multiple checkboxes from model."""
        return self.__retrieve_attributes(attributes=self.multiple_checkbox_attributes)

    @property
    def fields(self) -> Union[Dict[str, Any], List[Dict[str, Any]]]:
        """A serialization of all non-checkbox fields from model."""
        return self.__retrieve_attributes(attributes=self.field_attributes)

    def __retrieve_attributes(self, attributes: List[str]) -> Dict[str, Any]:
        """
        Private method to selectively serialize portions of the model
        based on a list of attribute names.
        """
        section_filtered: Dict[str, Any] = dict()
        section_model_dump: Dict[str, Any] = self.model_dump()
        for attribute in attributes:
            section_filtered.update({attribute: section_model_dump[attribute]})
        return section_filtered

    def __gather_checked_checkboxes(self, dictionary: Dict[str, Any]) -> Dict[str, Any]:
        """
        Private recursive method to find all checked checkboxes from model.
        """
        checked_checkboxes: Dict[str, Any] = dict()

        # Iterate through each key (attribute name),
        # value (attribute value) pair in dictionary
        for key, value in dictionary.items():

            # If the attribute is a single checkbox then
            # update checked checkbox dictionary if it has
            # been checked
            if key in self.single_checkbox_attributes:
                if value:
                    checked_checkboxes.update({key: value})

            # Otherwise, if it is multiple checkbox, then recursively
            # run the function to get all checked nested single checkboxes
            elif key in self.multiple_checkbox_attributes:
                checked_checkboxes_multiple: Dict[str, Any] = {
                    k: v for k, v in
                    self.__gather_checked_checkboxes(dictionary=value).items()
                }
                
                # If any checkboxes within the multiple checkboxes
                # were found to be checked, then update the
                # checkbox dictionary
                if checked_checkboxes_multiple:
                    checked_checkboxes.update(
                        {key: checked_checkboxes_multiple}
                    )
        return checked_checkboxes

    @property
    def checked_checkboxes(self) -> Dict[str, Any]:
        """Returns a serialization of all checked checkboxes."""
        return self.__gather_checked_checkboxes(
            dictionary=dict(self.single_checkboxes, **self.multiple_checkboxes)
        )

    @classmethod
    def model_validate(cls, fields: Dict[str, Any]) -> BaseModel:
        """Custom model validation class method."""
        try:
            return super().model_validate(fields)
        except ValidationError:
            raise InvalidSectionError(
                message='error when validating contents of section from form'
            )


class BaseCheckboxYesNo(BaseModel):
    """Pydantic model for checkboxes that have Yes and No."""
    yes: bool = Field(..., title='Yes')
    no: bool = Field(..., title='No')


class CheckboxEntityType(BaseModel):
    """Pydantic model for the entity type checkbox."""
    corporation: bool = Field(..., title='Corporation')
    limited_partnership: bool = Field(..., title='Limited Partnership')
    limited_liability_co: bool = Field(..., title='Limited Liability Company')
    general_partnership: bool = Field(..., title='General Partnership')
    business_trust: bool = Field(..., title='Business Trust')
    other: bool = Field(..., title='Other (Specify)')


class CheckboxYearofIncorporation(BaseModel):
    """Pydantic model for the year of incorporation checkbox."""
    over_five_years_ago: bool = Field(..., title='Over Five Years Ago')
    within_last_five_years: bool = Field(
        ..., title='Within Last Five Years (Specify Year)'
    )
    yet_to_be_formed: bool = Field(..., title='Yet to Be Formed')
    

class CheckboxRelationship(BaseModel):
    """Pydantic model for the relationship checkbox."""
    executive_officer: bool = Field(..., title='Executive Officer')
    director: bool = Field(..., title='Director')
    promoter: bool = Field(..., title='Promoter')


class CheckboxIssuerRegistered(BaseCheckboxYesNo):
    """Derived from the BaseCheckboxYesNo model."""
    pass


class CheckboxRevenueRange(BaseModel):
    """Pydantic model for the revenue range checkbox."""
    no_revenues: bool = Field(..., title='No Revenues')
    one_to_one_mil: bool = Field(..., title='$1 - $1,000,000')
    one_mil_to_five_mil: bool = Field(..., title='$1,000,001 - $5,000,000')
    five_to_twenty_five_mil: bool = Field(..., title='$5,000,001 - $25,000,000')
    twenty_five_to_one_hundred_mil: bool = Field(..., title='$25,000,001 - $100,000,000')
    over_one_hundred_mil: bool = Field(..., title='Over $100,000,000')
    decline_to_disclose: bool = Field(..., title='Decline to Disclose')
    not_applicable: bool = Field(..., title='Not Applicable')


class CheckboxNavRange(BaseModel):
    """Pydantic model for the nav range checkbox."""
    no_net_asset_value: bool = Field(..., title='No Aggregate Net Asset Value')
    one_mil_to_five_mil: bool = Field(..., title='$1,000,001 - $5,000,000')
    five_to_twenty_five_mil: bool = Field(..., title='$5,000,001 - $25,000,000')
    twenty_five_to_one_hundred_mil: bool = Field(..., title='$25,000,001 - $100,000,000')
    over_one_hundred_mil: bool = Field(..., title='Over $100,000,000')
    decline_to_disclose: bool = Field(..., title='Decline to Disclose')
    not_applicable: bool = Field(..., title='Not Applicable')


class CheckboxOfferingIntention(BaseCheckboxYesNo):
    """Derived from the BaseCheckboxYesNo model."""
    pass


class CheckboxBusinessTransaction(BaseCheckboxYesNo):
    """Derived from the BaseCheckboxYesNo model."""
    pass


class CheckboxStateofSolication(BaseModel):
    """Pydantic model for the solicitation state checkbox."""
    all_states: bool = Field(..., title='All States')


class CheckboxIndefiniteAmount(BaseModel):
    """Pydantic model for the indefinite amount checkbox."""
    indefinite: bool = Field(..., title='Indefinite')


class CheckboxEstimateAmount(BaseModel):
    """Pydantic model for the estimate amount checkbox."""
    estimate: bool = Field(..., title='Estimate')


class SectionOneSchema(BaseSchema):
    """Pydantic model for section one."""
    cik: str = Field(..., title='CIK (Filer ID Number)')
    previous_names: Optional[str] = Field(..., title='Previous Names')
    issuer_name: str = Field(..., title='Name of Issuer')
    jurisdiction: str = Field(..., title='Jurisdiction of Incorporation/Organization')
    entity_type: CheckboxEntityType = Field(..., title='Entity Type')
    year_of_incorporation: CheckboxYearofIncorporation = Field(
        ..., title='Year of Incorporation/Organization'
    )


class SectionTwoSchema(BaseSchema):
    """Pydantic model for section two."""
    issuer_name: str = Field(..., title='Name of Issuer')
    street_address_1: str = Field(..., title='Street Address 1')
    street_address_2: Optional[str] = Field(..., title='Street Address 2')
    city: str = Field(..., title='City')
    state_or_country: str = Field(..., title='State/Province/Country')
    zip_code: str = Field(..., title='ZIP/PostalCode')
    phone_number: str = Field(..., title='Phone Number of Issuer')


class SectionThreeSchema(BaseSchema):
    """Pydantic model for section three."""
    last_name: str = Field(..., title='Last Name')
    first_name: str = Field(..., title='First Name')
    middle_name: Optional[str] = Field(..., title='Middle Name')
    street_address_1: str = Field(..., title='Street Address 1')
    street_address_2: Optional[str] = Field(..., title='Street Address 2')
    city: str = Field(..., title='City')
    state_or_country: str = Field(..., title='State/Province/Country')
    zip_code: str = Field(..., title='ZIP/PostalCode')
    relationship: CheckboxRelationship = Field(..., title='Relationship:')
    clarification_of_response: Optional[str] = Field(
        ..., title='Clarification of Response (if Necessary):'
    )


class SectionFourSchema(BaseSchema):
    """Pydantic model for section four."""
    agriculture: bool = Field(..., title='Agriculture')
    commercial_banking: bool = Field(..., title='Commercial Banking')
    insurance: bool = Field(..., title='Insurance')
    investing: bool = Field(..., title='Investing')
    investment_banking: bool = Field(..., title='Investment Banking')
    pooled_investment_fund: bool = Field(..., title='Pooled Investment Fund')
    issuer_registered_under_ICA_of_1940: CheckboxIssuerRegistered = Field(
        ..., title='Is the issuer registered as an investment company under the Investment Company Act of 1940?'
    )
    other_banking_and_financial_services: bool = Field(..., title='Other Banking & Financial Services')
    business_services: bool = Field(..., title='Business Services')
    coal_mining: bool = Field(..., title='Coal Mining')
    electric_utilities: bool = Field(..., title='Electric Utilities')
    energy_conservation: bool = Field(..., title='Energy Conservation')
    environmental_services: bool = Field(..., title='Environmental Services')
    oil_and_gas: bool = Field(..., title='Oil & Gas')
    other_energy: bool = Field(..., title='Other Energy')
    biotechnology: bool = Field(..., title='Biotechnology')
    health_insurance: bool = Field(..., title='Health Insurance')
    hospitals_and_physicians: bool = Field(..., title='Hospitals & Physicians')
    pharmaceuticals: bool = Field(..., title='Pharmaceuticals')
    other_health_care: bool = Field(..., title='Other Health Care')
    manufacturing: bool = Field(..., title='Manufacturing')
    commercial: bool = Field(..., title='Commercial')
    construction: bool = Field(..., title='Construction')
    reits_and_finance: bool = Field(..., title='REITS & Finance')
    residential: bool = Field(..., title='Residential')
    other_real_estate: bool = Field(..., title='Other Real Estate')
    retailing: bool = Field(..., title='Retailing')
    restaurants: bool = Field(..., title='Restaurants')
    computers: bool = Field(..., title='Computers')
    telecommunications: bool = Field(..., title='Telecommunications')
    other_technology: bool = Field(..., title='Other Technology')
    airlines_and_airports: bool = Field(..., title='Airlines & Airports')
    lodging_and_conventions: bool = Field(..., title='Lodging & Conventions')
    tourism_and_travel_services: bool = Field(..., title='Tourism & Travel Services')
    other_travel: bool = Field(..., title='Other Travel')
    other: bool = Field(..., title='Other')


class SectionFiveSchema(BaseSchema):
    """Pydantic model for section five."""
    revenue_range: CheckboxRevenueRange = Field(..., title='Revenue Range')
    nav_range: CheckboxNavRange = Field(..., title='Aggregate Net Asset Value Range')


class SectionSixSchema(BaseSchema):
    """Pydantic model for section six."""
    rule_504_b: bool = Field(..., title='Rule 504(b)(1) (not (i), (ii) or (iii))')
    rule_504_b_1_i: bool = Field(..., title='Rule 504 (b)(1)(i)')
    rule_504_b_1_ii: bool = Field(..., title='Rule 504 (b)(1)(ii)')
    rule_504_b_1_iii: bool = Field(..., title='Rule 504 (b)(1)(iii)')
    rule_506_b: bool = Field(..., title='Rule 506(b)')
    rule_506_c: bool = Field(..., title='Rule 506(c)')
    securities_act_section_4_a_5: bool = Field(..., title='Securities Act Section 4(a)(5)')
    investment_company_act_section_3_c: bool = Field(
        ..., title='Investment Company Act Section 3(c)'
    )
    section_3_c_1: bool = Field(..., title='Section 3(c)(1)')
    section_3_c_2: bool = Field(..., title='Section 3(c)(2)')
    section_3_c_3: bool = Field(..., title='Section 3(c)(3)')
    section_3_c_4: bool = Field(..., title='Section 3(c)(4)')
    section_3_c_5: bool = Field(..., title='Section 3(c)(5)')
    section_3_c_6: bool = Field(..., title='Section 3(c)(6)')
    section_3_c_7: bool = Field(..., title='Section 3(c)(7)')
    section_3_c_9: bool = Field(..., title='Section 3(c)(9)')
    section_3_c_10: bool = Field(..., title='Section 3(c)(10)')
    section_3_c_11: bool = Field(..., title='Section 3(c)(11)')
    section_3_c_12: bool = Field(..., title='Section 3(c)(12)')
    section_3_c_13: bool = Field(..., title='Section 3(c)(13)')
    section_3_c_14: bool = Field(..., title='Section 3(c)(14)')


class SectionSevenSchema(BaseSchema):
    """Pydantic model for section seven."""
    new_notice: bool = Field(..., title='New Notice')
    first_sale_yet_to_occur: bool = Field(..., title='First Sale Yet to Occur')
    amendment: bool = Field(..., title='Amendment')
    date_of_first_sale: Optional[str] = Field(..., title='Date of First Sale')


class SectionEightSchema(BaseSchema):
    """Pydantic model for section eight."""
    offering_intention: CheckboxOfferingIntention = Field(
        ..., title='Does the Issuer intend this offering to last more than one year?'
    )


class SectionNineSchema(BaseSchema):
    """Pydantic model for section nine."""
    equity: bool = Field(..., title='Equity')
    debt: bool = Field(..., title='Debt')
    pooled_fund: bool = Field(..., title='Pooled Investment Fund Interests')
    tenant_securities: bool = Field(..., title='Tenant-in-Common Securities')
    mineral_securities: bool = Field(..., title='Mineral Property Securities')
    options_warrants: bool = Field(..., title='Option, Warrant or Other Right to Acquire Another Security')
    security_acquired: bool = Field(
        ..., title='Security to be Acquired Upon Exercise of Option, Warrant or Other Right to Acquire Security'
    )
    other: bool = Field(..., title='Other (describe)')


class SectionTenSchema(BaseSchema):
    """Pydantic model for section ten."""
    business_transaction: CheckboxBusinessTransaction = Field(
        ..., title='Is this offering being made in connection with a business combination transaction, such as a merger, acquisition or exchange offer?'
    )
    clarification_of_response: Optional[str] = Field(
        ..., title='Clarification of Response (if Necessary):'
    )


class SectionElevenSchema(BaseSchema):
    """Pydantic model for section eleven."""
    minimum_investment: int = Field(
        ..., title='Minimum investment accepted from any outside investor'
    )

    @field_validator('minimum_investment', mode='before')
    @classmethod
    def validate_investement(cls, investment: Union[str, int]) -> Union[str, int]:
        return _numeric_validation(number=investment)


class SectionTwelveSchema(BaseSchema):
    """Pydantic model for section twelve."""
    recipient: Optional[str] = Field(..., title='Recipient')
    recipient_crd: Optional[str] = Field(..., title='Recipient CRD Number')
    broker_or_dealer: Optional[str] = Field(..., title='(Associated) Broker or Dealer')
    broker_or_dealer_crd: Optional[str] = Field(..., title='(Associated) Broker or Dealer CRD Number')
    street_address_1: Optional[str] = Field(..., title='Street Address 1')
    street_address_2: Optional[str] = Field(..., title='Street Address 2')
    city: Optional[str] = Field(..., title='City')
    state_or_country: Optional[str] = Field(..., title='State/Province/Country')
    zip_code : Optional[str] = Field(..., title='ZIP/Postal Code')
    state_of_solicitation: CheckboxStateofSolication = Field(
        ..., title='State(s) of Solicitation (select all that apply)Check “All States” or check individual States'
    )
    foreign: bool = Field(..., title='Foreign/non-US')


class SectionThirteenSchema(BaseSchema):
    """Pydantic model for section thirteen."""
    offering_amount: Optional[int] = Field(..., title='Total Offering Amount')
    offering_amount_indefinite: CheckboxIndefiniteAmount = Field(..., title='Total Offering Amount')
    amount_sold: Optional[int] = Field(..., title='Total Amount Sold')
    remaining_sold: Optional[int] = Field(..., title='Total Remaining to be Sold')
    remaining_sold_indefinite: CheckboxIndefiniteAmount = Field(
        ..., title='Total Remaining to be Sold'
    )
    clarification_of_response: Optional[str] = Field(
        ..., title='Clarification of Response (if Necessary):'
    )

    @field_validator(
        'offering_amount', 'amount_sold', 'remaining_sold', mode='before'
    )
    @classmethod
    def validate_amounts(cls, amount: Union[str, int]) -> Optional[Union[str, int]]:
        return _numeric_validation(number=amount)


class SectionFourteenSchema(BaseSchema):
    """Pydantic model for section fourteen."""
    num_non_accredited: Optional[int] = Field(
        ..., title='Select if securities in the offering have been or may be sold to persons who do not qualify as accredited investors, and enter the number of such non-accredited investors who already have invested in the offering.'
    )
    num_investors: Optional[int] = Field(
        ..., title='Regardless of whether securities in the offering have been or may be sold to persons who do not qualify as accredited investors, enter the total number of investors who already have invested in the offering:'
    )

    @field_validator('num_non_accredited', 'num_investors', mode='before')
    @classmethod
    def validate_investors(cls, investors: Union[str, int]) -> Optional[Union[str, int]]:
        return _numeric_validation(number=investors)


class SectionFifteenSchema(BaseSchema):
    """Pydantic model for section fifteen."""
    sales_commisions: int = Field(..., title='Sales Commissions')
    sales_commisions_estimate: CheckboxEstimateAmount = Field(
        ..., title='Sales Commissions'
    )
    finders_fees: int = Field(..., title="Finders' Fees")
    finders_fees_estimate: CheckboxEstimateAmount = Field(..., title="Finders' Fees")
    clarification_of_response: Optional[str] = Field(
        ..., title='Clarification of Response (if Necessary):'
    )

    @field_validator('sales_commisions', 'finders_fees', mode='before')
    @classmethod
    def validate_sales(cls, sales: Union[str, int]) -> Union[str, int]:
        return _numeric_validation(number=sales)


class SectionSixteenSchema(BaseSchema):
    """Pydantic model for section sixteen."""
    gross_proceeds: int = Field(
        ..., title='Provide the amount of the gross proceeds of the offering that has been or is proposed to be used for payments to any of the persons required to be named as executive officers, directors or promoters in response to Item 3 above. If the amount is unknown, provide an estimate and check the box next to the amount.'
    )
    gross_proceeds_estimate: CheckboxEstimateAmount = Field(
        ..., title='Provide the amount of the gross proceeds of the offering that has been or is proposed to be used for payments to any of the persons required to be named as executive officers, directors or promoters in response to Item 3 above. If the amount is unknown, provide an estimate and check the box next to the amount.'
    )
    clarification_of_response: Optional[str] = Field(
        ..., title='Clarification of Response (if Necessary):'
    )

    @field_validator('gross_proceeds', mode='before')
    @classmethod
    def validate_proceeds(cls, proceeds: Union[str, int]) -> Union[str, int]:
        return _numeric_validation(number=proceeds)


class SectionSignatureSchema(BaseSchema):
    """Pydantic model for the signature section."""
    issuer: str = Field(..., title='Issuer')
    signature: str = Field(..., title='Signature')
    signer_name: str = Field(..., title='Name of Signer')
    title: str = Field(..., title='Title')
    date: str = Field(..., title='Date')