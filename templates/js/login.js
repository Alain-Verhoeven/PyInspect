document.getElementById("loginForm").addEventListener("submit", function(event) {
    event.preventDefault(); // Prevent form submission

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
            window.location.href = "/protected";
        } else {
            alert("Invalid credentials");
        }
    })
    .catch(error => console.error("Error:", error));
});