# 🌍 India Village Search System

A full-stack data application built using Python, Flask, and SQLite to provide structured access to Indian village-level data.

---

## 🚀 Features

* 🔍 Search by State, District, and Village
* 📊 Handles 4.6+ lakh records efficiently
* 🌐 Web UI for user-friendly interaction
* 🔗 REST API endpoints for data access
* 🔐 API Key authentication for security
* 📈 Stats endpoint for dataset insights

---

## 🛠 Tech Stack

* Python
* Flask
* SQLite
* Pandas
* HTML + CSS

---

## 📂 Project Structure

VillageProject/
│── app.py
│── csv_to_db.py
│── village.db
│── templates/
│   └── index.html

---

## ▶️ How to Run

1. Clone the repository:
   git clone https://github.com/yourusername/village-search-system.git
   cd village-search-system

2. Install dependencies:
   pip install flask pandas

3. Run the application:
   python app.py

4. Open in browser:
   http://127.0.0.1:5000

---

## 🔗 API Endpoints

* /api/state/<name>?api_key=12345
* /api/district/<name>?api_key=12345
* /api/village/<name>?api_key=12345

---

## 📊 Stats Endpoint

* /stats → Returns total number of records in database

---

## 🔐 API Key

12345

---

## 📌 Future Improvements

* PostgreSQL integration
* Cloud deployment (Render / Railway)
* Advanced filtering & search
* Admin dashboard

---

## 👨‍💻 Author

Ketan Zode
