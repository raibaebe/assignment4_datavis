# Prometheus and Grafana Monitoring – Assignment #4

## Overview
This project demonstrates real-time system and database monitoring using Prometheus and Grafana.
It includes three dashboards that visualize metrics from PostgreSQL, system resources, and a custom Python exporter for weather data.
The setup allows monitoring, alerting, and data visualization in a containerized environment.

## Project Structure

| File | Description |
|------|--------------|
| docker-compose.yml | Defines all running services including Prometheus, Grafana, Node Exporter, PostgreSQL, and Custom Exporter. |
| prometheus.yml | Prometheus configuration file with scrape jobs for exporters. |
| custom_exporter.py | Custom Python exporter that collects weather metrics from the OpenWeather API and exposes them for Prometheus. |
| Database Exporter.json | Grafana dashboard for PostgreSQL metrics. |
| Node Exporter (Windows System Metrics).json | Grafana dashboard for system metrics. |
| Custom Exporter (Weather API).json | Grafana dashboard for custom weather metrics. |

## Setup Instructions

### 1. Run Containers
Make sure Docker Desktop is running, then open a terminal in the project directory and run:

```bash
docker compose up -d
```

Check running containers:
```bash
docker ps
```

### 2. Access Services
- Prometheus: [http://localhost:9090](http://localhost:9090)
- Grafana: [http://localhost:3000](http://localhost:3000)

Default Grafana credentials:
```
Username: admin
Password: admin
```

### 3. Dashboards
- **Database Exporter Dashboard:** PostgreSQL performance metrics (connections, size, TPS, rollbacks, etc.).
- **Node Exporter Dashboard:** System metrics (CPU, memory, disk, network, uptime, etc.).
- **Custom Exporter Dashboard:** Weather data (temperature, humidity, wind speed, pressure, etc.).

### 4. Alerts
Grafana alert rules are configured to monitor critical thresholds (e.g., high temperature, CPU overload).
Alerts can be integrated with Microsoft Teams or other webhooks for real-time notifications.

### 5. Custom Exporter
To run the weather exporter manually:
```bash
python custom_exporter.py
```

It starts an HTTP server at `http://localhost:8000/metrics` and updates data every 20 seconds.

### 6. Pushing to GitHub
```bash
git add .
git commit -m "Added dashboards, alerts, and custom exporter"
git push origin main
```

## Author
Raihan Kasymkyzy  
Astana IT University  
November 2025
