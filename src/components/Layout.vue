<template>
  <div class="flex flex-col h-screen bg-gray-50">
    <!-- 顶部标题栏 -->
    <header class="bg-blue-600 text-white py-4 px-8 shadow-md">
      <div class="max-w-7xl mx-auto flex justify-between items-center">
        <h1 class="text-2xl font-bold">🎬 短视频脚本智能生成平台</h1>
        <div class="flex items-center gap-4">
          <button class="text-sm text-white hover:text-blue-100 transition-colors">
            通知
          </button>
          <button class="text-sm text-white hover:text-blue-100 transition-colors">
            设置
          </button>
        </div>
      </div>
    </header>

    <!-- 主内容区 -->
    <div class="flex flex-1 overflow-hidden">
      <!-- 左侧导航栏 -->
      <nav class="w-72 bg-white shadow-md p-4 border-r border-gray-200">
        <ul class="space-y-2">
          <li v-for="item in menuItems" :key="item.id">
            <button
              class="w-full flex items-center gap-3 px-4 py-3 rounded-lg transition-colors"
              :class="activePage === item.id ? 'bg-blue-100 text-blue-600 font-medium' : 'hover:bg-gray-100'"
              @click="activePage = item.id"
            >
              <span class="text-xl">{{ item.icon }}</span>
              <span>{{ item.label }}</span>
            </button>
          </li>
        </ul>
        
        <!-- 导航栏底部信息 -->
        <div class="mt-8 pt-6 border-t border-gray-200">
          <div class="text-xs text-gray-500 px-4">
            <p>版本 1.0.0</p>
            <p class="mt-2">© 2024 短视频脚本智能生成平台</p>
          </div>
        </div>
      </nav>

      <!-- 内容区域 -->
      <main class="flex-1 p-8 overflow-y-auto">
        <div class="max-w-7xl mx-auto">
          <HotTopics v-if="activePage === 'hot'" />
          <ScriptGenerator v-else-if="activePage === 'generate'" />
          <TopicPredictor v-else-if="activePage === 'predict'" />
          <ScriptEditor v-else-if="activePage === 'edit'" />
          <div v-else-if="activePage === 'manage'" class="bg-white rounded-lg shadow-lg p-6">
            <h2 class="text-2xl font-bold mb-6">脚本管理</h2>
            <p class="text-gray-600">脚本管理功能开发中...</p>
          </div>
        </div>
      </main>
    </div>

    <!-- 底部信息栏 -->
    <footer class="bg-white border-t border-gray-200 py-4 px-8">
      <div class="max-w-7xl mx-auto flex justify-between items-center">
        <div class="text-sm text-gray-500">
          © 2024 短视频脚本智能生成平台 | 保留所有权利
        </div>
        <div class="flex items-center gap-6">
          <button class="text-sm text-gray-600 hover:text-blue-600 transition-colors">
            帮助中心
          </button>
          <button class="text-sm text-gray-600 hover:text-blue-600 transition-colors">
            关于我们
          </button>
          <button class="text-sm text-gray-600 hover:text-blue-600 transition-colors">
            隐私政策
          </button>
          <button class="flex items-center gap-2 text-sm text-blue-600 font-medium hover:underline">
            <span class="w-8 h-8 rounded-full bg-gray-200 flex items-center justify-center">
              U
            </span>
            个人中心
          </button>
        </div>
      </div>
    </footer>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import HotTopics from './HotTopics.vue'
import ScriptGenerator from './ScriptGenerator.vue'
import TopicPredictor from './TopicPredictor.vue'
import ScriptEditor from './ScriptEditor.vue'

const activePage = ref('hot') // 默认页面为热榜

const menuItems = [
  { id: 'hot', label: '当日热榜', icon: '🔥' },
  { id: 'generate', label: '脚本生成', icon: '📝' },
  { id: 'predict', label: '爆款预测', icon: '📈' },
  { id: 'edit', label: '脚本编辑', icon: '✏️' },
  { id: 'manage', label: '脚本管理', icon: '📁' },
]
</script>

<style scoped>
/* 布局样式 */
</style>