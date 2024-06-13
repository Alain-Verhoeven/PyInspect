async function login() {
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    try {
        const response = await fetch('/token', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded'
            },
            body: `username=${username}&password=${password}`
        });
        if (!response.ok) {
            throw new Error('Login failed');
        }
        const data = await response.json();
        localStorage.setItem('accessToken', data.access_token);
        document.getElementById('responseMessage').textContent = 'Login successful.';
    } catch (error) {
        console.error('Login error:', error);
        document.getElementById('responseMessage').textContent = 'Login failed. Please try again.';
    }
}

async function getProtectedContent() {
    const token = localStorage.getItem('accessToken');

    if (token) {

        try {
            const response = await fetch('/protected', {
                method: 'GET',
                headers: {
                    'Authorization': `Bearer ${token}`
                }
            });
            if (response.ok) {
                console.log('OK')
                     //window.location.href = '/static/views/register.html';
                const response1 = await fetch('/register', {
                    method: 'GET',
                    headers: {
                        'Authorization': `Bearer ${token}`
                    }
                }).then(response => {
                    if (!response.ok) {
                      throw new Error(`HTTP error! Status: ${response.status}`);
                    }
                    return response.json(); // Parse JSON response asynchronously
                  })
                  .then(data => {
                     window.location.href = data.url;
                  })
                  .catch(error => {
                    console.error('Fetch error:', error);
                  });

            }
            if (!response.ok) {
             alert('Token expired')
                throw new Error('Failed to fetch protected content');
            }
        } catch (error) {
            console.error('error:', error);
        };
    }
    else{
        alert('Token expired');
        console.error('Access token not found');
        return;
    }
}                    console.log(data.url); // Process JSON data


function logout() {
    localStorage.removeItem('accessToken');
    document.getElementById('responseMessage').textContent = 'Logged out successfully.';
    // Optional: Redirect to login page or update UI as needed
}


