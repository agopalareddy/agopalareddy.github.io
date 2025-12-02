---
date: 2025-12-01
title: "MLB Statcast Real-Time Data Pipeline"
collection: projects
permalink: /projects/2025-12-mlb-statcast-pipeline
excerpt: "Built a real-time data pipeline for MLB pitch data using Apache Airflow, Snowflake, and Kafka, with an interactive Streamlit dashboard for pitch analysis and visualization."
venue: "Washington University in St. Louis"
last_modified_at: 2025-12-02 00:00:00
---

This project implements a comprehensive real-time data pipeline for MLB Statcast pitch data, developed as part of Washington University in St. Louis's CSE 5114: Data Manipulation and Management at Scale course.

### Project Overview

The pipeline ingests, processes, and visualizes MLB pitch-by-pitch data from Baseball Savant's Statcast system. It demonstrates modern data engineering practices including ETL automation, data warehousing, stream processing, and interactive analytics.

### Architecture

The system consists of several integrated components:

1. **Data Ingestion**: Automated fetching of Statcast pitch data from MLB's Baseball Savant API
2. **ETL Pipeline**: Apache Airflow DAGs for daily and historical backfill processing
3. **Data Warehouse**: Snowflake for scalable storage and analytics
4. **Stream Processing**: Kafka simulation for real-time pitch data streaming
5. **Dashboard**: Interactive Streamlit application for pitch analysis and visualization

### Key Features

- **Composite Key Design**: Unique pitch identification using `game_pk`, `at_bat_number`, and `pitch_number`
- **Automated ETL**: Airflow DAGs for daily incremental loads and historical backfills
- **Real-Time Simulation**: Kafka-based streaming for live pitch data simulation
- **Interactive Analytics**: Streamlit dashboard with pitch visualizations, player statistics, and game analysis
- **Scalable Storage**: Snowflake data warehouse with optimized schema design

### Technologies Used

- Python
- Apache Airflow
- Snowflake
- Apache Kafka
- Streamlit
- Pandas
- pybaseball (Statcast API)

### GitHub Repository

[View the project on GitHub](https://github.com/agopalareddy/CSE-5114-Project)
