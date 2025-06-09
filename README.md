# Optoma UHD51A Home Assistant Integration

A custom integration for [Home Assistant](https://www.home-assistant.io) that allows control of the **Optoma UHD51A projector** over Telnet.

---

## 🔧 Features

- Power On/Off via Telnet (`~0000 1` / `~0000 0`)
- Status detection using response from `~00150 1` (expects `Ok1`)
- No YAML configuration required
- Setup via Home Assistant UI
- Creates a single switch entity: `switch.optoma_projector`
- Lightweight and fast

---

## 📦 Installation

1. Download the ZIP from the [Releases](https://github.com/yourusername/ha-optoma-uhd51a/releases) section.
2. Extract the contents to:
   ```
   config/custom_components/optoma/
   ```
3. Restart Home Assistant.

---

## ⚙️ Configuration

1. Go to **Settings > Devices & Services > Add Integration**.
2. Search for **Optoma UHD51A Projector**.
3. Enter the IP address of your projector (e.g., `10.0.0.133`).
4. Click Submit.

Home Assistant will automatically create the switch entity and handle communication with the projector.

---

## 🧪 Example Usage

```yaml
- alias: Power on Optoma Projector
  trigger:
    platform: time
    at: "20:00:00"
  action:
    service: switch.turn_on
    target:
      entity_id: switch.optoma_projector
```

---

## 🧠 Notes

- Telnet Port: `23`
- Power ON command: `~0000 1`
- Power OFF command: `~0000 0`
- Status query: `~00150 1` → response must contain `"Ok1"`

---

## 🙏 Credits

Created by [timcloud](https://github.com/Timman70)

---

## 📄 License

This project is licensed under the MIT License.
