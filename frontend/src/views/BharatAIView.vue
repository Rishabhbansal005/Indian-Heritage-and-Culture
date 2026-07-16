<template>
  <div class="ai-page">
    <div class="chat-container">
      <div class="chat-messages" ref="messagesEl">
        <div
          v-for="(msg, i) in messages"
          :key="i"
          :class="['message-bubble', msg.role === 'user' ? 'user-message' : 'ai-message']"
        >
          {{ msg.content }}
        </div>
        <div v-if="loading" class="typing-indicator">
          <span></span><span></span><span></span>
        </div>
      </div>

      <div class="chat-input-area">
        <input
          v-model="inputText"
          type="text"
          placeholder="Ask Bharat AI about Bharat..."
          @keypress.enter="sendMessage"
          :disabled="loading"
        />
        <button @click="sendMessage" :disabled="loading">
          <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" fill="currentColor" viewBox="0 0 16 16">
            <path d="M15.964.686a.5.5 0 0 0-.65-.65L.767 5.855H.766l-.452.18a.5.5 0 0 0-.082.887l.41.26.001.002 4.995 3.178 3.178 4.995.002.002.26.41a.5.5 0 0 0 .886-.083zm-1.833 1.89L6.637 10.07l-.215-.338a.5.5 0 0 0-.154-.154l-.338-.215 7.494-7.494 1.178-.471z"/>
          </svg>
          <span class="btn-text">Send</span>
        </button>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, nextTick } from 'vue'

interface Message {
  role: 'user' | 'assistant'
  content: string
}

const messages = ref<Message[]>([
  { role: 'assistant', content: 'Namaste! I am Bharat AI, your dedicated guide to the culture and heritage of Bharat. How may I assist you today?' }
])
const inputText = ref('')
const loading = ref(false)
const messagesEl = ref<HTMLElement | null>(null)

async function scrollToBottom() {
  await nextTick()
  if (messagesEl.value) {
    messagesEl.value.scrollTop = messagesEl.value.scrollHeight
  }
}

async function sendMessage() {
  const text = inputText.value.trim()
  if (!text || loading.value) return

  messages.value.push({ role: 'user', content: text })
  inputText.value = ''
  loading.value = true
  await scrollToBottom()

  try {
    const response = await fetch('/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        message: text,
        chatHistory: messages.value.slice(0, -1)
      })
    })

    if (!response.ok) throw new Error('Server error')

    const data = await response.json()
    let reply: string = data.response || 'I apologize, I could not process that.'
    reply = reply.replace(/\s*<think>.*?<\/think>\s*/gis, '').trim()
    reply = reply.replace(/\bIndia\b/gi, 'Bharat')

    messages.value.push({ role: 'assistant', content: reply })
  } catch {
    messages.value.push({ role: 'assistant', content: 'I am currently unable to connect to the backend. Please check your Python terminal.' })
  } finally {
    loading.value = false
    await scrollToBottom()
  }
}
</script>

<style scoped>
.ai-page {
  background: #000;
  min-height: 100vh;
  display: flex;
  justify-content: center;
  align-items: flex-start;
  padding: 100px 16px 40px;
  box-sizing: border-box;
}

.chat-container {
  width: 100%;
  max-width: 680px;
  background: #fff;
  border-radius: 1.5rem;
  box-shadow: 0 25px 60px rgba(0,0,0,0.4);
  display: flex;
  flex-direction: column;
  overflow: hidden;
  height: calc(100vh - 140px);
  max-height: 900px;
  animation: fadeUp 0.7s ease-out;
}

@keyframes fadeUp {
  from { opacity: 0; transform: translateY(20px); }
  to   { opacity: 1; transform: translateY(0); }
}

.chat-messages {
  flex-grow: 1;
  padding: 1.4rem;
  overflow-y: auto;
  display: flex;
  flex-direction: column;
  gap: 1.1rem;
  background: #fafafa;
  scroll-behavior: smooth;
}

.chat-messages::-webkit-scrollbar { width: 5px; }
.chat-messages::-webkit-scrollbar-thumb { background: #FF9933; border-radius: 4px; }

.message-bubble {
  max-width: 85%;
  padding: 0.9rem 1.2rem;
  border-radius: 1.2rem;
  font-size: 0.98rem;
  line-height: 1.6;
  word-wrap: break-word;
  animation: slideIn 0.35s ease-out forwards;
  opacity: 0;
}

@keyframes slideIn {
  from { opacity: 0; transform: translateY(12px); }
  to   { opacity: 1; transform: translateY(0); }
}

.user-message {
  align-self: flex-end;
  background: linear-gradient(135deg, #FF9933 0%, #ff7700 100%);
  color: #fff;
  box-shadow: 0 3px 10px rgba(255, 153, 51, 0.3);
  border-bottom-right-radius: 4px;
}

.ai-message {
  align-self: flex-start;
  background: #f0f0f0;
  color: #222;
  border: 1px solid #e0e0e0;
  border-bottom-left-radius: 4px;
}

/* Typing dots */
.typing-indicator {
  align-self: flex-start;
  display: flex;
  gap: 6px;
  padding: 14px 18px;
  background: #f0f0f0;
  border-radius: 1.2rem;
  border-bottom-left-radius: 4px;
}

.typing-indicator span {
  width: 8px;
  height: 8px;
  background: #FF9933;
  border-radius: 50%;
  animation: bounce 1.3s infinite ease-in-out both;
}
.typing-indicator span:nth-child(1) { animation-delay: -0.3s; }
.typing-indicator span:nth-child(2) { animation-delay: -0.15s; }

@keyframes bounce {
  0%, 80%, 100% { transform: translateY(0); }
  40%            { transform: translateY(-10px); }
}

/* Input area */
.chat-input-area {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 1rem;
  border-top: 1px solid #e8e8e8;
  background: #fff;
}

.chat-input-area input {
  flex-grow: 1;
  min-width: 0;
  padding: 0.8rem 1.2rem;
  border: 1.5px solid #ddd;
  border-radius: 1.5rem;
  font-size: 0.97rem;
  outline: none;
  transition: border-color 0.3s, box-shadow 0.3s;
  background: #f9f9f9;
  font-family: 'Poppins', sans-serif;
}

.chat-input-area input:focus {
  border-color: #FF9933;
  box-shadow: 0 0 0 3px rgba(255, 153, 51, 0.15);
}

.chat-input-area button {
  flex-shrink: 0;
  display: flex;
  align-items: center;
  gap: 6px;
  padding: 0.8rem 1.4rem;
  background: linear-gradient(135deg, #FF9933, #ff6600);
  color: #fff;
  border: none;
  border-radius: 1.5rem;
  font-size: 0.95rem;
  font-weight: 600;
  cursor: pointer;
  transition: transform 0.2s, box-shadow 0.3s;
  box-shadow: 0 4px 14px rgba(255, 153, 51, 0.35);
  white-space: nowrap;
}

.chat-input-area button:hover:not(:disabled) {
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(255, 153, 51, 0.5);
}

.chat-input-area button:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

/* Responsive */
@media (max-width: 768px) {
  .ai-page { padding: 82px 8px 20px; }
  .chat-container { height: calc(100vh - 100px); max-height: none; border-radius: 1rem; }
  .message-bubble { font-size: 0.91rem; max-width: 90%; }
  .chat-input-area { padding: 0.75rem; }
}

@media (max-width: 480px) {
  .ai-page { padding: 72px 4px 12px; }
  .chat-container { border-radius: 0.75rem; height: calc(100vh - 84px); }
  .btn-text { display: none; }
  .chat-input-area button { padding: 0.8rem 1rem; }
}
</style>
