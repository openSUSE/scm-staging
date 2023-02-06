from abc import ABC
import dataclasses
import enum
import types
import typing
import xml.etree.ElementTree as ET

from aiohttp import ClientResponse


StrElementField = typing.NewType("StrElementField", str)


T = typing.TypeVar("T")


class MetaMixin(ABC):
    _element_name: typing.ClassVar[str] = ""
    _field_converters: typing.ClassVar[
        dict[str, typing.Callable[[ET.Element], typing.Any]] | None
    ] = None

    M = typing.TypeVar("M", bound="MetaMixin")

    def __init__(self, *args: typing.Any, **kwargs: typing.Any) -> None:
        super().__init__(*args, **kwargs)
        if not self._element_name:
            raise ValueError("attribute '_element_name' must be set")

    @classmethod
    def element_name(cls) -> str:
        return cls._element_name

    @staticmethod
    def _list_to_xml(element_name: str, entries: list[typing.Any]) -> list[ET.Element]:
        res = []
        for entry in entries:
            if hasattr(entry, "meta"):
                res.append(entry.meta)
            else:
                (lst_elem := ET.Element(element_name)).text = entry
                res.append(lst_elem)
        return res

    @staticmethod
    def _is_union_type(type: typing.Any) -> bool:
        return (
            (origin := typing.get_origin(type)) is typing.Union
            or origin is types.UnionType
            or isinstance(origin, types.UnionType)
        )

    # def field_converter(self, field: dataclasses.Field[typing.Any], xml_element: ET.Element) -> typing.Any:

    def field_transformer(
        self, field: dataclasses.Field[typing.Any]
    ) -> tuple[T, str, typing.Type[T]]:
        """Override this method if you wish for certain fields to use a
        different value or type or xml tag.

        Args:
            field: A field (obtained via :py:func:`dataclasses.fields()`)
                belonging to this class.

        Returns:
            A tuple of the field's value, name and type.

        """
        return (getattr(self, field.name), field.name, field.type)

    @property
    def meta(self) -> ET.Element:
        elem = ET.Element(self._element_name)
        for field in dataclasses.fields(self):
            # omit private fields
            if field.name.startswith("_"):
                continue

            val: typing.Any
            type: typing.Any
            val, name, type = self.field_transformer(field)

            if isinstance(val, list):
                for entry in MetaMixin._list_to_xml(name, val):
                    elem.append(entry)
            elif (
                StrElementField in (args := typing.get_args(type))
                or type is StrElementField
            ):
                if self._is_union_type(type) and types.NoneType in args and val is None:
                    continue
                (field_as_subelement := ET.Element(name)).text = str(val)
                elem.append(field_as_subelement)
            elif hasattr(val, "meta"):
                elem.append(val.meta)
            else:
                if val:
                    elem.attrib[name] = str(val)

            if (
                MetaMixin._is_union_type(type)
                and not types.NoneType in typing.get_args(type)
                and val is None
            ):
                raise ValueError(f"field '{field.name}' is None, but it must not be")

        return elem

    @staticmethod
    def _get_value_from_xml(
        name: str, xml_element: ET.Element, type: typing.Any
    ) -> typing.Any:
        if hasattr(type, "from_xml"):
            matching_children = xml_element.findall(type._element_name)
            if len(matching_children) != 1:
                raise ValueError(
                    "Expected to find one element with the tag "
                    f"{type._element_name}, but got {len(matching_children)}"
                )
            return type.from_xml(matching_children[0])

        if type is str:
            return xml_element.attrib[name]
        if type is StrElementField:
            matching_children = xml_element.findall(name)
            if len(matching_children) != 1:
                raise ValueError(
                    f"Expected exactly 1 child element with the name {name}, but got {len(matching_children)}"
                )
            return matching_children[0].text

        try:
            if issubclass(type, enum.Enum):
                return type(xml_element.attrib[name])
        except TypeError:
            # type is not a class
            pass

        if type is int:
            return int(xml_element.attrib[name])
        if typing.get_origin(type) is list:
            assert len(list_types := typing.get_args(type)) == 1
            if hasattr(list_types[0], "from_xml"):
                return [
                    list_types[0].from_xml(elem) for elem in xml_element.findall(name)
                ]
            else:
                return [list_types[0](elem.text) for elem in xml_element.findall(name)]

        if MetaMixin._is_union_type(type):
            # try all possible types in a Union and store them for later
            results = []
            for possible_type in typing.get_args(type):
                try:
                    results.append(
                        MetaMixin._get_value_from_xml(name, xml_element, possible_type)
                    )
                except (ValueError, KeyError):
                    pass

            # special handling for optional lists:
            # _get_value_from_xml will return an empty list for optional lists,
            # but then we actually want to return None and not []
            list_in_types = any(typing.get_origin(tp) for tp in typing.get_args(type))
            if types.NoneType in typing.get_args(type) and (
                not results
                or (list_in_types and results and all(not res for res in results))
            ):
                return None

            return results[0]

        raise ValueError(f"Unknown type {type}")

    @classmethod
    async def from_response(cls: typing.Type[M], resp: ClientResponse) -> M:
        return cls.from_xml(await resp.read())

    @classmethod
    def from_xml(cls: typing.Type[M], xml: ET.Element | str | bytes) -> M:
        xml_element = ET.fromstring(xml) if isinstance(xml, (str, bytes)) else xml

        if xml_element.tag != cls._element_name:
            raise ValueError(
                f"Invalid XML tag '{xml_element.tag}', expected {cls._element_name}"
            )

        kwargs: dict[str, typing.Any] = {}

        for field in dataclasses.fields(cls):
            # omit private fields
            if field.name.startswith("_"):
                continue

            if cls._field_converters and field.name in cls._field_converters:
                val = cls._field_converters[field.name](xml_element)
            else:
                val = MetaMixin._get_value_from_xml(field.name, xml_element, field.type)

            kwargs[field.name] = val

        return cls(**kwargs)
