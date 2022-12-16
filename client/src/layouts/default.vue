<template>
    <v-app app>
        <v-app-bar app color="primary" dark row center px-4>
            <Icon icon="simple-icons:fastapi" @click="drawer = !drawer" color="accent" x2 mx-2 cp scale sh rf/>
            <v-toolbar-title>FastAPI GUI <FormModal/></v-toolbar-title>
            <v-spacer></v-spacer>
            <v-btn icon
                mx-2
            >
                <v-icon>mdi-magnify</v-icon>
            </v-btn>
            <v-btn icon
                mx-2
            >
                <v-icon>mdi-apps</v-icon>
            </v-btn>
        </v-app-bar>
        <v-navigation-drawer
            v-model="drawer"
            app
            clipped
            color="primary"
            dark
        >
        <v-list
            dense
            nav
        >
            <v-list-item
                v-for="item in items"
                :key="item.title"
                link
            >
            <RouterLink :to="item.title.toLowerCase()" row start align-middle gap-2 text-caption text-light >
                <v-icon text-center >{{ item.icon }}</v-icon>
  
                <span text-lg text-center>{{ item.title }}</span>
            </RouterLink>
            </v-list-item>
        </v-list>
        </v-navigation-drawer>
            <v-main pt-16>
                <RouterView />
            </v-main>
            <v-footer
                app
                bg-accent
                no-outline
                >
            <Terminal />
        </v-footer>
    </v-app>
</template>
<style global>
.router-link-active {
    background-color: rgba(0, 0, 0, 0.1);
}

</style>

<script setup lang="ts">
const items = [
    { title: 'Home', icon: 'mdi-home'},
    { title: 'Dashboard', icon: 'mdi-view-dashboard' },
    { title: 'Schema', icon: 'mdi-database' },
    { title: 'Messages', icon: 'mdi-message' },
    { title: 'Settings', icon: 'mdi-cog' },
]
const drawer = ref(false)
</script>