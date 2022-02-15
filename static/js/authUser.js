//authUser.js

function Login() {
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;

    var payload = { 'username': username, 'password': password };
    document.getElementById("status").innerHTML = '<div class="spinner-border" role="status"></div>';
    fetch("/api/v1/login", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(payload),
        })
        .then((res) => res.json())
        .then((data) => {
            console.log(data);
            if (data['status'] == 'success') {
                window.location.href = "/";
            } else {
                document.getElementById("status").innerHTML = '<p style="color:red">' + data['status'] + "</p>";
            }
        })
        .catch((err) => console.log(err));
}