// Fetch user data using the token stored in localStorage
fetch("/abcprotected", {
    headers: {
        "Authorization": "Bearer " + localStorage.getItem("token"),
        "X-CSRF-Token": "fakecsrf_token" // Assuming CSRF token is static in this example
    }
})
.then(response => response.json())
.then(data => {
    console.log(data)
    document.getElementById("userData").innerText = JSON.stringify(data);
    document.getElementById("email").innerText = data["email"];
})
.catch(error => console.error("Error:", error));