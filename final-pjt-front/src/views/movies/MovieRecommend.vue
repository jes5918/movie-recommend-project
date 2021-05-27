<template>
  <div class="container">
    <h1>영화추천</h1>
    <hr />
    <br />
    <HottestMovie />
    <RatingNaver />
    <hr />
    <RatingTmdb />
    <hr />
    <GroupGenre @search-genre="searchGenre" />
    <div class="row d-flex justify-content-center">
      <figure
        v-for="movie in movies"
        :key="movie.id"
        class="snip1436 col-6 col-md-4 col-lg-2"
      >
        <img
          v-if="movie.image"
          :src="movie.image"
          class="img-thumbnail"
          style="height: 15rem; width: 11rem"
          :alt="movie.title"
        />
        <figcaption>
          <p>{{ movie.title }}</p>
          <p>{{ movie.subtitle }}</p>
          <router-link
            type="button"
            class="read-more"
            :to="{
              name: 'MovieDetail',
              params: { movie_title: movie.title, movie_id: movie.id },
            }"
          >
            영화 상세
          </router-link>
        </figcaption>
      </figure>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import _ from "lodash";

import GroupGenre from "@/components/movieRecommend/GroupGenre.vue";
import RatingNaver from "@/components/movieRecommend/RatingNaver.vue";
import RatingTmdb from "@/components/movieRecommend/RatingTmdb.vue";
import HottestMovie from "@/components/movieRecommend/HottestMovie.vue";

const SERVER_URL = "http://127.0.0.1:8000";

export default {
  name: "MovieRecommend",
  components: {
    GroupGenre,
    RatingNaver,
    RatingTmdb,
    HottestMovie,
  },
  data() {
    return {
      movies: [],
    };
  },
  methods: {
    searchGenre: function (genreKeyword) {
      axios
        .get(SERVER_URL + "/movies/")
        .then((res) => {
          const resultMovies = res.data.filter((movie) =>
            movie.genre.includes(genreKeyword)
          );
          const imgMovies = resultMovies.filter((movie) =>
            movie.image
          );
          this.movies = _.sampleSize(imgMovies, 6);
        })
        .catch((err) => console.error(err.response));
    },
    checkLoggedIn() {
      if (!this.$cookies.isKey("auth-token")) {
        alert("로그인 후 사용가능합니다");
        this.$router.push({ name: "Login" });
      }
    },
  },
  created() {
    this.checkLoggedIn();
  },
};
</script>

<style>
</style>