import { useState } from 'react';

interface Script {
  id: string;
  title: string;
  content: string;
  createdAt: Date;
}

export const useScriptStore = () => {
  const [scripts, setScripts] = useState<Script[]>([]);
  const [isLoading, setIsLoading] = useState(false);

  const generateScript = async (subject: string, videoLength: number, creativity: number) => {
    setIsLoading(true);
    try {
      // 模拟API调用
      const response = await fetch('http://localhost:8000/api/scripts/generate', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ subject, video_length: videoLength, creativity }),
      });
      
      if (!response.ok) throw new Error('生成脚本失败');
      
      const data = await response.json();
      const newScript: Script = {
        id: Date.now().toString(),
        title: data.title,
        content: data.content,
        createdAt: new Date(),
      };
      
      setScripts(prev => [newScript, ...prev]);
      return newScript;
    } catch (error) {
      console.error('生成脚本失败:', error);
      throw error;
    } finally {
      setIsLoading(false);
    }
  };

  return {
    scripts,
    isLoading,
    generateScript,
  };
};