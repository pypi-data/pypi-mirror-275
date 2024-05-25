from dataclasses import dataclass
from typing import Any, Dict, List, Optional
from abc import ABC, abstractmethod

#### Field type dataclasses used in schemas

@dataclass
class BaseFieldType:
    """
    A base field type class, representing a field
    existing within a section.

    Args:
        field_name (str): The name of the field appearing
            in the form.
        attr_name (str): The name of the attribute in the
            section schema that corresponds to the field
            name appearing in the section.
    """
    field_name: str
    attr_name: str


@dataclass
class FieldType(BaseFieldType):
    """
    Represents a non-checkbox data field within a form.
    """
    pass


@dataclass
class CheckBoxSingleType(BaseFieldType):
    """
    Represents a single checkbox within a form.
    """
    pass


@dataclass
class CheckBoxMultipleType(BaseFieldType):
    """
    Represents a multiple checkbox within a form. That is,
    a group of single checkboxes that are related and are
    grouped together.

    Args:
        fields (List[CheckBoxSingleType]): A list of CheckBoxSingleType
            objects that are grouped within the multiple checkbox.
    """
    fields: List[CheckBoxSingleType]

    @property
    def fields_mapping(self) -> Dict[str, Any]:
        """A seralized mapping of all single checkboxes appearing in checkbox."""
        from sec_form_d.utils import serialize_field_names
        return serialize_field_names(fields=self.fields)

#### Field dataclasses used in parsing

@dataclass
class BaseField(ABC):
    """
    Abstract base class for all field dataclasses, whose
    purpose is to store the data extracted from the form.

    Args:
        name (str): The name of the field.
    """
    name: str

    @abstractmethod
    def to_dict(self) -> Dict[str, Any]:
        """Abstract method to serialize object."""
        pass


@dataclass
class FormField(BaseField):
    """
    Dataclass for storing data for a non-checkbox field.

    Args:
        data (str | None): The data corresponding to the field.
    """
    data: Optional[str]

    def to_dict(self) -> Dict[str, Any]:
        """Serializes the FormField object."""
        return {self.name: self.data}


@dataclass
class FormCheckBox(BaseField):
    """
    Dataclass for storing data for a single checkbox.

    Args:
        data (str | None): The data corresponding to the field.
    """
    data: bool

    def to_dict(self) -> Dict[str, Any]:
        """Serializes the FormCheckBox object."""
        return {self.name: self.data}


@dataclass
class FormCheckBoxMultiple(BaseField):
    """
    Dataclass for storing data for a multiple checkbox.

    Args:
        name (str): The name of the checkbox.
        fields (List[FormCheckBox]): A list of FormCheckBox
            objects each representing data for a single checkbox
            appearing within the multiple checkbox.
    """
    fields: List[FormCheckBox]

    def to_dict(self) -> Dict[str, Any]:
        """Serializes the FormCheckBoxMultiple object."""
        field_dictionary: Dict[str, Any] = {
            k: v for field in self.fields for k, v in field.to_dict().items()
        }
        return {self.name: field_dictionary}