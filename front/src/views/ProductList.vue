<template>
  <main>
    <h1>Products</h1>

    <!-- Bouton recherche vocale -->
    <div class="voice-search">
      <button @click="startListening">🎤 Rechercher par voix</button>
      <p v-if="transcript">Texte reconnu : <strong>{{ transcript }}</strong></p>
    </div>

    <div v-if="loading">Loading products...</div>
    <div v-else-if="products.length === 0">No products available</div>

    <ul v-else>
      <li v-for="product in products" :key="product.id" class="product-card">
        <h2>{{ product.name }}</h2>
        <p>{{ product.description }}</p>
        <p><strong>Price:</strong> {{ product.price }} €</p>
        <p><strong>Stock:</strong> {{ product.stock }}</p>

        <button @click="viewDetails(product.id)">Voir détails</button>
        <button @click="addToWishlist(product.id)">Ajouter à ma liste de souhaits</button>

        <div class="rating">
          <label>Votre note :</label>
          <select v-model="product.userRating">
            <option disabled value="">Choisir</option>
            <option v-for="n in 5" :key="n" :value="n">{{ n }} ⭐</option>
          </select>

          <label>Commentaire :</label>
          <textarea v-model="product.userComment" placeholder="Votre commentaire..."></textarea>

          <button @click="submitRating(product.id, product.userRating, product.userComment)">Noter</button>
        </div>
      </li>
    </ul>
  </main>
</template>

<script>
    import api from "../api";

    export default {
    name: "ProductList",
    data() {
        return {
        products: [],
        loading: true,
        transcript: "" // texte reconnu par la voix
        };
    },
    methods: {
        async fetchProducts() {
            this.loading = true;
            try {
                const response = await api.get("/products");
                this.products = response.data.map(p => ({
                ...p,
                userRating: "",
                userComment: ""
                }));
            } catch (error) {
                console.error("Error fetching products:", error);
            } finally {
                this.loading = false;
            }
        },

        async searchProducts(query) {
            this.loading = true;
            try {
                const response = await api.get(`/search?query=${encodeURIComponent(query)}`);
                this.products = response.data.map(p => ({
                ...p,
                userRating: "",
                userComment: ""
                }));
            } catch (error) {
                console.error("Error searching products:", error);
            } finally {
                this.loading = false;
            }
        },

        startListening() {
        const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
        recognition.lang = "fr-FR";
        recognition.interimResults = false;
        recognition.maxAlternatives = 1;

        recognition.start();

        recognition.onresult = (event) => {
            this.transcript = event.results[0][0].transcript;
            this.searchProducts(this.transcript);
        };

        recognition.onerror = (event) => {
            console.error("Erreur reconnaissance vocale:", event.error);
        };
        },

        viewDetails(productId) {
            this.$router.push(`/product-detail/${productId}`);
        },

        async addToWishlist(productId) {
            try {
                const user = JSON.parse(localStorage.getItem("user"));
                if (!user) {
                    alert("Vous devez être connecté pour ajouter à la wishlist ❌");
                    this.$router.push("/login");
                    return;
                }

                const response = await api.post(`/add-wish/${user.id}/${productId}`);
                alert("✅ " + response.data.message);
            } catch (error) {
                console.error("Error adding product to wishlist:", error);
                alert("❌ Erreur lors de l'ajout à la wishlist");
            }
        },

        async submitRating(productId, rating, comment) {
            if (!rating) {
                alert("Veuillez sélectionner une note !");
                return;
            }

            try {
                const user = JSON.parse(localStorage.getItem("user"));
                if (!user) {
                alert("Vous devez être connecté pour noter un produit ❌");
                this.$router.push("/login");
                return;
                }

                const response = await api.post(`/add-rating/${user.id}/${productId}`, {
                rating,
                comment
                });
                alert("✅ " + response.data.message);

                // reset des champs
                const product = this.products.find(p => p.id === productId);
                if (product) {
                product.userRating = "";
                product.userComment = "";
                }
            } catch (error) {
                console.error("Error submitting rating:", error);
                alert("❌ Impossible de noter le produit");
            }
        }
    },
    mounted() {
        this.fetchProducts();
    }
    };
</script>

<style>
    .product-card {
    border: 1px solid #ccc;
    padding: 1rem;
    margin-bottom: 1rem;
    border-radius: 5px;
    }
    button {
    margin-right: 0.5rem;
    }
    .rating {
    margin-top: 10px;
    }
    .rating select,
    .rating textarea {
    display: block;
    margin-bottom: 5px;
    width: 100%;
    }
    .voice-search {
    margin-bottom: 20px;
    }
</style>