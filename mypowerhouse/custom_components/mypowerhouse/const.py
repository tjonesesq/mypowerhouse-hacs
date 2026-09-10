DOMAIN = "mypowerhouse"
PLATFORMS = ["sensor"]

CONF_SOLAR_POWER = "solar_power_entity"
CONF_HOME_POWER = "home_power_entity"
CONF_GRID_POWER = "grid_power_entity"
CONF_BATTERY_POWER = "battery_power_entity"
CONF_BATTERY_SOC = "battery_soc_entity"
CONF_IMPORT_RATE = "import_rate_entity"
CONF_EXPORT_RATE = "export_rate_entity"

ENTITY_CONFIGS = (
    CONF_SOLAR_POWER,
    CONF_HOME_POWER,
    CONF_GRID_POWER,
    CONF_BATTERY_POWER,
    CONF_BATTERY_SOC,
    CONF_IMPORT_RATE,
    CONF_EXPORT_RATE,
)

DEFAULT_EXPORT_RATE = 0.12
