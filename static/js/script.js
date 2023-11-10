// static/js/script.js
function resizeImage() {
    fetch("/", {
        method: "POST",
        body: new FormData(document.forms[0]),
    })
    .then(response => response.json())
    .then(data => {
        var resultDiv = document.getElementById("result");
        resultDiv.innerHTML = `<img src="${data.resized_image_path}" alt="Resized Image">`;
    })
    .catch(error => {
        console.error("Error:", error);
    });
}
