import os
import requests
import streamlit as st
from dotenv import load_dotenv

load_dotenv()


# 
st.set_page_config(page_title="SymptomGPT", layout="centered")
st.title("🩺 SymptomGPT - AI Health Assistant")

st.markdown("""
Bir sağlık uzmanı değilim. Bu araç, belirttiğiniz semptomları analiz eder ve dikkat etmeniz gereken noktaları önerir.
Kesin tanı veya tıbbi tavsiye vermez. 🧠
""")

# Fireworks API anahtarını oku (env üzerinden)
FIREWORKS_API_KEY = os.getenv("FIREWORKS_API_KEY") or "BURAYA_API_KEYİNİ_YAZ"

# Kullanıcının girdiği semptom
user_input = st.text_area("Semptomlarınızı detaylı olarak yazın:", height=200)

# Butona tıklanınca modeli çağır
if st.button("Analiz Et"):
    if not FIREWORKS_API_KEY or FIREWORKS_API_KEY.startswith("BURAYA"):
        st.error("❌ Fireworks API anahtarını ayarlaman gerekiyor!")
    elif not user_input.strip():
        st.warning("Lütfen semptomlarınızı girin.")
    else:
        st.info("🤖 Yapay zeka analiz ediyor...")

        # Fireworks API ayarları
        headers = {
            "Authorization": f"Bearer {FIREWORKS_API_KEY}",
            "Content-Type": "application/json"
        }

        data = {
            "model": "accounts/sentientfoundation/models/dobby-unhinged-llama-3-3-70b-new",
            "max_tokens": 1024,
            "temperature": 0.5,
            "top_p": 0.95,
            "messages": [
                {"role": "system", "content": (
                    "You are SymptomGPT, a helpful virtual assistant for interpreting health symptoms. "
                    "When users describe symptoms, respond with informative and cautious suggestions. "
                    "Never provide a diagnosis or medical certainty. Always remind users to consult a real doctor."
                )},
                {"role": "user", "content": user_input}
            ]
        }

        try:
            response = requests.post(
                "https://api.fireworks.ai/inference/v1/chat/completions",
                headers=headers,
                json=data
            )

            if response.status_code == 200:
                output = response.json()["choices"][0]["message"]["content"]
                st.success("🩻 Analiz Tamamlandı:")
                st.markdown(output)
            else:
                st.error(f"Hata: {response.status_code} - {response.text}")

        except Exception as e:
            st.error(f"İstek gönderilirken bir hata oluştu: {e}")

