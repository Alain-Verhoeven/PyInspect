console.log('A1')
// Fetch user data using the token stored in localStorage
fetch("/abcprotected", {
    headers: {
        "Authorization": "Bearer " + localStorage.getItem("token"),
        "X-CSRF-Token": "fakecsrf_token" // Assuming CSRF token is static in this example
    }
})

console.log('A2')

document.getElementById("loginForm").addEventListener("submit", function(event) {
    event.preventDefault(); // Prevent form submission
    console.log('A3')
    // Fetch the token using provided credentials
    fetch("/token", {
        method: "POST",
        body: new FormData(document.getElementById("loginForm"))
    })
    .then(response => response.json())
    .then(data => {
        // If token received, save it in localStorage
        if (data.access_token) {
            localStorage.setItem("token", data.access_token);
            // Redirect to protected page
            windowdocument.getElementById("loginForm").addEventListener("submit", function(event) {
                event.preventDefault(); // Prevent form submission
                console.log('A3')
                // Fetch the token using provided credentials
                fetch("/token", {
                    method: "POST",
                    body: new FormData(document.getElementById("loginForm"))
                })w.location.href = "/protected";
        } else {
            alert("Invalid credentials");
        }
    })
    .catch(error => console.error("Error:", error));
})
.then(response => response.json())
.then(data => {
    document.getElementById("userData").innerText = JSON.stringify(data);
})
.catch(error => console.error("Error:", error));