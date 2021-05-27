<template>
  <section class="home-stockoffice">
    <h2>TMDB 베스트</h2>
    <div
      id="carouselExampleControls2"
      class="carousel slide home-boxoffice-carousel"
      data-ride="carousel"
    >
      <div class="carousel-inner">
        <div class="carousel-item active">
          <div class="d-block w-100">
            <div class="fcknflexbox">
              <div v-for="movie in movies" :key="movie.id">
                <router-link
                  v-if="movies[0] == movie"
                  type="button"
                  class="read-more"
                  :to="{
                    name: 'MovieTMDBdetail',
                    params: { tmdbmovie: movie.title, movie_id: movie.id },
                  }"
                  ><img
                    v-if="movie.poster_path && movies[0] == movie"
                    :src="`https://image.tmdb.org/t/p/w500${movie.poster_path}`"
                    :alt="movie.title"
                /></router-link>

                <p v-if="movies[0] == movie">1. {{ movie.title }}</p>
                <p v-if="movies[0] == movie"></p>
              </div>
              <div v-for="movie in movies" :key="movie.id">
                <router-link
                  v-if="movies[1] == movie"
                  type="button"
                  class="read-more"
                  :to="{
                    name: 'MovieTMDBdetail',
                    params: { tmdbmovie: movie.title, movie_id: movie.id },
                  }"
                  ><img
                    v-if="movie.poster_path && movies[1] == movie"
                    :src="`https://image.tmdb.org/t/p/w500${movie.poster_path}`"
                    :alt="movie.title"
                /></router-link>

                <p v-if="movies[1] == movie">2. {{ movie.title }}</p>
                <p v-if="movies[1] == movie"></p>
              </div>
              <div v-for="movie in movies" :key="movie.id">
                <router-link
                  v-if="movies[2] == movie"
                  type="button"
                  class="read-more"
                  :to="{
                    name: 'MovieTMDBdetail',
                    params: { tmdbmovie: movie.title, movie_id: movie.id },
                  }"
                  ><img
                    v-if="movie.poster_path && movies[2] == movie"
                    :src="`https://image.tmdb.org/t/p/w500${movie.poster_path}`"
                    :alt="movie.title"
                /></router-link>

                <p v-if="movies[2] == movie">3. {{ movie.title }}</p>
                <p v-if="movies[2] == movie"></p>
              </div>
              <div v-for="movie in movies" :key="movie.id">
                <router-link
                  v-if="movies[3] == movie"
                  type="button"
                  class="read-more"
                  :to="{
                    name: 'MovieTMDBdetail',
                    params: { tmdbmovie: movie.title, movie_id: movie.id },
                  }"
                  ><img
                    v-if="movie.poster_path && movies[3] == movie"
                    :src="`https://image.tmdb.org/t/p/w500${movie.poster_path}`"
                    :alt="movie.title"
                /></router-link>

                <p v-if="movies[3] == movie">4. {{ movie.title }}</p>
                <p v-if="movies[3] == movie"></p>
              </div>
              <div v-for="movie in movies" :key="movie.id">
                <router-link
                  v-if="movies[4] == movie"
                  type="button"
                  class="read-more"
                  :to="{
                    name: 'MovieTMDBdetail',
                    params: { tmdbmovie: movie.title, movie_id: movie.id },
                  }"
                  ><img
                    v-if="movie.poster_path && movies[4] == movie"
                    :src="`https://image.tmdb.org/t/p/w500${movie.poster_path}`"
                    :alt="movie.title"
                /></router-link>

                <p v-if="movies[4] == movie">5. {{ movie.title }}</p>
                <p v-if="movies[4] == movie"></p>
              </div>
            </div>
          </div>
        </div>

        <div class="carousel-item">
          <div class="d-block w-100">
            <div class="fcknflexbox">
              <div v-for="movie in movies" :key="movie.id">
                <router-link
                  v-if="movies[5] == movie"
                  type="button"
                  class="read-more"
                  :to="{
                    name: 'MovieTMDBdetail',
                    params: { tmdbmovie: movie.title, movie_id: movie.id },
                  }"
                  ><img
                    v-if="movie.poster_path && movies[5] == movie"
                    :src="`https://image.tmdb.org/t/p/w500${movie.poster_path}`"
                    :alt="movie.title"
                /></router-link>

                <p v-if="movies[5] == movie">6. {{ movie.title }}</p>
                <p v-if="movies[5] == movie"></p>
              </div>
              <div v-for="movie in movies" :key="movie.id">
                <router-link
                  v-if="movies[6] == movie"
                  type="button"
                  class="read-more"
                  :to="{
                    name: 'MovieTMDBdetail',
                    params: { tmdbmovie: movie.title, movie_id: movie.id },
                  }"
                  ><img
                    v-if="movie.poster_path && movies[6] == movie"
                    :src="`https://image.tmdb.org/t/p/w500${movie.poster_path}`"
                    :alt="movie.title"
                /></router-link>

                <p v-if="movies[6] == movie">7. {{ movie.title }}</p>
                <p v-if="movies[6] == movie"></p>
              </div>
              <div v-for="movie in movies" :key="movie.id">
                <router-link
                  v-if="movies[7] == movie"
                  type="button"
                  class="read-more"
                  :to="{
                    name: 'MovieTMDBdetail',
                    params: { tmdbmovie: movie.title, movie_id: movie.id },
                  }"
                >
                  <img
                    v-if="movie.poster_path && movies[7] == movie"
                    :src="`https://image.tmdb.org/t/p/w500${movie.poster_path}`"
                    :alt="movie.title"
                  />
                </router-link>
                <p v-if="movies[7] == movie">8. {{ movie.title }}</p>
                <p v-if="movies[7] == movie"></p>
              </div>
              <div v-for="movie in movies" :key="movie.id">
                <router-link
                  v-if="movies[8] == movie"
                  type="button"
                  class="read-more"
                  :to="{
                    name: 'MovieTMDBdetail',
                    params: { tmdbmovie: movie.title, movie_id: movie.id },
                  }"
                >
                  <img
                    v-if="movie.poster_path && movies[8] == movie"
                    :src="`https://image.tmdb.org/t/p/w500${movie.poster_path}`"
                    :alt="movie.title"
                  />
                </router-link>

                <p v-if="movies[8] == movie">9. {{ movie.title }}</p>
                <p v-if="movies[8] == movie"></p>
              </div>
              <div v-for="movie in movies" :key="movie.id">
                <router-link
                  v-if="movies[9] == movie"
                  type="button"
                  class="read-more"
                  :to="{
                    name: 'MovieTMDBdetail',
                    params: { tmdbmovie: movie.title, movie_id: movie.id },
                  }"
                >
                  <img
                    v-if="movie.poster_path && movies[9] == movie"
                    :src="`https://image.tmdb.org/t/p/w500${movie.poster_path}`"
                    :alt="movie.title"
                  />
                </router-link>
                <p v-if="movies[9] == movie">10. {{ movie.title }}</p>
                <p v-if="movies[9] == movie"></p>
              </div>
            </div>
          </div>
        </div>
      </div>
      <a
        class="carousel-control-prev"
        href="#carouselExampleControls2"
        role="button"
        data-slide="prev"
      >
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="sr-only">Previous</span>
      </a>
      <a
        class="carousel-control-next"
        href="#carouselExampleControls2"
        role="button"
        data-slide="next"
      >
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="sr-only">Next</span>
      </a>
    </div>
  </section>
