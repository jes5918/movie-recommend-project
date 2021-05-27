<template>
  <main class="main-home">
    <RatingTmdb />
    <hr />
    <RatingNaver />
    <hr />
    <HottestMovie />
    <GroupGenre @search-genre="searchGenre" />
    <div class="fckncenter" style="margin-bottom: 40px">
      <figure v-for="movie in movies" :key="movie.id" style="margin: 0px 10px">
        <img
          v-if="movie.image"
          :src="movie.image"
          @click="clickevent(movie.title, movie.id)"
          :alt="movie.title"
          style="width: 213px"
        />
        <figcaption>
          <p style="font-weight: 700">{{ movie.title }}</p>
          <!-- <router-link
            type="button"
            class="read-more"
            :to="{
              name: 'MovieDetail',
              params: { movie_title: movie.title, movie_id: movie.id },
            }"
          >
            영화 상세
          </router-link> -->
        </figcaption>
      </figure>
    </div>
  </main>
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
          const imgMovies = resultMovies.filter((movie) => movie.image);
          this.movies = _.sampleSize(imgMovies, 5);
        })
        .catch((err) => console.error(err.response));
    },
    checkLoggedIn() {
      if (!this.$cookies.isKey("auth-token")) {
        alert("로그인 후 사용가능합니다");
        this.$router.push({ name: "Login" });
      }
    },
    clickevent(title, id) {
      this.$router.push({
        name: "MovieDetail",
        params: { movie_title: title, movie_id: id },
      });
    },
  },
  created() {
    this.checkLoggedIn();
  },
};
</script>

<style scoped>
.fckncenter {
  flex-direction: row;
  margin-bottom: 20px;
}
img {
  width: 213px;
  border-radius: 5px;
}
</style>