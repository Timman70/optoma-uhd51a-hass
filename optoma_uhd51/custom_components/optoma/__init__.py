async def async_setup_entry(hass, entry):
    await hass.config_entries.async_forward_entry_setups(entry, ["switch"])
    return True
