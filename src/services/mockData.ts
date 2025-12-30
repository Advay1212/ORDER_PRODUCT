import { Product, Order } from '../types';

export const mockProducts: Product[] = [
  {
    id: 1,
    name: 'Laptop',
    description: 'High-performance laptop for work and gaming',
    price: 999.99,
    created_at: '2025-12-16T00:00:00Z',
    updated_at: '2025-12-16T00:00:00Z'
  },
  {
    id: 2,
    name: 'Smartphone',
    description: 'Latest model smartphone with advanced features',
    price: 699.99,
    created_at: '2025-12-16T00:00:00Z',
    updated_at: '2025-12-16T00:00:00Z'
  },
  {
    id: 3,
    name: 'Headphones',
    description: 'Wireless noise-cancelling headphones',
    price: 199.99,
    created_at: '2025-12-16T00:00:00Z',
    updated_at: '2025-12-T00:00:00Z'
  }
];

export const mockOrders: Order[] = [
  {
    id: 1,
    customer_name: 'Advay',
    customer_email: 'aasuryavnshi123@gmail.com',
    shipping_address: '123 , Bengaluru, Karnataka 12345',
    order_date: '2024-01-15T10:30:00Z',
    status: 'DELIVERED',
    total_amount: 999.99,
    items: [
      {
        product_id: 1,
        quantity: 1,
        price_at_time: 999.99
      }
    ]
  },
  {
    id: 2,
    customer_name: 'Tharun',
    customer_email: 'Tharun@gmail.com',
    shipping_address: '456 MG Road, Bengaluru, Karnataka 67890',
    order_date: '2024-01-16T14:20:00Z',
    status: 'SHIPPED',
    total_amount: 899.98,
    items: [
      {
        product_id: 2,
        quantity: 1,
        price_at_time: 699.99
      },
      {
        product_id: 3,
        quantity: 1,
        price_at_time: 199.99
      }
    ]
  }
];