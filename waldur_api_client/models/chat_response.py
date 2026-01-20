from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.chat_response_m import ChatResponseM


T = TypeVar("T", bound="ChatResponse")


@_attrs_define
class ChatResponse:
    """
    Attributes:
        k (Union[Unset, str]): Component Alias (e.g. 'markdown', 'code', 'table').
        c (Union[Unset, str]): Content payload.
        t (Union[Unset, str]): Tag or language for dynamic blocks.
        h (Union[Unset, list[Any]]): Table headers.
        r (Union[Unset, list[Any]]): Table rows.
        n (Union[Unset, int]): Total row count.
        m (Union[Unset, ChatResponseM]): System metadata.
        e (Union[Unset, str]): Error message.
    """

    k: Union[Unset, str] = UNSET
    c: Union[Unset, str] = UNSET
    t: Union[Unset, str] = UNSET
    h: Union[Unset, list[Any]] = UNSET
    r: Union[Unset, list[Any]] = UNSET
    n: Union[Unset, int] = UNSET
    m: Union[Unset, "ChatResponseM"] = UNSET
    e: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        k = self.k

        c = self.c

        t = self.t

        h: Union[Unset, list[Any]] = UNSET
        if not isinstance(self.h, Unset):
            h = self.h

        r: Union[Unset, list[Any]] = UNSET
        if not isinstance(self.r, Unset):
            r = self.r

        n = self.n

        m: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.m, Unset):
            m = self.m.to_dict()

        e = self.e

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if k is not UNSET:
            field_dict["k"] = k
        if c is not UNSET:
            field_dict["c"] = c
        if t is not UNSET:
            field_dict["t"] = t
        if h is not UNSET:
            field_dict["h"] = h
        if r is not UNSET:
            field_dict["r"] = r
        if n is not UNSET:
            field_dict["n"] = n
        if m is not UNSET:
            field_dict["m"] = m
        if e is not UNSET:
            field_dict["e"] = e

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.chat_response_m import ChatResponseM

        d = dict(src_dict)
        k = d.pop("k", UNSET)

        c = d.pop("c", UNSET)

        t = d.pop("t", UNSET)

        h = cast(list[Any], d.pop("h", UNSET))

        r = cast(list[Any], d.pop("r", UNSET))

        n = d.pop("n", UNSET)

        _m = d.pop("m", UNSET)
        m: Union[Unset, ChatResponseM]
        if isinstance(_m, Unset):
            m = UNSET
        else:
            m = ChatResponseM.from_dict(_m)

        e = d.pop("e", UNSET)

        chat_response = cls(
            k=k,
            c=c,
            t=t,
            h=h,
            r=r,
            n=n,
            m=m,
            e=e,
        )

        chat_response.additional_properties = d
        return chat_response

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
