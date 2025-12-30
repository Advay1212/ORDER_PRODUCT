import React, { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { Product } from '../types';
import { productService } from '../services/api';

const ProductEdit: React.FC = () => {
  const { id } = useParams<{ id: string }>();
  const navigate = useNavigate();
  const [formData, setFormData] = useState({
    name: '',
    description: '',
    price: ''
  });
  const [loading, setLoading] = useState(true);
  const [submitting, setSubmitting] = useState(false);
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
      const product = response.data;
      setFormData({
        name: product.name,
        description: product.description,
        price: product.price.toString()
      });
    } catch (err) {
      setError('Product not found');
    } finally {
      setLoading(false);
    }
  };

  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    
    if (!formData.name || !formData.description || !formData.price) {
      setError('All fields are required');
      return;
    }

    try {
      setSubmitting(true);
      setError(null);
      await productService.updateProduct(parseInt(id!), {
        name: formData.name,
        description: formData.description,
        price: parseFloat(formData.price)
      });
      navigate('/products');
    } catch (err) {
      setError('Failed to update product');
    } finally {
      setSubmitting(false);
    }
  };

  if (loading) return <div>Loading...</div>;

  return (
    <div>
      <h1>Edit Product</h1>
      
      {error && (
        <div style={{ padding: '0.75rem', backgroundColor: '#f8d7da', color: '#721c24', border: '1px solid #f5c6cb', borderRadius: '4px', marginBottom: '1rem' }}>
          {error}
        </div>
      )}
      
      <form onSubmit={handleSubmit} style={{ maxWidth: '500px' }}>
        <div style={{ marginBottom: '1rem' }}>
          <label style={{ display: 'block', marginBottom: '0.5rem', fontWeight: 'bold' }}>
            Name *
          </label>
          <input
            type="text"
            name="name"
            value={formData.name}
            onChange={handleChange}
            style={{ width: '100%', padding: '0.5rem', border: '1px solid #ced4da', borderRadius: '4px' }}
            required
          />
        </div>
        
        <div style={{ marginBottom: '1rem' }}>
          <label style={{ display: 'block', marginBottom: '0.5rem', fontWeight: 'bold' }}>
            Description *
          </label>
          <textarea
            name="description"
            value={formData.description}
            onChange={handleChange}
            rows={4}
            style={{ width: '100%', padding: '0.5rem', border: '1px solid #ced4da', borderRadius: '4px', resize: 'vertical' }}
            required
          />
        </div>
        
        <div style={{ marginBottom: '1rem' }}>
          <label style={{ display: 'block', marginBottom: '0.5rem', fontWeight: 'bold' }}>
            Price *
          </label>
          <input
            type="number"
            name="price"
            value={formData.price}
            onChange={handleChange}
            step="0.01"
            min="0"
            style={{ width: '100%', padding: '0.5rem', border: '1px solid #ced4da', borderRadius: '4px' }}
            required
          />
        </div>
        
        <div style={{ display: 'flex', gap: '1rem' }}>
          <button
            type="submit"
            disabled={submitting}
            style={{ 
              padding: '0.75rem 1.5rem', 
              backgroundColor: submitting ? '#6c757d' : '#007bff', 
              color: 'white', 
              border: 'none', 
              borderRadius: '4px', 
              cursor: submitting ? 'not-allowed' : 'pointer' 
            }}
          >
            {submitting ? 'Updating...' : 'Update Product'}
          </button>
          
          <button
            type="button"
            onClick={() => navigate('/products')}
            style={{ padding: '0.75rem 1.5rem', backgroundColor: '#6c757d', color: 'white', border: 'none', borderRadius: '4px', cursor: 'pointer' }}
          >
            Cancel
          </button>
        </div>
      </form>
    </div>
  );
};

export default ProductEdit;