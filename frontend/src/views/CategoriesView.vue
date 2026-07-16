<template>
  <div class="categories-page">
    <div class="slider" :class="{ next: isNext, prev: isPrev }">
      <div class="list">
        <div v-for="cat in categories" :key="cat.name" class="item">
          <img :src="cat.img" :alt="cat.name" loading="lazy" />
          <div class="content">
            <div class="title">EXPLORE</div>
            <div class="type">{{ cat.name }}</div>
            <div class="description">{{ cat.description }}</div>
            <div class="button">
              <button @click="openWiki(cat.wiki)">SEE MORE</button>
            </div>
          </div>
        </div>
      </div>

      <div class="thumbnail">
        <div v-for="cat in categories" :key="'t-' + cat.name" class="item">
          <img :src="cat.img" :alt="cat.name" loading="lazy" />
        </div>
      </div>

      <div class="nextPrevArrows">
        <button class="prev" @click="moveSlider('prev')">&lt;</button>
        <button class="next" @click="moveSlider('next')">&gt;</button>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'

interface Category {
  name: string
  description: string
  img: string
  wiki: string
}

const categories = ref<Category[]>([
  { name: 'INDIAN MUSIC',     description: 'Indian music: a dynamic blend of classical, folk, and contemporary genres, reflecting rich cultural heritage through intricate melodies and rhythms.', img: '/categories/assets2/music.webp',     wiki: 'https://en.wikipedia.org/wiki/Music_of_India' },
  { name: 'INDIAN FOLK DANCE',description: 'Indian folk dance vibrantly reflects cultural diversity, from energetic Garba and Bhangra to graceful Kathak and Bharatanatyam, preserving unique traditions.', img: '/categories/assets2/dance3.webp',    wiki: 'https://en.wikipedia.org/wiki/List_of_Indian_folk_dances' },
  { name: 'INDIAN CRAFT',     description: 'Indian craft: diverse regional artistry, from pottery to textiles, preserving heritage.', img: '/categories/assets2/craft.webp',     wiki: 'https://en.wikipedia.org/wiki/Crafts_of_India' },
  { name: 'INDIAN CUISINE',   description: 'Indian cuisine: a rich tapestry of flavors, from spicy curries to delicate sweets, reflecting diverse regional traditions.', img: '/categories/assets2/cuisine.webp',   wiki: 'https://en.wikipedia.org/wiki/Indian_cuisine' },
  { name: 'INDIAN FESTIVALS', description: 'Indian festivals: vibrant celebrations of culture, religion, and community, from Diwali\'s lights to Holi\'s colors.', img: '/categories/assets2/festivals.webp', wiki: 'https://en.wikipedia.org/wiki/List_of_festivals_in_India' },
])

const isNext = ref(false)
const isPrev = ref(false)

function moveSlider(direction: 'next' | 'prev') {
  if (direction === 'next') {
    isNext.value = true
    isPrev.value = false
    const first = categories.value.splice(0, 1)[0]
    categories.value.push(first)
  } else {
    isPrev.value = true
    isNext.value = false
    const last = categories.value.splice(categories.value.length - 1, 1)[0]
    categories.value.unshift(last)
  }
  setTimeout(() => { isNext.value = false; isPrev.value = false }, 500)
}

function openWiki(url: string) { window.open(url, '_blank') }
</script>

<style scoped>
.categories-page { background: #000; min-height: 100vh; }
.slider { height: 100vh; width: 100vw; overflow: hidden; position: relative; }
.list .item { width: 100%; height: 100%; position: absolute; inset: 0; }
.list .item img { width: 100%; height: 100%; object-fit: cover; }
.list .item .content {
  position: absolute; top: 20%;
  width: 1140px; max-width: 80%;
  left: 50%; transform: translateX(-50%);
  padding-right: 30%; box-sizing: border-box;
  color: #fff; text-shadow: 0 5px 10px rgba(0,0,0,0.25);
}
.content .title, .content .type { font-size: clamp(2em, 5vw, 4em); font-weight: bold; line-height: 1.3; }
.content .type { color: #11e249d6; }
.content .description { font-size: clamp(0.85em, 1.5vw, 1.1em); margin-top: 10px; }
.button { margin-top: 20px; }
.button button {
  padding: 10px 28px; border: none; background: #eee;
  border-radius: 23px; font-weight: 500; cursor: pointer;
  letter-spacing: 2px; transition: all 0.4s;
}
.button button:hover { letter-spacing: 3px; background: linear-gradient(to right, #FF9933, #fff, #138808); }
.thumbnail { position: absolute; bottom: 50px; left: 50%; width: max-content; z-index: 100; display: flex; gap: 20px; }
.thumbnail .item { width: 150px; height: 220px; flex-shrink: 0; }
.thumbnail .item img { width: 100%; height: 100%; object-fit: cover; border-radius: 20px; box-shadow: 5px 0 15px rgba(0,0,0,0.3); }
.nextPrevArrows { position: absolute; top: 80%; right: 52%; z-index: 100; display: flex; gap: 10px; }
.nextPrevArrows button { width: 40px; height: 40px; border-radius: 50%; background: #14ff72cb; border: none; color: #fff; font-weight: bold; cursor: pointer; transition: 0.4s; }
.nextPrevArrows button:hover { background: #fff; color: #000; }
.list .item:nth-child(1) { z-index: 1; }
.list .item:nth-child(1) .content .title,
.list .item:nth-child(1) .content .type,
.list .item:nth-child(1) .content .description,
.list .item:nth-child(1) .content .button {
  transform: translateY(50px); filter: blur(20px); opacity: 0;
  animation: showContent 0.5s 0.5s linear forwards;
}
@keyframes showContent { to { transform: translateY(0); filter: blur(0); opacity: 1; } }
.slider.next .list .item:nth-child(1) img { width: 150px; height: 220px; position: absolute; bottom: 50px; left: 50%; border-radius: 30px; animation: showImage 0.5s linear forwards; }
@keyframes showImage { to { bottom: 0; left: 0; width: 100%; height: 100%; border-radius: 0; } }
.slider.next .thumbnail .item:nth-last-child(1) { overflow: hidden; animation: showThumbnail 0.5s linear forwards; }
@keyframes showThumbnail { from { width: 0; opacity: 0; } }
.slider.next .thumbnail { animation: effectNext 0.5s linear forwards; }
@keyframes effectNext { from { transform: translateX(150px); } }
.slider.prev .list .item:nth-child(2) { z-index: 2; }
.slider.prev .list .item:nth-child(2) img { animation: outFrame 0.5s linear forwards; position: absolute; bottom: 0; left: 0; }
@keyframes outFrame { to { width: 150px; height: 220px; bottom: 50px; left: 50%; border-radius: 20px; } }
.slider.prev .thumbnail .item:nth-child(1) { overflow: hidden; opacity: 0; animation: showThumbnail 0.5s linear forwards; }
.slider.next .nextPrevArrows button, .slider.prev .nextPrevArrows button { pointer-events: none; }
@media (max-width: 678px) {
  .list .item .content { padding-right: 0; top: 12%; }
  .content .title, .content .type { font-size: 2em; }
  .thumbnail { bottom: 16px; gap: 8px; }
  .thumbnail .item { width: 90px; height: 130px; }
  .nextPrevArrows { top: 68%; right: 50%; transform: translateX(50%); }
}
</style>
