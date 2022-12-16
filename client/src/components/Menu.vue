<script setup lang="ts">
import { Ref } from 'vue';
const items = [
    { title: 'Payloads', icon: 'logos:json' },
    { title: 'Scanner', icon: 'mdi-barcode-scan' },
    { title: 'Network', icon: 'mdi-wifi' },
    { title: 'Geo', icon: 'mdi-map-marker' },
    { title: 'Terminal', icon: 'oi-terminal' },
];

const emits = defineEmits(['switchApp']);
const currentApp = ref(null) as Ref<string | null>;
const drawer = ref(false);

const handleSwitchApp = (app: string) => {
    emits('switchApp', app);
    drawer.value = false;
    currentApp.value = app;
};

</script>

<template>
    <v-btn icon mx-2 @click="drawer = !drawer" v-if="!drawer">
        <v-icon>mdi-apps</v-icon>
    </v-btn>
    <v-btn icon mx-2 @click="drawer = !drawer" v-else>
        <v-icon>mdi-close</v-icon>
    </v-btn>


    <v-navigation-drawer v-model="drawer" app clipped color="primary" dark location="right">

        <v-list>
            <v-list-item v-for="item in items">
                <Icon :icon="item.icon" size="2x" text-primary @click="handleSwitchApp(item.title)" />
            </v-list-item>
        </v-list>
    </v-navigation-drawer>
</template>
<style global>
.router-link-active {
    background-color: rgba(0, 0, 0, 0.1);
    color: white;
}
</style>