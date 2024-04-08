<template>

    <form @submit.prevent="saveMovie" id="movieform">
        <h1>Add Movie</h1>
        <hr>

        <div v-if="message || errors.length > 0" :class="{'alert alert-success': message, 'alert alert-danger': errors.length > 0}" role="alert">
            <p v-if="message">{{ message }}</p>
            <ul v-if="errors">
                <li v-for="(error, index) in errors" :key="index">{{ error }}</li>
            </ul>
        </div>

        <div class="form-group mb-3">
            <label for="title" class="form-label">Title</label>
            <input type="text" name="title" class="form-control" />
        </div>

        <div class="form-group mb-3">
            <label for="description" class="form-label">Description</label>
            <textarea name="description" class="form-control" ></textarea>
        </div>

        <div class="form-group mb-3">
            <label for="poster" class="form-label">Poster</label>
            <input type="file" name="poster" class="form-control" accept=".jpg,.png.jpeg" />
        </div>

        <button type="submit" class="btn btn-primary">Submit</button>
    </form>

</template>

<script setup>

    import {ref, onMounted} from "vue";
    let csrf_token = ref("");
    let message = ref("");
    let errors = ref([]);


    function getCsrfToken() {
        fetch('/api/v1/csrf-token')
        .then((response) => response.json())
        .then((data) => {
            console.log(data);
            csrf_token.value = data.csrf_token;
        })
    }

    onMounted(() => {
    getCsrfToken();
    });


    function saveMovie(){

        let movieForm = document.querySelector("#movieform")
        let form_data = new FormData(movieForm);
        // let movieForm = document.getElementById("movieform");
        // let form_data
        // if (movieForm !== null && movieForm instanceof HTMLFormElement)
        // { 
        //     // Now you're sure that movieForm is not null and it's an HTMLFormElement
        //     form_data = new FormData(movieForm);
        // }
        // else 
        //     // Handle the case where movieForm is null or not an HTMLFormElement
        //     console.error("Form element not found or not of type HTMLFormElement");
        


        fetch("/api/v1/movies", {
                method: 'POST',
                body: form_data,
                headers: {
                    'X-CSRFToken': csrf_token.value
                }
        })
        .then(function (response) { 
            return response.json(); 
        }) 
        .then(function (data) {
            console.log(data);
            fetchResponse.value = data
            
            if(data.hasOwnProperty('errors')) {
                fetchResponseType.value = "danger"
            } else {
                fetchResponseType.value = "success"
            }
        })
        .catch(function (error) {
            console.log(error);
        });

    } 
        
</script>
    
<style>
body {
    padding-top: 5rem;
    background-color: rgb(198, 228, 250);
    height: 100vh;
}

.form-label{
    font-weight: bold;
}

form{
    max-width: 900px;
    background-color: white;
    padding: 50px;
    border-radius: 5px;
    margin:0 auto;
    margin-top: 50px;
}
</style>