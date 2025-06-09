
import logging
import telnetlib
from homeassistant.components.switch import SwitchEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities):
    host = entry.data.get("host")
    async_add_entities([OptomaSwitch(host)], True)

class OptomaSwitch(SwitchEntity):
    def __init__(self, host):
        self._host = host
        self._attr_name = "Optoma Projector"
        self._attr_unique_id = f"optoma_projector_{host.replace('.', '_')}"
        self._attr_entity_id = f"switch.optoma_projector"
        self._is_on = False

    @property
    def is_on(self):
        return self._is_on

    @property
    def device_info(self):
        return {
            "identifiers": {(DOMAIN, self._host)},
            "name": "Optoma UHD51A",
            "manufacturer": "Optoma",
            "model": "UHD51A"
        }

    def turn_on(self, **kwargs):
        self._send_command("~0000 1")
        self._is_on = True

    def turn_off(self, **kwargs):
        self._send_command("~0000 0")
        self._is_on = False

    def update(self):
        # Called by Home Assistant to refresh the state
        self._is_on = self._query_state()

    def _query_state(self):
        try:
            with telnetlib.Telnet(self._host, 23, timeout=1.0) as tn:
                tn.write(b"~00150 1\r")
                response = tn.read_until(b"\r", timeout=1.0).decode("ascii")
                _LOGGER.debug("Status response: %s", response)
                return "Ok1" in response
        except Exception as e:
            _LOGGER.error("Failed to read status from %s: %s", self._host, e)
            return False

    def _send_command(self, command):
        try:
            with telnetlib.Telnet(self._host, 23, timeout=10) as tn:
                tn.write(command.encode('ascii') + b"\r")
                _LOGGER.info("Sent command '%s' to %s", command, self._host)
        except Exception as e:
            _LOGGER.error("Telnet command failed to %s: %s", self._host, e)
