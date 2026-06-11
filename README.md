# 🛰️ Vigil Sense — Industrial Safety Monitoring using mmWave Radar

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)
![PyQt5](https://img.shields.io/badge/UI-PyQt5-41CD52?logo=qt)
![License](https://img.shields.io/badge/License-MIT-green)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey)

---

## 📌 Overview

**Vigil Sense** is a real-time industrial safety monitoring system built with Python and mmWave radar technology. It detects, tracks, and visualises human movement inside a factory environment to prevent accidents and enforce restricted-area boundaries.

The system interfaces with a **TI IWR6843AOP 60 GHz mmWave radar** over USB/UART, processes raw TLV binary frames in real-time, and displays multi-target tracking results in an interactive 3D industrial floor plan with animated hazard alerts.

📂 **Main application file:** [`Vigle_Sense_v2.py`](Vigle_Sense_v2.py) (Integrated and Structured version)
📄 **Original version:** [`Vigle_Sense.py`](Vigle_Sense.py)

---

## 🎯 Key Features

| Feature | Description |
|---|---|
| 📡 Real-time detection | Human presence detected with mmWave point cloud |
| 🧠 Multi-target tracking | Unique IDs assigned to each tracked person |
| 📏 Height estimation | IIR-filtered height with bias correction (+15 cm) |
| ⚠️ Restricted zone alerts | Breach detection for configurable hazard chambers |
| 🚨 Machine proximity | Critical alert when person is within 1 m of machine |
| 🏭 3D floor visualisation | Interactive isometric industrial facility view |
| 📊 Live zone chart | Real-time people-per-zone line chart |
| 🔌 Auto port detection | Auto-assigns CLI & Data COM ports on connect |
| 🔊 Audio alerts | Beep on rising-edge breach events (mutable) |
| 💾 CSV data export | Session data logged to `session_YYYYMMDD_HHMMSS.csv` |
| ⚙️ Settings persistence | Remembers ports, zones, and chamber bounds between sessions |

---

## 🧱 System Architecture

```
TI IWR6843AOP mmWave Radar  (60 GHz)
           │
           │  USB (two virtual COM ports)
           │  CLI  port  @ 115 200 baud  ← radar config commands
           │  Data port  @ 921 600 baud  ← TLV binary frame stream
           ▼
  ┌─────────────────────────────────────┐
  │         SerialWorker (QThread)      │
  │  • Sends AOP config on connect      │
  │  • Reads & buffers raw bytes        │
  │  • RadarParser decodes TLV frames   │
  │  • Emits frame signal to UI thread  │
  └──────────────┬──────────────────────┘
                 │ pyqtSignal  (thread-safe)
                 ▼
  ┌─────────────────────────────────────┐
  │           MainWindow (Qt)           │
  │  • PersonState tracking per ID      │
  │  • Zone / chamber breach detection  │
  │  • Machine proximity check          │
  │  • Drives all view widgets          │
  └───────────┬─────────────────────────┘
              │
   ┌──────────┼────────────────────┐
   ▼          ▼                    ▼
3D Floor   Radar Top         Dual 3D View
Plan View   View             (Front + Side)
```

---

## 🖥️ Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.10+ |
| UI Framework | PyQt5 |
| Hardware | TI IWR6843AOP mmWave Radar (EVM) |
| Data Processing | NumPy |
| Serial Comms | PySerial |
| Logging | Python `logging` (rotating file + console) |
| Data Export | CSV (`session_*.csv`) |
| Settings | JSON (`settings.json`) |

---

## ⚙️ Installation

### 1. Clone the repository
```bash
git clone https://github.com/HariMuthuGanesh/Vigle_Sense.git
cd Vigle_Sense
```

### 2. Create a virtual environment (recommended)
```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

---

## ▶️ How to Run

```bash
python Vigle_Sense_v2.py
```

*Note: The original, standalone version can still be run with `python Vigle_Sense.py`.*

The application opens in **demo mode** immediately (animated synthetic persons visible in Tab 2) so you can explore the UI without hardware.

---

## 🔌 Hardware Setup

### Requirements
- TI IWR6843AOP EVM (or IWR6843ISK-ODS)
- XDS110 USB-UART bridge drivers installed
- **People Tracking** firmware flashed (not the default out-of-box firmware)

### Steps
1. Connect the EVM to your PC via USB
2. Open Device Manager → verify two COM ports appear (XDS110)
3. Launch the app → click **⟳ REFRESH PORTS**
4. The lower COM number = **CLI port**, higher = **Data port**
5. Click **▶ CONNECT** — the app auto-detects and may swap ports if needed

> **Baud rates**
> - CLI port: `115 200` baud
> - Data port: `921 600` baud

---

## 📁 Project Structure

```
Vigle_Sense/
├── Vigle_Sense.py         # Original unmodified application
├── Vigle_Sense_v2.py      # Upgraded application incorporating all packages
├── config/                # Configuration package
│   ├── __init__.py
│   └── config.py
├── logger/                # Logging package
│   ├── __init__.py
│   └── logger.py
├── alerts/                # Alerts package
│   ├── __init__.py
│   └── alerts.py
├── data_logger/           # Data event logging package
│   ├── __init__.py
│   └── data_logger.py
├── settings/              # User settings persistence package
│   ├── __init__.py
│   └── settings.py
├── stats_tracker/         # Live performance tracking package
│   ├── __init__.py
│   └── stats_tracker.py
└── port_utils/            # Serial port utilities package
    ├── __init__.py
    └── port_utils.py
├── requirements.txt       # Python dependencies
├── CHANGELOG.md           # Version history
└── README.md              # This file
```

---

## 📄 CSV Data Format

Each session creates `session_YYYYMMDD_HHMMSS.csv` with one row per confirmed target per frame:

| Column | Type | Description |
|---|---|---|
| `timestamp` | string | `YYYY-MM-DD HH:MM:SS` |
| `frame_num` | int | Radar frame counter |
| `target_id` | int | Tracker-assigned person ID |
| `x_m` | float | Lateral position (metres, sensor origin) |
| `y_m` | float | Depth position (metres) |
| `z_m` | float | Height of centroid (metres) |
| `height_m` | float | Estimated person height (IIR filtered) |
| `zone` | string | `safe` / `alert` / `restricted` / `chamber_a` / `chamber_b` |
| `in_chamber_a` | 0/1 | Person inside Unit A |
| `in_chamber_b` | 0/1 | Person inside Unit B |
| `mach_a_prox` | 0/1 | Within machine-prox radius in Unit A |
| `mach_b_prox` | 0/1 | Within machine-prox radius in Unit B |

---

## ⚠️ Known Issues

| Issue | Workaround |
|---|---|
| Radar requires reconnect after STOP | Power-cycle EVM, then click CONNECT again |
| `0xffe` calibration error on sensorStart | Move EVM away from metallic objects; retry |
| Serial port stays locked after crash | Unplug/replug USB or use Device Manager to reset |
| Minor UI latency at >20 fps | Expected — Python/Qt rendering bound |

---

## 🔧 Module Usage Examples

### Audio alerts
```python
from alerts import AlertManager
am = AlertManager()
am.muted = False
# Call once per frame:
am.on_frame(ch_a_breach=True, ch_b_breach=False,
            mach_a_prox=False, mach_b_prox=False,
            any_restricted=False)
```

### Settings persistence
```python
from settings import Settings
with Settings() as s:          # auto load on enter, save on exit
    port = s.get("cli_port", "")
    s.set("safe_max", 3.5)
```

### CSV data logging
```python
from data_logger import DataLogger
dl = DataLogger()
dl.start()
dl.log_frame(frame_num=1, targets=[...], persons={...},
             zone_counts={...}, ch_a_breach=False, ...)
dl.stop()
dl.open_in_os()   # opens CSV in Excel / LibreOffice
```

---

## 💡 Use Cases

- 🏭 Industrial safety monitoring and compliance
- 🚧 Restricted zone enforcement without cameras
- 🤖 Human-machine interaction safety interlocks
- 🛑 Real-time accident prevention in factories

---

## ⭐ Future Scope

- AI-based behaviour prediction (fall detection, loitering)
- Cloud-based monitoring dashboard (FastAPI + WebSocket)
- Multi-sensor fusion (radar + camera)
- Mobile app for remote alerts
- Integration with PLC/SCADA safety systems

---

## 👥 Team

| Name | Role |
|---|---|
| Hari Muthu Ganesh R | Lead Developer |
| Benshya B | UI/UX & Visualisation |
| Rupha | Hardware Integration |
| Sanjay Kumar | Signal Processing |
| SabariSastha | Testing & Documentation |

---

## 📜 License

MIT License — see [LICENSE](LICENSE) for details.  
Developed as a team project focused on **Industrial Safety using mmWave Radar Technology**.
