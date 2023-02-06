import pytest
from dataclasses import dataclass, Field
from typing import ClassVar, Optional, Any
from xml.etree.ElementTree import fromstring, tostring, canonicalize
from scm_staging.xml_factory import MetaMixin, StrElementField


@dataclass(frozen=True)
class XmlWithBoolean(MetaMixin):
    _element_name: ClassVar[str] = "with_bool"

    a_bool: bool


@dataclass(frozen=True)
class XmlTestElement(MetaMixin):
    string: str
    number: int
    a_list_of_strings: list[str]
    optional_str: str | None
    another_optional_str: Optional[str]

    _private_elem: str = "should not appear"

    _element_name: ClassVar[str] = "test"


@dataclass(frozen=True)
class ElementWithOptionals(MetaMixin):
    a_list: list[str] | None = None
    a_number: int | None = None

    _element_name: ClassVar[str] = "with_optionals"


@dataclass(frozen=True)
class WithFieldsAsSubelements(MetaMixin):
    a_string: str
    string_as_subelement: StrElementField
    optional_string_as_subelement: StrElementField | None = None

    _element_name: ClassVar[str] = "subelements"


@dataclass(frozen=True)
class WithTransformer(MetaMixin):
    test_element: XmlTestElement

    def field_transformer(self, field: Field[Any]) -> tuple[Any, str, Any]:
        if field.name == "test_element":
            return self.test_element.string, "just_a_string", StrElementField
        return super().field_transformer(field)

    _field_converters = {
        "test_element": lambda elem: XmlTestElement(
            string=elem.find("just_a_string").text,
            number=2,
            a_list_of_strings=["3", "4"],
            optional_str="5",
            another_optional_str="6",
        )
    }

    _element_name: ClassVar[str] = "transformer"


@dataclass(frozen=True)
class NestedChild(MetaMixin):
    number: int

    with_optionals: ElementWithOptionals

    _element_name: ClassVar[str] = "nested_child"


@dataclass(frozen=True)
class Nested(MetaMixin):
    val: str

    nested_child: NestedChild

    _element_name: ClassVar[str] = "nested"


@pytest.mark.parametrize(
    "element,expected_xml",
    [
        (
            (
                xml_test_element := XmlTestElement(
                    string="1",
                    number=2,
                    a_list_of_strings=["3", "4"],
                    optional_str="5",
                    another_optional_str="6",
                )
            ),
            """<test string="1" optional_str="5" number="2" another_optional_str="6"><a_list_of_strings>3</a_list_of_strings><a_list_of_strings>4</a_list_of_strings></test>""",
        ),
        (ElementWithOptionals(), """<with_optionals/>"""),
        (
            ElementWithOptionals(a_list=["6", "7"]),
            """<with_optionals><a_list>6</a_list><a_list>7</a_list></with_optionals>""",
        ),
        (
            WithFieldsAsSubelements(
                a_string="foo", string_as_subelement=StrElementField("bar")
            ),
            """<subelements a_string="foo"><string_as_subelement>bar</string_as_subelement></subelements>""",
        ),
        (
            WithTransformer(test_element=xml_test_element),
            """<transformer><just_a_string>1</just_a_string></transformer>""",
        ),
        (
            Nested(
                "str",
                nested_child=NestedChild(4, with_optionals=ElementWithOptionals()),
            ),
            """<nested val="str"><nested_child number="4"><with_optionals/></nested_child></nested>""",
        ),
        (XmlWithBoolean(True), """<with_bool a_bool="true"/>"""),
    ],
)
def test_xml_generation(element: MetaMixin, expected_xml: str):
    assert canonicalize(expected_xml) == canonicalize(tostring(element.meta))
    assert element.from_xml(fromstring(expected_xml)) == element
