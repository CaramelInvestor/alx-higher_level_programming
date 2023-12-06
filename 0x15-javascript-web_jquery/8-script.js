const baseUrl = "https://swapi-api.alx-tools.com/api/films/?format=json";

$.get(baseUrl, function(data){
    const movies = data.results; // Access the 'results' property

    // Iterate through the array of movies
    $.each(movies, function(index, movie){
        // Append each movie title to the UL with ID list_movies
        $("ul#list_movies").append("<li>" + movie.title + "</li>");
    });
});
