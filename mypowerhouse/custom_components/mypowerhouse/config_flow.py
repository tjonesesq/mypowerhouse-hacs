"""Configuration flow for MyPowerHouse."""
from __future__ import annotations

import voluptuous as vol

from homeassistant.config_entries import ConfigFlow
from homeassistant.helpers import selector

from .const import DOMAIN, ENTITY_CONFIGS


def _entity_selector() -> selector.EntitySelector:
    return selector.EntitySelector(selector.EntitySelectorConfig(domain="sensor"))


class MyPowerHouseConfigFlow(ConfigFlow, domain=DOMAIN):
    """Handle a config flow for MyPowerHouse."""

    VERSION = 1

    async def async_step_user(self, user_input=None):
        if user_input is not None:
            await self.async_set_unique_id("mypowerhouse")
            self._abort_if_unique_id_configured()
            return self.async_create_entry(title="MyPowerHouse", data=user_input)

        schema = vol.Schema({
            vol.Required("solar_power_entity"): _entity_selector(),
            vol.Required("home_power_entity"): _entity_selector(),
            vol.Required("grid_power_entity"): _entity_selector(),
            vol.Required("battery_power_entity"): _entity_selector(),
            vol.Required("battery_soc_entity"): _entity_selector(),
            vol.Required("import_rate_entity"): _entity_selector(),
            vol.Optional("export_rate_entity"): _entity_selector(),
            vol.Optional("export_rate", default=0.12): selector.NumberSelector(
                selector.NumberSelectorConfig(min=0, max=2, step=0.001, unit_of_measurement="GBP/kWh")
            ),
        })
        return self.async_show_form(step_id="user", data_schema=schema)
