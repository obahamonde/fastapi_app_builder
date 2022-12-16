<script setup lang="ts">
const router = useRouter();
onMounted(() => {
  router.push("/");
});
</script>
<template>
<section>
<Spinner :size="100" color="#000000" :speed="1" />
</section>
</template>