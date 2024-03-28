import React, { useState, useEffect } from 'react';
import Cookies from 'js-cookie';

function Login() {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState(null);
    const [token, setToken] = useState(null);

    useEffect(() => {
        const storedToken = Cookies.get('token');
        if (storedToken) {
            setToken(storedToken);
        }
    }, []);

    const handleLogin = async (e) => {
        e.preventDefault();
        setError(null);
        try {
            const response = await fetch('http://localhost:8000/token', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                },
                body: new URLSearchParams({ username, password }).toString(),
            });
            const data = await response.json();
            if (!response.ok) {
                if (data.detail) {
                    setError(data.detail.map((errorDetail) => errorDetail.msg).join(', '));
                } else {
                    setError('Failed to log in');
                }
                return;
            }
            const accessToken = data.access_token;
            const expiresInMinutes = data.exp;
            setToken(accessToken);
            Cookies.set('token', accessToken, { expires: expiresInMinutes / (24 * 60) });
        } catch (error) {
            setError('Failed to log in');
        }
    };
    
    return (
        <div className='login'>
            {error && <p>{error}</p>}
            {token ? (
                <p>You are logged in!</p>
            ) : (
                <form className='login__form' onSubmit={handleLogin}>
                    <input type="text" placeholder="Username" value={username} onChange={(e) => setUsername(e.target.value)}/>
                    <input type="password" placeholder="Password" value={password} onChange={(e) => setPassword(e.target.value)}/>
                    <button type="submit">Login</button>
                </form>
            )}
        </div>
    );
}

export default Login;
