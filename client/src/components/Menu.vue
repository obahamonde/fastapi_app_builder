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

</template>