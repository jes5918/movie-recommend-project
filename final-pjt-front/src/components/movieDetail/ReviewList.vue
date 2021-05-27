<template>
  <div style="margin-bottom: 40px">
    <div class="input-group">
      <div class="input-group-prepend">
        <span class="input-group-text" id="basic-addon1"
          ><i class="far fa-comment-dots"></i
        ></span>
      </div>
      <input
        v-model="reviewData.content"
        class="form-control"
        placeholder="댓글을 작성하세요."
        id="content"
        rows="3"
        @keyup.enter="createReview"
      />
      <button @click="createReview" type="submit" class="btn btn-dark">
        작성
      </button>
    </div>

    <hr />

    <div class="form-check form-check-inline">
      <input
        class="form-check-input"
        v-model="reviewData.rank"
        type="radio"
        name="exampleRadios"
        id="exampleRadios1"
        value="1"
        checked
      />
      <label class="form-check-label" for="exampleRadios1"
        ><i class="fas fa-star text-warning"></i
      ></label>
    </div>
    <div class="form-check form-check-inline">
      <input
        class="form-check-input"
        v-model="reviewData.rank"
        type="radio"
        name="exampleRadios"
        id="exampleRadios2"
        value="2"
        checked
      />
      <label class="form-check-label" for="exampleRadios2"
        ><i class="fas fa-star text-warning"></i
        ><i class="fas fa-star text-warning"></i
      ></label>
    </div>
    <div class="form-check form-check-inline">
      <input
        class="form-check-input"
        v-model="reviewData.rank"
        type="radio"
        name="exampleRadios"
        id="exampleRadios3"
        value="3"
        checked
      />
      <label class="form-check-label" for="exampleRadios3"
        ><i class="fas fa-star text-warning"></i
        ><i class="fas fa-star text-warning"></i
        ><i class="fas fa-star text-warning"></i
      ></label>
    </div>
    <div class="form-check form-check-inline">
      <input
        class="form-check-input"
        v-model="reviewData.rank"
        type="radio"
        name="exampleRadios"
        id="exampleRadios4"
        value="4"
        checked
      />
      <label class="form-check-label" for="exampleRadios4"
        ><i class="fas fa-star text-warning"></i
        ><i class="fas fa-star text-warning"></i
        ><i class="fas fa-star text-warning"></i
        ><i class="fas fa-star text-warning"></i
      ></label>
    </div>
    <div class="form-check form-check-inline">
      <input
        class="form-check-input"
        v-model="reviewData.rank"
        type="radio"
        name="exampleRadios"
        id="exampleRadios5"
        value="5"
        checked
      />
      <label class="form-check-label" for="exampleRadios5"
        ><i class="fas fa-star text-warning"></i
        ><i class="fas fa-star text-warning"></i
        ><i class="fas fa-star text-warning"></i
        ><i class="fas fa-star text-warning"></i
        ><i class="fas fa-star text-warning"></i
      ></label>
    </div>

    <hr />

    <div
      class="review-comment"
      v-for="review in reviews.slice().reverse()"
      :key="`review_${review.id}`"
    >
      <reviewEdit
        @edit-review="getReviews"
        :review="review"
        :movie_id="movie_id"
      />
      <div class="courses-container">
        <div class="course">
          <div class="course-preview">
            <h2>{{ review.user.username }}</h2>
            <div v-if="review.rank === 1" class="card-text">
              <i class="fas fa-star text-warning"></i>
            </div>
            <div v-else-if="review.rank === 2" class="card-text">
              <i class="fas fa-star text-warning"></i
              ><i class="fas fa-star text-warning"></i>
            </div>
            <div v-else-if="review.rank === 3" class="card-text">
              <i class="fas fa-star text-warning"></i
              ><i class="fas fa-star text-warning"></i
              ><i class="fas fa-star text-warning"></i>
            </div>
            <div v-else-if="review.rank === 4" class="card-text">
              <i class="fas fa-star text-warning"></i
              ><i class="fas fa-star text-warning"></i
              ><i class="fas fa-star text-warning"></i
              ><i class="fas fa-star text-warning"></i>
            </div>
            <div v-else-if="review.rank === 5" class="card-text">
              <i class="fas fa-star text-warning"></i
              ><i class="fas fa-star text-warning"></i
              ><i class="fas fa-star text-warning"></i
              ><i class="fas fa-star text-warning"></i
              ><i class="fas fa-star text-warning"></i>
            </div>
            <span v-if="user == review.user.username" style="float: right">
              <button
                @click="checkUser(review.id)"
                data-toggle="modal"
                :data-target="`#review_${review.id}`"
                class="fucn align-items-end"
              >
                <i class="fas fa-edit"></i>
              </button>
              <button @click="DeleteReview(review.id)" class="fucn">
                <i class="far fa-trash-alt"></i>
              </button>
            </span>
          </div>
          <div class="course-info">
            <h5 class="text-break">{{ review.content }}</h5>
            <div
              class="d-flex justify-content-start"
              style="margin-bottom: 10px"
            >
              <p class="my-auto datetime">작성 : {{ review.created_at }} |</p>
              <p class="my-auto datetime">수정 : {{ review.updated_at }}</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import ReviewEdit from "./ReviewEdit";

