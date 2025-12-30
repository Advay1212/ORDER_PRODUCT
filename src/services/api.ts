import axios from 'axios';
import { Product, Order } from '../types';
import { mockProducts, mockOrders } from './mockData';

const API_BASE_URL = 'https://order-product.onrender.com';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
  timeout: 5000
});

// Add response interceptor for better error handling
api.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 422) {
      // Validation error
      const errorData = error.response.data;
      throw new Error(errorData.message || 'Validation failed');
    } else if (error.response?.status === 404) {
      // Not found error
      const errorData = error.response.data;
      throw new Error(errorData.message || 'Resource not found');
    } else if (error.response?.status === 400) {
      // Bad request error
      const errorData = error.response.data;
      throw new Error(errorData.message || 'Bad request');
    }
    throw error;
  }
);

let productCounter = 4;

export const productService = {
  getProducts: async () => {
    const response = await api.get<Product[]>('/products');
    return response;
  },
  getProduct: async (id: number) => {
    const response = await api.get<Product>(`/products/${id}`);
    return response;
  },
  createProduct: async (product: Omit<Product, 'id' | 'created_at' | 'updated_at'>) => {
    const response = await api.post<Product>('/products', product);
    return response;
  },
  updateProduct: async (id: number, product: Omit<Product, 'id' | 'created_at' | 'updated_at'>) => {
    const response = await api.put<Product>(`/products/${id}`, product);
    return response;
  },
  deleteProduct: async (id: number) => {
    const response = await api.delete(`/products/${id}`);
    return response;
  },
};

export const orderService = {
  getOrders: async () => {
    const response = await api.get<Order[]>('/orders');
    return response;
  },
  getOrder: async (id: number) => {
    const response = await api.get<Order>(`/orders/${id}`);
    return response;
  },
  createOrder: async (order: Omit<Order, 'id' | 'order_date'>) => {
    const response = await api.post<Order>('/orders', order);
    return response;
  },
};