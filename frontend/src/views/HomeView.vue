<template>
  <div class="home-page">
    <!-- 3D Rotating Banner -->
    <div class="banner">
      <div class="slider" :style="{ '--quantity': cardImages.length }">
        <div
          v-for="(img, i) in cardImages"
          :key="i"
          class="item"
          :style="{ '--position': i + 1 }"
        >
          <img :src="img" :alt="`Culture image ${i + 1}`" loading="lazy" />
        </div>
      </div>
    </div>

    <!-- Welcome Text Ticker -->
    <div class="text-ticker" aria-hidden="true">
      <ul>
        <li v-for="(w, i) in welcomeWords" :key="i" :class="w.color">{{ w.text }}</li>
      </ul>
      <ul aria-hidden="true">
        <li v-for="(w, i) in welcomeWords" :key="'b' + i" :class="w.color">{{ w.text }}</li>
      </ul>
    </div>

    <!-- Heading -->
    <div class="head" ref="headEl">
      <p class="heading-text">Welcome to the rich culture of Bharat</p>
      <p class="para">
        Witness Bharat's vibrant soul, a living tapestry woven with dynamic traditions
        and a kaleidoscope of colorful celebrations. Its rich culture endlessly unfolds.
      </p>
    </div>

    <!-- Bottom Images -->
    <div class="images" ref="imagesEl">
      <div
        v-for="(img, i) in bottomImages"
        :key="i"
        class="img-bottom"
        :style="{ transform: i % 2 === 0 ? 'translateX(-40px)' : 'translateX(40px)' }"
      >
        <img :src="img.src" :alt="img.alt" loading="lazy" />
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'

const headEl = ref<HTMLElement | null>(null)
const imagesEl = ref<HTMLElement | null>(null)

const cardImages: string[] = Array.from({ length: 10 }, (_, i) => `/assets/card images/${i + 1}.webp`)

const welcomeWords = [
  { text: 'स्वागत',     color: 'saffron' },
  { text: 'ਸੁਆਗਤ',     color: 'white'   },
  { text: 'ಸ್ವಾಗತ',     color: 'green'   },
  { text: 'സ്വാഗതം',   color: 'saffron' },
  { text: 'வாங்க',      color: 'white'   },
  { text: 'સ્વાગત છે', color: 'green'   },
  { text: 'స్వాగతం',   color: 'saffron' },
  { text: 'স্বাগত',     color: 'white'   },
  { text: 'Welcome',    color: 'green'   },
]

const bottomImages = [
  { src: '/assets/imges/img-1.jpg',  alt: 'Indian Culture 1' },
  { src: '/assets/imges/img-2.webp', alt: 'Indian Culture 2' },
  { src: '/assets/imges/img-3.jpg',  alt: 'Indian Culture 3' },
  { src: '/assets/imges/img-4.webp', alt: 'Indian Culture 4' },
  { src: '/assets/imges/img-5.webp', alt: 'Indian Culture 5' },
]

onMounted(() => {
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) entry.target.classList.add('is-in-view')
    })
  }, { threshold: 0.15 })

  if (headEl.value)   observer.observe(headEl.value)
  if (imagesEl.value) observer.observe(imagesEl.value)
})
</script>

<style scoped>
@import url('https://fonts.cdnfonts.com/css/poppins');
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&display=swap');

.home-page {
  min-height: 100vh;
  background: #000;
  overflow-x: hidden;
}

/* === Banner === */
.banner {
  width: 100%;
  height: 135vh;
  text-align: center;
  overflow: hidden;
  position: relative;
  padding-top: 100px;
}

.slider {
  position: absolute;
  width: 200px;
  height: 250px;
  top: 80px;
  left: calc(50% - 100px);
  transform-style: preserve-3d;
  animation: autoRun 20s linear infinite;
  z-index: 2;
}

@keyframes autoRun {
  from { transform: perspective(1000px) rotateX(-16deg) rotateY(0deg); }
  to   { transform: perspective(1000px) rotateX(-16deg) rotateY(360deg); }
}

