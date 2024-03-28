import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Navbar from './components/Navbar';
import AllPotions from './pages/AllPotions';
import Login from './components/Login';
import UserPage from './pages/UserPage';

function App() {
  return (
    <Router>
      <Navbar />
      <main>
        <Routes>
          <Route path="/" element={<AllPotions />} />
          <Route path="/login" element={<Login />} />
          <Route path="/my_account" element={<UserPage />} />
        </Routes>
      </main>
    </Router>
  );
}

export default App;
