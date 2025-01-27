document.addEventListener('DOMContentLoaded', function() {
    const searchButton = document.querySelector('.boton-buscar');
    const searchInput = document.querySelector('.busqueda');

    searchButton.addEventListener('click', function() {
        const query = searchInput.value;
        if (query) {
            // Implement the search functionality here
            console.log('Searching for:', query);
            // For example, you could redirect to a search results page
            window.location.href = `/search?query=${encodeURIComponent(query)}`;
        }
    });
});
