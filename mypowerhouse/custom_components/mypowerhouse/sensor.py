"""Sensors exposed by MyPowerHouse."""
from __future__ import annotations

from homeassistant.components.sensor import SensorEntity, SensorEntityDescription
from homeassistant.const import PERCENTAGE, UnitOfPower
from homeassistant.helpers.device_registry import DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DOMAIN
from .coordinator import MyPowerHouseCoordinator

DESCRIPTIONS = (
    SensorEntityDescription(key="solar_power", name="Solar generation", native_unit_of_measurement=UnitOfPower.WATT),
    SensorEntityDescription(key="home_power", name="Home consumption", native_unit_of_measurement=UnitOfPower.WATT),
    SensorEntityDescription(key="grid_power", name="Grid power", native_unit_of_measurement=UnitOfPower.WATT),
    SensorEntityDescription(key="battery_power", name="Battery power", native_unit_of_measurement=UnitOfPower.WATT),
    SensorEntityDescription(key="battery_soc", name="Battery state of charge", native_unit_of_measurement=PERCENTAGE),
    SensorEntityDescription(key="import_rate", name="Import rate", native_unit_of_measurement="GBP/kWh"),
    SensorEntityDescription(key="export_rate", name="Export rate", native_unit_of_measurement="GBP/kWh"),
    SensorEntityDescription(key="recommendation", name="Recommendation"),
)


async def async_setup_entry(hass, entry, async_add_entities: AddEntitiesCallback) -> None:
    coordinator: MyPowerHouseCoordinator = entry.runtime_data
    async_add_entities(MyPowerHouseSensor(coordinator, description) for description in DESCRIPTIONS)


class MyPowerHouseSensor(CoordinatorEntity[MyPowerHouseCoordinator], SensorEntity):
    entity_description: SensorEntityDescription
    _attr_has_entity_name = True

    def __init__(self, coordinator, description) -> None:
        super().__init__(coordinator)
        self.entity_description = description
        self._attr_unique_id = f"mypowerhouse_{description.key}"
        self._attr_device_info = DeviceInfo(identifiers={(DOMAIN, "mypowerhouse")}, name="MyPowerHouse", manufacturer="PowerHouse Living")

    @property
    def native_value(self):
        return self.coordinator.data.get(self.entity_description.key)
