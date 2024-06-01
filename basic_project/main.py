# main.py
from fastapi import FastAPI
from routes.question_routes import router as question_router

app = FastAPI()

# Include the routes from question_routes.py
app.include_router(question_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
