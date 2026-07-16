<template>
  <div class="states-page">
    <div class="slider" :class="{ next: isNext, prev: isPrev }">
      <!-- Main List -->
      <div class="list">
        <div v-for="(state, i) in states" :key="state.name" class="item">
          <img :src="state.img" :alt="state.name" loading="lazy" />
          <div class="content">
            <div class="title">EXPLORE</div>
            <div class="type">{{ state.name }}</div>
            <div class="description">{{ state.description }}</div>
            <div class="button">
              <button @click="openWiki(state.wiki)">SEE MORE</button>
            </div>
          </div>
        </div>
      </div>

      <!-- Thumbnails -->
      <div class="thumbnail">
        <div v-for="state in states" :key="'t-' + state.name" class="item">
          <img :src="state.img" :alt="state.name" loading="lazy" />
        </div>
      </div>

      <!-- Arrows -->
      <div class="nextPrevArrows">
        <button class="prev" @click="moveSlider('prev')">&lt;</button>
        <button class="next" @click="moveSlider('next')">&gt;</button>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'

interface State {
  name: string
  description: string
  img: string
  wiki: string
}

const states = ref<State[]>([
  { name: 'ANDHRA PRADESH', description: 'Known for its rich heritage, Andhra Pradesh offers a blend of traditional and modern culture.', img: '/states/assets states/andhra pradesh.webp', wiki: 'https://en.wikipedia.org/wiki/Andhra_Pradesh' },
  { name: 'ARUNACHAL PRADESH', description: 'This state is famed for its stunning landscapes and diverse tribal culture.', img: '/states/assets states/arunachal pradesh.webp', wiki: 'https://en.wikipedia.org/wiki/Arunachal_Pradesh' },
  { name: 'ASSAM', description: 'Known for its tea gardens and rich biodiversity, Assam is a cultural hotspot.', img: '/states/assets states/assam.webp', wiki: 'https://en.wikipedia.org/wiki/Assam' },
  { name: 'BIHAR', description: 'Bihar boasts a rich history and is known for its ancient universities and cultural heritage.', img: '/states/assets states/bihar.webp', wiki: 'https://en.wikipedia.org/wiki/Bihar' },
  { name: 'CHHATTISGARH', description: 'This state is renowned for its tribal culture and beautiful landscapes.', img: '/states/assets states/CHHATTISGARH.webp', wiki: 'https://en.wikipedia.org/wiki/Chhattisgarh' },
  { name: 'GOA', description: 'Famous for its beaches and vibrant nightlife, Goa is a major tourist destination.', img: '/states/assets states/goa.webp', wiki: 'https://en.wikipedia.org/wiki/Goa' },
  { name: 'GUJARAT', description: 'Gujarat is known for its diverse culture, vibrant festivals, and delicious cuisine.', img: '/states/assets states/GUJARAT.webp', wiki: 'https://en.wikipedia.org/wiki/Gujarat' },
  { name: 'HARYANA', description: 'This state is recognized for its rich agricultural heritage and folk traditions.', img: '/states/assets states/haryana.webp', wiki: 'https://en.wikipedia.org/wiki/Haryana' },
  { name: 'HIMACHAL PRADESH', description: 'Known for its stunning mountains, Himachal Pradesh is a haven for nature lovers.', img: '/states/assets states/HIMACHAL PRADESH.webp', wiki: 'https://en.wikipedia.org/wiki/Himachal_Pradesh' },
  { name: 'JHARKHAND', description: 'Jharkhand is famous for its forests, wildlife, and rich tribal culture.', img: '/states/assets states/JHARKHAND.webp', wiki: 'https://en.wikipedia.org/wiki/Jharkhand' },
  { name: 'KARNATAKA', description: 'Karnataka boasts a rich cultural heritage and diverse landscapes.', img: '/states/assets states/KARNATAKA.webp', wiki: 'https://en.wikipedia.org/wiki/Karnataka' },
  { name: 'KERALA', description: 'Known for its backwaters and ayurvedic treatments, Kerala is a unique destination.', img: '/states/assets states/KERALA.webp', wiki: 'https://en.wikipedia.org/wiki/Kerala' },
  { name: 'MADHYA PRADESH', description: 'Madhya Pradesh is known for its historical sites and rich wildlife.', img: '/states/assets states/MADHYA PRADESH.webp', wiki: 'https://en.wikipedia.org/wiki/Madhya_Pradesh' },
  { name: 'MAHARASHTRA', description: 'Maharashtra is famous for its Bollywood film industry and diverse landscapes.', img: '/states/assets states/MAHARASHTRA.webp', wiki: 'https://en.wikipedia.org/wiki/Maharashtra' },
  { name: 'MANIPUR', description: 'Manipur is known for its classical dance forms and scenic beauty.', img: '/states/assets states/manipur.webp', wiki: 'https://en.wikipedia.org/wiki/Manipur' },
  { name: 'MEGHALAYA', description: 'Famous for its living root bridges and monsoon rains, Meghalaya is a natural wonder.', img: '/states/assets states/MEGHALAYA.webp', wiki: 'https://en.wikipedia.org/wiki/Meghalaya' },
  { name: 'MIZORAM', description: 'Mizoram is known for its lush greenery and diverse tribal cultures.', img: '/states/assets states/mizoram.webp', wiki: 'https://en.wikipedia.org/wiki/Mizoram' },
  { name: 'NAGALAND', description: 'Nagaland is famous for its vibrant festivals and tribal heritage.', img: '/states/assets states/NAGALAND.webp', wiki: 'https://en.wikipedia.org/wiki/Nagaland' },
  { name: 'ODISHA', description: 'Odisha is known for its classical dance forms, temple architecture, and beautiful beaches.', img: '/states/assets states/ODISHA.webp', wiki: 'https://en.wikipedia.org/wiki/Odisha' },
  { name: 'PUNJAB', description: 'Punjab is famous for its vibrant culture, Bhangra dance, and delicious cuisine.', img: '/states/assets states/PUNJAB.webp', wiki: 'https://en.wikipedia.org/wiki/Punjab,_India' },
  { name: 'RAJASTHAN', description: 'Known for its royal heritage, Rajasthan boasts stunning forts and colorful festivals.', img: '/states/assets states/RAJASTHAN.webp', wiki: 'https://en.wikipedia.org/wiki/Rajasthan' },
  { name: 'SIKKIM', description: 'Sikkim is known for its breathtaking landscapes and vibrant culture.', img: '/states/assets states/SIKKIM.webp', wiki: 'https://en.wikipedia.org/wiki/Sikkim' },
  { name: 'TAMIL NADU', description: 'Famous for its classical music and dance forms, Tamil Nadu has a rich cultural heritage.', img: '/states/assets states/TAMIL NADU.webp', wiki: 'https://en.wikipedia.org/wiki/Tamil_Nadu' },
  { name: 'TELANGANA', description: 'Telangana is known for its unique culture, cuisine, and rich history.', img: '/states/assets states/TELANGANA.webp', wiki: 'https://en.wikipedia.org/wiki/Telangana' },
  { name: 'TRIPURA', description: 'Tripura is known for its tribal heritage, temples, and natural beauty.', img: '/states/assets states/TRIPURA.webp', wiki: 'https://en.wikipedia.org/wiki/Tripura' },
  { name: 'UTTARAKHAND', description: 'Known for its natural beauty and pilgrimage sites, Uttarakhand is a spiritual haven.', img: '/states/assets states/UTTARAKHAND.webp', wiki: 'https://en.wikipedia.org/wiki/Uttarakhand' },
  { name: 'UTTAR PRADESH', description: 'Uttar Pradesh is famous for its historical landmarks, rich culture, and cuisine.', img: '/states/assets states/UTTAR PRADESH.webp', wiki: 'https://en.wikipedia.org/wiki/Uttar_Pradesh' },
  { name: 'WEST BENGAL', description: 'West Bengal is known for its literature, art, and delicious sweets.', img: '/states/assets states/WEST BENGAL.webp', wiki: 'https://en.wikipedia.org/wiki/West_Bengal' },
])

