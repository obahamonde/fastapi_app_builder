<script setup lang="ts">
const props = defineProps<{
  size: number;
  color: string;
  speed: number;
}>();
</script>
<template>
<section>
    <Icon
        :style="{ fontSize: `${props.size}px`, color: props.color, animation: `spin ${props.speed}s linear infinite` }"  
    name="mdi-loading"
    />
</section>
</template>