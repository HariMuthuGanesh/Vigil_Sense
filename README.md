# 🛰️ Vigil Sense – Industrial Safety Monitoring using mmWave Radar

## 📌 Overview

**Vigil Sense** is a real-time industrial safety monitoring system built using Python and mmWave radar technology. It detects, tracks, and visualizes human movement inside a factory environment to prevent accidents and enforce safety zones.

The system uses **TI IWR6843AOP mmWave radar** to capture point cloud data and track multiple individuals, displaying them in an interactive 3D industrial floor plan with hazard alerts.

📂 Main implementation: 

---

## 🎯 Key Features

* 📡 Real-time human detection using mmWave radar
* 🧠 Multi-target tracking with unique IDs
* 📏 Height estimation with filtering and bias correction
* ⚠️ Hazard zone detection (restricted areas)
* 🚨 Machine proximity alerts
* 🏭 Interactive 3D industrial floor visualization
* 🎨 Smooth UI built with PyQt5
* 🔌 Serial communication with radar device
* 🔄 Config-based initialization

---

## 🧱 System Architecture

```text
mmWave Radar (IWR6843AOP)
        ↓
Serial Communication (CLI + Data Ports)
        ↓
Python Backend (Parsing + Tracking)
        ↓
PyQt5 UI (3D Visualization + Alerts)
```

---

## 🖥️ Tech Stack

| Layer           | Technology                 |
| --------------- | -------------------------- |
| Language        | Python                     |
| UI Framework    | PyQt5                      |
| Hardware        | TI IWR6843AOP mmWave Radar |
| Data Processing | NumPy                      |
| Communication   | PySerial                   |

---

## 📸 Application Preview

* 3D industrial floor layout
* Real-time person tracking
* Restricted chamber visualization
* Hazard alerts (BREACH, MACHINE RISK)

---

## ⚙️ Installation

```bash
pip install pyqt5 numpy pyserial
```

---

## ▶️ How to Run

```bash
python Vigle_Sense.py
```

---

## 🔌 Hardware Setup

1. Connect mmWave radar via USB
2. Identify:

   * CLI Port (115200 baud)
   * Data Port (921600 baud)
3. Ensure correct firmware (People Tracking) is flashed

---

## ⚠️ Known Issues

* 🔁 Radar requires reconnect after stop (hardware reset issue)
* 🐞 Minor UI latency due to real-time rendering
* 🔌 Serial port may lock if not closed properly

---

## 🔧 Improvements (Planned)

* 🔄 Refresh button for system reset
* 🌐 Fullstack dashboard (FastAPI + Web UI)
* ⚡ Performance optimization for rendering
* 📊 Data logging and analytics
* 🎥 Integration with camera systems

---

## 💡 Use Cases

* 🏭 Industrial safety monitoring
* 🚧 Restricted zone enforcement
* 🤖 Human-machine interaction safety
* 🛑 Accident prevention systems

---

## 🧠 Learning Outcomes

* Real-time systems design
* Sensor data processing
* GUI development with PyQt5
* Serial communication handling
* 3D visualization techniques

---
## 👥 Team Members

This project was developed collaboratively by:

* 👩‍💻 **Benshya B**
* 👩‍💻 **Rupha**
* 👨‍💻 **Sanjay Kumar**
* 👨‍💻 **SabariSastha**
* 👨‍💻 **Hari Muthu Ganesh R**

---

## 📌 Author

Developed as a team project focused on **Industrial Safety using mmWave Radar Technology**, combining embedded systems, real-time processing, and UI development.


---

## ⭐ Future Scope

This project can be extended into:

* AI-based behavior prediction
* Smart factory automation
* Cloud-based monitoring dashboards
* Multi-sensor fusion systems

---

## 📜 License

This project is for educational and research purposes.
