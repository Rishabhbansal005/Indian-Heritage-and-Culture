import { fileURLToPath, URL } from 'node:url'
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

export default defineConfig({
  plugins: [vue()],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  },
  server: {
    port: 5173,
    proxy: {
      '/chat':    'http://localhost:8000',
      '/assets':  'http://localhost:8000',
      '/static':  'http://localhost:8000',
      '/states':  'http://localhost:8000',
      '/story':   'http://localhost:8000',
      '/categories': 'http://localhost:8000',
      '/home':    'http://localhost:8000',
    }
  },
  build: {
    outDir: '../dist',
    emptyOutDir: true,
  }
})
