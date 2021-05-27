<template>
  <section class="container">
    <hr />
    <h3>현재 BOXOFFICE 주식기반 추천영화!!</h3>
    <hr />
    <div class="mt-4 col">
      <div class="col-md-10 col-lg-12 col-xl-12 mb-r">
        <div class="card card-body mb-3">
          <div class="media d-block d-md-flex">
            <img
              v-if="navermovies[0].image"
              class="d-flex avatar-2 mb-md-0 mb-3 mx-auto"
              style="width: 300px; height: 400px"
              :src="navermovies[0].image"
            />
            <div class="media-body text-center text-md-left ml-md-3 ml-0">
              <h3 v-html="navermovies[0].title"></h3>
              <p>{{ navermovies[0].subtitle }}</p>
              <p>{{ navermovies[0].director }}</p>
              <p>{{ navermovies[0].actor }}</p>
              <p>개봉일 : {{ boxoffice[0].openDt }}</p>
              <p>수익 : {{ boxoffice[0].salesAmt }} 원</p>
              <p>관객수 : {{ boxoffice[0].audiCnt }}</p>
              <a
                :href="navermovies[0].link"
                type="button"
                class="btn btn-primary btn-md"
              >
                네이버 영화정보
              </a>
              <span class="badge"
                ><i class="fas fa-user" aria-hidden="true">
                  {{ navermovies[0].userRating }}</i
                ></span
              >
            </div>
          </div>
        </div>
        <hr />
        <h3>{{ this.company }}</h3>
        <hr />
        <div>
          <button @click="fillData()">차트보기</button>
          <div>
            <StockChart
              :chart-data="dataprops()"
            />
          </div>

          <div>
            <Reactive
              :chart-data="dataprops()"
            />
          </div>
        </div>
      </div>
    </div>
    <hr />
  </section>
</template>

<script>
import Axios from "axios";
import StockChart from "../components/stock/StockChart.vue";
import Reactive from "../components/stock/Reactive.vue";
const KOBIS_URL =
  "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json";
const SERVER_URL = "http://127.0.0.1:8000/";

export default {
  components: { Reactive, StockChart },
  name: "Stock",
  data() {
    return {
      code: "005940",
      boxoffice: {},
      boxofiicename: "",
      boxofficecode: "",
      company: "",
      navermovies: [],
      resdata: [1, 2],
      datacollection: null,
    };
  },
  methods: {
    getboxoffice() {
      Axios({
        method: "GET",
        url: KOBIS_URL,
        params: {
          key: "430156241533f1d058c603178cc3ca0e",
          targetDt: "20201110",
        },
      })
        .then((res) => {
          console.log(
            "🚀 ~ file: Stock.vue ~ line 53 ~ getboxoffice ~ res",
            res.data.boxOfficeResult.weeklyBoxOfficeList
          );
          this.boxoffice = res.data.boxOfficeResult.weeklyBoxOfficeList;
          this.boxofiicename =
            res.data.boxOfficeResult.weeklyBoxOfficeList[0].movieNm;
          this.boxofficecode =
            res.data.boxOfficeResult.weeklyBoxOfficeList[0].movieCd;
          this.getnavermovies();
          this.getmoviecompany();
        })
        .catch((err) => {
          console.error(
            "🚀 ~ file: Stock.vue ~ line 28 ~ getKrStockData ~ err",
            err
          );
        });
    },
    getmoviecompany() {
      Axios({
        method: "GET",
        url:
          "http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json",
        params: {
          key: "430156241533f1d058c603178cc3ca0e",
          movieCd: this.boxofficecode,
        },
      })
        .then((res) => {
          console.log(
            "🚀 ~ file: Stock.vue ~  ~ res",
            res.data.movieInfoResult.movieInfo.companys[1].companyNmEn.substring(
              0,
              6
            )
          );
          this.company = res.data.movieInfoResult.movieInfo.companys[1].companyNmEn.substring(
            0,
            6
          );
          this.getKrStockData();
        })
        .catch((err) => {
          console.error(
            "🚀 ~ file: Stock.vue ~ line 28 ~ getKrStockData ~ err",
            err
          );
        });
    },
    getnavermovies() {
      console.log(this.boxofiicename);
      this.keyword = this.boxofiicename;
      Axios({
        method: "GET",
        url: SERVER_URL + "movies/search/",
        params: {
          query: this.keyword,
        },
      })
        .then((res) => {
          console.log(res);
          this.navermovies = res.data.items;
        })
        .catch((err) => console.error(err));
    },
    getKrStockData() {
      Axios({
        method: "GET",
        url: SERVER_URL + "stock" + "/" + this.company + "/",
      })
        .then((res) => {
          console.log("🚀 ~ file: Stock.vue ~ line 126 ~ .then ~ res", res);
          this.resdata = res.data;
        })
        .catch((err) => {
          console.error(
            "🚀 ~ file: Stock.vue ~ line 28 ~ getKrStockData ~ err",
            err
          );
        });
    },
    filldata() {
      this.datacollection ={
        labels: `${this.resdata[0]}`,
        datasets: [
          {
            label: "주식차트",
            backgroundColor: "#f87979",
            pointBackgroundColor: "white",
            borderWidth: 1,
            pointBorderColor: "#249EBF",
            data: `${this.resdata[1]}`,
          },
        ],
        options: {
          scales: {
            yAxes: [
              {
                ticks: {
                  beginAtZero: false,
                },
                gridLines: {
                  display: true,
                },
              },
            ],
            xAxes: [
              {
                gridLines: {
                  display: false,
                },
              },
            ],
          },
          legend: {
            display: true,
          },
          responsive: true,
          maintainAspectRatio: true,
        },
      };
    },
  },
  watch: {
    dataprops() {
      return {
        labels: `${this.resdata[0]}`,
        datasets: [
          {
            label: "주식차트",
            backgroundColor: "#f87979",
            pointBackgroundColor: "white",
            borderWidth: 1,
            pointBorderColor: "#249EBF",
            data: `${this.resdata[1]}`,
          },
        ],
        options: {
          scales: {
            yAxes: [
              {
                ticks: {
                  beginAtZero: false,
                },
                gridLines: {
                  display: true,
                },
              },
            ],
            xAxes: [
              {
                gridLines: {
                  display: false,
                },
              },
            ],
          },
          legend: {
            display: true,
          },
          responsive: true,
          maintainAspectRatio: true,
        },
      };
      }
  },
  created() {
    this.getboxoffice();
  },
  mounted() {
    this.filldata();
  },
};
</script>

<style>
</style>