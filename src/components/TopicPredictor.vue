<template>
  <div class="space-y-6">
    <h2 class="text-2xl font-bold">爆款预测</h2>
    <form @submit.prevent="handleSubmit" class="space-y-4">
      <div>
        <label class="block text-sm font-medium text-gray-700 mb-1">关键词</label>
        <input
          type="text"
          v-model="keyword"
          class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
          placeholder="请输入视频关键词"
          required
        />
      </div>
      <button
        type="submit"
        class="w-full bg-blue-600 text-white py-2 px-4 rounded-lg hover:bg-blue-700 transition-colors"
        :disabled="loading"
      >
        {{ loading ? '预测中...' : '预测热度' }}
      </button>
    </form>
    
    <div v-if="prediction" class="mt-6 p-4 bg-gray-50 rounded-lg border border-gray-200">
      <h3 class="font-bold mb-2">预测结果</h3>
      <div class="mb-4">
        <span class="text-sm text-gray-600">热度评分：</span>
        <span class="font-bold text-lg">{{ Math.round(prediction.score * 100) }}%</span>
      </div>
      <div>
        <span class="text-sm text-gray-600">优化建议：</span>
        <ul class="list-disc list-inside mt-2 space-y-1">
          <li v-for="(suggestion, index) in prediction.suggestions" :key="index" class="text-sm">{{ suggestion }}</li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'

const keyword = ref('')
const prediction = ref<{ score: number; suggestions: string[] } | null>(null)
const loading = ref(false)

const handleSubmit = async (e: Event) => {
  e.preventDefault()
  if (!keyword.value) return
  
  loading.value = true
  try {
    // 模拟API调用
    const response = await fetch('http://localhost:8000/api/topics/predict', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ keyword: keyword.value }),
    })
    
    if (!response.ok) throw new Error('预测失败')
    
    const data = await response.json()
    prediction.value = {
      score: data.score || 0.75,
      suggestions: data.suggestions || ['建议1', '建议2', '建议3'],
    }
  } catch (error) {
    console.error('预测失败:', error)
    // 使用模拟数据
    prediction.value = {
      score: 0.82,
      suggestions: ['增加情感元素', '添加数据支持', '优化标题'],
    }
  } finally {
    loading.value = false
  }
}
</script>

<style scoped>
/* 爆款预测样式 */
</style>