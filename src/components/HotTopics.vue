<template>
  <div class="space-y-6">
    <div class="flex justify-between items-center">
      <h2 class="text-2xl font-bold">当日热榜</h2>
      <button class="px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition-colors">
        刷新热榜
      </button>
    </div>
    <div class="bg-white p-6 rounded-lg border border-gray-200 shadow-sm">
      <iframe 
        src="http://localhost:5173" 
        class="w-full h-[700px] border-0 rounded-lg shadow-sm"
        title="当日热榜"
        loading="lazy"
      ></iframe>
    </div>
  </div>
</template>

<script setup lang="ts">
// 嵌入hot-project项目
</script>

<style scoped>
/* 热榜样式 */
</style>