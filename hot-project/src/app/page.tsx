/*
 * @Author: 白雾茫茫丶<baiwumm.com>
 * @Date: 2025-11-19 15:55:09
 * @LastEditors: 白雾茫茫丶<baiwumm.com>
 * @LastEditTime: 2025-11-20 15:42:05
 * @Description: 首页
 */
'use client';

import { useLocalStorageState } from 'ahooks';
import { AnimatePresence, motion } from 'framer-motion';
import { useMemo } from 'react';

import HotCard from '@/components/HotCard';
import { hotCardConfig, LOCAL_KEY } from '@/lib/constant';
import type { HotTypes } from '@/lib/type';

export default function Home() {
  const [hiddenHotList] = useLocalStorageState<HotTypes[]>(
    LOCAL_KEY.HOTHIDDEN,
    {
      defaultValue: [],
      listenStorageChange: true,
    }
  );

  const visibleConfigs = useMemo(() => {
    const hiddenSet = new Set(hiddenHotList || []);
    return hotCardConfig.filter((config) => !hiddenSet.has(config.value));
  }, [hiddenHotList]);

  return (
    // 👇 父容器必须是 motion.div 并开启 layout
    <motion.div
      className="grid gap-4"
      style={{ gridTemplateColumns: 'repeat(auto-fill, minmax(20rem, 1fr))' }}
      layout // ✅ 启用布局动画
    >
      <AnimatePresence>
        {visibleConfigs.map((config) => (
          // 👇 每个子项也必须是 motion.div + layout
          <motion.div
            key={config.value}
            layout // ✅ 关键：让位置变化可动画
            initial={{ opacity: 0, scale: 0.9 }}
            animate={{ opacity: 1, scale: 1 }}
            exit={{ opacity: 0, scale: 0.8, transition: { duration: 0.25 } }}
            transition={{ type: 'spring', stiffness: 300, damping: 24 }}
          >
            <HotCard {...config} />
          </motion.div>
        ))}
      </AnimatePresence>
    </motion.div>
  );
}
