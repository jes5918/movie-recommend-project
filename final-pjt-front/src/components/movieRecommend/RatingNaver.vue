<template>
  <section class="home-boxoffice">
    <h2>네이버 베스트</h2>

    <div
      id="carouselExampleControls"
      class="carousel slide home-boxoffice-carousel"
      data-ride="carousel"
    >
      <div class="carousel-inner">
        <div class="carousel-item active">
          <div class="d-block w-100">
            <div class="fcknflexbox">
              <div v-for="movie in movies" :key="movie.id">
                <router-link
                  type="button"
                  v-if="movies[0] == movie"
                  :to="{
                    name: 'MovieDetail',
                    params: { movie_title: movie.title, movie_id: movie.id },
                  }"
                >
                  <img
                    v-if="movie.image && movies[0] == movie"
                    :src="movie.image"
                    :alt="movie.title"
                  />
                  <img
                    v-if="!movie.image && movies[1]"
                    src="@/assets/replace.jpg"
                    :alt="movie.title"
                  />
                </router-link>

                <p v-if="movies[0] == movie">1. {{ movie.title }}</p>
                <p v-if="movies[0] == movie"></p>
              </div>
              <div v-for="movie in movies" :key="movie.id">
                <router-link
                  type="button"
                  v-if="movies[1] == movie"
                  :to="{
                    name: 'MovieDetail',
                    params: { movie_title: movie.title, movie_id: movie.id },
                  }"
                >
                  <img
                    v-if="movie.image && movies[1] == movie"
                    :src="movie.image"
                    :alt="movie.title"
                  />
                  <img
                    v-if="!movie.image && movies[1]"
                    src="@/assets/replace.jpg"
                    :alt="movie.title"
                  />
                </router-link>

                <p v-if="movies[1] == movie">2. {{ movie.title }}</p>
                <p v-if="movies[1] == movie"></p>
              </div>
              <div v-for="movie in movies" :key="movie.id">
                <router-link
                  type="button"
                  v-if="movies[2] == movie"
                  :to="{
                    name: 'MovieDetail',
                    params: { movie_title: movie.title, movie_id: movie.id },
                  }"
                >
                  <img
                    v-if="movie.image && movies[2] == movie"
                    :src="movie.image"
                    :alt="movie.title"
                  />
                  <img
                    v-if="!movie.image && movies[2]"
                    src="@/assets/replace.jpg"
                    :alt="movie.title"
                  />
                </router-link>

                <p v-if="movies[2] == movie">3. {{ movie.title }}</p>
                <p v-if="movies[2] == movie"></p>
              </div>
              <div v-for="movie in movies" :key="movie.id">
                <router-link
                  type="button"
                  v-if="movies[3] == movie"
                  :to="{
                    name: 'MovieDetail',
                    params: { movie_title: movie.title, movie_id: movie.id },
                  }"
                >
                  <img
                    v-if="movie.image && movies[3] == movie"
                    :src="movie.image"
                    :alt="movie.title"
                  />
                  <img
                    v-if="!movie.image && movies[3]"
                    src="@/assets/replace.jpg"
                    :alt="movie.title"
                  />
                </router-link>

                <p v-if="movies[3] == movie">4. {{ movie.title }}</p>
                <p v-if="movies[3] == movie"></p>
              </div>
              <div v-for="movie in movies" :key="movie.id">
                <router-link
                  type="button"
                  v-if="movies[4] == movie"
                  :to="{
                    name: 'MovieDetail',
                    params: { movie_title: movie.title, movie_id: movie.id },
                  }"
                >
                  <img
                    v-if="movie.image && movies[4] == movie"
                    :src="movie.image"
                    :alt="movie.title"
                  />
                  <img
                    v-if="!movie.image && movies[4]"
                    src="@/assets/replace.jpg"
                    :alt="movie.title"
                  />
                </router-link>

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
                  type="button"
                  v-if="movies[5] == movie"
                  :to="{
                    name: 'MovieDetail',
                    params: { movie_title: movie.title, movie_id: movie.id },
                  }"
                >
                  <img
                    v-if="movie.image && movies[5] == movie"
                    :src="movie.image"
                    :alt="movie.title"
                  />
                  <img
                    v-if="!movie.image && movies[5]"
                    src="@/assets/replace.jpg"
                    :alt="movie.title"
                  />
                </router-link>

                <p v-if="movies[5] == movie">6. {{ movie.title }}</p>
                <p v-if="movies[5] == movie"></p>
              </div>
              <div v-for="movie in movies" :key="movie.id">
                <router-link
                  type="button"
                  v-if="movies[6] == movie"
                  :to="{
                    name: 'MovieDetail',
                    params: { movie_title: movie.title, movie_id: movie.id },
                  }"
                >
                  <img
                    v-if="movie.image && movies[6] == movie"
                    :src="movie.image"
                    :alt="movie.title"
                  />
                  <img
                    v-if="!movie.image && movies[6]"
                    src="@/assets/replace.jpg"
                    :alt="movie.title"
                  />
                </router-link>

                <p v-if="movies[6] == movie">7. {{ movie.title }}</p>
                <p v-if="movies[6] == movie"></p>
              </div>
              <div v-for="movie in movies" :key="movie.id">
                <router-link
                  type="button"
                  v-if="movies[7] == movie"
                  :to="{
                    name: 'MovieDetail',
                    params: { movie_title: movie.title, movie_id: movie.id },
                  }"
                >
                  <img
                    v-if="movie.image && movies[7] == movie"
                    :src="movie.image"
                    :alt="movie.title"
                  />
                  <img
                    v-if="!movie.image && movies[7]"
                    src="@/assets/replace.jpg"
                    :alt="movie.title"
                  />
                </router-link>

                <p v-if="movies[7] == movie">8. {{ movie.title }}</p>
                <p v-if="movies[7] == movie"></p>
              </div>
              <div v-for="movie in movies" :key="movie.id">
                <router-link
                  type="button"
                  v-if="movies[8] == movie"
                  :to="{
                    name: 'MovieDetail',
                    params: { movie_title: movie.title, movie_id: movie.id },
                  }"
                >
                  <img
                    v-if="movie.image && movies[8] == movie"
                    :src="movie.image"
                    :alt="movie.title"
                  />
                  <img
                    v-if="!movie.image && movies[8]"
                    src="@/assets/replace.jpg"
                    :alt="movie.title"
                  />
                </router-link>

                <p v-if="movies[8] == movie">9. {{ movie.title }}</p>
                <p v-if="movies[8] == movie"></p>
              </div>
              <div v-for="movie in movies" :key="movie.id">
                <router-link
                  type="button"
                  v-if="movies[9] == movie"
                  :to="{
                    name: 'MovieDetail',
                    params: { movie_title: movie.title, movie_id: movie.id },
                  }"
                >
                  <img
                    v-if="movie.image && movies[9] == movie"
                    :src="movie.image"
                    :alt="movie.title"
                  />
                  <img
                    v-if="!movie.image && movies[9]"
                    src="@/assets/replace.jpg"
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
        href="#carouselExampleControls"
        role="button"
        data-slide="prev"
      >
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="sr-only">Previous</span>
      </a>
      <a
        class="carousel-control-next"
        href="#carouselExampleControls"
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

const SERVER_URL = "http://127.0.0.1:8000";

export default {
  name: "RatingNaver",
  data: function () {
    return {
      movies: [],
    };
  },
  methods: {
    ratingSort: function () {
      axios
        .get(SERVER_URL + "/movies/")
        .then((res) => {
          const ratingResult = res.data.filter((movie) => movie.userRating > 8);
          const imgResult = ratingResult.filter((movie) => movie.image);
          this.movies = _.sampleSize(imgResult, 18);
        })
        .catch((err) => console.error(err.response));
    },
    clickevent(title, id) {
      this.$router.push({
        name: "MovieDetail",
        params: { movie_title: title, movie_id: id },
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