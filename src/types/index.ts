export interface Product {
  id?: number;
  name: string;
  description: string;
  price: number;
  created_at?: string;
  updated_at?: string;
}

export interface OrderItem {
  product_id: number;
  quantity: number;
  price_at_time: number;
}

export interface Order {
  id?: number;
  customer_name: string;
  customer_email: string;
  shipping_address: string;
  order_date?: string;
  status: 'PENDING' | 'PROCESSING' | 'SHIPPED' | 'DELIVERED' | 'CANCELLED';
  total_amount: number;
  items: OrderItem[];
}