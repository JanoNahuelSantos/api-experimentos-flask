# API for Experiment Management

## 🚀 Description
This project is a REST API built with Flask that allows managing scientists and their experiments.

It was designed applying layered architecture concepts (routes, repositories, entities) and uses JSON files as data persistence.

---

## 🧠 Features

- CRUD for scientists
- CRUD for experiments
- Relationship between scientists and experiments
- Data persistence using JSON files
- Organized architecture (routes, repositories, entities)

---

## 🛠 Technologies

- Python
- Flask
- JSON

---

## 📂 Project Structure

- `rutas/` → API endpoints
- `modelos/entidades/` → domain models
- `modelos/repositorios/` → data access layer
- `datos/` → JSON storage
- `app.py` → main application

---

## 📊 System Design

![Diagram](diagram.png)

---

## ⚙️ How to Run

1. Clone the repository:
```bash
git clone https://github.com/JanoNahuelSantos/api-experimentos-flask.git

2.	Go to the project folder:
cd api-experimentos-flask

3. Install dependencies:
pip install flask

4.	Run the application:
python app.py

## 📡 API Endpoints

Scientists
	•	GET /cientificos
	•	POST /cientificos
	•	PUT /cientificos/<id>
	•	DELETE /cientificos/<id>

Experiments
	•	GET /experimentos
	•	POST /experimentos
	•	PUT /experimentos/<id>
	•	DELETE /experimentos/<id>

## 📥 Example Request
{
  "id": 1,
  "titulo": "Test Experiment",
  "descripcion": "Example experiment",
  "resultado": "Success",
  "fecha": "2026-01-01",
  "autor": 123
}

## 👤 Author

Jano Nahuel Santos
