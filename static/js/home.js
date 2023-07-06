const BACKEND_URL = 'http://localhost:5000/api/v1'

async function search() {
    let searchQuery  = $('#search-bar').val();
    console.log(searchQuery);
    
    const URL = `${BACKEND_URL}/books/search?q=${searchQuery}`;
    const fetchOptions = {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
    }
    // Perform search and render results dynamically
    if (searchQuery) {
        await fetch(URL, fetchOptions)
            .then(response => response.json())
            .then(data => {
                // Render search results
                console.log(data)
                $('#search-results').html(data)
            })
            .catch(error => {
                console.error(error);
            });
    }
}

$(document).ready(function() {
    // Homepage render
    $('#home').ready(async function(){
        const URL = `${BACKEND_URL}/books`;
        const fetchOptions = {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
        }
        // Perform fetch and render results dynamically
        await fetch(URL, fetchOptions)
            .then(response => response.json()) 
            .then(data => {
                // Render fetch results
                console.log(data)
                $('#search-results').html(data)
            })
            .catch(error => {
                console.error(error);
            });
    })
    // Search bar functionality
    $('#search-button').on('click', async function(event) {
        event.preventDefault();
        await search()
    });
    $('#search-bar').on('keypress', async function(event) {
        if (event.which === 13)
        {
            event.preventDefault();
            await search();
        }
    });

    // Dropdown filter functionality
    $('#filter-dropdown').on('change', function() {
        var selectedFilter = $(this).val();
        // Apply selected filter and render results dynamically
        // ...
    });

    // Add Book button click event
    $('#addButton').on('click', function() {
        // Perform the API request to add a book
        // Use AJAX or fetch() to send a POST request to the backend
        // Handle the response and update the displaySection accordingly
        // Example: Display a success message
        $('#displaySection').text('Book added successfully.');
    });

    // Update Book button click event
    $('#updateButton').on('click', function() {
        // Perform the API request to update a book
        // Use AJAX or fetch() to send a PUT request to the backend
        // Handle the response and update the displaySection accordingly
        // Example: Display a success message
        $('#displaySection').text('Book updated successfully.');
    });

    // Delete Book button click event
    $('#deleteButton').on('click', function() {
        // Perform the API request to delete a book
        // Use AJAX or fetch() to send a DELETE request to the backend
        // Handle the response and update the displaySection accordingly
        // Example: Display a success message
        $('#displaySection').text('Book deleted successfully.');
    });

    
});