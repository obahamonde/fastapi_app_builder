//main.ts
import { createApp } from "vue";
import { createRouter, createWebHistory } from "vue-router";
import { createPinia } from "pinia"
import App from "./App.vue";
import "vuetify/styles";
import { createVuetify } from "vuetify";
import * as components from "vuetify/components";
import * as directives from "vuetify/directives";
import "uno.css";
import { Icon } from "@iconify/vue";
import generatedRoutes from "virtual:generated-pages"
import { setupLayouts } from "virtual:generated-layouts";
import "@mdi/font/css/materialdesignicons.css";

const routes = setupLayouts(generatedRoutes);

createApp(App)
.use(
    createRouter({
      history: createWebHistory(import.meta.env.BASE_URL),
      routes,
    })
  )
  .use(createPinia())
  .use(
    createVuetify({
      components,
      directives,
    })
  )
  .component("Icon", Icon)
  .mount("#app")