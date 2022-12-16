<template>
    <v-app app>
        <v-app-bar app color="primary" dark row center px-4>
                <Icon icon="simple-icons:fastapi" @click="drawer = !drawer" color="accent" x2 mx-2 cp scale sh rf/>
            <v-toolbar-title>FastAPI GUI </v-toolbar-title> 
            <v-spacer></v-spacer>
           
            <strong text-light text-caption mx-2>
            {{ now.toLocaleTimeString() }}
        </strong>
        
        <v-btn icon
                mx-2
            >     <Icon icon="mdi-magnify" color="accent" x2 mx-2 cp scale sh rf p-1 text-center />
            </v-btn>
            <v-btn icon
                mx-2
                @click="drawerRight = !drawerRight"
            >
                <Icon icon="mdi-apps" color="accent" x2 mx-2 cp scale sh rf p-1 text-center />
                        </v-btn>
        </v-app-bar>
        <v-navigation-drawer
            v-model="drawer"
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
                <Icon :icon="item.icon" color="accent" x2 mx-2 cp scale sh rf p-1 text-center />
                <span text-lg text-center>{{ item.title }}</span>
            </RouterLink>
            </v-list-item>
        </v-list>
        </v-navigation-drawer>
            <v-main pt-16>
                <RouterView />
            </v-main>
            <v-navigation-drawer
            v-model="drawerRight"
            clipped
            color="primary"
            dark
            location="right"
        >
        <v-list
            dense
            nav
        >
            <v-list-item>
                <v-list-item-title text-light text-caption row>Terminal</v-list-item-title>
                <Icon icon="oi:terminal" color="accent" x2 mx-2 cp scale sh rf p-1 text-center
                    @click="footer = !footer"
                />
            </v-list-item>
    </v-list>
        </v-navigation-drawer>
        <v-footer v-if="footer" bg-black app>
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
    ]

const drawer = ref(false)
const drawerRight = ref(false)
const footer = ref(false)
const now = useNow()
</script>