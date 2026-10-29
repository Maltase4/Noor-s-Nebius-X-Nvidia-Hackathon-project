# 🌱 Binly: Personal Recycling Assistant

> **Scan. Sort. Sustain.**

Binly is an intelligent, eco-friendly personal recycling assistant designed to help users correctly dispose of waste, learn local recycling rules, and track their personal sustainability impact over time. Built for the hackathon's **Personal AI Track**, Binly combines multimodal AI vision with lightweight local tracking.

---

## 🚀 Key Features

* **Multimodal AI Vision:** Upload a photo of any item (e.g., plastic packaging, electronics, boxes) and let Binly instantly tell you how to recycle or dispose of it.
* **Powered by Nebius Cloud & NVIDIA Models:** Utilizes high-performance vision models (`Qwen/Qwen2-VL-72B-Instruct`) via Nebius token factory infrastructure.
* **Smart Rule Lookup:** Combines quick local keyword guidelines to provide accurate, context-aware recycling instructions.
* **Personal Waste Memory:** Automatically tracks your logged items using local JSON storage so you can monitor your eco-friendly habits.
* **Interactive Streamlit UI:** Clean, modern, and responsive chat interface with a dedicated sidebar for tracking history and explicit logging.

---

## 🛠️ Tech Stack

* **Frontend & UI:** [Streamlit](https://streamlit.io/)
* **AI Model & Inference:** Nebius Cloud, OpenAI Python SDK, Qwen2-VL-72B-Instruct (NVIDIA ecosystem compatible)
* **Data Persistence:** Local JSON Storage (`recycling_memory.json`)
* **Environment Management:** `python-dotenv`

---

## 📂 Project Structure

```text
├── main.py              # Main Streamlit application UI & chat loop
├── ai_client.py         # Nebius API client integration with vision support
├── tools.py             # Local guideline rules lookup
├── memory.py            # Local JSON history and stats manager
├── requirements.txt     # Project dependencies
├── .gitignore           # Excludes sensitive keys and local data
└── README.md            # Project documentation
```

## ⚙️ Local Installation & Setup For Local Deployment 
(run these in your terminal following the file path where you want to install)

1. **Clone the repository:**
   ```bash
   git clone [github link]
   ```
2. **Installing required stuff**
   ```text
   pip install -r requirements.txt
   ```
3. **Launching 🚀**
   ```text
   python -m streamlit run main.py
   ```
4. **Set up the environment file**
   ```text
   api_key=your_actual_chatbot_api_key_here
   TAVILY_API_KEY=your_actual_web_api_key_here
   ```
