<template>
  <header>
    <nav class="navbar">
      <!-- Logo -->
      <RouterLink to="/" class="logo">
        <img :src="logoSrc" alt="Essence of Bharat Logo" />
        <p>ESSENCE OF भारत</p>
      </RouterLink>

      <!-- Desktop Links -->
      <ul class="links">
        <li v-for="link in navLinks" :key="link.path">
          <RouterLink :to="link.path" :class="{ active: route.path === link.path }">
            <img :src="link.icon" :alt="link.label" />
            {{ link.label }}
          </RouterLink>
        </li>
      </ul>

      <!-- Mobile Diya Toggle -->
      <div class="toggle" @click="toggleMenu">
        <img class="icon" :src="diyaSrc" alt="Toggle Menu" />
      </div>
    </nav>

    <!-- Mobile Dropdown -->
    <Transition name="dropdown">
      <div v-if="menuOpen" class="dropdownmenu">
        <ul>
          <li v-for="link in navLinks" :key="link.path">
            <RouterLink :to="link.path" @click="menuOpen = false">
              <img :src="link.icon" :alt="link.label" />
              {{ link.label }}
            </RouterLink>
          </li>
        </ul>
        <div class="tricolor-bar"></div>
      </div>
    </Transition>
  </header>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { useRoute } from 'vue-router'

const route = useRoute()
const menuOpen = ref(false)

// Plain strings — not processed by Vite's static import analysis
const logoSrc = '/static/logo/logo 5.webp'
const diyaSrc = '/static/toggle-image/diya.gif'

const navLinks = [
  { path: '/',           label: 'Home',       icon: '/static/icon/home.png'        },
  { path: '/categories', label: 'Categories', icon: '/static/icon/lotus (1).png'   },
  { path: '/states',     label: 'States',     icon: '/static/icon/temple.png'      },
  { path: '/stories',    label: 'Stories',    icon: '/static/icon/book.png'        },
  { path: '/bharat-ai',  label: 'Bharat AI',  icon: '/static/icon/bharat ai.png'   },
]

function toggleMenu() {
  menuOpen.value = !menuOpen.value
}

// Close on outside click
if (typeof window !== 'undefined') {
  document.addEventListener('click', (e: MouseEvent) => {
    const target = e.target as HTMLElement
    if (!target.closest('header')) {
      menuOpen.value = false
    }
  })
}
</script>

<style scoped>
header {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  z-index: 1000;
}

.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 8px 32px;
  background: transparent;
}

/* ---- Logo ---- */
.logo {
  display: flex;
  align-items: center;
  gap: 12px;
  text-decoration: none;
  flex-shrink: 0;
}

.logo img {
  width: clamp(38px, 6vw, 62px);
  height: clamp(38px, 6vw, 62px);
  object-fit: contain;
}

.logo p {
  font-family: 'Kumar One', cursive;
  font-size: clamp(13px, 2.5vw, 24px);
  background: linear-gradient(to right, #FF9933, #ffffff, #138808);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  white-space: nowrap;
}

/* ---- Desktop Links ---- */
.links {
  list-style: none;
  display: flex;
  align-items: center;
  gap: 4px;
  margin: 0;
  padding: 0;
}

.links li a {
  display: flex;
  align-items: center;
  gap: 7px;
  color: #fff;
  text-decoration: none;
  font-family: 'Noto Sans Devanagari', sans-serif;
  font-size: clamp(13px, 1.4vw, 17px);
  font-weight: 600;
  padding: 6px 10px;
  border-radius: 8px;
  white-space: nowrap;
  position: relative;
  transition: background 0.3s;
}

.links li a::after {
  content: '';
  position: absolute;
  bottom: 2px;
  left: 10px;
  right: 10px;
  height: 2px;
  background: linear-gradient(to right, #FF9933, #fff, #138808);
  border-radius: 2px;
  transform: scaleX(0);
  transform-origin: left;
  transition: transform 0.35s ease;
}

.links li a:hover::after,
.links li a.active::after {
  transform: scaleX(1);
}

.links li a:hover {
  background: rgba(255,255,255,0.07);
}

.links li a img {
  width: 20px;
  height: 20px;
  filter: invert(1);
  flex-shrink: 0;
}

.links li a:hover img,
.links li a.active img {
  filter: invert(60%) sepia(90%) saturate(500%) hue-rotate(15deg);
}

/* ---- Diya Toggle ---- */
.toggle {
  display: none;
  cursor: pointer;
  background: transparent;
  border: none;
  padding: 4px;
  flex-shrink: 0;
}

.toggle .icon {
  width: 52px;
  height: 52px;
  object-fit: contain;
  filter: drop-shadow(0 0 8px rgba(255, 153, 51, 0.6));
  transition: filter 0.3s, transform 0.3s;
}

.toggle:hover .icon {
  filter: drop-shadow(0 0 16px rgba(255, 153, 51, 1));
  transform: scale(1.1);
}

/* ---- Dropdown ---- */
.dropdownmenu {
  width: 100%;
  background: rgba(5, 5, 5, 0.94);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  border-top: 1px solid rgba(255, 153, 51, 0.15);
}

.dropdownmenu ul {
  list-style: none;
  padding: 10px 0;
}

.dropdownmenu li a {
  display: flex;
  align-items: center;
  gap: 14px;
  color: #fff;
  font-family: 'Noto Sans Devanagari', sans-serif;
  font-size: 1rem;
  font-weight: 600;
  text-decoration: none;
  padding: 14px 28px;
  border-left: 3px solid transparent;
  transition: background 0.25s, border-color 0.25s, color 0.25s;
}

.dropdownmenu li a:hover {
  background: rgba(255, 153, 51, 0.1);
  border-left-color: #FF9933;
  color: #FF9933;
}

.dropdownmenu li a img {
  width: 22px;
  height: 22px;
  filter: invert(1);
  flex-shrink: 0;
}

.dropdownmenu li a:hover img {
  filter: invert(60%) sepia(90%) saturate(500%) hue-rotate(15deg);
}

.tricolor-bar {
  height: 3px;
  background: linear-gradient(to right, #FF9933 33%, #fff 33% 66%, #138808 66%);
  margin-top: 6px;
}

/* ---- Dropdown Transition ---- */
.dropdown-enter-active, .dropdown-leave-active {
  transition: opacity 0.3s ease, transform 0.3s ease;
}
.dropdown-enter-from, .dropdown-leave-to {
  opacity: 0;
  transform: translateY(-10px);
}

/* ---- Responsive ---- */
@media (max-width: 1024px) {
  .links { display: none; }
  .toggle { display: block; }
  .navbar { padding: 6px 16px; }
}

@media (max-width: 480px) {
  .logo img { width: 36px; height: 36px; }
  .logo p { font-size: 13px; }
  .toggle .icon { width: 44px; height: 44px; }
  .dropdownmenu li a { padding: 12px 20px; font-size: 0.93rem; }
}
</style>
