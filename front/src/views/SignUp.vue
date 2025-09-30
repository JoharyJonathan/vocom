<template>
  <main>
    <h1>Signup</h1>
    <form @submit.prevent="signup">
      <div>
        <label>Username:</label>
        <input type="text" v-model="form.username" required />
      </div>
      <div>
        <label>Email:</label>
        <input type="email" v-model="form.email" required />
      </div>
      <div>
        <label>Password:</label>
        <input type="password" v-model="form.password" required />
      </div>
      <button type="submit">Register</button>
    </form>
  </main>
</template>

<script>
    import api from "../api";

    export default {
        name: "Signup",
        data() {
            return {
            form: { username: "", email: "", password: "" },
            };
        },
        methods: {
            async signup() {
            try {
                await api.post("/signup", this.form);
                alert("Account created! ✅");
                this.$router.push("/login");
            } catch (error) {
                alert(error.response?.data?.error || "Signup failed ❌");
            }
            },
        },
    };
</script>