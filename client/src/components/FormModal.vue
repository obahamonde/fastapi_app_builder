<script setup lang="ts">
const dialog = ref(false);
</script>
<template>
    <v-row row center>
        <v-dialog v-model="dialog" persistent col>
            <template v-slot:activator="{ props }">
                    <Icon icon="logos:python" x2 v-bind="props" translate-y--4 translate-x--36 cp scale />
            </template>
            <v-card>
                <v-card-title>
                    <span class="text-h5">Application Data</span>
                </v-card-title>
                <v-card-text>
                    <v-container>
                        <v-row>
                            <v-col cols="12" sm="6" md="4">
                                <v-text-field label="App Title" required></v-text-field>
                            </v-col>
                            <v-col cols="12">
                                <v-text-field label="App Description" type="text" required></v-text-field>
                            </v-col>
                        </v-row>
                    </v-container>
                </v-card-text>
                <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn color="blue-darken-1" variant="text" @click="dialog = false">
                        Close
                    </v-btn>
                    <v-btn color="blue-darken-1" variant="text" @click="dialog = false">
                        Save
                    </v-btn>
                </v-card-actions>
            </v-card>
        </v-dialog>
    </v-row>
</template>