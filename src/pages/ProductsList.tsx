import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { Product } from '../types';
import { productService } from '../services/api';

const ProductsList: React.FC = () => {
  const [products, setProducts] = useState<Product[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    fetchProducts();
  }, []);

  const fetchProducts = async () => {
    try {
      setLoading(true);
      const response = await productService.getProducts();
      setProducts(response.data);
    } catch (err) {
      setError('Failed to fetch products');
    } finally {
      setLoading(false);
    }
  };

  const handleDelete = async (id: number) => {
    if (window.confirm('Are you sure you want to delete this product?')) {
      try {
        await productService.deleteProduct(id);
        setProducts(products.filter(p => p.id !== id));
      } catch (err) {
        setError('Failed to delete product');
      }
    }
  };

  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error: {error}</div>;

  return (
    <div>
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '1rem' }}>
        <h1>Products</h1>
        <Link to="/products/create" style={{ padding: '0.5rem 1rem', backgroundColor: '#007bff', color: 'white', textDecoration: 'none', borderRadius: '4px' }}>
          Add Product
        </Link>
      </div>
      
      <table style={{ width: '100%', borderCollapse: 'collapse' }}>
        <thead>
          <tr style={{ backgroundColor: '#f8f9fa' }}>
            <th style={{ padding: '0.75rem', border: '1px solid #dee2e6', textAlign: 'left' }}>ID</th>
            <th style={{ padding: '0.75rem', border: '1px solid #dee2e6', textAlign: 'left' }}>Name</th>
            <th style={{ padding: '0.75rem', border: '1px solid #dee2e6', textAlign: 'left' }}>Description</th>
            <th style={{ padding: '0.75rem', border: '1px solid #dee2e6', textAlign: 'left' }}>Price</th>
            <th style={{ padding: '0.75rem', border: '1px solid #dee2e6', textAlign: 'left' }}>Actions</th>
          </tr>
        </thead>
        <tbody>
          {products.map((product) => (
            <tr key={product.id}>
              <td style={{ padding: '0.75rem', border: '1px solid #dee2e6' }}>{product.id}</td>
              <td style={{ padding: '0.75rem', border: '1px solid #dee2e6' }}>{product.name}</td>
              <td style={{ padding: '0.75rem', border: '1px solid #dee2e6' }}>{product.description}</td>
              <td style={{ padding: '0.75rem', border: '1px solid #dee2e6' }}>${product.price}</td>
              <td style={{ padding: '0.75rem', border: '1px solid #dee2e6' }}>
                <div style={{ display: 'flex', gap: '0.5rem' }}>
                  <Link to={`/products/${product.id}`} style={{ padding: '0.25rem 0.5rem', backgroundColor: '#17a2b8', color: 'white', textDecoration: 'none', borderRadius: '3px', fontSize: '0.875rem' }}>
                    View
                  </Link>
                  <Link to={`/products/${product.id}/edit`} style={{ padding: '0.25rem 0.5rem', backgroundColor: '#ffc107', color: 'black', textDecoration: 'none', borderRadius: '3px', fontSize: '0.875rem' }}>
                    Edit
                  </Link>
                  <button 
                    onClick={() => handleDelete(product.id!)}
                    style={{ padding: '0.25rem 0.5rem', backgroundColor: '#dc3545', color: 'white', border: 'none', borderRadius: '3px', fontSize: '0.875rem', cursor: 'pointer' }}
                  >
                    Delete
                  </button>
                </div>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
      
      {products.length === 0 && (
        <div style={{ textAlign: 'center', padding: '2rem', color: '#6c757d' }}>
          No products found. <Link to="/products/create">Create your first product</Link>
        </div>
      )}
    </div>
  );
};

export default ProductsList;