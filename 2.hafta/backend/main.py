from fastapi import FastAPI
import uvicorn

app = FastAPI(title="VibeCheck API")

@app.get("/")
def home():
    return {
        "status": "online",
        "message": "VibeCheck Backend Motoru Calisiyor!",
        "version": "1.0.0"
    }

# Uygulamayi dogrudan calistirmak icin gereken blok
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
