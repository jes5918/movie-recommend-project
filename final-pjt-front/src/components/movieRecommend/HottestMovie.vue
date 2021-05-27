<template>
  <section class="home-boxoffice">
    <h2>유저 베스트</h2>
    <div class="d-block w-100">
      <div class="fcknflexbox">
        <figure
          v-for="movie in movies"
          :key="movie.id"
          style="margin: 5px 10px"
        >
          <router-link
            type="button"
            :to="{
              name: 'MovieDetail',
              params: { movie_title: movie.title, movie_id: movie.id },
            }"
            ><img v-if="movie.image" :src="movie.image" :alt="movie.title" />
            <img
              v-if="!movie.image"
              src="@/assets/replace.jpg"
              :alt="movie.title"
          /></router-link>
          <figcaption>
            <p>{{ movie.title }}</p>
            <p>{{ movie.subtitle }}</p>
          </figcaption>
        </figure>
      </div>
    </div>
  </section>
</template>

<script>
import axios from "axios";

const SERVER_URL = "http://127.0.0.1:8000";

export default {
  name: "HottestMovie",
  data: function () {
    return {
      movies: [],
      total: {},
    };
  },
  methods: {
    ratingSort: function () {
      let i = 1;
      for (i = 1; i < 127; ++i) {
        axios
          .get(SERVER_URL + "/movies/" + `${i}` + "/review/")
          .then((res) => {
            if (res.data.length > 0 && this.movies.length < 5) {
              this.movies.push(res.data[0].movie);
            }
          })
          .catch(() => {});
      }
    },
    clickevent(title, id) {
      this.$router.push({
        name: "MovieDetail",
        params: { movie_title: title, movie_id: id },
      });
    },
  },
  mounted() {
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