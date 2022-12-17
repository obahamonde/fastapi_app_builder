<script setup lang="ts">
const dialog = ref(false);
</script>
<template>
    <v-row row center>
        <v-dialog v-model="dialog" w-96 rounded-lg sh p-4>
            <template v-slot:activator="{ props }">
                <span row center v-bind="props">
                    <Icon icon="mdi-account" x2  cp scale mx-2 />
                    <p>Authentication</p></span>
            </template>
            <v-card>
                <Auth />

                <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn color="blue-darken-1" variant="text" @click="dialog = false">
                        Close
                    </v-btn>
                </v-card-actions>
            </v-card>
        </v-dialog>
    </v-row>
</template>