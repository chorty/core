"""Diagnostics support for Tankerkoenig."""

from __future__ import annotations

from dataclasses import asdict
from typing import Any

from homeassistant.components.diagnostics import async_redact_data
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import (
    CONF_API_KEY,
    CONF_LATITUDE,
    CONF_LONGITUDE,
    CONF_UNIQUE_ID,
)
from homeassistant.core import HomeAssistant

from .const import DOMAIN
from .coordinator import TankerkoenigDataUpdateCoordinator

TO_REDACT = {CONF_API_KEY, CONF_LATITUDE, CONF_LONGITUDE, CONF_UNIQUE_ID}


async def async_get_config_entry_diagnostics(
    hass: HomeAssistant, entry: ConfigEntry
) -> dict[str, Any]:
    """Return diagnostics for a config entry."""
    coordinator: TankerkoenigDataUpdateCoordinator = hass.data[DOMAIN][entry.entry_id]

    return {
        "entry": async_redact_data(entry.as_dict(), TO_REDACT),
        "data": {
            station_id: asdict(price_info)
            for station_id, price_info in coordinator.data.items()
        },
    }
