"""State collection and recommendations for MyPowerHouse."""
from __future__ import annotations

from datetime import timedelta
import logging
from typing import Any

from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator

from .const import DEFAULT_EXPORT_RATE, DOMAIN

_LOGGER = logging.getLogger(__name__)


class MyPowerHouseCoordinator(DataUpdateCoordinator[dict[str, Any]]):
    """Collect configured Home Assistant energy entities every minute."""

    def __init__(self, hass: HomeAssistant, entry) -> None:
        super().__init__(
            hass,
            logger=_LOGGER,
            name=DOMAIN,
            update_interval=timedelta(minutes=1),
            config_entry=entry,
        )
        self.entry = entry

    def _number(self, key: str, default: float = 0.0) -> float:
        entity_id = self.entry.data.get(key)
        if not entity_id:
            return default
        state = self.hass.states.get(entity_id)
        if not state or state.state in ("unknown", "unavailable"):
            return default
        try:
            return float(state.state)
        except ValueError:
            return default

    async def _async_update_data(self) -> dict[str, Any]:
        solar = self._number("solar_power_entity")
        home = self._number("home_power_entity")
        grid = self._number("grid_power_entity")
        battery = self._number("battery_power_entity")
        battery_soc = self._number("battery_soc_entity")
        import_rate = self._number("import_rate_entity")
        export_rate = self._number("export_rate_entity", self.entry.data.get("export_rate", DEFAULT_EXPORT_RATE))

        # Positive grid is import and positive battery is discharge. These are
        # configurable conventions and can be corrected in the entity setup later.
        if grid > 100:
            recommendation = "You are importing from the grid. Reduce discretionary load or use stored energy if your Powerwall reserve permits."
        elif grid < -100 and battery_soc < 95:
            recommendation = "You are exporting solar while the battery has space. Consider storing this energy for the evening peak."
        elif import_rate >= 0.25 and battery_soc < 30:
            recommendation = "Electricity is expensive and battery charge is low. Prioritise essential loads and protect remaining capacity."
        elif import_rate <= 0.12 and battery_soc < 70:
            recommendation = "This is a comparatively low-cost period. Charging flexible loads or the battery may be worthwhile."
        else:
            recommendation = "Your energy position is balanced. No immediate action is recommended."

        return {
            "solar_power": solar,
            "home_power": home,
            "grid_power": grid,
            "battery_power": battery,
            "battery_soc": battery_soc,
            "import_rate": import_rate,
            "export_rate": export_rate,
            "recommendation": recommendation,
        }