const isNext = ref(false)
const isPrev = ref(false)

function moveSlider(direction: 'next' | 'prev') {
  if (direction === 'next') {
    isNext.value = true
    isPrev.value = false
    const first = states.value.splice(0, 1)[0]
    states.value.push(first)
  } else {
    isPrev.value = true
    isNext.value = false
    const last = states.value.splice(states.value.length - 1, 1)[0]
    states.value.unshift(last)
  }
  setTimeout(() => { isNext.value = false; isPrev.value = false }, 500)
}

function openWiki(url: string) {
  window.open(url, '_blank')
}
</script>

<style scoped>
.states-page {
  background: #000;
  min-height: 100vh;
}

.slider {
  height: 100vh;
  width: 100vw;
  overflow: hidden;
  position: relative;
}

.list .item {
  width: 100%;
  height: 100%;
  position: absolute;
  inset: 0;
}

.list .item img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.list .item .content {
  position: absolute;
  top: 20%;
  width: 1140px;
  max-width: 80%;
  left: 50%;
  transform: translateX(-50%);
  padding-right: 30%;
  box-sizing: border-box;
  color: #fff;
  text-shadow: 0 5px 10px rgba(0,0,0,0.25);
}

.content .title,
.content .type {
  font-size: clamp(2em, 5vw, 4em);
  font-weight: bold;
  line-height: 1.3;
}

