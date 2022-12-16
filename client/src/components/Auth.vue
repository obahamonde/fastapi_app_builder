<script setup lang="ts">
const user = reactive({
  username: "",
  email: "",
  password: ""
});
const login = async()=>{
    const formdata = new FormData();
    formdata.append("username", user.username);
    formdata.append("client_id", user.email);
    formdata.append("password", user.password);

    const { data } = await useFetch("/api/auth/token", {
        method: "POST",
        body: formdata
    }).json();
    const token = unref(data).token
    alert(token)    
}
</script>
<template>
<section>
<v-container>
  <v-row>
    <v-col cols="12" sm="6" md="4">
      <v-card>
        <v-card-title>
          <h2 class="headline mb-0">Sign In</h2>
        </v-card-title>
        <v-card-text>
          <v-form>
            <v-text-field
              v-model="user.username"
              label="Username"
              outlined
              dense
              required
            />
            <v-text-field
              v-model="user.email"
              label="Email"
              outlined
              dense
              required
            />
            <v-text-field
              v-model="user.password"
              label="Password"
              outlined
              dense
              required
            />
          </v-form>
        </v-card-text>
        <v-card-actions>
          <v-btn color="primary" @click="login">Login</v-btn>
        </v-card-actions>
      </v-card>
    </v-col>
  </v-row>
</v-container>
</section>
</template>
