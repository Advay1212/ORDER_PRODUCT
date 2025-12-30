import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { Order } from '../types';
import { orderService } from '../services/api';

const OrdersList: React.FC = () => {
  const [orders, setOrders] = useState<Order[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    fetchOrders();
  }, []);

  const fetchOrders = async () => {
    try {
      setLoading(true);
      const response = await orderService.getOrders();
      setOrders(response.data);
    } catch (err) {
      setError('Failed to fetch orders');
    } finally {
      setLoading(false);
    }
  };

  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error: {error}</div>;

  return (
    <div>
      <h1>Orders</h1>
      
      <table style={{ width: '100%', borderCollapse: 'collapse' }}>
        <thead>
          <tr style={{ backgroundColor: '#f8f9fa' }}>
            <th style={{ padding: '0.75rem', border: '1px solid #dee2e6', textAlign: 'left' }}>ID</th>
            <th style={{ padding: '0.75rem', border: '1px solid #dee2e6', textAlign: 'left' }}>Customer</th>
            <th style={{ padding: '0.75rem', border: '1px solid #dee2e6', textAlign: 'left' }}>Email</th>
            <th style={{ padding: '0.75rem', border: '1px solid #dee2e6', textAlign: 'left' }}>Status</th>
            <th style={{ padding: '0.75rem', border: '1px solid #dee2e6', textAlign: 'left' }}>Total</th>
            <th style={{ padding: '0.75rem', border: '1px solid #dee2e6', textAlign: 'left' }}>Date</th>
            <th style={{ padding: '0.75rem', border: '1px solid #dee2e6', textAlign: 'left' }}>Actions</th>
          </tr>
        </thead>
        <tbody>
          {orders.map((order) => (
            <tr key={order.id}>
              <td style={{ padding: '0.75rem', border: '1px solid #dee2e6' }}>{order.id}</td>
              <td style={{ padding: '0.75rem', border: '1px solid #dee2e6' }}>{order.customer_name}</td>
              <td style={{ padding: '0.75rem', border: '1px solid #dee2e6' }}>{order.customer_email}</td>
              <td style={{ padding: '0.75rem', border: '1px solid #dee2e6' }}>
                <span style={{ 
                  padding: '0.25rem 0.5rem', 
                  borderRadius: '3px', 
                  fontSize: '0.875rem',
                  backgroundColor: order.status === 'DELIVERED' ? '#d4edda' : order.status === 'SHIPPED' ? '#d1ecf1' : '#fff3cd',
                  color: order.status === 'DELIVERED' ? '#155724' : order.status === 'SHIPPED' ? '#0c5460' : '#856404'
                }}>
                  {order.status}
                </span>
              </td>
              <td style={{ padding: '0.75rem', border: '1px solid #dee2e6' }}>${order.total_amount}</td>
              <td style={{ padding: '0.75rem', border: '1px solid #dee2e6' }}>
                {order.order_date ? new Date(order.order_date).toLocaleDateString() : '-'}
              </td>
              <td style={{ padding: '0.75rem', border: '1px solid #dee2e6' }}>
                <Link 
                  to={`/orders/${order.id}`}
                  style={{ padding: '0.25rem 0.5rem', backgroundColor: '#17a2b8', color: 'white', textDecoration: 'none', borderRadius: '3px', fontSize: '0.875rem' }}
                >
                  View
                </Link>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
      
      {orders.length === 0 && (
        <div style={{ textAlign: 'center', padding: '2rem', color: '#6c757d' }}>
          No orders found.
        </div>
      )}
    </div>
  );
};

export default OrdersList;