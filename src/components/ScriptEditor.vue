<template>
  <div class="space-y-6">
    <h2 class="text-2xl font-bold">脚本编辑</h2>
    <div>
      <label class="block text-sm font-medium text-gray-700 mb-1">选择脚本</label>
      <select
        v-model="selectedScript"
        class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
      >
        <option value="">请选择脚本</option>
        <option v-for="script in scripts" :key="script.id" :value="script.id">
          {{ script.title }}
        </option>
      </select>
    </div>
    
    <div v-if="selectedScript" class="space-y-4">
      <div>
        <label class="block text-sm font-medium text-gray-700 mb-1">脚本内容</label>
        <textarea
          v-model="editedContent"
          class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 min-h-[300px]"
          placeholder="请编辑脚本内容"
        ></textarea>
      </div>
      <button
        @click="handleSave"
        class="w-full bg-blue-600 text-white py-2 px-4 rounded-lg hover:bg-blue-700 transition-colors"
      >
        保存修改
      </button>
    </div>
    
    <div v-if="scripts.length === 0" class="text-center py-8 text-gray-500">
      暂无脚本，请先生成脚本
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, watch } from 'vue'

interface Script {
  id: string
  title: string
  content: string
  createdAt: Date
}

const selectedScript = ref('')
const editedContent = ref('')
const scripts = ref<Script[]>([])

// 模拟脚本数据
scripts.value = [
  {
    id: '1',
    title: '人工智能新突破',
    content: '这是一个关于人工智能新突破的脚本内容...',
    createdAt: new Date(),
  },
  {
    id: '2',
    title: '健康生活方式',
    content: '这是一个关于健康生活方式的脚本内容...',
    createdAt: new Date(),
  },
]

watch(selectedScript, (newValue) => {
  if (newValue) {
    const script = scripts.value.find(s => s.id === newValue)
    if (script) {
      editedContent.value = script.content
    }
  }
})

const handleSave = async () => {
  if (!selectedScript.value) return
  
  try {
    // 模拟API调用
    const response = await fetch(`http://localhost:8000/api/scripts/${selectedScript.value}`, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ content: editedContent.value }),
    })
    
    if (!response.ok) throw new Error('保存失败')
    
    alert('保存成功')
  } catch (error) {
    console.error('保存失败:', error)
    alert('保存失败，请重试')
  }
}
</script>

<style scoped>
/* 脚本编辑样式 */
</style>