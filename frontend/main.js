const functionUrl = ""; // Replace with your actual function URL

async function updateCounter() {
    try {
        const response = await fetch(functionUrl);
        
        if (response.ok) {
            const data = await response.json(); // Parse the JSON response
            
            const counterValue = data.count;

            // Update the HTML element with id "counter"
            document.getElementById('counter').textContent = counterValue;
        } else {
            console.error('Failed to fetch counter:', response.status);
        }
    } catch (error) {
        console.error('Error:', error);
    }
}


window.onload = updateCounter;
