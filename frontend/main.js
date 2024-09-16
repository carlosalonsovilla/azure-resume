const functionUrl = ""; // Replace with your actual function URL

async function updateCounter() {
    try {
        const response = await fetch(functionUrl);
        
        if (response.ok) {
            const data = await response.json(); // Parse the JSON response
            
            // Assuming your Azure function returns an object like { count: 123 }
            const counterValue = data.count; // Ensure 'count' is the correct field

            // Update the HTML element with id "counter"
            document.getElementById('counter').textContent = counterValue;
        } else {
            console.error('Failed to fetch counter:', response.status);
        }
    } catch (error) {
        console.error('Error:', error);
    }
}

// Call the function when the page loads
window.onload = updateCounter;
