# 🌍 AI-Enhanced Citizen Pollution Monitor

### *End-to-End IoT System for Air, Water, and Noise Pollution Monitoring*

---

## 📘 Abstract

The **AI-Enhanced Citizen Pollution Monitor** is a comprehensive IoT-based environmental monitoring system designed to measure **air pollution**, **water quality**, and **noise pollution** using a single integrated hardware node.

The system combines **embedded hardware**, **cloud backend services**, **AI-based anomaly detection**, and a **web-based dashboard** to deliver real-time environmental insights at a local level.

Although developed as a **college academic project**, the architecture, modularity, and implementation approach are intentionally designed to resemble a **market-ready smart-city monitoring platform**.

---

## 🎯 Problem Statement

Conventional environmental monitoring systems suffer from:

* High installation and maintenance cost
* Low spatial coverage (few centralized stations)
* Lack of hyper-local pollution data
* Limited public access to real-time environmental insights

As a result, citizens and local authorities often lack actionable, real-time data to identify pollution events or environmental hazards.

---

## 💡 Proposed Solution

This project proposes a **low-cost, scalable, and modular pollution monitoring system** that:

* Collects **real-time environmental data** using IoT sensors
* Processes and stores data on a **cloud backend**
* Applies **AI-based anomaly detection** to identify abnormal pollution events
* Visualizes insights using a **web dashboard**

The solution enables **hyper-local environmental awareness** and demonstrates how citizen-deployed sensors can complement traditional monitoring infrastructure.

---

## 🧩 System Architecture Overview

### High-Level Data Flow

```
Environmental Sensors
        ↓
ESP32 Edge Node
        ↓
Wi-Fi / Internet
        ↓
Backend APIs (FastAPI)
        ↓
Database (PostgreSQL)
        ↓
AI Analytics Engine
        ↓
Web Dashboard (React)
```

### Architectural Layers

1. **Sensing Layer** – Air, water, and noise sensors
2. **Edge Layer** – ESP32 firmware
3. **Communication Layer** – Wi-Fi (HTTP/REST)
4. **Backend Layer** – APIs, data storage, alerts
5. **Analytics Layer** – AI-based anomaly detection
6. **Presentation Layer** – Web dashboard

---

## 🔧 Hardware Design

### 1. Controller Unit

* **ESP32 Microcontroller**

  * Central processing unit
  * Built-in Wi-Fi
  * Handles sensor interfacing and data transmission

---

### 2. Sensors Used

#### Air Pollution

| Sensor | Parameter Measured              |
| ------ | ------------------------------- |
| MQ-135 | Harmful gases (NH₃, CO₂, smoke) |
| DHT11  | Temperature & Humidity          |

#### Noise Pollution

| Sensor                 | Parameter Measured       |
| ---------------------- | ------------------------ |
| MAX4466 / Sound Sensor | Ambient sound level (dB) |

#### Water Pollution

| Sensor           | Parameter Measured |
| ---------------- | ------------------ |
| pH Sensor        | Acidity / Basicity |
| Turbidity Sensor | Water clarity      |

---

### 3. Physical Deployment Structure

```
[ Noise Sensor ]
       │
[ Waterproof Enclosure ]
[ ESP32 + Air Sensors ]
       │
[ Pole / Wall Mount ]
       │
[ Water Sensor Probe ]
```

**Design Principles**

* Electronics remain **dry and protected**
* Water probes remain **submerged**
* Air sensors allow airflow but block rain
* Noise sensor isolated from vibration

---

## ⚡ Electrical & Wiring Design

### Power Distribution

* **5V Supply** → MQ-135, pH sensor, Turbidity sensor
* **3.3V Supply** → DHT11, Sound sensor
* **Common Ground** shared by all components

### ESP32 Pin Mapping

