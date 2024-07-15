// main.js

document.addEventListener('DOMContentLoaded', function() {
    console.log('JavaScript is loaded and DOM is ready.');

    // Example: Change text content of an element
    const exampleElement = document.getElementById('example');
    if (exampleElement) {
        exampleElement.textContent = 'Hello, Django!';
    }

    // Example: Add an event listener to a button
    const exampleButton = document.getElementById('example-button');
    if (exampleButton) {
        exampleButton.addEventListener('click', function() {
            alert('Button clicked!');
        });
    }

    // Example: Fetch data from the server
    const fetchDataButton = document.getElementById('fetch-data-button');
    if (fetchDataButton) {
        fetchDataButton.addEventListener('click', function() {
            fetch('/api/data/')
                .then(response => response.json())
                .then(data => {
                    console.log(data);
                    // Update the DOM with the fetched data
                    const dataContainer = document.getElementById('data-container');
                    if (dataContainer) {
                        dataContainer.textContent = JSON.stringify(data);
                    }
                })
                .catch(error => console.error('Error fetching data:', error));
        });
    }
});
