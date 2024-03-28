import React from 'react';
import { Link } from 'react-router-dom';
import logo from '../img/logo.svg'

function Navbar() {
  return (
    <nav>
      <div className='navbar__container'>
        <div className="navbar__left">
          <img src={logo} alt="logo" />
          <div>
            <Link className="navbar__link" to="/">Catalog</Link>
            <Link className="navbar__link" to="/">About us</Link>
          </div>
        </div>
        <div className="navbar__right">
          <Link className="navbar__link" to="/login">Login</Link>
        </div>
      </div>
    </nav>
  );
}

export default Navbar;
