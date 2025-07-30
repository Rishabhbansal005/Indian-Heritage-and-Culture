from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from groq import Groq
from dotenv import load_dotenv
import os
import uvicorn


load_dotenv()


app = FastAPI(
    title="Bharat AI Chatbot Backend",
    description="Backend for Bharat AI, interacting with Groq Cloud for LLM responses."
)


app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="static")


GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY environment variable not set. Please create a .env file or set the variable.")

groq_client = Groq(api_key=GROQ_API_KEY)


GROQ_DEEPSEEK_MODEL = "deepseek-r1-distill-llama-70b"

# --- Initial System Prompt for Bharat AI ---
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
- NEVER include any internal thoughts, reasoning steps, or conversational filler like "Okay, the user is asking...", "I should respond...", "I'll make sure...", or any similar self-talk.
- Do NOT generate any XML-like tags (e.g., <think>, <response>, <tool_code>, <tool_output>).
- Get straight to the point with the factual information.
- Keep your responses factual and to the necessary detail, unless explicitly asked for more detail.
- If a greeting is received, respond with a simple, direct greeting and an offer to help with Bharat-related information, without any internal monologue.
- Ensure your output is purely the response for the user.
"""


@app.post("/chat")
async def chat_endpoint(request: Request):
    """
    Handles chat messages from the frontend, sends them to Groq Cloud,
    and returns the AI's response.
    """
    try:
        data = await request.json()
        user_message = data.get("message")
        
        chat_history = data.get("chatHistory", [])

        if not user_message:
            raise HTTPException(status_code=400, detail="Message cannot be empty.")

       
        messages_for_groq = [
            {"role": "system", "content": SYSTEM_PROMPT}
        ]
       
        for msg in chat_history:
            
            if msg.get("role") in ["user", "assistant"] and "content" in msg:
                messages_for_groq.append({"role": msg["role"], "content": msg["content"]})
            else:
                print(f"Warning: Skipping invalid chat history message: {msg}")

        
        messages_for_groq.append({"role": "user", "content": user_message})

        
        chat_completion = groq_client.chat.completions.create(
            messages=messages_for_groq,
            model=GROQ_DEEPSEEK_MODEL,
            temperature=0.7, 
            max_tokens=1024, 
        )

        ai_response_text = chat_completion.choices[0].message.content
        return {"response": ai_response_text}

    except HTTPException as e:
        
        raise e
    except Exception as e:
       
        print(f"Error in chat_endpoint: {e}")
        raise HTTPException(status_code=500, detail=f"Internal server error: {e}")


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    """
    Serves the main bharatai.html file for the chatbot.
    """
    
    return templates.TemplateResponse("bharatai.html", {"request": request})