.item {
  position: absolute;
  inset: 0;
  transform: rotateY(calc((var(--position) - 1) * (360 / var(--quantity)) * 1deg)) translateZ(410px);
}

.item img {
  margin-top: 50px;
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
  -webkit-box-reflect: below 10px linear-gradient(transparent, rgba(0,0,0,0.4));
  transition: transform 0.3s ease;
}

.item img:hover { transform: scale(1.15); }

/* === Ticker === */
.text-ticker {
  font-size: clamp(14px, 4vw, 25px);
  padding-block: 10px;
  overflow: hidden;
  user-select: none;
  --gap: clamp(30px, 8vw, 100px);
  display: flex;
  gap: var(--gap);
  white-space: nowrap;
}

.text-ticker ul {
  list-style: none;
  flex-shrink: 0;
  min-width: 100%;
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: var(--gap);
  animation: scrollTicker 15s linear infinite;
}

.text-ticker:hover ul { animation-play-state: paused; }

@keyframes scrollTicker {
  to { transform: translateX(calc(-100% - var(--gap))); }
}

.text-ticker li { font-size: larger; font-weight: bold; font-family: sans-serif; }
.saffron { color: #ff9933; }
.white   { color: #fff; text-shadow: 0 0 5px #000; }
.green   { color: #138808; }

/* === Heading === */
.head {
  text-align: center;
  max-width: 800px;
  margin: 0 auto;
  padding: 20px 16px;
  margin-top: 0;
  opacity: 0;
  transform: translateY(50px);
  transition: opacity 0.8s ease-out, transform 0.8s ease-out;
}

.head.is-in-view {
  opacity: 1;
  transform: translateY(0);
}

.heading-text {
  font-family: 'Playfair Display', serif;
  font-weight: 700;
  color: #fff;
  font-size: clamp(1.4em, 5vw, 3em);
  line-height: 1.2;
  margin-bottom: 10px;
  margin-top: 130px;
}

.para {
  font-family: 'Playfair Display', serif;
  font-weight: 500;
  color: #fff;
  font-size: clamp(0.9em, 2.5vw, 1.2em);
  line-height: 1.6;
  margin-top: 10px;
}

/* === Bottom Images === */
.images {
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 100%;
  max-width: 1200px;
  margin: 32px auto 60px;
  padding: 0 16px;
  opacity: 0;
  transform: translateY(50px);
  transition: opacity 0.8s ease-out 0.2s, transform 0.8s ease-out 0.2s;
}

.images.is-in-view {
  opacity: 1;
  transform: translateY(0);
}

.img-bottom {
  width: 100%;
  max-width: 523px;
  height: 271px;
  border: 3px solid #000;
  background: #111;
  display: flex;
  justify-content: center;
  align-items: center;
  overflow: hidden;
  margin: 0 auto 20px;
  box-shadow: 5px 5px 15px rgba(0,0,0,0.3);
  border-radius: 15px;
  transition: transform 0.35s ease;
}

.img-bottom img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  border-radius: 15px;
}

/* === Responsive === */
@media (max-width: 1024px) {
  .banner { height: 110vh; }
  .item { transform: rotateY(calc((var(--position) - 1) * (360 / var(--quantity)) * 1deg)) translateZ(300px); }
  .slider { width: 160px; height: 200px; left: calc(50% - 80px); }
}

@media (max-width: 768px) {
  .banner { height: 90vh; padding-top: 80px; }
  .slider { width: 80px; height: 120px; left: calc(50% - 40px); }
  .item { transform: rotateY(calc((var(--position) - 1) * (360 / var(--quantity)) * 1deg)) translateZ(150px); }
  .img-bottom { width: 90%; height: auto; aspect-ratio: 523/271; transform: none !important; }
  .heading-text { margin-top: 80px; }
}

@media (max-width: 480px) {
  .banner { height: 80vh; padding-top: 70px; }
  .slider { width: 60px; height: 90px; left: calc(50% - 30px); }
  .item { transform: rotateY(calc((var(--position) - 1) * (360 / var(--quantity)) * 1deg)) translateZ(110px); }
  .img-bottom { width: 95%; }
}
</style>
