# 🌍 Smart City Traffic Intelligence Platform

An AI-powered intelligent transportation platform built with **Python, Streamlit, Machine Learning, OpenAI GPT, and Interactive GIS Visualization** to analyze traffic congestion, predict traffic speed, generate engineering reports, and support smart city transportation planning.

This project demonstrates how **Artificial Intelligence, Machine Learning, Large Language Models (LLMs), Geospatial Analytics, and Interactive Dashboards** can be integrated into a single intelligent decision-support platform for urban mobility.

---

# 🌐 Live Application

🔗 https://olonisakin.streamlit.app/

---

# 📌 Project Overview

Rapid urbanization has increased traffic congestion, travel delays, and transportation inefficiencies in many cities.

This project was developed to demonstrate how Artificial Intelligence can support transportation engineers, planners, and decision-makers through intelligent traffic monitoring and predictive analytics.

The platform integrates:

- Machine Learning
- OpenAI GPT
- GIS Visualization
- Traffic Analytics
- Automated Report Generation
- Interactive Dashboards

into one intelligent Smart City Traffic Management System.

---

# 🎯 Problem → Solution → Impact

## Problem

Urban traffic congestion reduces productivity, increases travel time, and affects economic activities. Transportation agencies require intelligent systems capable of monitoring traffic conditions and supporting evidence-based decision-making.

## Solution

This platform combines **Machine Learning, Artificial Intelligence, GIS visualization, and Generative AI** to predict traffic conditions, visualize congestion, generate engineering reports, and provide intelligent recommendations through an interactive dashboard.

## Impact

The system demonstrates how AI can support:

- Smart City Initiatives
- Intelligent Transportation Systems
- Urban Traffic Monitoring
- Traffic Engineering
- Transportation Planning
- Decision Support Systems

---

# 🚀 Key Features

## 📊 Smart Traffic Dashboard

Displays key traffic indicators including:

- Predicted Speed
- Actual Speed
- Percentage Difference
- Traffic Status

---

## 🤖 Machine Learning Prediction

Uses a **Random Forest Regressor** to predict traffic speed using:

- Route Length
- Travel Time
- Hour of Day

---

## 🚦 Intelligent Congestion Detection

Automatically classifies congestion levels as:

🟢 Normal

🟡 Moderate

🟠 Heavy

🔴 Critical

---

## 🗺️ Interactive GIS Traffic Map

Visualizes traffic conditions using **PyDeck** with interactive maps.

---

## 📡 Live Traffic Feed

Simulates a live traffic monitoring system displaying:

- Current Traffic Status
- Average Speed
- Congestion Alerts
- Incident Notifications

---

## 🤖 AI Engineering Report

Powered by **OpenAI GPT**, the application automatically generates professional transportation engineering reports including:

- Traffic Analysis
- Root Cause Assessment
- Impact Evaluation
- Engineering Recommendations

---

## 💬 AI Traffic Assistant

Users can ask transportation-related questions and receive AI-generated responses through an integrated conversational assistant.

---

## 📄 PDF Report Export

Generate professional traffic engineering reports in PDF format for documentation and decision-making.

---

# 📸 Application Screenshots

## 🖥️ Dashboard

![Dashboard](assets/Dashboard.png)

---

## 🗺️ Interactive Traffic Map

![Traffic Map](assets/Map.png)

---

## 📡 Live Traffic Feed

![Traffic Feed](assets/Traffic%20Feed.png)

---

## 🤖 AI Engineering Report

![AI Report](assets/AI.png)

---

# 🏗️ System Architecture

```text
Traffic Dataset
        │
        ▼
Data Processing (Pandas)
        │
        ▼
Machine Learning Model
(Random Forest Regressor)
        │
        ├──────────────┐
        ▼              ▼
Traffic Prediction    Congestion Detection
        │              │
        └──────┬───────┘
               ▼
Interactive GIS Map (PyDeck)
               │
               ▼
OpenAI GPT Engineering Report
               │
               ▼
PDF Report Generation
               │
               ▼
Interactive Streamlit Dashboard
               │
               ▼
Smart Transportation Decision Support
```

---

# 🧠 Artificial Intelligence Components

## Machine Learning

Random Forest Regressor predicts:

- Traffic Speed

---

## Generative AI

OpenAI GPT generates:

- Engineering Reports
- Traffic Analysis
- Recommendations
- Question & Answer Support

---

# 📊 Model Development & Evaluation

This project was designed as a prototype to demonstrate how **Machine Learning and Large Language Models (LLMs)** can work together within an intelligent transportation platform.

Rather than focusing solely on predictive accuracy, the application emphasizes the integration of multiple AI technologies into a unified decision-support system.

The project demonstrates:

- Machine Learning Prediction
- AI-powered Engineering Reporting
- Interactive GIS Visualization
- Traffic Monitoring
- PDF Report Generation
- Conversational AI Assistance

One important lesson from this project is that modern AI systems are most valuable when predictive models, visualization tools, and generative AI capabilities work together to support better decision-making.

Future development will focus on expanding the transportation dataset, integrating live traffic APIs, improving predictive performance, and enhancing the AI assistant with domain-specific transportation knowledge.

---

# 🛠️ Technology Stack

## Programming

- Python

## Machine Learning

- Scikit-learn
- Random Forest Regressor

## Artificial Intelligence

- OpenAI GPT API

## Data Analysis

- Pandas
- NumPy

## Geospatial Analytics

- PyDeck

## Web Framework

- Streamlit

## Report Generation

- FPDF

---

# 📂 Project Structure

```text
Smart-City-Traffic-Intelligence-Platform/
│── assets/
│   ├── AI.png
│   ├── Dashboard.png
│   ├── Map.png
│   ├── Traffic Feed.png
│── dad4.py
│── requirements.txt
│── README.md
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/kola56de/Smart-City-Traffic-Intelligence-Platform.git

cd Smart-City-Traffic-Intelligence-Platform
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Configure OpenAI API Key

Create:

```text
.streamlit/secrets.toml
```

Add:

```toml
OPENAI_API_KEY = "your_api_key_here"
```

---

## Run Application

```bash
streamlit run dad4.py
```

---

# 🎯 Applications

- Intelligent Transportation Systems
- Smart City Planning
- Urban Traffic Monitoring
- Transportation Engineering
- Traffic Analytics
- AI Decision Support
- Smart Mobility
- Transportation Research

---

# 📈 Future Roadmap

- Real-Time Traffic API Integration
- Google Maps Integration
- GPS-Based Traffic Monitoring
- AI Congestion Forecasting
- Accident Detection System
- Vehicle Tracking Dashboard
- Power BI Executive Dashboard
- Mobile Application
- Multi-City Deployment
- Deep Learning Traffic Prediction

---

# 👨‍💻 Author

## **Engr. Dr. Kolade Olonisakin, FNSE**

**Civil Engineer | Data Scientist | Machine Learning Engineer | AI Engineer | Transportation & GIS Analytics**

🌍 **Portfolio**

https://kola56de.github.io/Engr-Dr-Kolade-Portfolio.github.io/

💼 **LinkedIn**

https://www.linkedin.com/in/engr-dr-kolade-olonisakin-fnse/

💻 **GitHub**

https://github.com/kola56de

---

# ⭐ Support

If you found this project useful, please consider giving it a **⭐ Star** on GitHub.

Feedback, suggestions, and collaboration opportunities are always welcome.
