<template>
    <main>
        <h1>New Product</h1>
        <form @submit.prevent="submitProduct">
            <div>
                <label>Name : </label>
                <input type="text" v-model="product.name" placeholder="Product name ... " required>
            </div>
            <div>
                <label>Description : </label>
                <input type="text" v-model="product.description" placeholder="Product description ... " required>
            </div>
            <div>
                <label>Price : </label>
                <input type="number" v-model.number="product.price" step="0.01" placeholder="Product price ... " required>
            </div>
            <div>
                <label>Stock : </label>
                <input type="number" v-model.number="product.stock" placeholder="Product stock ... " required>
            </div>
            <button type="submit">Add new product</button>
        </form>
    </main>
</template>

<script>
    import axios from 'axios';

    export default {
        name: "NewProduct",
        data() {
            return {
                product: {
                    name: "",
                    description: "",
                    price: 0,
                    stock: 0,
                }
            }
        },
        methods: {
            async submitProduct() {
                const formdata = new FormData();
                for (const key in this.product) {
                    formdata.append(key, this.product[key]);
                }

                try {
                    const response = await axios.post("http://127.0.0.1:5000/new-product", formdata);
                    alert("Product added successfully ! ");
                    this.resetForm();
                } catch (error) {
                    console.error('Error adding new product ', error);
                }
            },
            resetForm() {
                this.product = {
                    name: "",
                    description: "",
                    price: 0,
                    stock: 0,
                };
            },
        }
    }
</script>