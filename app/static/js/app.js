document.getElementById("login-form").addEventListener("submit", function(event) {
    event.preventDefault();

    let formData = new FormData(this);

    fetch("/login", {
        method: "POST",
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("message").textContent = data.message;
        document.getElementById("message").style.color = data.message.includes("successful") ? "#00ff00" : "#ff0000";
    })
    .catch(error => console.error("Error:", error));
});
