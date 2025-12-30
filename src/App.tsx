import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Navbar from './components/Navbar';
import Home from './pages/Home';
import ProductsList from './pages/ProductsList';
import ProductCreate from './pages/ProductCreate';
import ProductDetails from './pages/ProductDetails';
import ProductEdit from './pages/ProductEdit';
import OrdersList from './pages/OrdersList';
import NotFound from './pages/NotFound';
import './App.css';

function App() {
  return (
    <Router>
      <div className="App">
        <Navbar />
        <div style={{ padding: '0 2rem' }}>
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/products" element={<ProductsList />} />
            <Route path="/products/create" element={<ProductCreate />} />
            <Route path="/products/:id" element={<ProductDetails />} />
            <Route path="/products/:id/edit" element={<ProductEdit />} />
            <Route path="/orders" element={<OrdersList />} />
            <Route path="*" element={<NotFound />} />
          </Routes>
        </div>
      </div>
    </Router>
  );
}

export default App;
