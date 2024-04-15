<script setup>

    import { ref, onMounted } from "vue";
    let movies = ref([]);

    function fetchMovies(){
        fetch("/api/v1/movies", {
        method: 'GET',
        }) 
        .then(response => {
            if(response.ok){
                return response.json()
            }else{
                return Promise.reject('Something was wrong with fetch request!')}
            })
            .then(data => {
                console.log(data);
                movies.value = data["movies"]
            })
            .catch(error => {
                console.log(error);
            })
    }

    onMounted(() => {
        fetchMovies()
    })

</script>

<template>

    <div class="page-header">
        <h1 class = movie-heading>Movies</h1>
    </div>

    <div class="grid-container">

        <div class="movie-card" v-for="movie in movies">
            <img :src="movie.poster" alt="Movie Poster">
            <div class = "card-body">
                <h2>{{ movie.title }}</h2>
                <p>{{ movie.description }}</p>
            </div>
        </div>

    </div>
</template>

<style>
.grid-container {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-around;
    background-color: transparent;
}

.movie-card {
    max-width: 550px;
    height: 270px;
    width: 100%;
    overflow: hidden;
    display: grid;
    grid-template-columns: 1fr 2fr;
    margin: 20px;
    border-radius: 5px;
    box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.2);
}

.movie-card img {
    width: 100%;
    height: 270px;
    object-fit: contain;
}

.card-body {
    padding: 15px;
}

.movie-card h2 {
    font-size: 1.5rem;
    margin: 0;
}

.movie-card p {
    font-size: 1.2rem;
    margin: 10px 0 0 0;
}

.movie-heading{
    margin-left: 60px;
}
</style>