const SERVER_URL = "http://localhost:8000";

export default {
  name: "ReviewList",
  components: {
    ReviewEdit,
  },
  props: {
    movie_id: Number,
  },
  data() {
    return {
      reviews: [],
      user: "",
      config: {
        headers: {
          Authorization: `Token ${this.$cookies.get("auth-token")}`,
        },
      },
      reviewData: {
        content: null,
        rank: 1,
      },
    };
  },
  methods: {
    getReviews() {
      console.log(this.movie_id);
      // axios.get(SERVER_URL+'/movies/'+this.movie_id+'/review/', this.config)
      axios
        .get(SERVER_URL + "/movies/" + this.movie_id + "/review/")
        .then((res) => {
          console.log(res);
          this.reviews = res.data;
          this.$emit("get-rank");
        })
        .catch((err) => {
          console.error(err.response);
        });
    },
    createReview() {
      event.preventDefault();
      axios
        .post(
          SERVER_URL + "/movies/" + this.movie_id + "/review/",
          this.reviewData,
          this.config
        )
        .then(() => {
          this.getReviews();
          this.reviewData.content = null;
          // alert("댓글 작성됨");
        })
        .catch((err) => console.log(err.response.data));
    },

    DeleteReview(review_id) {
      this.checkUser(review_id);
      axios
        .delete(
          SERVER_URL +
            "/movies/" +
            this.movie_id +
            "/review/" +
            review_id +
            "/",
          this.config
        )
        .then(() => {
          this.getReviews();
          // alert("댓글 삭제됨");
        })
        .catch((err) => console.error(err.response));
    },
    checkUser(review_id) {
      this.user = localStorage.getItem("username");
      axios
        .get(
          SERVER_URL +
            "/movies/" +
            this.movie_id +
            "/review/" +
            review_id +
            "/check/" +
            this.user +
            "/",

          this.config
        )
        .then(() => {})
        .catch((err) => {
          console.error(err);
          // alert("작성한 본인만 가능합니다.");
        });
    },
  },
  created() {
    this.user = localStorage.getItem("username");
  },
  mounted() {
    this.getReviews();
  },
};
</script>

<style scoped>
.review-comment {
  background-color: #f8f8f8;
  margin: 10px;
  padding: 8px;
  border-radius: 5px;
  box-shadow: 0 14px 28px rgba(0, 0, 0, 0.05), 0 10px 10px rgba(0, 0, 0, 0.05);
}
.review-comment * {
  margin: 3px 0px;
}
</style>