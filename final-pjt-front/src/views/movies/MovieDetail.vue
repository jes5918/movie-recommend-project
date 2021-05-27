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
          <div class="detail-tmdb">
            <h4>유저 평점(1~5): {{ rank_avg }}</h4>
            <div class="col-lg-11">
              <i class="fas fa-star text-warning"></i>1
              <k-progress
                class="d-inline"
                style="width: 70vh"
                :percent="rank_info[1] * 10"
                status="error"
                :show-text="false"
                :line-height="18"
                active
              ></k-progress>
              <br />
              <i class="fas fa-star text-warning"></i>2
              <k-progress
                class="d-inline"
                :percent="rank_info[2] * 10"
                status="error"
                :show-text="false"
                :line-height="15"
                active
              ></k-progress>
              <i class="fas fa-star text-warning"></i>3
              <k-progress
                class="d-inline"
                :percent="rank_info[3] * 15"
                status="error"
                :show-text="false"
                :line-height="15"
                active
              ></k-progress>
              <i class="fas fa-star text-warning"></i>4
              <k-progress
                class="d-inline"
                :percent="rank_info[4] * 15"
                status="error"
                :show-text="false"
                :line-height="15"
                active
              ></k-progress>
              <i class="fas fa-star text-warning"></i>5
              <k-progress
                class="d-inline"
                :percent="rank_info[5] * 10"
                status="error"
                :show-text="false"
                :line-height="15"
                active
              ></k-progress>
            </div>
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
          <p>감독 : {{ movie.director }}</p>
          <p>배우 : {{ movie.actor }}</p>
          <p>{{ movie_info.overview }}</p>
        </div>
      </div>
    </section>

    <div style="width: 980px">
      <ReviewList :movie_id="movie.id" @get-rank="rankInfo" />
    </div>
  </div>
</template>

<script>
import axios from "axios";
import ReviewList from "@/components/movieDetail/ReviewList.vue";

const SERVER_URL = "http://127.0.0.1:8000";
const API_KEY = "AIzaSyCXIrZdWD7A8aaMCRE-WMaRv0Pv6-qnpKo";
const API_URL = "https://www.googleapis.com/youtube/v3/search";
const TMDB_API_URL = "https://api.themoviedb.org/3/search/movie";
const TMDB_API_KEY = "41243d6a8fbb557d88ebb0da26a7ae12";

export default {
  name: "MovieDetail",
  data() {
    return {
      movie: {},
      video: [],
      movie_info: [],
      rank_info: null,
      rank_avg: 0,
      inputValue: "",
    };
  },
  components: {
    ReviewList,
  },
  methods: {
    movieDetail() {
      const movie_id = this.$route.params.movie_id;
      axios
        .get(SERVER_URL + "/movies/" + movie_id + "/")
        .then((res) => {
          console.log(res);
          this.movie = res.data;
        })
        .catch((err) => console.error(err));
    },

    inputVideos() {
      // console.log('@@@',this.$route.params.movie_title)
      const movie_title = this.$route.params.movie_title;
      this.inputValue = movie_title + " 예고편";
      // console.log('inputval = ',this.inputValue)

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
          console.error("유튜브", err);
        });
    },

    movieInfo() {
      const movie_title = this.$route.params.movie_title;
      this.inputValue = movie_title;
      axios
        .get(TMDB_API_URL, {
          params: {
            api_key: TMDB_API_KEY,
            append_to_response: "videos",
            language: "ko",
            query: this.inputValue,
          },
        })
        .then((res) => {
          console.log("TMDB", res);
          this.movie_info = res.data.results[0];
        })
        .catch((err) => {
          console.error(err);
        });
    },

    rankInfo() {
      const movie_id = this.$route.params.movie_id;
      let rank_cnt = [0, 0, 0, 0, 0, 0];
      let rank_total = 0;
      let total_cnt = 0;
      axios
        .get(SERVER_URL + "/movies/" + `${movie_id}` + "/review/")
        .then((res) => {
          res.data.forEach((rank) => {
            rank_cnt[rank.rank] += 1;
            total_cnt += 1;
            rank_total += rank.rank;
          });
          let avg = rank_total / total_cnt;
          this.rank_avg = avg.toFixed(1);
          this.rank_info = rank_cnt;
        })
        .catch((err) => {
          console.error(err);
        });
    },
  },
  created() {
    this.movieDetail();
    this.inputVideos();
    this.movieInfo();
    this.rankInfo();
  },
};
</script>

<style scoped>
.detail-naver,
.detail-tmdb {
  margin-bottom: 15px;
}
.detail-naver *,
.detail-tmdb * {
  margin-bottom: 10px;
}

img {
  border-radius: 5px;
}

h4 {
  font-weight: 700;
}
strong {
  font-weight: 700;
}
</style>
