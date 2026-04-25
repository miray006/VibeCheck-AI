from fastapi import FastAPI
from typing import Optional

app = FastAPI(title="VibeCheck API")

@app.get("/")
def home():
    return {
        "status": "online",
        "message": "VibeCheck Backend Motoru Çalışıyor!",
        "version": "1.0.0"
    }

@app.get("/recommend")
def get_recommendation(vibe: str, duration: int):
    # Bu kısım Faz 2'de AI algoritması ile dolacak
    return {
        "input_vibe": vibe,
        "input_duration": duration,
        "recommendation": "Algoritma geliştirme aşamasında. Çok yakında moduna uygun aktivite burada!"
    }