# Converea - AIoT Automatic Plant Cultivation

> AI and IoT integrated automatic plant cultivation system

## Overview

Converea is a smart plant cultivation system developed during the SeSac AIoT program. Uses Raspberry Pi and Jetson Nano to collect sensor data and measure plant growth with AI models.

## Key Features

- **Sensor Monitoring**: Temperature, humidity, pH, water level, turbidity
- **AI Growth Analysis**: Jetson Nano camera-based plant growth measurement
- **Cloud Integration**: Real-time Firestore DB upload
- **Automatic Control**: Pump, fan automatic control

## Architecture

```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│ Raspberry Pi │───│ Jetson Nano │───│  Firestore  │
│  (Sensors)   │    │  (AI/Camera) │    │    (DB)     │
└─────────────┘    └─────────────┘    └─────────────┘
```

## Tech Stack

| Category | Technologies |
|----------|-------------|
| Hardware | Raspberry Pi, Jetson Nano |
| Sensors | DHT11, pH sensor, water level, turbidity |
| AI | TensorFlow, OpenCV |
| Database | Firebase Firestore |

## Project Structure

```
converea_sesac/
├── raspberry/      # Raspberry Pi code
├── jetsonnano/     # Jetson Nano code
└── sensor/         # Individual sensor modules
```

## Period

Nov - Dec 2022 (SeSac AIoT Program)
