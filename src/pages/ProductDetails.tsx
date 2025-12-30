import React, { useState, useEffect } from 'react';
import { useParams, Link } from 'react-router-dom';
import { Product } from '../types';
import { productService } from '../services/api';

const ProductDetails: React.FC = () => {
  const { id } = useParams<{ id: string }>();
  const [product, setProduct] = useState<Product | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    if (id) {
      fetchProduct(parseInt(id));
    }
  }, [id]);

  const fetchProduct = async (productId: number) => {
    try {
      setLoading(true);
      const response = await productService.getProduct(productId);
      setProduct(response.data);
    } catch (err) {
      setError('Product not found');
    } finally {
      setLoading(false);
    }
  };

  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error: {error}</div>;
  if (!product) return <div>Product not found</div>;

  return (
    <div>
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '2rem' }}>
        <h1>Product Details</h1>
        <div style={{ display: 'flex', gap: '1rem' }}>
          <Link 
            to={`/products/${product.id}/edit`}
            style={{ padding: '0.5rem 1rem', backgroundColor: '#ffc107', color: 'black', textDecoration: 'none', borderRadius: '4px' }}
          >
            Edit Product
          </Link>
          <Link 
            to="/products"
            style={{ padding: '0.5rem 1rem', backgroundColor: '#6c757d', color: 'white', textDecoration: 'none', borderRadius: '4px' }}
          >
            Back to List
          </Link>
        </div>
      </div>
      
      <div style={{ backgroundColor: '#f8f9fa', padding: '2rem', borderRadius: '8px', maxWidth: '600px' }}>
        <div style={{ marginBottom: '1rem' }}>
          <strong>ID:</strong> {product.id}
        </div>
        
        <div style={{ marginBottom: '1rem' }}>
          <strong>Name:</strong> {product.name}
        </div>
        
        <div style={{ marginBottom: '1rem' }}>
          <strong>Description:</strong> {product.description}
        </div>
        
        <div style={{ marginBottom: '1rem' }}>
          <strong>Price:</strong> ${product.price}
        </div>
        
        {product.created_at && (
          <div style={{ marginBottom: '1rem' }}>
            <strong>Created:</strong> {new Date(product.created_at).toLocaleString()}
          </div>
        )}
        
        {product.updated_at && (
          <div style={{ marginBottom: '1rem' }}>
            <strong>Updated:</strong> {new Date(product.updated_at).toLocaleString()}
          </div>
        )}
      </div>
    </div>
  );
};

export default ProductDetails;