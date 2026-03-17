// vite.config.js (プロジェクトルート)
import { defineConfig } from 'vite'
import tailwindcss from '@tailwindcss/vite'

export default defineConfig({
  plugins: [tailwindcss()],
  build: {
    outDir: 'config/static/dist',
    emptyOutDir: true,
    manifest: true,
    rollupOptions: {
      input: 'config/static/css/input.css',
      output: {
        entryFileNames: 'assets/[name].js',
        assetFileNames: 'assets/[name].[ext]',
      },
    },
  },
  server: {
    host: true, // 0.0.0.0 で待ち受け（Docker からホストでアクセス可能にする）
    port: 5173,
    origin: 'http://127.0.0.1:5174',
    cors: true,
  },
})