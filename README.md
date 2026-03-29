# 🚀 E-commerce Analytics Dashboard

A full-stack data analytics and machine learning project that provides deep insights into e-commerce data through an interactive and visually rich dashboard.

---

## 📌 Project Overview

This project transforms raw e-commerce data into actionable business insights using:

* 📊 Data Analysis & Visualization
* 🤖 Machine Learning (Customer Segmentation)
* 🌐 Interactive Dashboard (Streamlit)

The dashboard enables users to explore revenue trends, customer behavior, and product performance in a clean, professional interface inspired by modern SaaS analytics tools.

---

## 🎯 Key Features

### 📊 Interactive Dashboard

* Real-time filtering (Year, State, All combined view)
* Revenue trends visualization
* Top cities and product categories analysis
* Scatter plots for pricing insights

### 🤖 Machine Learning

* Customer segmentation using **K-Means Clustering**
* RFM (Recency, Frequency, Monetary) analysis
* Identification of:

  * High-value customers
  * Frequent buyers
  * Low-engagement users

### 💼 Business Insights

* KPI metrics (Revenue, Orders, Customers)
* Customer segment distribution
* Data-driven decision support

### 📥 Export Functionality

* Download filtered dataset directly from dashboard

---

## 🧠 Tech Stack

| Category      | Tools Used            |
| ------------- | --------------------- |
| Language      | Python                |
| Data Handling | Pandas                |
| Visualization | Plotly                |
| ML Model      | Scikit-learn (KMeans) |
| Dashboard     | Streamlit             |
| Deployment    | Streamlit Cloud       |

---

## 📂 Project Structure

```
Ecommerce-Dashboard/
│
├── dashboard/
│   └── app.py
├── data/
│   ├── cleaned_data.csv
│   └── rfm_data.csv
├── models/
│   └── kmeans_model.pkl
├── src/
│   └── model.py
├── notebooks/
│   └── eda.ipynb
└── requirements.txt
```

---

## ⚙️ How to Run Locally

1. Clone the repository:

```
git clone https://github.com/your-username/ecommerce-dashboard.git
```

2. Navigate to project:

```
cd Ecommerce-Dashboard/dashboard
```

3. Install dependencies:

```
pip install -r ../requirements.txt
```

4. Run the app:

```
python -m streamlit run app.py
```

---

## 🌐 Live Demo

👉 *(Add your deployed link here after deployment)*

---

## 📊 Sample Insights

* High-value customers contribute disproportionately to total revenue
* Certain cities dominate sales performance
* Product categories show clear demand patterns
* Pricing has a direct relationship with revenue clusters

---

## 🚀 Future Improvements

* Multi-select and date range filters
* AI-generated insights
* Real-time data integration
* User authentication system
* Advanced ML models (churn prediction, recommendation systems)

---

## 🤝 Contribution

Contributions are welcome! Feel free to fork the repo and submit pull requests.


## ⭐ If you like this project

Give it a ⭐ on GitHub — it really helps!
