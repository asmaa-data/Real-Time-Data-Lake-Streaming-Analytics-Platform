# Real-Time-Data-Lake-Streaming-Analytics-Platform

## 🧠 Overview

This project is a **production-style Big Data streaming pipeline** designed to simulate real-world data engineering systems used in modern data platforms.

It demonstrates how raw data is ingested, streamed, processed, stored, and visualized in real-time using a full Big Data ecosystem.

The system collects real-world data from a web API, processes it through distributed streaming technologies, stores it in both a Data Lake (HDFS) and a Time-Series Database (InfluxDB), and visualizes it using Grafana dashboards.

---

## ⚠️ Environment Challenges (Real-World Constraint)

This project was built on a **CentOS 6.5 legacy environment**, which introduced significant engineering constraints:

* Outdated OS compatibility issues
* Manual dependency resolution for Hadoop ecosystem
* Version conflicts between Kafka, Spark, and Java
* Limited system resources and legacy package management
* Strict configuration tuning for distributed services

These constraints reflect real-world enterprise environments where engineers often work with **legacy infrastructure rather than ideal setups**.

---

## 🏗️ System Architecture

```
Open-Meteo API (Data Source)
        ↓
Python Producer (Real-time JSON Generator)
        ↓
Flume Agent (File Tailing Ingestion)
        ↓
Kafka Topic: weather_stream
        ↓
──────────────────────────────
        ↓                  ↓
Flume → HDFS        Spark Streaming Engine
(Data Lake)              ↓
                         InfluxDB (Time-Series DB)
                                ↓
                             Grafana Dashboard
```

---

## 🔧 Technologies Used

### 🧠 Big Data Ecosystem

* Apache Kafka (Distributed Streaming Platform)
* Apache Flume (Data Ingestion Layer)
* Apache Spark Structured Streaming (Real-Time Processing)
* Hadoop HDFS (Data Lake Storage)

### 📊 Storage & Visualization

* InfluxDB 1.7.10 (Time-Series Database)
* Grafana 8.3.3 (Real-Time Dashboards)

### 🐍 Data Source Layer

* Python (API ingestion & JSON generation)
* Open-Meteo Weather API

### 🖥️ Infrastructure

* CentOS 6.5 (Legacy Enterprise Linux Environment)

---

## 📦 Folder Structure

```
real-time-data-lake-platform/
│
├── producer/
│   ├── weather_producer.py
│
├── flume/
│   ├── file_tailing.conf
│   └── kafka_hdfs.conf
│
├── spark/
│   └── spark_weather.py
│
├── grafana/
│   ├── dashboard_queries.md
│   └── setup_instructions.md
│
├── architecture/
│   └── system_design.png
│
└── README.md
```

---

## 🔄 Data Flow (Step-by-Step)

1. Python fetches real-time data from Open-Meteo API
2. Data is written as JSON events to a local file
3. Flume tails the file and pushes events into Kafka
4. Kafka streams data into:

   * HDFS (Data Lake storage)
   * Spark Streaming engine
5. Spark processes and transforms streaming data
6. Cleaned data is stored in InfluxDB
7. Grafana visualizes real-time dashboards

---

## 📊 Key Features

### ⚡ Real-Time Streaming Pipeline

End-to-end streaming system with sub-second data propagation.

### 🏞️ Data Lake Architecture

Raw data stored in Hadoop HDFS for historical analysis.

### 📈 Time-Series Analytics

InfluxDB enables fast aggregation of streaming metrics.

### 📊 Live Dashboards

Grafana visualizes:

* Live data ingestion rate
* Time-series trends
* System health monitoring

### 🧩 Distributed Processing

Spark handles real-time transformation of streaming data.

---

## 💼 Business Value

This system replicates real-world enterprise data platforms used in:

* Aviation analytics
* Financial trading systems
* IoT monitoring platforms
* Logistics tracking systems
* Real-time recommendation engines

### Key Business Benefits:

* Real-time decision making
* High-throughput event processing
* Scalable data ingestion pipeline
* Fault-tolerant data architecture
* Historical + real-time analytics combination

---

## 🧪 Example Use Cases

* Real-time weather monitoring dashboards
* Predictive analytics pipelines
* Streaming anomaly detection systems
* Live monitoring of IoT sensor data

---

## 📉 Grafana Dashboards

* Data ingestion rate per minute
* Real-time temperature trends
* System health monitoring
* Peak load detection
* Streaming latency visualization

---

## 🧠 What This Project Demonstrates

* Distributed streaming system design
* Kafka-based event-driven architecture
* Spark Structured Streaming processing
* Data lake vs real-time storage separation
* Time-series database modeling
* Production-style engineering constraints handling

---

## 🚀 How to Run

follow the basic commands .txt file
```


## 📈 Status

✔ Completed
✔ End-to-end streaming pipeline
✔ Production-style architecture simulation
