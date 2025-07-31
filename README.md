<h1>Bharat Darshan: A Modern Gateway to Indian Heritage and Culture
Overview</h1>
This project is a modern and visually refreshed website dedicated to showcasing the rich heritage and vibrant culture of Bharat. My aim was to provide an engaging and intuitive experience for users exploring Indian culture.

[![Watch the full demo video](https://img.youtube.com/vi/38/hqdefault.jpg)](https://www.youtube.com/watch?v=fII9_hPRFzM)

A key feature of this website is the integrated Bharat AI chatbot.

<h2>Bharat AI: Your Personal Guide to Bharat</h2>
Bharat AI is an AI-powered chatbot seamlessly integrated into the website. Its sole purpose is to provide comprehensive and accurate information exclusively about Bharat. It guides users on Bharat's history, traditions, and current affairs. It is user-friendly, provides concise information, and consistently uses 'Bharat' in its responses.

<h2>Technologies Used</h2>
Frontend (UI/UX)
HTML5: For website structure.

CSS3 (Custom & Tailwind CSS): For unique design, animations, and rapid, consistent development.

JavaScript: Controls interactive elements and chatbot behavior.

Backend (Bharat AI Chatbot)
FastAPI (Python Framework): Secure and high-performance API backend for Bharat AI.

Groq Cloud API: For low-latency and fast responses.

DeepSeek-R1 Model: A powerful LLM hosted on Groq Cloud, focused on Bharat-related information.

python-dotenv: For secure loading of API keys.

<h2>Setup and Running Locally</h2>
To run this project locally:

Clone the Repository

Install Python Dependencies:

pip install fastapi uvicorn python-dotenv groq

Set Your Groq API Key: Obtain GROQ_API_KEY from GroqCloud Console and add it to a .env file in the project root. (Do not commit .env to Git.)

Run the Backend Server:

uvicorn main:app --reload

The server will start at http://127.0.0.1:8000.

Access the Website: Open your browser to http://127.0.0.1:8000/. The Bharat AI chatbot will be available via its floating icon or navigation bar link.

Deployment
To make the project public, deploy both frontend and backend separately:

Frontend Hosting: Deploy HTML, CSS, JS files to a static site host (e.g., Netlify).

Backend Hosting: Deploy main.py (FastAPI) to a backend host (e.g., Google Cloud Run).

Update backendApiUrl in frontend JS to the deployed backend's public URL.

Securely configure GROQ_API_KEY on the platform.
