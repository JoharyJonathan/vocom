<template>
    <main>
        <router-link to="/new-product">Add new product</router-link>
        <h1>Liste des produits</h1>
        <li v-for="(item, index) in products" :key="index">
        {{ item.name }} - {{ item.description }} - {{ item.stock }} available - {{ item.price }} €  <router-link :to="`/edit-product/${item.id}`">Edit</router-link> <button @click="deleteProduct(item.id)">Delete product</button>
        </li>
    </main>
</template>

<script>
    import axios from 'axios'

    export default {
        name: "Products",
        data() {
            return {
                products: [],
            }
        },
        created() {
            this.fetchProducts();
        },
        methods: {
            async fetchProducts() {
                try {
                    const url = 'http://localhost:5000/products';
                    const response = await axios.get(url);
                    this.products = response.data;
                    return response.data;
                } catch (error) {
                    console.error('Error fetching products ', error);
                }
            },
            async deleteProduct(id) {
                try {
                    const response = await axios.delete(`http://localhost:5000/delete-product/${id}`);
                    this.products = this.products.filter(p => p.id !== id);
                    return response.data;
                } catch (error) {
                    console.error('Error deleting product', error);
                }
            }
        }
    }
</script>