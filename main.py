from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Status": "AI Food Agent System Online"}