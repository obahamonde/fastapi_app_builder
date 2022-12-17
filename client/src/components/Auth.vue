<script setup lang="ts">
import { Ref } from "vue";
const user = reactive({
  username: "",
  email: "",
  password: ""
});
const token = ref("") as Ref<string>;

const handleClipboard = async() => {
  await navigator.clipboard.writeText(token.value);
};


const login = async()=>{
    const formdata = new FormData();
    formdata.append("username", user.username);
    formdata.append("client_id", user.email);
    formdata.append("password", user.password);

    const { data } = await useFetch("/api/auth/token", {
        method: "POST",
        body: formdata
    }).json();
    token.value = unref(data).access_token
    
}


</script>
<template>
  <v-card p-8>
          <v-form col>
            <v-text-field
              v-model="user.username"
              label="Username"
              outlined
              dense
              required
            />
            <v-text-field
              v-model="user.email"
              type="email"
              label="Email"
              outlined
              dense
              required
            />
            <v-text-field
              type="password"
              v-model="user.password"
              label="Password"
              outlined
              dense
              required
            />
          </v-form>
        <v-card-actions>
          <v-btn btn-get @click="login">Login</v-btn>
        </v-card-actions>
        <v-card-subtitle v-if="token.length>0" font-mono text-primary drop-shadow-xl shadow-black font-bold text-lg>
           AccessToken: <p text-info>{{token}}</p> <Icon icon="mdi:clipboard-text-multiple" x2 cp scale @click="handleClipboard" />
        </v-card-subtitle>
</v-card>      
</template>
