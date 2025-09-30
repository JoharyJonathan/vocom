<template>
  <main>
    <h1>Cart</h1>

    <div v-if="products.length === 0">
      <p>No product in Cart</p>
    </div>

    <div v-else>
      <ul>
        <li v-for="item in products" :key="item.cart_id">
          {{ item.name }} - {{ item.description }} - {{ item.stock }} disponibles - 
          {{ item.price }} € - Quantity: {{ item.quantity }}
          <button @click="deleteProduct(item.cart_id)">❌ Supprimer</button>
        </li>
      </ul>

      <!-- Bouton pour confirmer la commande -->
      <button @click="confirmOrder" class="confirm-btn">✅ Confirmer la commande</button>
    </div>
  </main>
</template>

<script>
    import api from "../api";

    export default {
        name: "Cart",
        data() {
            return {
            products: [],
            };
        },
        methods: {
            async getCart() {
                try {
                    const user = JSON.parse(localStorage.getItem("user"));
                    if (!user) {
                    alert("Vous devez être connecté");
                    this.$router.push("/login");
                    return;
                    }
                    const response = await api.get(`/cart/${user.id}`);
                    this.products = response.data;
                } catch (error) {
                    console.error("Error fetching cart ", error);
                }
            },
            async deleteProduct(cartId) {
                try {
                    await api.delete(`/remove-cart/${cartId}`);
                    this.products = this.products.filter((p) => p.cart_id !== cartId);
                } catch (error) {
                    console.error("Error deleting product from cart", error);
                }
            },
            async confirmOrder() {
                try {
                    const user = JSON.parse(localStorage.getItem("user"));
                    if (!user) {
                    alert("Vous devez être connecté");
                    this.$router.push("/login");
                    return;
                    }

                    const response = await api.post(`/create-order/${user.id}`);
                    
                    alert(`Commande validée ! Total : ${response.data.total} €`);
                    this.products = []; // vider le panier côté front
                } catch (error) {
                    console.error("Erreur lors de la création de la commande", error);
                    alert("Impossible de créer la commande");
                }
            },
        },
        mounted() {
            this.getCart();
        },
    };
</script>

<style>
    .confirm-btn {
    margin-top: 20px;
    padding: 10px 15px;
    background-color: green;
    color: white;
    border: none;
    cursor: pointer;
    }
</style>