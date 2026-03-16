<template>
  <div class="space-y-6">
    <h2 class="text-2xl font-bold">脚本生成</h2>
    <form @submit.prevent="handleSubmit" class="space-y-4">
      <div>
        <label class="block text-sm font-medium text-gray-700 mb-1">视频主题</label>
        <input
          type="text"
          v-model="subject"
          class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
          placeholder="请输入视频的主题"
          required
        />
      </div>
      <div>
        <label class="block text-sm font-medium text-gray-700 mb-1">视频时长（分钟）</label>
        <input
          type="number"
          v-model.number="videoLength"
          min="0.1"
          step="0.1"
          class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
          required
        />
      </div>
      <div>
        <label class="block text-sm font-medium text-gray-700 mb-1">创造力（{{ creativity }}）</label>
        <input
          type="range"
          v-model.number="creativity"
          min="0"
          max="1.5"
          step="0.1"
          class="w-full"
        />
        <div class="flex justify-between text-xs text-gray-500">
          <span>严谨</span>
          <span>多样</span>
        </div>
      </div>
      <button
        type="submit"
        class="w-full bg-blue-600 text-white py-2 px-4 rounded-lg hover:bg-blue-700 transition-colors"
        :disabled="loading"
      >
        {{ loading ? '生成中...' : '生成脚本' }}
      </button>
    </form>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'

const subject = ref('')
const videoLength = ref(1.0)
const creativity = ref(0.7)
const loading = ref(false)
const scripts = ref<any[]>([])

const handleSubmit = async (e: Event) => {
  e.preventDefault()
  if (!subject.value) return
  
  loading.value = true
  try {
    // 模拟API调用
    const response = await fetch('http://localhost:8000/api/scripts/generate', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ subject: subject.value, video_length: videoLength.value, creativity: creativity.value }),
    })
    
    if (!response.ok) throw new Error('生成脚本失败')
    
    const data = await response.json()
    const newScript = {
      id: Date.now().toString(),
      title: data.title,
      content: data.content,
      createdAt: new Date(),
    }
    
    scripts.value = [newScript, ...scripts.value]
  } catch (error) {
    console.error('生成脚本失败:', error)
  } finally {
    loading.value = false
  }
}
</script>

<style scoped>
/* 脚本生成样式 */
</style>