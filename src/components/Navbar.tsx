import React from 'react';
import { Link } from 'react-router-dom';

const Navbar: React.FC = () => {
  return (
    <nav style={{ padding: '1rem', backgroundColor: '#f5f5f5', marginBottom: '2rem' }}>
      <div style={{ display: 'flex', gap: '1rem' }}>
        <Link to="/" style={{ textDecoration: 'none', color: '#007bff' }}>Home</Link>
        <Link to="/products" style={{ textDecoration: 'none', color: '#007bff' }}>Products</Link>
        <Link to="/orders" style={{ textDecoration: 'none', color: '#007bff' }}>Orders</Link>
      </div>
    </nav>
  );
};

export default Navbar;