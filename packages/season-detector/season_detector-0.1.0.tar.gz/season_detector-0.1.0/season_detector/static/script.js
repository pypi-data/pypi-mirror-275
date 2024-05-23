document.getElementById('uploadForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const fileInput = document.getElementById('fileInput');
    const formData = new FormData();
    formData.append('file', fileInput.files[0]);

    fetch('/upload', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        const resultDiv = document.getElementById('result');
        if (data.error) {
            resultDiv.innerHTML = `<p>${data.error}</p>`;
        } else {
            resultDiv.innerHTML = `
                <p>Season: ${data.season}</p>
                <p>Average RGB: ${data.rgb}</p>
                <img src="${data.image_url}" alt="Uploaded Image">
            `;
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
});
