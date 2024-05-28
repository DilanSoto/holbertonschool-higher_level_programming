document.addEventListener('DOMContentLoaded', function() {
    const apiUrl = 'https://fourtonfish.com/hellosalut/?lang=fr';
  
    fetch(apiUrl)
    .then(response => response.json())
    .then(data => {
      const helloDiv = document.getElementById('hello');
      helloDiv.textContent = data.hello;
    })
    .catch(error => console.error('Error fetching data:', error));
  });