</template>

<script>
import axios from "axios";
import _ from "lodash";

const TMDB_API_URL = "https://api.themoviedb.org/3/movie/top_rated";
const TMDB_API_KEY = "41243d6a8fbb557d88ebb0da26a7ae12";

export default {
  name: "RatingTmdb",
  data: function () {
    return {
      movies: [],
    };
  },
  methods: {
    ratingSort() {
      axios
        .get(TMDB_API_URL, {
          params: {
            api_key: TMDB_API_KEY,
            language: "ko-KR",
            region: "kr",
            page: "1",
          },
        })
        .then((res) => {
          const ratingResult = res.data.results.filter(
            (movie) => movie.vote_average > 6 && movie.title
          );
          // const imgResult = ratingResult.filter(movie => movie.poster_path)
          this.movies = _.sampleSize(ratingResult, 18);
        })
        .catch((err) => {
          console.error(err.response);
        })
        .catch((err) => {
          console.error(err.response);
        });
    },
  },
  created() {
    this.ratingSort();
  },
};
</script>

<style scoped>
img {
  width: 213px;
  border-radius: 5px;
}

.fcknflexbox {
  padding: 0px 100px;
}

.carousel-control-prev,
.carousel-control-next {
  width: 110px;
}
p {
  font-weight: bold;
}
</style>
