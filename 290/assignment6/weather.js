document.getElementById('compare-button').addEventListener('click', function() {
    const city1 = document.getElementById('city1').value;
    const state1 = document.getElementById('state1').value;
    const city2 = document.getElementById('city2').value;
    const state2 = document.getElementById('state2').value;
    const units = document.getElementById('units').value;

    if (!city1) {
        displayError('City 1 is missing');
    } else if (!city2) {
        displayError('City 2 is missing');
    } else {
        fetchWeather(city1, state1, units, 'city1-forecast');
        fetchWeather(city2, state2, units, 'city2-forecast');
    }
});

function displayError(message) {
    document.getElementById('error-message').innerText = message;
    document.getElementById('city1-forecast').innerHTML = '';
    document.getElementById('city2-forecast').innerHTML = '';
}

function fetchWeather(city, state, units, elementId) {
    const apiKey = 'e11c3f909df1144d4a10ff69200375e2';
    const url = `https://api.openweathermap.org/data/2.5/forecast?q=${city},${state},us&units=${units}&appid=${apiKey}`;

    fetch(url)
        .then(response => {
            if (!response.ok) {
                throw new Error('City not found');
            }
            return response.json();
        })
        .then(data => {
            displayWeather(data, elementId);
        })
        .catch(error => {
            document.getElementById(elementId).innerHTML = `<p class="error-message">${error.message}</p>`;
        });
}

function displayWeather(data, elementId) {
    const forecasts = data.list.filter(item => item.dt_txt.endsWith('12:00:00'));
    const table = `
        <table>
            <thead>
                <tr>
                    <th>Day</th>
                    <th>High</th>
                    <th>Low</th>
                    <th>Outlook</th>
                </tr>
            </thead>
            <tbody>
                ${forecasts.map(forecast => `
                    <tr>
                        <td>${new Date(forecast.dt_txt).toLocaleDateString('en-US', { weekday: 'long' })}</td>
                        <td>${forecast.main.temp_max}°</td>
                        <td>${forecast.main.temp_min}°</td>
                        <td><img src="images/${getOutlookImage(forecast.weather[0].main)}" alt="${forecast.weather[0].main}"></td>
                    </tr>
                `).join('')}
            </tbody>
        </table>
    `;
    document.getElementById(elementId).innerHTML = table;
}

function getOutlookImage(outlook) {
    switch (outlook.toLowerCase()) {
        case 'clear':
            return 'clear.png';
        case 'clouds':
            return 'cloudy.png';
        case 'rain':
            return 'rain.png';
        // Add more cases as necessary
        default:
            return 'default.png';
    }
}
