<template>
    <v-app app>
        <v-app-bar app color="primary" dark row center px-4>
                <Icon icon="simple-icons:fastapi" @click="drawer = !drawer" color="accent" x3 hover:animate-spin mx-2 cp scale sh rf/>
            <v-toolbar-title text-3xl class="merienda" text-amber>FastAPI App Builder </v-toolbar-title> 
            <v-spacer></v-spacer>
           
            <strong text-light text-caption mx-2>
            {{ now.toLocaleTimeString() }}
        </strong>
        
        <v-btn icon
                mx-2
            >     <FormModal />
            </v-btn>
            <v-btn icon
                mx-2
                @click="drawerRight = !drawerRight"
            >
                <Icon icon="mdi-apps" color="accent" x2 mx-2 cp scale  rf p-1 text-center />
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
            col
            start
        >
            <p my-4 row center  @click="footer = !footer"  cp scale  >
                <Icon icon="oi:terminal" color="accent" x2 mx-2 ml-5 p-1 cp scale text-center
                   
                /><span text-lg text-center>Terminal</span>
            </p>
            <p my-4 row center>
            <AuthModal mx-2 p-1 cp scale text-center  />
        </p>
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
    { title: 'Swagger' , icon: 'logos:swagger'},
    { title: 'Dashboard', icon: 'mdi-view-dashboard' },
    { title: 'Schema', icon: 'mdi-database' },
    ]

const drawer = ref(false)
const drawerRight = ref(false)
const footer = ref(false)
const now = useNow()
</script>