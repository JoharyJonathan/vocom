<template>
  <main>
    <div v-if="!product">
      <p>Chargement du produit...</p>
    </div>
    <div v-else>
      <h1>{{ product.name }}</h1>
      <p>{{ product.description }}</p>
      <p><strong>Price:</strong> {{ product.price }} €</p>
      <p><strong>Stock:</strong> {{ product.stock }}</p>

      <!-- Wishlist -->
      <button @click="addToWishlist(product)">Ajouter à ma liste de souhaits</button>

      <!-- Formulaire d'ajout au panier -->
      <form @submit.prevent="addToCart">
        <label for="quantity">Quantité :</label>
        <input
          id="quantity"
          type="number"
          v-model.number="quantity"
          min="1"
          :max="product.stock"
          required
        />
        <button type="submit">Ajouter au panier 🛒</button>
      </form>

      <br />
      <button @click="$router.push('/product-list')">Retour</button>
    </div>
  </main>
</template>

<script>
    import api from "../api";

    export default {
        name: "ProductDetails",
        data() {
            return {
            product: null,
            quantity: 1,
            };
        },
        methods: {
            async fetchProduct() {
                const id = this.$route.params.id;
                try {
                    const response = await api.get(`/product/${id}`);
                    this.product = response.data;
                } catch (error) {
                    console.error("Error fetching product:", error);
                }
            },
            addToWishlist(product) {
                let wishlist = JSON.parse(localStorage.getItem("wishlist") || "[]");
                if (!wishlist.find((p) => p.id === product.id)) {
                    wishlist.push(product);
                    localStorage.setItem("wishlist", JSON.stringify(wishlist));
                    alert(`${product.name} ajouté à votre liste de souhaits ✅`);
                } else {
                    alert(`${product.name} est déjà dans votre liste ❌`);
                }
            },
            async addToCart() {
                try {
                    const user = JSON.parse(localStorage.getItem("user"));
                    if (!user) {
                        alert("Vous devez être connecté pour ajouter au panier ❌");
                        this.$router.push("/login");
                        return;
                    }
                    if (this.quantity > this.product.stock) {
                        alert("❌ La quantité dépasse le stock disponible");
                        return;
                    }
                    await api.post(`/add-cart/${user.id}/${this.product.id}`, {
                    quantity: this.quantity,
                    });
                    alert("✅ Produit ajouté au panier !");
                } catch (error) {
                    console.error("Erreur lors de l'ajout au panier:", error);
                    alert("❌ Impossible d'ajouter au panier");
                }
            },
        },
        mounted() {
            this.fetchProduct();
        },
    };
</script>