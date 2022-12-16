<script setup lang="ts">
const dialog = ref(false);
</script>
<template>
    <v-row row center>
        <v-dialog v-model="dialog" persistent col>
            <template v-slot:activator="{ props }">
                    <Icon icon="mdi-account" x2 v-bind="props" cp scale />
                    <p>Authentication</p>
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