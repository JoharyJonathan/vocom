<template>
  <main>
    <h1>My Profile</h1>
    <div v-if="user">
      <p><strong>ID:</strong> {{ user.id }}</p>
      <p><strong>Username:</strong> {{ user.username }}</p>
      <p><strong>Email:</strong> {{ user.email }}</p>
      <p><strong>Created at:</strong> {{ user.created_at }}</p>
    </div>
    <button @click="logout">Logout</button>
  </main>
</template>

<script>
    import api from "../api";

    export default {
        name: "Profile",
        data() {
            return {
            user: null,
            };
        },
        methods: {
            async fetchProfile() {
            try {
                const response = await api.get("/profile");
                this.user = response.data;
            } catch (error) {
                alert("You must login first ❌");
                this.$router.push("/login");
            }
            },
            logout() {
            localStorage.removeItem("token");
            localStorage.removeItem("user");
            this.$router.push("/login");
            },
        },
        mounted() {
            this.fetchProfile();
        },
    };
</script>