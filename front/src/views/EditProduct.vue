<template>
  <main>
    <h1>Edit product</h1>
    <form @submit.prevent="editProduct">
      <div>
        <label>Name : </label>
        <input type="text" v-model="product.name" required>
      </div>
      <div>
        <label>Description : </label>
        <input type="text" v-model="product.description" required>
      </div>
      <div>
        <label>Price : </label>
        <input type="number" v-model.number="product.price" step="0.01" required>
      </div>
      <div>
        <label>Stock : </label>
        <input type="number" v-model.number="product.stock" required>
      </div>
      <button type="submit">Edit</button> 
    </form>
  </main>
</template>

<script>
import axios from 'axios';

export default {
  name: "EditProduct",
  data() {
    return {
      product: {
        id: null,
        name: "",
        description: "",
        price: 0,
        stock: 0,
      }
    }
  },
  methods: {
    async getProduct() {
      const id = this.$route.params.id;
      try {
        const response = await axios.get(`http://127.0.0.1:5000/product/${id}`);
        this.product = response.data; 
      } catch (error) {
        console.error('Error fetching this product ', error);
      }
    },
    async editProduct() {
      const id = this.$route.params.id;
      try {
        await axios.put(`http://127.0.0.1:5000/update-product/${id}`, this.product, {
          headers: {
            "Content-Type": "application/json"
          }
        });
        alert("Product updated successfully ✅");
        this.$router.push("/products");
      } catch (error) {
        console.error('Error updating this product', error);
      }
    }
  },
  mounted() {
    this.getProduct();
  }
}
</script>