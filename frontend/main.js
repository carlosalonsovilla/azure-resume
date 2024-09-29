import config from './config.js';

async function updateCounter() {
  try {
    const response = await fetch(config.functionUrl);
    if (response.ok) {
      const data = await response.json();
      const counterValue = data.count;
      document.getElementById('counter').textContent = counterValue;
    } else {
      console.error('Failed to fetch counter:', response.status);
    }
  } catch (error) {
    console.error('Error:', error);
  }
}

window.onload = updateCounter;
