import { useState, useEffect } from 'react';

interface Topic {
  id: string;
  title: string;
  description: string;
  source: string;
  heat: number;
  createdAt: Date;
}

export const useTopicStore = () => {
  const [hotTopics, setHotTopics] = useState<Topic[]>([]);
  const [isLoading, setIsLoading] = useState(false);

  const fetchHotTopics = async () => {
    setIsLoading(true);
    try {
      // 模拟API调用
      const response = await fetch('http://localhost:8000/api/topics/hot');
      
      if (!response.ok) throw new Error('获取热点失败');
      
      const data = await response.json();
      const topics: Topic[] = data.map((topic: any, index: number) => ({
        id: index.toString(),
        title: topic.title,
        description: topic.summary || '暂无描述',
        source: topic.source,
        heat: topic.heat || 0,
        createdAt: new Date(),
      }));
      
      setHotTopics(topics);
      return topics;
    } catch (error) {
      console.error('获取热点失败:', error);
      // 使用模拟数据作为后备
      const mockTopics: Topic[] = [
        {
          id: '1',
          title: '人工智能新突破',
          description: '最新AI技术在各个领域的应用',
          source: '科技日报',
          heat: 95,
          createdAt: new Date(),
        },
        {
          id: '2',
          title: '健康生活方式',
          description: '如何保持身心健康的方法',
          source: '健康杂志',
          heat: 88,
          createdAt: new Date(),
        },
        {
          id: '3',
          title: '旅行攻略分享',
          description: '热门旅游目的地推荐',
          source: '旅游网站',
          heat: 76,
          createdAt: new Date(),
        },
      ];
      setHotTopics(mockTopics);
      return mockTopics;
    } finally {
      setIsLoading(false);
    }
  };

  // 初始化时获取热点
  useEffect(() => {
    fetchHotTopics();
  }, []);

  return {
    hotTopics,
    isLoading,
    fetchHotTopics,
  };
};