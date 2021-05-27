<template>
  <div class="padding">
    <h2>Rising Cinema 에서 검색하신 "{{ keyword }}"의 결과입니다.</h2>
    <div v-show="movies[0]">
      <div class="mt-4 row">
        <div
          v-for="movie in movies"
          :key="movie.id"
          class="col-md-10 col-lg-9 col-xl-6 mb-r"
        >
          <div class="card card-body mb-3">
            <div class="media d-block d-md-flex">
              <img
                class="d-flex avatar-2 mb-md-0 mb-3 mx-auto"
                :src="movie.image"
              />
              <div class="media-body text-center text-md-left ml-md-3 ml-0">
                <p v-html="movie.title"></p>
                <p>{{ movie.subtitle }}</p>
                <p>{{ movie.director }}</p>
                <p>{{ movie.actor }}</p>
                <router-link
                  :to="{
                    name: 'MovieDetail',
                    params: { movie_title: movie.title, movie_id: movie.id },
                  }"
                >
                  <button>영화 상세</button>
                </router-link>
                <span class="badge"
                  ><i class="fas fa-user" aria-hidden="true">
                    {{ movie.userRating }}</i
                  ></span
                >
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div v-show="!movies[0]">{{ keyword }}에 대한 DB 검색 결과가 없습니다.</div>

    <div v-show="tmdbmovies[0]">
      <h2>TMDB 영화 "{{ keyword }}" 검색 결과입니다.</h2>
      <div class="mt-4 row">
        <div
          v-for="tmdbmovie in tmdbmovies"
          :key="tmdbmovie.id"
          class="col-md-10 col-lg-9 col-xl-6 mb-r"
        >
          <div class="card card-body mb-3">
            <div class="media d-block d-md-flex">
              <img
                class="d-flex avatar-2 mb-md-0 mb-3 mx-auto"
                :src="`https://image.tmdb.org/t/p/w200${tmdbmovie.poster_path}`"
              />
              <div class="media-body text-center text-md-left ml-md-3 ml-0">
                <h3 v-html="tmdbmovie.title"></h3>
                <p>{{ tmdbmovie.original_title }}</p>
                <p
                  style="
                    width: 300px;
                    white-space: nowrap;
                    overflow: hidden;
                    text-overflow: ellipsis;
                  "
                >
                  {{ tmdbmovie.overview }}
                </p>
                <p>개봉일 : {{ tmdbmovie.release_date }}</p>
                <p>투표수 : {{ tmdbmovie.vote_count }}</p>
                <p>평점 : {{ tmdbmovie.vote_average }}</p>
                <!-- <p>{{ tmdbmovie.title }}</p> -->
                <router-link
                  :to="{
                    name: 'MovieTMDBdetail',
                    params: {
                      tmdbmovie: tmdbmovie.title,
                      movie_id: tmdbmovie.id,
                    },
                  }"
                >
                  <button>영화 상세</button>
                </router-link>
                <span class="badge"
                  ><i class="fas fa-user" aria-hidden="true">
                    {{ tmdbmovie.vote_average }}</i
                  ></span
                >
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div v-show="!tmdbmovies[0]">
      {{ keyword }}에 대한 네이버 검색 결과가 없습니다.
    </div>

    <div v-show="navermovies[0]">
      <h2>네이버 영화 "{{ keyword }}" 검색 결과입니다.</h2>
      <div class="mt-4 row">
        <div
          v-for="navermovie in navermovies"
          :key="navermovie.id"
          class="col-md-10 col-lg-9 col-xl-6 mb-r"
        >
          <div class="card card-body mb-3">
            <div class="media d-block d-md-flex">
              <img
                v-if="navermovie.image"
                class="d-flex avatar-2 mb-md-0 mb-3 mx-auto"
                :src="navermovie.image"
              />
              <img
                v-else
                class="d-flex avatar-2 mb-md-0 mb-3 mx-auto"
                style="width: 114px; height: auto"
                src="@/assets/replace.jpg"
              />
              <div class="media-body text-center text-md-left ml-md-3 ml-0">
                <h3 v-html="navermovie.title"></h3>
                <p>{{ navermovie.subtitle }}</p>
                <p>{{ navermovie.director }}</p>
                <p>{{ navermovie.actor }}</p>
                <a :href="navermovie.link"><button>영화 상세</button></a>
                <span class="badge"
                  ><i class="fas fa-user" aria-hidden="true">
                    {{ navermovie.userRating }}</i
                  ></span
                >
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div v-show="!navermovies[0]">
      {{ keyword }}에 대한 네이버 검색 결과가 없습니다.
    </div>
  </div>
</template>

<script>
import axios from "axios";
const SERVER_URL = "http://127.0.0.1:8000";
const TMDB_API_URL = "https://api.themoviedb.org/3/search/movie";
const TMDB_API_KEY = "41243d6a8fbb557d88ebb0da26a7ae12";

export default {
  name: "MovieSearchResult",
  data() {
    return {
      keyword: "",
      naverlink: "",
      inputValue: "",
      tmdbmovies: [],
    };
  },
  props: {
    movies: [],
    navermovies: [],
  },
  methods: {
    getmovies() {
      this.keyword = this.$route.query.keyword;
      axios
        .get(SERVER_URL + "/movies/")
        .then((res) => {
          const resultMovies = res.data.filter((movie) =>
            movie.title.includes(this.keyword)
          );
          this.movies = resultMovies;
        })
        .catch((err) => console.error(err.response));
    },
    getnavermovies() {
      this.keyword = this.$route.query.keyword;
      axios({
        method: "GET",
        url: SERVER_URL + "/movies/search/",
        params: {
          query: this.keyword,
        },
      })
        .then((res) => {
          console.log(res);
          this.navermovies = res.data.items;
        })
        .catch((err) => console.error(err.response));
    },
    getTMDBmovies() {
      this.inputValue = this.$route.query.keyword;
      axios
        .get(TMDB_API_URL, {
          params: {
            api_key: TMDB_API_KEY,
            language: "ko",
            query: this.inputValue,
          },
        })
        .then((res) => {
          console.log("TMDB", res.data.results);
          this.tmdbmovies = res.data.results;
        })
        .catch((err) => {
          console.error(err);
        });
    },
  },
  mounted() {
    this.getmovies(), this.getnavermovies(), this.getTMDBmovies();
  },
};
</script>

<style>
.padding {
  padding: 30px 100px;
}
.padding * {
  margin: 15px 0px;
  border-radius: 5px;
}
</style>