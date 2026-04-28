# 🌿 Mental Health Companion

An AI-powered mental wellness chatbot built using Streamlit and a local LLM (phi3 via Ollama).
The application provides emotional support, detects user mood in real-time, and visualizes mood trends through an interactive dashboard.

---

## 🚀 Features

* 💬 **Conversational AI**
  Engage in natural conversations powered by a local language model.

* 🌟 **Positive Affirmations**
  Generates short motivational affirmations to uplift users.

* 🧘 **Guided Meditation**
  Provides calming meditation instructions to reduce stress.

---

## 🛠️ Tech Stack

* **Frontend & App Framework:** Streamlit
* **Backend Logic:** Python
* **LLM Integration:** Ollama (phi3 model)
* **UI Styling:** HTML + CSS (custom styling inside Streamlit)

---

## 📸 Screenshots

### 💬 Chat Interface
![Chat UI](screenshots/chat.png)

### 🌟 Affirmation Feature
![Affirmation](screenshots/affirmation.png)

### 🧘 Meditation Guide
![Meditation](screenshots/meditation.png)
---

## ▶️ How to Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/mental-health-chatbot.git
cd mental-health-chatbot
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Start Ollama (Ensure it's running)

```bash
ollama run phi3
```

### 4. Run the App

```bash
streamlit run app.py
```

---

## 🧠 How It Works

1. User inputs a message via chat
2. The system:

   * Sends input to the LLM (phi3 via Ollama)
   * Detects mood using prompt-based classification
3. Displays:
   * Chat response
---

## 📊 Sample Use Cases

* Stress management and relaxation
* Self-reflection and emotional awareness
* AI-based conversational support

---

## 🔐 Privacy Advantage

This project uses a **local LLM (Ollama)**, meaning:

* No data is sent to external servers
* User conversations remain private
* Suitable for sensitive mental health interactions
---

## 📌 Future Enhancements

* 🎤 Voice-based interaction
* 📅 Mood trends over time (weekly/monthly)
* 📈 Advanced analytics dashboard
* 🌐 Cloud deployment with API-based LLM
* 🔔 Personalized mental health recommendations

---

## 🤝 Contributing

Contributions are welcome!
Feel free to fork the repository and submit a pull request.

---

## 📄 License

This project is for educational and demonstration purposes.

---

## 🙌 Acknowledgements

* Streamlit for rapid UI development
* Ollama for local LLM support
* Open-source AI community

---
