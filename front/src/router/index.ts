import { createRouter, createWebHistory } from 'vue-router';
import Home from '../views/Home.vue';
import Products from '../views/Products.vue';
import NewProduct from '../views/NewProduct.vue';
import EditProduct from '../views/EditProduct.vue';
import SignUp from '../views/SignUp.vue';
import Login from '../views/Login.vue';
import Profile from '../views/Profile.vue';
import ProductList from '../views/ProductList.vue';
import ProductDetail from '../views/ProductDetail.vue';
import WishList from '../views/WishList.vue';
import Cart from '../views/Cart.vue';

const routes = [
    { path: '/', component: Home },
    { path: '/products', component: Products },
    { path: '/new-product', component: NewProduct },
    { path: '/edit-product/:id', component: EditProduct },
    { path: '/signup', component: SignUp },
    { path: '/login', component: Login },
    { path: '/profile', component: Profile },
    { path: '/product-list', component: ProductList },
    { path: '/product-detail/:id', component: ProductDetail },
    { path: '/wishList', component: WishList },
    { path: '/cart', component: Cart },
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router;