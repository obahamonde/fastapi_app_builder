<template>
  <RouterView />
</template>
<style global>
@import url('https://fonts.googleapis.com/css2?family=Merienda:wght@500&display=swap');

.merienda {
  font-family: 'Merienda', cursive;
}
/* custom scrollbar */
*::-webkit-scrollbar {
  width: 20px;
}

*::-webkit-scrollbar-track {
  background-color: transparent;
}

*::-webkit-scrollbar-thumb {
  background-color: #ccc;
  border-radius: 20px;
  border: 6px solid transparent;
  background-clip: content-box;
  cursor: pointer;
}

*::-webkit-scrollbar-thumb:hover {
  background-color: #a8bbbf;
  cursor: pointer;
}
</style>