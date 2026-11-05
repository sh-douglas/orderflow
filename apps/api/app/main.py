from fastapi import FastAPI, status

app = FastAPI(title="OrderFlow API")

@app.get("/health", status_code=status.HTTP_200_OK)
async def health_check():
    return {"status": "ok"}
