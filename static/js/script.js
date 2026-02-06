function login() {
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    if (username === "" || password === "") {
        document.getElementById("msg").innerText = "Please fill all fields";
        return;
    }

    // Backend connection will be added here later
    document.getElementById("msg").innerText = "Login button clicked";
}