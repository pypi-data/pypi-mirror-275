from typing import Self, Any

from attrs import define, field

from ..common.models import Address


@define
class WarehouseRequest:
    name: str
    origin_address: Address
    return_address: Address = field(default=None)
    is_default: bool = field(default=None)


@define
class Warehouse:
    warehouse_id: str
    name: str
    created_at: str
    origin_address: Address
    return_address: Address
    is_default: bool = field(default=None)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Self:
        origin_address: Address = Address(**data.pop("origin_address"))
        return_address: Address = Address(**data.pop("return_address"))
        return cls(origin_address=origin_address, return_address=return_address, **data)
