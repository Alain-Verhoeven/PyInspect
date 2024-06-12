// Get the form element
const testForm = document.getElementById('testForm');

// Add event listener to form submission
testForm.addEventListener('submit', function(event) {
    // Prevent the default form submission behavior
    event.preventDefault();

    // Your code to execute when the form is submitted goes here
    // For example, you can make an AJAX request or perform some other action
    console.log('Form submitted! Executing test.js...');
    DoSomething()
});

const login = async (username, password) => {
    try {
        const response = await fetch('/token', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: new URLSearchParams({
                'grant_type': 'password',
                'username': username,
                'password': password,
            }),
        });

        if (!response.ok) {
            throw new Error(`Failed to login: ${response.statusText}`);
        }

        const data = await response.json();
        console.log('Access Token:', data.access_token);
        return data.access_token;
    } catch (error) {
        console.error('Error:', error);
    }
};
const loginForm = document.getElementById('loginForm');

// Add event listener to form submission
loginForm.addEventListener('submit', function(event) {
    // Prevent the default form submission behavior
    event.preventDefault();

    // Your code to execute when the form is submitted goes here
    // For example, you can make an AJAX request or perform some other action
    console.log('login submitted! Executing test.js...');
    login('Alain','1234')
});

function DoSomething(){
    // Fetch user data using the token stored in localStorage
    fetch("/sometest", {
        headers: {
            "Authorization": "Bearer " + "Veerle"
        }
    })
    .then(response => response.json())
    .then(data => {
        console.log(data)
    })
    .catch(error => console.error("Error:", error));
}