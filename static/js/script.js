async function login() {
    const usernameInput = document.getElementById("username");
    const passwordInput = document.getElementById("password");
    const msg = document.getElementById("msg"); // Message element
    const loginBtn = document.querySelector('button[onclick="login()"]');

    const username = usernameInput.value;
    const password = passwordInput.value;

    if (username === "" || password === "") {
        msg.innerText = "Please fill all fields";
        msg.className = "text-center text-red-500 font-medium mt-4 h-6 animate-pulse";
        return;
    }

    // Prepare UI for loading
    msg.innerText = "";
    loginBtn.innerText = "Logging in...";
    loginBtn.disabled = true;
    loginBtn.classList.add("opacity-50", "cursor-not-allowed");

    try {
        const response = await fetch('/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ username: username, password: password })
        });

        const data = await response.json();

        if (response.ok && data.message === "Login successful") {
            msg.innerText = "Login Successful! Redirecting...";
            msg.className = "text-center text-green-500 font-medium mt-4 h-6";
            // Optional: Redirect
            // window.location.href = "/dashboard"; 
        } else {
            msg.innerText = data.message || "Invalid username or password";
            msg.className = "text-center text-red-500 font-medium mt-4 h-6";
        }

    } catch (error) {
        console.error('Error:', error);
        msg.innerText = "An error occurred. Please try again.";
        msg.className = "text-center text-red-500 font-medium mt-4 h-6";
    } finally {
        // Reset button state
        loginBtn.innerText = "LOG IN";
        loginBtn.disabled = false;
        loginBtn.classList.remove("opacity-50", "cursor-not-allowed");
    }
}