import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    host: '0.0.0.0',  // This will expose the server on all interfaces
    port: 5173,        // Port to listen on (default is 5173)
  },
})
