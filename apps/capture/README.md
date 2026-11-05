# Capture app

Browser app (PWA) that runs the motor tasks on a stylus tablet and records every pen sample.

## Scope for the MVP

- Device certification: sampling rate, timing jitter, ruler calibration (px -> mm)
- Tasks: Archimedes spiral, lines between targets, alternating tapping
- Kiosk-style session flow with pseudonymous participant code
- Encrypted local storage and upload when online

## First milestone

A diagnostic page that records raw Pointer Events on the reference tablet and reports
the real sampling rate, timing jitter and which fields (pressure, tilt, hover) are available.
