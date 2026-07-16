<template>
  <div id="root">
    <AppNavbar />
    <AudioPlayer />
    <RouterView />
  </div>
</template>

<script setup lang="ts">
import AppNavbar from './components/AppNavbar.vue'
import AudioPlayer from './components/AudioPlayer.vue'
</script>
