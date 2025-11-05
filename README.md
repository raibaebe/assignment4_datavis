# Prometheus and Grafana Monitoring – Assignment #4

## Overview
This project demonstrates real-time monitoring using **Prometheus**, **Grafana**, and exporters.  
It includes three dashboards: PostgreSQL (Database Exporter), Windows System (Node Exporter), and Weather API (Custom Exporter).  
All components run with Docker and can be accessed through local URLs.

## Files Overview

| File | Description |
|------|--------------|
| docker-compose.yml | Defines all running services |
| prometheus.yml | Prometheus configuration file |
| custom_exporter.py | Exports weather metrics from OpenWeather API |
| Database Exporter.json | Grafana dashboard for PostgreSQL |
| Node Exporter (Windows).json | Grafana dashboard for system metrics |
| Custom Exporter (Weather).json | Grafana dashboard for weather data |

## How to Run

### 1. Open Project Folder
```bash
cd "C:\Users\Raikhan\Desktop\projects\assignment4"
```

### 2. Start All Containers
```bash
docker compose up -d
```
To verify:
```bash
docker ps
```

### 3. Access Services

| Service | URL |
|----------|-----|
| Prometheus | http://localhost:9090 |
| Grafana | http://localhost:3000 |
| Custom Exporter | http://localhost:8000/metrics |

**Grafana login:** admin / admin

### 4. Import Dashboards
In Grafana → **Dashboards → Import**, upload each `.json` file and select the **Prometheus** data source.

### 5. Custom Exporter (Manual Run)
If needed, start it manually:
```bash
python custom_exporter.py
```

### 6. PostgreSQL Demo Data (Optional)
Insert and rollback data to show metrics:
```bash
docker exec -it db psql -U postgres -d testdb
```
```sql
INSERT INTO users (name) VALUES ('Alice'), ('Bob');
DO $$
BEGIN
  FOR i IN 1..3 LOOP
    BEGIN
      INSERT INTO users (name) VALUES ('err_' || i);
      RAISE NOTICE 'Simulated error';
      ROLLBACK;
    EXCEPTION WHEN OTHERS THEN ROLLBACK;
    END;
  END LOOP;
END $$;
```

### 7. Stop Containers
```bash
docker compose down
```

## Result
Three Grafana dashboards with real-time metrics:  
- **Database Exporter** – PostgreSQL performance  
- **Node Exporter** – system CPU, memory, and network stats  
- **Custom Exporter** – weather metrics via API

## Author
Raikhan Kassymkyzy  
Astana IT University, November 2025
