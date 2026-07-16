<template>
  <button
    id="music-toggle-btn"
    :class="{ muted: isMuted }"
    @click="toggleMusic"
    :title="isMuted ? 'Play Music' : 'Mute Music'"
  >
    {{ isMuted ? '🔇' : '🔊' }}
  </button>
  <audio ref="audioEl" loop>
    <source :src="audioSrc" type="audio/mp3" />
  </audio>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'

// Plain string — not processed by Vite's static import analysis
const audioSrc = '/static/Ram Navami Bhajan. Raghupati Raghava Raja Ram Instrumental Bhajan Flute Sitar Tabla Yajur Veda Band..mp3'

const audioEl = ref<HTMLAudioElement | null>(null)
const isMuted = ref(localStorage.getItem('musicPaused') === 'true')

onMounted(() => {
  const audio = audioEl.value
  if (!audio) return
  audio.volume = 0.5
  // Must call load() first when src is set via dynamic binding
  audio.load()
  if (!isMuted.value) {
    // Use 'canplay' event as fallback for browsers that block autoplay
    const tryPlay = () => {
      audio.play().catch(() => { isMuted.value = true })
    }
    audio.addEventListener('canplay', tryPlay, { once: true })
  }
})

function toggleMusic() {
  const audio = audioEl.value
  if (!audio) return
  if (audio.paused) {
    audio.play()
    isMuted.value = false
    localStorage.setItem('musicPaused', 'false')
  } else {
    audio.pause()
    isMuted.value = true
    localStorage.setItem('musicPaused', 'true')
  }
}
</script>

<style>
/* Bottom-LEFT so it never overlaps the chat Send button on the right */
#music-toggle-btn {
  position: fixed !important;
  bottom: 24px !important;
  left: 24px !important;
  right: auto !important;
  width: 48px;
  height: 48px;
  border-radius: 50%;
  background: rgba(255, 153, 51, 0.18);
  border: 1px solid rgba(255, 153, 51, 0.5);
  color: white;
  font-size: 20px;
  display: flex;
  justify-content: center;
  align-items: center;
  cursor: pointer;
  z-index: 9998;
  backdrop-filter: blur(8px);
  box-shadow: 0 4px 16px rgba(255, 153, 51, 0.2);
  transition: all 0.3s ease;
}

#music-toggle-btn:hover {
  background: rgba(255, 153, 51, 0.35);
  transform: scale(1.1);
}

#music-toggle-btn.muted {
  background: rgba(200, 30, 30, 0.2);
  border-color: rgba(200, 30, 30, 0.45);
}
</style>
