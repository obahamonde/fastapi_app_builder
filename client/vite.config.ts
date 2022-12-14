//vite.config.ts
import { defineConfig } from "vite";
import Vue from "@vitejs/plugin-vue";
import Pages from "vite-plugin-pages";
import Layouts from "vite-plugin-vue-layouts";
import Components from "unplugin-vue-components/vite";
import AutoImport from "unplugin-auto-import/vite";
import Unocss from "unocss/vite";
import path from "path";

export default defineConfig({
  resolve: {
    alias: {
      "~/": path.resolve(__dirname, "src") + "/",
    },
  },
  server:{
    proxy:{
      "/api": {
        target: "http://localhost:3000/api",
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/api/, ""),
      }
    }
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