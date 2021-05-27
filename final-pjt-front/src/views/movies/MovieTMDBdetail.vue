<template>
  <div class="moviedetail">
    <section class="moviedetail-top">
      <h2 class="moviedetail-title">
        {{ movie_info.title }} - {{ movie.subtitle }}
      </h2>

      <div class="moviedetail-detail">
        <img
          :src="`https://image.tmdb.org/t/p/w500${movie_info.poster_path}`"
          :alt="movie.title"
          style="width: 250px; margin-right: 15px"
        />
        <div class="moviedetail-detail-rated" style="position: relative">
          <div class="detail-naver">
            <h4>네이버 평점(1~10): {{ movie.userRating }}</h4>
            <k-progress
              style="width: 670px"
              :percent="movie.userRating * 10"
              :show-text="false"
              :line-height="30"
              active
            ></k-progress>
          </div>
          <div class="detail-tmdb">
            <h4>TMDB 평점(1~10): {{ movie_info.vote_average }}</h4>
            <k-progress
              :percent="movie_info.vote_average * 10"
              status="error"
              :line-height="30"
              :show-text="false"
              active
            ></k-progress>
          </div>
        </div>
      </div>

      <div class="moviedetail-content">
        <h3>예고편</h3>
        <div class="embed-responsive embed-responsive-16by9">
          <iframe
            class="embed-responsive-item"
            :src="`https://www.youtube.com/embed/${video.id.videoId}`"
            allowfullscreen
          ></iframe>
        </div>

        <h3>주요 정보</h3>
        <div>
          <p><strong>감독</strong> : {{ movie.director }}</p>
          <p><strong>배우</strong> : {{ movie.actor }}</p>
          <p style="line-height: 130%">{{ movie_info.overview }}</p>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import axios from "axios";
const SERVER_URL = "http://127.0.0.1:8000";
const API_KEY = "AIzaSyCXIrZdWD7A8aaMCRE-WMaRv0Pv6-qnpKo";
const API_URL = "https://www.googleapis.com/youtube/v3/search";
const TMDB_API_URL = "https://api.themoviedb.org/3/search/multi";
const TMDB_API_KEY = "41243d6a8fbb557d88ebb0da26a7ae12";

export default {
  name: "MovieTMDBdetail",
  data() {
    return {
      movie: {},
      video: [],
      movie_info: [],
      inputValue: "",
    };
  },
  methods: {
    movieInfo() {
      this.inputValue = this.$route.params.tmdbmovie;
      console.log(this.inputValue);
      axios
        .get(TMDB_API_URL, {
          params: {
            api_key: TMDB_API_KEY,
            language: "ko-KR",
            query: this.inputValue,
          },
        })
        .then((res) => {
          console.log("TMDB", res.data);
          const ratingResult = res.data.results.filter(
            (movie) => movie.poster_path
          );
          this.movie_info = ratingResult[0];
          console.log("TMDB무비에요", this.movie_info);
        })
        .catch((err) => {
          console.error("@@@@", err);
        });
    },
    movieDetail() {
      this.inputValue = this.$route.params.tmdbmovie;
      axios({
        method: "GET",
        url: SERVER_URL + "/movies/search/",
        params: {
          query: this.inputValue,
        },
      })
        .then((res) => {
          const temp = res.data.items;
          this.movie = temp[0];
          // console.log(this.movie);
        })
        .catch((err) => console.error(err));
    },
    inputVideos() {
      const movie_title = this.$route.params.tmdbmovie;
      this.inputValue = movie_title + "예고편";
      axios
        .get(API_URL, {
          params: {
            key: API_KEY,
            part: "snippet",
            type: "video",
            q: this.inputValue,
          },
        })
        .then((res) => {
          res.data.items.forEach((item) => {
            const parser = new DOMParser();
            const doc = parser.parseFromString(item.snippet.title, "text/html");
            item.snippet.title = doc.body.innerText;
          });
          this.video = res.data.items[0];
          console.log("YOUTUBE", this.video);
        })
        .catch((err) => {
          console.error("유튜브 에러남", err);
        });
    },
  },
  created() {
    this.movieInfo();
    this.movieDetail();
    this.inputVideos();
  },
};
</script>

<style scoped>
img {
  border-radius: 5px;
}

.detail-naver,
.detail-tmdb {
  margin-bottom: 30px;
}
.detail-naver *,
.detail-tmdb * {
  margin-bottom: 20px;
}

h4 {
  font-weight: 700;
}
strong {
  font-weight: 700;
}
</style>
