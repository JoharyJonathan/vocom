<template>
  <main>
    <h1>Login</h1>
    <form @submit.prevent="login">
      <div>
        <label>Email:</label>
        <input type="email" v-model="form.email" required />
      </div>
      <div>
        <label>Password:</label>
        <input type="password" v-model="form.password" required />
      </div>
      <button type="submit">Login</button>
    </form>
  </main>
</template>

<script>
    import api from "../api";

    export default {
        name: "Login",
        data() {
            return {
            form: { email: "", password: "" },
            };
        },
        methods: {
            async login() {
            try {
                const response = await api.post("/login", this.form);
                const { token, user } = response.data;
                localStorage.setItem("token", token);
                localStorage.setItem("user", JSON.stringify(user));
                alert("Welcome back " + user.username + " ✅");
                this.$router.push("/profile");
            } catch (error) {
                alert(error.response?.data?.error || "Login failed ❌");
            }
            },
        },
    };
</script>