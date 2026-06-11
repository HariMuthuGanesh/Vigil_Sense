# Changelog

All notable changes to **Vigil Sense** are documented in this file.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versions follow [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [Unreleased]

---

## [0.2.0] — 2026-06-11

### Added
- `requirements.txt` — pinned dependencies (`pyqt5`, `numpy`, `pyserial`)
  so the project can be installed with a single `pip install -r requirements.txt`.
- `.gitignore` — covers Python cache, virtual environments, IDE files,
  generated session CSVs, log files, and OS artefacts.
- `config.py` — all tunable constants extracted from `Vigle_Sense.py`
  into one easy-to-find module (baud rates, TLV IDs, colour palette,
  zone defaults, radar config string).
- `logger.py` — structured logging via Python's standard `logging` module.
  Writes to a rotating `vigle_sense.log` (5 MB, 3 backups) and to
  `stdout` at INFO level. Used by every new companion module.
- `data_logger.py` — session CSV data logger. Records one row per
  confirmed target per frame to `session_YYYYMMDD_HHMMSS.csv`:
  timestamp, frame number, target ID, 3D position, estimated height,
  zone classification, chamber flags, and machine proximity flags.
  Includes `open_in_os()` to launch the file in Excel/LibreOffice.
- `alerts.py` — cross-platform audio alert manager (`AlertManager`).
  Plays a beep on the **rising edge** of chamber breach, machine
  proximity, and restricted-zone events (once per event, not every
  frame). Uses `winsound` on Windows, `afplay` on macOS, `paplay` on
  Linux, with a terminal-bell fallback. Supports a `muted` flag.
- `settings.py` — JSON-backed settings persistence (`Settings` class).
  Saves last-used COM ports, zone radii, chamber bounds, machine
  proximity radius, and alert-muted state to `settings.json`.
  Provides a context-manager interface for automatic load/save.
- `stats_tracker.py` — rolling performance statistics (`StatsTracker`).
  Computes frames-per-second, point-cloud size, and confirmed track
  count from the live stream. Provides formatted strings ready for
  the three `StatCard` widgets that were stubbed as `None` in
  the original application.
- `port_utils.py` — serial port enumeration helpers. Single canonical
  implementation of `list_ports()`, `fill_combo()`, and `auto_assign()`,
  replacing the duplicated logic that existed across three methods in
  `Vigle_Sense.py`. Adds explicit XDS110 CLI / Data label detection.
- `CHANGELOG.md` — this file.

### Changed
- `README.md` — complete rewrite:
  - Filled in the blank "Main implementation:" placeholder.
  - Added architecture diagram showing the full data path from radar
    hardware through `SerialWorker` to the Qt UI.
  - Added project structure tree, CSV format table, module usage
    examples, known-issues table, and hardware setup guide.
  - Added GitHub badges (Python version, PyQt5, license, platform).

### Notes
- `Vigle_Sense.py` is intentionally **unchanged** in this release.
  All new modules are companion files that extend the original without
  modifying it.  The original remains a fully standalone application.

---

## [0.1.0] — 2026-06-10

### Added
- Initial commit: `Vigle_Sense.py` — full PyQt5 desktop application.
  - `RadarParser` — TLV binary frame decoder for IWR6843AOP.
  - `SerialWorker` — `QThread` handling CLI config dispatch and Data
    port reading at 921 600 baud.
  - `HazardZone` — 3D bounding-box geofence for restricted areas.
  - `PersonState` — per-target tracker with IIR height smoothing.
  - `IndustrialFloorPlanWidget` — interactive 3D isometric facility
    view with drag-to-rotate and scroll-to-zoom.
  - `RadarViewWidget` — 2D top-down radar field with zone rings.
  - `DualViewWidget` — side-by-side front/side orthographic 3D views.
  - `MiniRadarWidget` — compact top-view thumbnail.
  - `ZoneChartWidget` — live people-per-zone line chart.
  - `StatCard`, `AlertBanner`, `PersonRow`, `ChamberStatusWidget`
    — left-panel UI components.
  - `MainWindow` — root window, frame processing pipeline, demo mode
    with animated synthetic targets.
  - Demo mode: animated persons visible without hardware connection.
  - Configurable hazard zones, chamber bounds, and machine proximity
    radius via on-screen spinboxes.

---

[Unreleased]: https://github.com/HariMuthuGanesh/Vigle_Sense/compare/v0.2.0...HEAD
[0.2.0]: https://github.com/HariMuthuGanesh/Vigle_Sense/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/HariMuthuGanesh/Vigle_Sense/releases/tag/v0.1.0
