let myChart = null;

document.getElementById('growth-form').addEventListener('submit', function(event) {
    event.preventDefault();
    const age = document.getElementById('age').value;
    const weight = document.getElementById('weight').value;
    const height = document.getElementById('height').value;
    const gender = document.getElementById('gender').value;

    fetch('https://indianbabygrowthcalculator1-9df9a01a428b.herokuapp.com/calculate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ age, weight, height, gender }),
    })
    .then(response => {
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
    })
    .then(data => {
        document.getElementById('results').innerHTML = `
            <h2>Results:</h2>
            <p>Age: ${data.age} months</p>
            <p>Weight: ${data.weight} kg (Percentile: ${data.weightPercentile})</p>
            <p>Height: ${data.height} cm (Percentile: ${data.heightPercentile})</p>
        `;
        createChart(data);
    })
    .catch((error) => {
        console.error('Error:', error);
        document.getElementById('results').innerHTML = `<p>An error occurred: ${error.message}. Please try again.</p>`;
    });
});

function createChart(data) {
    const ctx = document.getElementById('growthChart').getContext('2d');
    
    // Destroy the existing chart if it exists
    if (myChart) {
        myChart.destroy();
    }

    // Clear the canvas
    ctx.clearRect(0, 0, ctx.canvas.width, ctx.canvas.height);

    // Create a new chart
    myChart = new Chart(ctx, {
        type: 'scatter',
        data: {
            datasets: [{
                label: 'Weight',
                data: [{x: data.age, y: data.weight}],
                backgroundColor: 'blue'
            }, {
                label: 'Height',
                data: [{x: data.age, y: data.height}],
                backgroundColor: 'green'
            }]
        },
        options: {
            scales: {
                x: {
                    type: 'linear',
                    position: 'bottom',
                    title: {
                        display: true,
                        text: 'Age (months)'
                    }
                },
                y: {
                    title: {
                        display: true,
                        text: 'Measurement'
                    }
                }
            }
        }
    });
}