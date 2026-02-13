from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from groq import Groq
from dotenv import load_dotenv
import os
import uvicorn

# Load environment variables
load_dotenv()

app = FastAPI(
    title="Bharat AI Chatbot Backend",
    description="Backend for Bharat AI, interacting with Groq Cloud for LLM responses."
)

# --- 1. SETUP PATHS AND MOUNTING ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app.mount("/static", StaticFiles(directory=os.path.join(BASE_DIR, "static")), name="static")
app.mount("/assets", StaticFiles(directory=os.path.join(BASE_DIR, "assets")), name="assets")
app.mount("/categories", StaticFiles(directory=os.path.join(BASE_DIR, "categories")), name="categories")
app.mount("/states", StaticFiles(directory=os.path.join(BASE_DIR, "states")), name="states")
app.mount("/story", StaticFiles(directory=os.path.join(BASE_DIR, "story")), name="story")
app.mount("/home", StaticFiles(directory=os.path.join(BASE_DIR, "home")), name="home")

templates = Jinja2Templates(directory="static")

# --- 2. GROQ SETUP ---
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY environment variable not set.")

groq_client = Groq(api_key=GROQ_API_KEY)
GROQ_DEEPSEEK_MODEL = "moonshotai/kimi-k2-instruct-0905"

# --- 3. SYSTEM PROMPT ---
SYSTEM_PROMPT = """
You are Bharat AI, a highly specialized AI assistant dedicated exclusively to providing information about Bharat.
Your purpose is to educate users about Bharat's rich history, diverse culture, geographical features, current affairs,
future prospects, traditions, festivals, art, and any other topic directly related to Bharat.

You MUST only answer questions that are about Bharat.
If a question is NOT about Bharat, you must politely state that you can only provide information related to Bharat
and cannot answer that specific query.

CRITICAL INSTRUCTION:
- Always use 'Bharat' instead of 'India'.
- Provide clear and direct answers.
- Do not include reasoning steps.
"""

# --- 4. ENDPOINTS ---
@app.post("/chat")
async def chat_endpoint(request: Request):
    try:
        data = await request.json()
        user_message = data.get("message")
        chat_history = data.get("chatHistory", [])

        if not user_message:
            raise HTTPException(status_code=400, detail="Message cannot be empty.")

        messages_for_groq = [{"role": "system", "content": SYSTEM_PROMPT}]

        for msg in chat_history:
            if msg.get("role") in ["user", "assistant"] and "content" in msg:
                messages_for_groq.append({
                    "role": msg["role"],
                    "content": msg["content"]
                })

        messages_for_groq.append({"role": "user", "content": user_message})

        chat_completion = groq_client.chat.completions.create(
            messages=messages_for_groq,
            model=GROQ_DEEPSEEK_MODEL,
            temperature=0.7,
            max_tokens=1024,
        )

        ai_response_text = chat_completion.choices[0].message.content
        return {"response": ai_response_text}

    except Exception as e:
        print(f"Error in chat_endpoint: {e}")
        raise HTTPException(status_code=500, detail=f"Internal server error: {e}")


@app.get("/", response_class=FileResponse)
async def serve_home():
    index_path = os.path.join(BASE_DIR, "home", "index.html")
    if os.path.exists(index_path):
        return FileResponse(index_path)
    return {"error": "index.html not found in home folder."}


@app.get("/bharat-ai", response_class=HTMLResponse)
async def read_chatbot(request: Request):
    return templates.TemplateResponse("bharatai.html", {"request": request})


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=9000)
