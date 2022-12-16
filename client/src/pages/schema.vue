<script setup lang="ts">
const schema = ref("")
const fetchSchema = async () => {
  const { data } = await useFetch("/api/schema").text();
    schema.value = unref(data) as string;
}
onMounted(async () => {
    await fetchSchema();
})
</script>
<template>
<label for="schema" h-full w-full p-16 font-mono text-succes bg-black>
<input id="schema" v-model="schema" type="text" h-full w-full p-16 font-mono text-succes bg-black />
</label>
</template>