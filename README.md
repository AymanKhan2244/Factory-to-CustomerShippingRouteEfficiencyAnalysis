# 🚚 Nassau Candy Logistics Analytics & Shipment Delay Prediction

An end-to-end **Data Science** project that analyzes logistics operations, identifies shipping bottlenecks, and predicts shipment delays using **Machine Learning**. The project includes interactive dashboards built with **Streamlit** to provide operational insights into factory-to-customer shipping performance.

---

# 📖 Overview

Efficient logistics operations are critical for reducing delivery delays and improving customer satisfaction. This project analyzes shipment data from **Nassau Candy Distributor** to evaluate shipping performance, identify inefficient routes, detect geographic bottlenecks, compare shipping methods, and predict shipment delays using an **XGBoost Classification Model**.

The application enables logistics managers to make informed decisions through interactive visualizations and predictive analytics.

---

# 🎯 Objectives

* Analyze factory-to-customer shipping performance.
* Identify efficient and inefficient shipping routes.
* Detect congestion-prone states and regions.
* Compare the effectiveness of different shipping modes.
* Predict shipment delays using Machine Learning.
* Provide an interactive dashboard for logistics analysis.

---

# ✨ Features

## 📊 Executive Summary

* Overall shipment statistics
* Average lead time
* Total delayed shipments
* Key performance indicators (KPIs)

---

## 🚛 Route Efficiency Analysis

* Average lead time by route
* Route performance leaderboard
* Top-performing routes
* Least efficient routes

---

## 🌍 Geographic Analysis

* State-wise shipping performance
* Region-wise shipping performance
* Geographic bottleneck analysis
* Congestion-prone states

---

## 📦 Ship Mode Analysis

* Shipment distribution
* Lead time comparison
* Ship mode performance
* Cost vs. efficiency insights

---

## 🔍 Route Drill-Down

* State-level performance
* Factory-level analysis
* Shipment timelines
* Detailed shipment records

---

## 🎛️ Advanced Filters

* Date Range Filter
* Region Filter
* State Filter
* Ship Mode Filter
* Lead Time Threshold

---

## 🤖 Shipment Delay Prediction

Predict whether a shipment is likely to be delayed using an **XGBoost Classifier**.

### Input Features

* Ship Mode
* Region
* State/Province
* Division
* Factory
* Sales
* Cost
* Gross Profit
* Order Month

### Output

* Delay Prediction
* Delay Probability

---

## 📈 Model Performance

* Accuracy
* Precision
* Recall
* F1 Score
* Confusion Matrix
* Feature Importance

---

# 🧠 Machine Learning

## Problem Type

Binary Classification

## Target Variable

```text
Delayed
```

## Algorithm

* XGBoost Classifier

## Evaluation Metrics

* Accuracy
* Precision
* Recall
* F1 Score
* Confusion Matrix
* Feature Importance

---

# 🛠 Tech Stack

## Programming Language

* Python

## Data Analysis

* Pandas
* NumPy

## Visualization

* Matplotlib
* Seaborn

## Machine Learning

* Scikit-learn
* XGBoost

## Dashboard

* Streamlit

## Model Serialization

* Joblib

## Package Manager

* uv

---

# 📂 Project Structure

```text
.
├── data
│   └── Nassau Candy Distributor.csv
│
├── notebooks
│   ├── DATA_ANALYSIS.ipynb
│   └── notebook_for_ML_model_training.ipynb
│
├── shipping-dashboard
│   ├── app.py
│   │
│   ├── data
│   │   └── Cleaned_shipping_data.csv
│   │
│   ├── model
│   │   └── CandyDistributerModel.joblib
│   │
│   ├── pages
│   │   ├── Executive_summary.py
│   │   ├── Route_Efiiciency.py
│   │   ├── Geographic_Analysis.py
│   │   ├── ship_mode_anaysis.py
│   │   ├── Route_Drilldown.py
│   │   ├── Delay_prediction.py
│   │   ├── model_performance.py
│   │   └── advanced_filteers.py
│   │
│   └── utils
│       └── data_loader.py
│
├── pyproject.toml
├── uv.lock
└── README.md
```

---

# 🚀 Installation Guide

## Step 1: Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
```

Navigate to the project folder.

```bash
cd YOUR_REPOSITORY
```

---

## Step 2: Install uv

### Windows

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### macOS / Linux

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Verify the installation.

```bash
uv --version
```

---

## Step 3: Create a Virtual Environment

```bash
uv venv
```

---

## Step 4: Activate the Virtual Environment

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

---

## Step 5: Install Project Dependencies

```bash
uv sync
```

This installs all required packages from the `uv.lock` file.

---

# ▶️ Running the Streamlit Application

Navigate to the Streamlit application directory.

```bash
cd shipping-dashboard
```

Run the application.

```bash
streamlit run app.py
```

Alternatively, you can use:

```bash
uv run streamlit run shipping-dashboard/app.py
```

Once the server starts, open your browser and navigate to:

```text
http://localhost:8501
```

---

# 📊 Dashboard Pages

* 🏠 Home
* 📊 Executive Summary
* 🚛 Route Efficiency Analysis
* 🌍 Geographic Analysis
* 📦 Ship Mode Analysis
* 🔍 Route Drill-Down
* 🤖 Delay Prediction
* 📈 Model Performance
* 🎛️ Advanced Filters

---

# 📈 Machine Learning Workflow

```text
Raw Dataset
      │
      ▼
Data Cleaning
      │
      ▼
Feature Engineering
      │
      ▼
Exploratory Data Analysis
      │
      ▼
Visualization
      │
      ▼
Model Training (XGBoost)
      │
      ▼
Model Evaluation
      │
      ▼
Delay Prediction
      │
      ▼
Interactive Streamlit Dashboard
```

---

# 📌 Key Insights

* Geographic location significantly impacts shipment lead time.
* Certain factory-to-state routes consistently outperform others.
* Seasonal variations influence shipping delays.
* Ship mode selection affects delivery performance.
* Machine learning enables proactive identification of high-risk shipments.

---

# 📸 Screenshots

Add screenshots of:

* Executive Summary
* Route Efficiency Dashboard
* Geographic Analysis
* Ship Mode Analysis
* Delay Prediction
* Model Performance

---

# 🔮 Future Enhancements

* Hyperparameter optimization
* Interactive geographic maps
* Real-time shipment monitoring
* Automated model retraining
* Cloud-native deployment
* Time-series forecasting for shipment demand

---

# 👨‍💻 Author

**Ayman Khan**

BCA Student | Aspiring Data Scientist & AI Engineer

### Skills

* Python
* Data Science
* Machine Learning
* Streamlit
* XGBoost
* Pandas
* NumPy
* Matplotlib
* Seaborn

---

# 🙏 Acknowledgements

This project was developed as part of a **Data Science Internship**, focusing on logistics analytics, business intelligence, and predictive modeling for shipment delay analysis.

---

# ⭐ Support

If you found this project useful, consider giving the repository a ⭐ on GitHub.
