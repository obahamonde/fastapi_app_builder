<script setup lang="ts">
import { Ref } from 'vue';
const dialog = ref(false);
const searchTerms = ref("");
const results = ref([]) as Ref<object[]>;
const search = async () => {
  const { data } = await useFetch(`/api/ApiReq/headers/${searchTerms.value}/contains`).json();
    results.value = unref(data) as object[];
};
</script>
<template>
    <v-row row center>
        <v-dialog v-model="dialog" persistent col>
            <template v-slot:activator="{ props }">
                    <Icon icon="mdi-magnify" x2 v-bind="props" cp scale />
            </template>
            <v-card>
                <v-card-text>
                    <v-container>
                        <v-row>
                            <v-col cols="12">
                                <v-text-field label="Browse within your requests" type="text" required
                                    v-model="searchTerms"
                                    @keyup.enter="search"
                                ></v-text-field>
                            </v-col>
                        </v-row>
                    </v-container>
                </v-card-text>
                <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn btn-del color="blue-darken-1" variant="text" @click="dialog = false">
                        Close
                    </v-btn>
                    <v-btn btn-get variant="text" @click="search">
                        Search
                    </v-btn>
                </v-card-actions>
                <p v-for="result in results" text-xs px-12 py-6 col center>
                {{ JSON.stringify(result) }}
            </p>
            </v-card>
           </v-dialog>
    </v-row>
</template>