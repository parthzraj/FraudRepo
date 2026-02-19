document.getElementById('detectionForm').addEventListener('submit', async (e) => {
    e.preventDefault();

    const formData = new FormData(e.target);
    const resultDiv = document.getElementById('result');
    const button = document.querySelector('.submit-button');

    // Show loading state
    button.textContent = 'Analyzing...';
    button.disabled = true;
    resultDiv.innerHTML = '<p class="loading">Analyzing audio for phishing threats</p>';
    resultDiv.classList.add('show');

    try {
        const response = await fetch('/detect', {
            method: 'POST',
            body: formData
        });
        const data = await response.json();

        if (data.error) {
            resultDiv.innerHTML = `<p class="error">Error: ${data.error}</p>`;
        } else {
            resultDiv.innerHTML = `
                <h3>Phishing Detection Result</h3>
                <p><strong>ID:</strong> ${data.id}</p>
                <p><strong>File Name:</strong> ${data.file_name}</p>
                <p><strong>Category:</strong> ${data.category}</p>
                <p><strong>Reason:</strong> ${data.reason}</p>
            `;
        }
    } catch (error) {
        resultDiv.innerHTML = `<p class="error">Error: ${error.message}</p>`;
    } finally {
        // Reset button state
        button.textContent = 'Detect Phishing';
        button.disabled = false;
    }
});