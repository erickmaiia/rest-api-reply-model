from fastapi import FastAPI
from app.routes.llm_routes import router as llm_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["POST"],
    allow_headers=["*"],
)

# Incluindo as rotas do LLM
app.include_router(llm_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Text Analysis API"}