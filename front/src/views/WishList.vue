<template>
  <main>
    <h1>Wish List</h1>

    <div v-if="products.length === 0">
      <p>Aucun produit dans la wishlist</p>
    </div>

    <ul v-else>
      <li v-for="item in products" :key="item.wish_id">
        {{ item.name }} - {{ item.description }} - {{ item.stock }} disponibles - {{ item.price }} €
        <button @click="deleteProduct(item.wish_id)">❌ Supprimer</button>
      </li>
    </ul>
  </main>
</template>

<script>
    import api from "../api";

    export default {
        name: "WishList",
        data() {
            return {
            products: [],
            };
        },
        methods: {
            async getWishList() {
                try {
                    const user = JSON.parse(localStorage.getItem("user"));
                    if (!user) {
                        alert("Vous devez être connecté");
                        this.$router.push("/login");
                        return;
                    }
                    const response = await api.get(`/wish/${user.id}`);
                    this.products = response.data;
                } catch (error) {
                    console.error("Error fetching wishlist ", error);
                }
            },
            async deleteProduct(wish_id) {
                try {
                    await api.delete(`/delete-wish/${wish_id}`);
                    this.products = this.products.filter((p) => p.wish_id !== wish_id);
                    alert("Produit supprimé de la wishlist ✅");
                } catch (error) {
                    console.error("Error deleting wishlist ", error);
                }
            },
        },
        mounted() {
            this.getWishList();
        },
    };
</script>