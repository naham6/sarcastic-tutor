# 🐍 Sarcastic Python Tutor AI

> *An AI-powered coding assistant that helps you learn Python... while roasting.*

Built with **FastAPI**, and **Streamlit**.

---

## 📂 Project Structure

This repository contains two versions of the application:

### 1. The Cloud Version (`app_online.py`)
A standalone Streamlit app designed for easy deployment on **Streamlit Cloud**. It combines the frontend and backend logic into a single file for simplicity. Easily deployable online.

### 2. The Local "Full-Stack" Version
A professional architecture separating the backend API from the frontend UI:
* **`main.py`**: The FastAPI backend server.
* **`frontend.py`**: The Streamlit frontend interface.
* **`my_agent.py`**: The AI logic module with prompt.

---

## 💻 How to Run Locally

Follow these steps to get the project running on your own machine.

### 1. Clone the repository
```bash
git clone [https://github.com/naham6/sarcastic-tutor.git](https://github.com/naham6/sarcastic-tutor.git)
cd sarcastic-tutor
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set up your API Key

1. Get a free API Key from Google AI Studio.
2. Create a file named `.env` in the root folder. If you are running online, put the secret key GEMINI_API_KEY="yourapi"
3. Add your key inside the file like this:

```env
GEMINI_API_KEY="your_actual_api_key_here"
```

### 4. Run the Backend (Terminal 1)

Open a terminal and start the FastAPI server:

```bash
uvicorn main:app --reload
```

*You should see: `Uvicorn running on http://127.0.0.1:8000*`

### 5. Run the Frontend (Terminal 2)

Open a **new** terminal window and launch the UI:

```bash
streamlit run frontend.py
```

---

## 🛠️ Tech Stack

* **AI Model:** Google Gemini 2.5 Flash
* **Backend:** FastAPI (Python)
* **Frontend:** Streamlit
* **Deployment:** Streamlit Cloud
