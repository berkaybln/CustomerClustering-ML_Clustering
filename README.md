# 🛒 Wholesale Customer Segmentation & AI Profiling

![Python](https://img.shields.io/badge/Python-3.12.12-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![Docker](https://img.shields.io/badge/Docker-Container-blue)
![Scikit-Learn](https://img.shields.io/badge/Sklearn-Machine%20Learning-orange)
![SQL](https://img.shields.io/badge/SQL-SQLite-lightgrey)

**"Discover who your customers are by looking at their 'behavior,' not their 'labels.'"**

This project is a Machine Learning and Data Science project that analyzes customer data for a wholesale company and segments them (end-to-end) based on their purchasing habits.

🔗 **Live App:** https://huggingface.co/spaces/berkaybln/CustomerSegmentation

---

## 🎯 Project Aim and Business Value

In traditional CRM systems, customers are only labeled as "Restaurant" or "Market." However, data shows that these labels can sometimes be misleading. With this project:

1.  **Hidden Opportunities Discovered:** Businesses registered as "Restaurants" (Horeca) but stocking up like a huge "Supermarket," etc., were identified.
2.  **Mistargeting Prevented:** Marketing budgets were optimized by segmenting businesses based on behavior rather than category.
3.  **Regional Myth Debunked:** It was proven that customer behavior is independent of geographic region; the strategy was extended to the national level.

---

## 🏗️ Architecture and Data Flow (Real-World Simulation)

Bu projede sadece hazır bir CSV dosyası kullanılmamış, **gerçek bir veri tabanı süreci simüle edilmiştir.**

### 1. Data Engineering & SQL
The raw dataset was divided into two to transform it into a relational structure:
* **Table 1 `clients`:** Customer ID, Channel, and Region information.
* **Table 2 `purchases`:** Annual spending data by product category.

These tables were stored in WholesaleCustomersDatabase.db (SQLite), and were processed by joining them with SQL JOIN queries during the analysis process.

### 2. Data Preprocessing
* Outlier analysis was performed.
* Yeo-Johnson Transform was applied to correct distribution distortion.
* The data was also subjected to Standard Scaling during the transformation process to bring them to the same scale.

### 3. Modeling (Unsupervised Learning)
* **Algorithm:** K-Means Clustering.
* **Optimization:** The optimal number of clusters ( k = 4 ) was determined using the Elbow Method.
* **Pipeline:** All preprocessing and modeling steps were packaged in a single Scikit-Learn Pipeline.

---

## 📊 Customer Segments (Personas)

The 4 main customer profiles resulting from the model:

| Cluster | Profile Name | Characteristics |
| :--- | :--- | :--- |
| **0** | **High Retail** 💰 | Retailers with very high volume inventory. |
| **1** | **Low Horeca** ☕ | Small-scale cafes and boutique restaurants. |
| **2** | **Low Retail** 💵 | This is a business with high spending potential. |
| **3** | **High Horeca** 🍽️ | Large hotels, catering companies, and luxury restaurants. |

---

## 💻 Technologies and Tools

* **Language:** Python 3.12.12
* **Database:** SQL (SQLite)
* **Data Processing:** Pandas, NumPy
* **Machine Learning:** Scikit-Learn (Pipeline, K-Means, PowerTransformer)
* **Visualization:** Plotly (Radar Charts), Seaborn, Matplotlib
* **Web Interface:** Streamlit
* **Deployment:** Docker & Hugging Face Spaces

---
