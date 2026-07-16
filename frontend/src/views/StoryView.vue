<template>
  <div class="story-page">
    <div class="title-section">
      <h1>UNTOLD STORIES</h1>
    </div>
    <div class="story-grid">
      <div
        v-for="story in stories"
        :key="story.title"
        class="story-card"
        @click="openLink(story.link)"
      >
        <img :src="story.img" :alt="story.title" loading="lazy" />
        <p>{{ story.title }}</p>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
interface Story {
  title: string
  img: string
  link: string
}

const stories: Story[] = [
  { title: 'Konark Sun Temple: Kalinga\'s Engineering Marvel',   img: '/story/assets/1.webp', link: 'https://en.wikipedia.org/wiki/Konark_Sun_Temple' },
  { title: 'Adi Shankara: Unifying India with Advaita Vedanta', img: '/story/assets/2.webp', link: 'https://en.wikipedia.org/wiki/Adi_Shankara' },
  { title: 'Vijayanagara Empire: Patrons of Hindu Arts',         img: '/story/assets/3.webp', link: 'https://en.wikipedia.org/wiki/Vijayanagara_Empire' },
  { title: 'Bhakti Movement: Devotion\'s Social Impact',         img: '/story/assets/4.webp', link: 'https://en.wikipedia.org/wiki/Bhakti_movement' },
  { title: 'Panini\'s Ashtadhyayi: Foundation of Sanskrit',      img: '/story/assets/5.webp', link: 'https://en.wikipedia.org/wiki/Ashtadhyayi' },
  { title: 'Aryabhata & Varahamihira: India\'s Ancient Astronomy',img: '/story/assets/6.webp', link: 'https://en.wikipedia.org/wiki/Aryabhata' },
  { title: 'Kautilya\'s Arthashastra: Ancient Indian Statecraft', img: '/story/assets/7.webp', link: 'https://en.wikipedia.org/wiki/Arthashastra' },
  { title: 'Ellora & Elephanta: Devotion Carved in Stone',        img: '/story/assets/8.webp', link: 'https://en.wikipedia.org/wiki/Ellora_Caves' },
  { title: 'The Rock-Cut Wonders of Ellora and Elephanta',        img: '/story/assets/9.webp', link: 'https://en.wikipedia.org/wiki/Elephanta_Caves' },
]

function openLink(url: string) { window.open(url, '_blank') }
</script>

<style scoped>
.story-page {
  background: #000;
  min-height: 100vh;
  padding-top: 100px;
}

.title-section {
  text-align: center;
  padding: 40px 20px 20px;
  color: #fff;
}

.title-section h1 {
  font-size: clamp(1.5rem, 5vw, 2.5rem);
  font-weight: 700;
  letter-spacing: 4px;
  background: linear-gradient(to right, #FF9933, #fff, #138808);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.story-grid {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 28px;
  padding: 40px 20px 80px;
  max-width: 1200px;
  margin: 0 auto;
}

.story-card {
  flex: 0 0 calc(33.333% - 20px);
  max-width: 350px;
  background: #1a1a1a;
  border: 1px solid rgba(255, 153, 51, 0.2);
  border-radius: 12px;
  padding: 20px;
  text-align: center;
  display: flex;
  flex-direction: column;
  cursor: pointer;
  transition: transform 0.3s ease, box-shadow 0.3s ease, border-color 0.3s;
}

.story-card:hover {
  transform: translateY(-10px);
  box-shadow: 0 16px 40px rgba(255, 153, 51, 0.2);
  border-color: rgba(255, 153, 51, 0.6);
}

.story-card img {
  width: 100%;
  height: 200px;
  object-fit: cover;
  border-radius: 8px;
  margin-bottom: 14px;
}

.story-card p {
  font-size: 1rem;
  color: #ddd;
  line-height: 1.5;
  flex-grow: 1;
}

@media (max-width: 992px) {
  .story-card { flex: 0 0 calc(50% - 20px); }
}

@media (max-width: 640px) {
  .story-card { flex: 0 0 90%; max-width: 400px; }
  .story-card img { height: 180px; }
}
</style>
