// Add event listener to the 'compare-button' element to trigger the weather comparison function
document.getElementById('compare-button').addEventListener('click', compareWeather);

// Function to compare weather forecasts for two cities
async function compareWeather() {
    // Retrieve input values for city names, states, and units
    const city1 = document.getElementById('city1').value;
    const state1 = document.getElementById('state1').value;
    const city2 = document.getElementById('city2').value;
    const state2 = document.getElementById('state2').value;
    const units = document.getElementById('units').value;
    const errorMessage = document.getElementById('error-message');
    errorMessage.textContent = ''; // Clear any previous error message

    // Validate input: ensure both city names are provided
    if (!city1 || !city2) {
        errorMessage.textContent = 'Both city names are required!';
        return;
    }

    try {
        // Fetch coordinates for the two cities
        const [lat1, lon1] = await getCoordinates(city1, state1);
        const [lat2, lon2] = await getCoordinates(city2, state2);

        // Fetch weather forecasts for the two cities
        const forecast1 = await fetchWeather(lat1, lon1, units);
        const forecast2 = await fetchWeather(lat2, lon2, units);

        // Clear previous city titles and forecasts
        const cityContainer = document.getElementById('city-title-container');
        cityContainer.innerHTML = '';
        const container = document.getElementById('forecast-container');
        container.innerHTML = '';

        // Display forecasts for both cities
        displayForecast(forecast1, city1);
        displayForecast(forecast2, city2);
    } catch (error) {
        // Handle errors by displaying an error message
        console.error(error);
        errorMessage.textContent = 'Error fetching weather data. Please check the city names and try again.';
    }
}

// Function to fetch coordinates (latitude and longitude) for a given city and state
async function getCoordinates(city, state) {
    const apiKey = 'API_KEY_HERE';
    const response = await fetch(`https://api.openweathermap.org/geo/1.0/direct?q=${city},${state},US&limit=1&appid=${apiKey}`);
    const data = await response.json();

    // Check if location data is available, throw error if not found
    if (data.length === 0) {
        throw new Error('Location not found');
    }

    return [data[0].lat, data[0].lon]; // Return latitude and longitude
}

// Function to fetch weather data for a given latitude, longitude, and units
async function fetchWeather(lat, lon, units) {
    const apiKey = 'API_KEY_HERE';
    const response = await fetch(`https://api.openweathermap.org/data/3.0/onecall?lat=${lat}&lon=${lon}&units=${units}&exclude=minutely,hourly,alerts&appid=${apiKey}`);
    
    // Check if weather data is fetched successfully, throw error if not found
    if (!response.ok) {
        throw new Error('Weather data not found');
    }

    return response.json(); // Return weather forecast data
}

// Function to display weather forecast in a table for a given city
function displayForecast(forecast, cityName) {
    const cityHeader = document.createElement('h2');
    const cityContainer = document.getElementById('city-title-container');
    const container = document.getElementById('forecast-container');

    // Set city header text and append to city title container
    cityHeader.textContent = `${cityName}:`;
    cityContainer.appendChild(cityHeader);

    // Create table element for forecast data
    const table = document.createElement('table');
    const headerRow = document.createElement('tr');

    // Set table header row with required forecast details
    headerRow.innerHTML = `
        <th>Day</th>
        <th>High Temp</th>
        <th>Low Temp</th>
        <th>Outlook</th>
        <th>Rainfall %</th>
    `;
    table.appendChild(headerRow);

    // Populate table rows with forecast data for each day
    forecast.daily.slice(0, 5).forEach(day => {
        const row = document.createElement('tr');
        const iconCode = day.weather[0].icon;
        const iconUrl = `photos/${iconCode}.png`;
        const rainPercentage = day.pop * 100; // Convert probability of precipitation to percentage

        // Populate row with forecast details
        row.innerHTML = `
            <td>${new Date(day.dt * 1000).toLocaleDateString('en-US', { weekday: 'long' })}</td>
            <td>${day.temp.max}°</td>
            <td>${day.temp.min}°</td>
            <td><img src="${iconUrl}" alt="${day.weather[0].description}"></td>
            <td>${rainPercentage.toFixed(2)}%</td>
        `;
        table.appendChild(row);
    });

    // Append forecast table to forecast container
    container.appendChild(table);
}