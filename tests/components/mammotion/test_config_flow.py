"""Test the Mammotion config flow."""

from __future__ import annotations

from homeassistant import config_entries
from homeassistant.components.mammotion.const import DOMAIN
from homeassistant.core import HomeAssistant
from homeassistant.data_entry_flow import FlowResultType


async def test_user_init_form(hass: HomeAssistant) -> None:
    """Test that the initial form is shown to the user."""
    result = await hass.config_entries.flow.async_init(
        DOMAIN, context={"source": config_entries.SOURCE_USER}
    )
    assert result["type"] is FlowResultType.FORM
