from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import os
import uvicorn
import google.generativeai as genai
from pydantic import BaseModel
from dotenv import load_dotenv

# .env dosyasındaki gizli API anahtarlarını yükle
load_dotenv()

app = FastAPI(title="VibeCheck AI API", version="2.0.0")

# 🔒 CORS AYARI: Frontend ile Backend'in güvenle konuşabilmesi için şart!
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 🧠 YAPAY ZEKA (GEMINI) AYARI
# .env dosyasından API anahtarını alıyoruz (Güvenlik Protokolü)
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    print("⚠️ UYARI: GEMINI_API_KEY bulunamadı! Lütfen .env dosyasını kontrol edin.")
else:
    genai.configure(api_key=GEMINI_API_KEY)

@app.get("/")
def read_root():
    return {
        "status": "online",
        "message": "VibeCheck Yapay Zeka Motoru Canlı Olarak Çalışıyor! 🚀"
    }

# 🎯 GERÇEK YAPAY ZEKA DESTEKLİ ENDPOINT
@app.get("/api/vibe")
async def get_vibe_suggestion(mood: str, time: int):
    if not GEMINI_API_KEY:
        raise HTTPException(status_code=500, detail="AI Servis bağlantısı yapılandırılmadı.")
    
    try:
        # Yapay zekaya ne yapacağını söyleyen Prompt (Prompt Engineering)
        prompt = f"""
        Sen 'VibeCheck' adında eğlenceli, cıvıl cıvıl ve motive edici bir Sosyal Enerji Planlama yapay zekasısın.
        Bir kullanıcı şu an '{mood}' modunda/duygu durumunda olduğunu belirtti ve bu aktivite için tam '{time}' dakikası var.
        
        Senden ricam:
        1. Kullanıcının moduna empati yapacak ve enerjisini yükseltecek çok kısa bir giriş cümlesi yaz.
        2. Bu {time} dakikalık süre içinde yapabileceği, o moda özel, nokta atışı ve çok eğlenceli MİKRO bir aktivite önerisi sun.
        3. Metnin içinde bol bol neşeli ve ilgili emojiler kullan.
        4. Yanıtın maksimum 2-3 cümle olsun, kısa, net ve harekete geçirici olsun.
        """

        # Gemini 1.5 Flash modelini çağırıyoruz (Hızlı ve optimize)
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(prompt)
        
        return {
            "mood": mood,
            "time_allocated": time,
            "suggestion": response.text.strip(),
            "source": "Google Gemini 1.5 Flash LLM Engine" # Gerçek AI imzası
        }
        
    except Exception as e:
        # Eğer yapay zeka servisinde anlık bir hata olursa sistem çökmesin diye fallback (B planı)
        return {
            "mood": mood,
            "time_allocated": time,
            "suggestion": f"Şu an modunu tam analiz edemedim ama bence harika bir müzik açıp {time} dakika boyunca dünyayı unutmalısın! 🎵✨",
            "source": "Backup Fallback Engine"
        }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
