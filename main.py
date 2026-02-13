from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from groq import Groq
from dotenv import load_dotenv
import os
import uvicorn

<<<<<<< HEAD
# Load environment variables
load_dotenv()

=======

load_dotenv()


>>>>>>> 951686f9f20212c10180c2cdb9b790159fb7ef3e
app = FastAPI(
    title="Bharat AI Chatbot Backend",
    description="Backend for Bharat AI, interacting with Groq Cloud for LLM responses."
)

<<<<<<< HEAD
# --- 1. SETUP PATHS AND MOUNTING ---
# This ensures the server knows exactly where your folders are located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Mount specific asset directories
app.mount("/static", StaticFiles(directory=os.path.join(BASE_DIR, "static")), name="static")
app.mount("/assets", StaticFiles(directory=os.path.join(BASE_DIR, "assets")), name="assets")
app.mount("/categories", StaticFiles(directory=os.path.join(BASE_DIR, "categories")), name="categories")
app.mount("/states", StaticFiles(directory=os.path.join(BASE_DIR, "states")), name="states")
app.mount("/story", StaticFiles(directory=os.path.join(BASE_DIR, "story")), name="story")

# THE SECRET FIX: Mount the 'home' folder to the root address
# This allows index.html to find 'home.css' and 'home.js' right at localhost:9000/
app.mount("/home", StaticFiles(directory=os.path.join(BASE_DIR, "home")), name="home")

# Setup Jinja2 Templates (Note: You can keep this pointing to static if bharatai.html is there)
templates = Jinja2Templates(directory="static")

# --- 2. GROQ SETUP ---
=======

app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="static")


>>>>>>> 951686f9f20212c10180c2cdb9b790159fb7ef3e
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY environment variable not set.")

groq_client = Groq(api_key=GROQ_API_KEY)
GROQ_DEEPSEEK_MODEL = "moonshotai/kimi-k2-instruct-0905"

<<<<<<< HEAD
# --- 3. SYSTEM PROMPT ---
=======

GROQ_DEEPSEEK_MODEL = "deepseek-r1-distill-llama-70b"

# --- Initial System Prompt for Bharat AI ---
>>>>>>> 951686f9f20212c10180c2cdb9b790159fb7ef3e
SYSTEM_PROMPT = """
You are Bharat AI, a highly specialized AI assistant dedicated exclusively to providing information about Bharat.
Your purpose is to educate users about Bharat's rich history, diverse culture, geographical features, current affairs,
future prospects, traditions, festivals, art, and any other topic directly related to Bharat.

You MUST only answer questions that are about Bharat.
If a question is NOT about Bharat, you must politely state that you can only provide information related to Bharat
and cannot answer that specific query.

**CRITICAL INSTRUCTION FOR LANGUAGE AND OUTPUT STYLE:**
- When a user refers to 'India' in their query, understand that they mean 'Bharat'. Always process and respond as if they said 'Bharat'.
- You MUST NOT use the word 'India' in any of your responses. Always use 'Bharat' instead.
- Provide clear, concise, and direct answers.
- NEVER include any internal thoughts, reasoning steps, or conversational filler like "Okay, the user is asking...".
- Do NOT generate any XML-like tags (e.g., <think>, <response>).
- Get straight to the point with the factual information.
"""

<<<<<<< HEAD
# --- 4. ENDPOINTS ---
=======

>>>>>>> 951686f9f20212c10180c2cdb9b790159fb7ef3e
@app.post("/chat")
async def chat_endpoint(request: Request):
    try:
        data = await request.json()
        user_message = data.get("message")
<<<<<<< HEAD
=======
        
>>>>>>> 951686f9f20212c10180c2cdb9b790159fb7ef3e
        chat_history = data.get("chatHistory", [])

        if not user_message:
            raise HTTPException(status_code=400, detail="Message cannot be empty.")

<<<<<<< HEAD
        messages_for_groq = [{"role": "system", "content": SYSTEM_PROMPT}]
        for msg in chat_history:
=======
       
        messages_for_groq = [
            {"role": "system", "content": SYSTEM_PROMPT}
        ]
       
        for msg in chat_history:
            
>>>>>>> 951686f9f20212c10180c2cdb9b790159fb7ef3e
            if msg.get("role") in ["user", "assistant"] and "content" in msg:
                messages_for_groq.append({"role": msg["role"], "content": msg["content"]})

<<<<<<< HEAD
        messages_for_groq.append({"role": "user", "content": user_message})

=======
        
        messages_for_groq.append({"role": "user", "content": user_message})

        
>>>>>>> 951686f9f20212c10180c2cdb9b790159fb7ef3e
        chat_completion = groq_client.chat.completions.create(
            messages=messages_for_groq,
            model=GROQ_DEEPSEEK_MODEL,
            temperature=0.7, 
            max_tokens=1024, 
        )

        ai_response_text = chat_completion.choices[0].message.content
        return {"response": ai_response_text}

<<<<<<< HEAD
    except Exception as e:
        print(f"Error in chat_endpoint: {e}")
        raise HTTPException(status_code=500, detail=f"Internal server error: {e}")

@app.get("/", response_class=FileResponse)
async def serve_home():
=======
    except HTTPException as e:
        
        raise e
    except Exception as e:
       
        print(f"Error in chat_endpoint: {e}")
        raise HTTPException(status_code=500, detail=f"Internal server error: {e}")


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
>>>>>>> 951686f9f20212c10180c2cdb9b790159fb7ef3e
    """
    Serves the main landing page using an absolute path to prevent 404s.
    """
    index_path = os.path.join(BASE_DIR, "home", "index.html")
    if os.path.exists(index_path):
        return FileResponse(index_path)
    return {"error": "index.html not found in home folder."}

@app.get("/bharat-ai", response_class=HTMLResponse)
async def read_chatbot(request: Request):
    """
    Serves the chatbot page.
    """
<<<<<<< HEAD
=======
    
>>>>>>> 951686f9f20212c10180c2cdb9b790159fb7ef3e
    return templates.TemplateResponse("bharatai.html", {"request": request})

if __name__ == "__main__":
    # Using Port 9000 as it was successfully used in your previous session
    uvicorn.run(app, host="127.0.0.1", port=9000)