.content .type { color: #11e249d6; }

.content .description {
  font-size: clamp(0.85em, 1.5vw, 1.1em);
  margin-top: 10px;
}

.button { margin-top: 20px; }

.button button {
  padding: 10px 28px;
  border: none;
  background: #eee;
  border-radius: 23px;
  font-weight: 500;
  cursor: pointer;
  letter-spacing: 2px;
  transition: all 0.4s ease;
}

.button button:hover {
  letter-spacing: 3px;
  background: linear-gradient(to right, #FF9933, #fff, #138808);
}

/* Thumbnails */
.thumbnail {
  position: absolute;
  bottom: 50px;
  left: 50%;
  width: max-content;
  z-index: 100;
  display: flex;
  gap: 20px;
}

.thumbnail .item {
  width: 150px;
  height: 220px;
  flex-shrink: 0;
}

.thumbnail .item img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  border-radius: 20px;
  box-shadow: 5px 0 15px rgba(0,0,0,0.3);
}

/* Arrows */
.nextPrevArrows {
  position: absolute;
  top: 80%;
  right: 52%;
  z-index: 100;
  display: flex;
  gap: 10px;
}

.nextPrevArrows button {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  background: #14ff72cb;
  border: none;
  color: #fff;
  font-weight: bold;
  cursor: pointer;
  transition: 0.4s;
}

.nextPrevArrows button:hover {
  background: #fff;
  color: #000;
}

/* First item always on top */
.list .item:nth-child(1) { z-index: 1; }

/* Animation entry */
.list .item:nth-child(1) .content .title,
.list .item:nth-child(1) .content .type,
.list .item:nth-child(1) .content .description,
.list .item:nth-child(1) .content .button {
  transform: translateY(50px);
  filter: blur(20px);
  opacity: 0;
  animation: showContent 0.5s 0.5s linear forwards;
}

@keyframes showContent {
  to { transform: translateY(0); filter: blur(0); opacity: 1; }
}

/* Next animation */
.slider.next .list .item:nth-child(1) img {
  width: 150px;
  height: 220px;
  position: absolute;
  bottom: 50px;
  left: 50%;
  border-radius: 30px;
  animation: showImage 0.5s linear forwards;
}

@keyframes showImage {
  to { bottom: 0; left: 0; width: 100%; height: 100%; border-radius: 0; }
}

.slider.next .thumbnail .item:nth-last-child(1) {
  overflow: hidden;
  animation: showThumbnail 0.5s linear forwards;
}

@keyframes showThumbnail {
  from { width: 0; opacity: 0; }
}

.slider.next .thumbnail { animation: effectNext 0.5s linear forwards; }

@keyframes effectNext {
  from { transform: translateX(150px); }
}

/* Prev animation */
.slider.prev .list .item:nth-child(2) { z-index: 2; }

.slider.prev .list .item:nth-child(2) img {
  animation: outFrame 0.5s linear forwards;
  position: absolute;
  bottom: 0;
  left: 0;
}

@keyframes outFrame {
  to { width: 150px; height: 220px; bottom: 50px; left: 50%; border-radius: 20px; }
}

.slider.prev .thumbnail .item:nth-child(1) {
  overflow: hidden;
  opacity: 0;
  animation: showThumbnail 0.5s linear forwards;
}

.slider.next .nextPrevArrows button,
.slider.prev .nextPrevArrows button { pointer-events: none; }

/* === Responsive === */
@media (max-width: 678px) {
  .list .item .content {
    padding-right: 0;
    top: 12%;
  }
  .content .title, .content .type { font-size: 2em; }
  .content .description { font-size: 0.85em; }
  .thumbnail { bottom: 16px; gap: 8px; }
  .thumbnail .item { width: 90px; height: 130px; }
  .nextPrevArrows { top: 68%; right: 50%; transform: translateX(50%); }
}

@media (max-width: 400px) {
  .content .title, .content .type { font-size: 1.6em; }
  .thumbnail .item { width: 70px; height: 100px; }
}
</style>
