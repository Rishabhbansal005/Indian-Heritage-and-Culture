import { createApp } from 'vue'
import { createRouter, createWebHashHistory } from 'vue-router'
import App from './App.vue'
import HomeView from './views/HomeView.vue'
import StatesView from './views/StatesView.vue'
import CategoriesView from './views/CategoriesView.vue'
import StoryView from './views/StoryView.vue'
import BharatAIView from './views/BharatAIView.vue'
import './assets/global.css'

const router = createRouter({
  history: createWebHashHistory(),
  routes: [
    { path: '/', component: HomeView },
    { path: '/states', component: StatesView },
    { path: '/categories', component: CategoriesView },
    { path: '/stories', component: StoryView },
    { path: '/bharat-ai', component: BharatAIView },
  ]
})

createApp(App).use(router).mount('#app')
