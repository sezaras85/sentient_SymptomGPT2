# 🤖 Dobby SymptomGPT

symptomGPT is a fun and stimulating Streamlit app that provides AI-powered health guidance by collecting symptoms from the user. Model: Dobby-70B (Fireworks AI)

---

## ✨ Features

- Symptom interpretation
- Joking but serious guidance
- (Coming soon) Location-based doctor/hospital recommendations


---

## 🚀 Quick Start

### 1. Requirements

- Python 3.9+
- A Fireworks AI API key → [https://app.fireworks.ai](https://app.fireworks.ai)




### 3. Clone the Repository

```bash

git clone https://github.com/sezaras85/sentient_SymptomGPT.git
cd symptom-gpt
cp .env.example .env
```

Edit the .env file with your own credentials:
```bash
FIREWORKS_API_KEY=your_fireworks_api_key
```

4. Install Dependencies
```bash
sudo apt install python3-venv -y
python3 -m venv symptomgpt-env
source symptomgpt-env/bin/activate

pip install --upgrade pip
pip install streamlit requests python-dotenv
```

5. Run the Bot
```bash
streamlit run app.py --server.address=0.0.0.0 --server.port=8501


```

You should see:

```bash
You can now view your Streamlit app in your browser.

  URL: http://0.0.0.0:8501
```



```
