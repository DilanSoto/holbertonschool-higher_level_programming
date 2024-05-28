const apiUrl = 'https://swapi-api.hbtn.io/api/people/5/?format=json';

fetch(apiUrl)
    .then(response => response.json())
    .then(data => {
        const characterDiv = document.getElementById('character');
        characterDiv.textContent = data.name;  // Asegurándose de que 'name' es la propiedad correcta
    })
    .catch(error => console.error('Error fetching data:', error));

