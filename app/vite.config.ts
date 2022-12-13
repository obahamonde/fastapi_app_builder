//vite.config.ts
import { defineConfig } from "vite";
import Vue from "@vitejs/plugin-vue";
import Pages from "vite-plugin-pages";
import Layouts from "vite-plugin-vue-layouts";
import Components from "unplugin-vue-components/vite";
import AutoImport from "unplugin-auto-import/vite";
import Unocss from "unocss/vite";

export default defineConfig({
  resolve: {
    alias: {
      "~/": "./src",
    },
  },
  server:{
  proxy: {
    "/api": {
      target: "http://localhost:8000",
      changeOrigin: true,
      rewrite: (path) => path.replace(/^\/api/, ""),
    },
  "/ws": {
      target: "http://localhost:8000/ws",
      changeOrigin: true,
      rewrite: (path) => path.replace(/^\/ws/, ""),
      ws: true,
    },
    "/docs": {
      target: "http://localhost:8000/docs",
      changeOrigin: true,
      rewrite: (path) => path.replace(/^\/docs/, ""),
    },
    "/openapi.json": {
      target: "http://localhost:8000/openapi.json",
      changeOrigin: true,
      rewrite: (path) => path.replace(/^\/openapi.json/, ""),
    },
  },
},

  plugins: [
    Vue({
      include: [/\.vue$/],
      reactivityTransform: true,
    }),
    Pages({
      extensions: ["vue"],
    }),
    Layouts(),
    AutoImport({
      imports: [
        "vue",
        "vue-router",
        "vue/macros",
        "@vueuse/head",
        "@vueuse/core",
      ],
      dts: "src/auto-imports.d.ts",
      dirs: ["src/hooks", "src/store"],
      vueTemplate: true,
    }),
    Unocss(),
    Components({
      extensions: ["vue"],
      include: [/\.vue$/, /\.vue\?vue/],
      dts: "src/components.d.ts",
    }),
  ],
  ssr: {
    noExternal: ["workbox-window"],
  },
  build: {
    outDir: "../www",
    emptyOutDir: true
  },
  assetsInclude: ["**/*.svg", "**/*.png", "**/*.jpg", "**/*.jpeg", "**/*.gif"],
});