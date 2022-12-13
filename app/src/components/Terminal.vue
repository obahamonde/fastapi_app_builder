<script setup lang="ts">

const { status, data, send, open, close } = useWebSocket("ws://localhost:8000/ws");


const message = ref("");
const responses = ref<string[]>([]);


onMounted(() => {
  open();
});

onUnmounted(() => {
  close();
});

watchEffect(() => {
  status.value !== "OPEN" ? open() : null;
});

watchEffect(() => {
  data.value ? responses.value.push(data.value) : null;
});

const handle = (msg:string) => {
  if (msg === "clear") {
    responses.value = [];
  } else {
    send(msg);
  }
};


</script>
<template>
  <label text-light font-mono for="term" h-full w-full cursor-text>
    <p v-for="msg in responses" :key="msg" font-mono text-light >{{ msg }}</p>
  <strong text-success>$root: </strong><input type="text" id="term" name="term" no-outline text-secondary  v-model="message"
    @keyup.enter="handle(message)"
  >  
</label>
</template>