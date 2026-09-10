"""MyPowerHouse integration."""
from __future__ import annotations

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

from .const import DOMAIN, PLATFORMS
from .coordinator import MyPowerHouseCoordinator

type MyPowerHouseConfigEntry = ConfigEntry[MyPowerHouseCoordinator]


async def async_setup_entry(hass: HomeAssistant, entry: MyPowerHouseConfigEntry) -> bool:
    coordinator = MyPowerHouseCoordinator(hass, entry)
    await coordinator.async_config_entry_first_refresh()
    entry.runtime_data = coordinator
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    return True


async def async_unload_entry(hass: HomeAssistant, entry: MyPowerHouseConfigEntry) -> bool:
    return await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