| Sensor           | ESP32 Pin     |
| ---------------- | ------------- |
| MQ-135           | GPIO 34 (ADC) |
| DHT11            | GPIO 4        |
| Sound Sensor     | GPIO 35 (ADC) |
| pH Sensor        | GPIO 32 (ADC) |
| Turbidity Sensor | GPIO 33 (ADC) |

---

## 🧠 Edge Software (ESP32 Firmware)

### Responsibilities

* Sensor initialization
* Periodic data acquisition
* Noise filtering and normalization
* JSON data packet generation
* Secure data transmission to backend

### Sampling Strategy

| Sensor Type | Sampling Interval |
| ----------- | ----------------- |
| Air         | Every 1 minute    |
| Noise       | Every 30 seconds  |
| Water       | Every 5 minutes   |

---

## 📦 Unified Data Model

```json
{
  "device_id": "NODE_01",
  "air": {
    "aqi": 158,
    "temperature": 31
  },
  "noise": {
    "db": 72
  },
  "water": {
    "ph": 6.9,
    "turbidity": 115
  },
  "timestamp": "2026-01-27T11:30:00"
}
```

This unified format simplifies backend processing and visualization.

---

## ☁️ Backend System Design

### Technology Stack

* **FastAPI (Python)**
* **PostgreSQL**
* **RESTful APIs**
* **Docker (for containerization)**

---

### Backend Responsibilities

* Device registration and authentication
* Sensor data ingestion
* Persistent data storage
* AI-based analytics
* Alert generation
* Data APIs for frontend

---

### Core API Endpoints

| Method | Endpoint           | Description              |
| ------ | ------------------ | ------------------------ |
| POST   | `/register-device` | Register sensor node     |
| POST   | `/upload-data`     | Upload sensor readings   |
| GET    | `/latest`          | Fetch latest values      |
| GET    | `/alerts`          | Fetch detected anomalies |

---

## 🧪 AI & Analytics Module

### Objective

To automatically detect **abnormal pollution levels** based on historical trends.

### Technique Used

**Statistical Anomaly Detection**

```
If current_value > mean + 2 × standard_deviation
→ Anomaly detected
```

### Parameters Analyzed

* Air AQI
* Noise level (dB)
* Water turbidity

This method is:

* Explainable
* Lightweight
* Academically sound

---

## 📊 Frontend (Web Dashboard)

### Technology Stack

* **React.js**
* **Chart.js / Recharts**
* **Leaflet / Mapbox**

### Dashboard Features

* Live pollution monitoring
* Historical trend analysis
* Sensor location mapping
* Pollution alerts log

---

## 📁 Project Directory Structure

```
citizen-pollution-monitor/
│
├── firmware/          # ESP32 firmware
├── backend/           # FastAPI backend
├── frontend/          # React dashboard
├── ai/                # Analytics & anomaly detection
├── docs/              # Architecture & documentation
├── docker-compose.yml
└── README.md
```

---

## 🚀 Execution Flow (High-Level)

1. Sensors collect environmental data
2. ESP32 formats and sends data to backend
3. Backend stores data in database
4. AI module analyzes readings
5. Alerts generated if anomalies detected
6. Dashboard displays real-time insights

---

## 🔮 Future Enhancements

* Solar-powered sensor nodes
* Mobile application
* Predictive pollution forecasting
* Multi-node city-level deployment
* Open data APIs for NGOs and researchers

---

## 🎓 Academic Significance

This project integrates concepts from:

* Internet of Things (IoT)
* Embedded Systems
* Cloud Computing
* Artificial Intelligence
* Smart City Technologies

---

## 🏁 Conclusion

The **AI-Enhanced Citizen Pollution Monitor** demonstrates a complete **end-to-end environmental monitoring solution**, integrating **hardware sensing**, **cloud computing**, **AI analytics**, and **web-based visualization**.

While implemented at an academic scale, the design principles and architecture closely follow **real-world smart-city monitoring systems**, making it a strong foundation for future expansion.

---
