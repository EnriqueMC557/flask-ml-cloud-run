document.getElementById('predictionForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const values = Array.from({ length: 4 }, (_, i) => document.getElementById(`input${i + 1}`).value);

    fetch('/api/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ values })
    })
    .then(response => {
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        return response.json();
    })
    .then(data => {
        const prediction = data.data;
        
        const riskMessages = {
            0: "Iris setosa",
            1: "Iris versicolor",
            2: "Iris virginica",
        };
        
        const riskMessage = riskMessages[prediction.prediction] || "Unknown";

        const riskPercentage = `Probability: ${prediction.probability} %`;
        
        document.getElementById('result').innerHTML = `
                <p>${riskMessage}</p>
                <p>${riskPercentage}</p>
        `;
    })
    .catch(error => {
        console.error('Error:', error);
        alert(`Error: ${error.message}`);
    });
});
