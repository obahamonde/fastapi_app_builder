<script setup lang="ts">
const schema = ref("");
onMounted(async() => {
  const { data } = await useFetch("/api/prisma").text();
  schema.value = unref(data) as string;
});
</script>
<template>
<section overflow-hidden>
  <pre
  pl-16
  pt-16
  pb-16
  bg-gray-700
  text-secondary
  overflow-hidden
  ><textarea h-screen w-full bg-transparent text-secondary no-outline font-mono type="text" v-model="schema"  /> </pre>
 
</section>
<v-btn
    icon
    tr
    mt-20
    m-2
    fixed
    color="primary"
    @click="() => useFetch('/api/prisma', { method: 'POST', body: schema })"
  >
<Icon icon="mdi-floppy" x2 />
  </v-btn>
</template>
