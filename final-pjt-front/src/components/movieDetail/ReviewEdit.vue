<template>
  <div>
    <div
      class="modal fade"
      :id="`review_${review.id}`"
      tabindex="-1"
      role="dialog"
      aria-labelledby="exampleModalLabel"
      aria-hidden="true"
    >
      <div class="modal-dialog" style="max-width: 750px">
        <div class="modal-content">
          <div class="modal-header">
            <h5
              class="modal-title"
              id="exampleModalLabel"
              v-html="`리뷰 수정`"
            ></h5>
            <button
              type="button"
              class="close"
              data-dismiss="modal"
              aria-label="Close"
            >
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <div class="modal-body">
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
              />
              <button
                @click="EditReview(review.id)"
                type="submit"
                class="btn btn-dark"
                data-dismiss="modal"
              >
                작성
              </button>
            </div>
            <br />
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
          </div>
          <div class="modal-footer">
            <button
              type="button"
              class="btn btn-secondary"
              data-dismiss="modal"
            >
              취소
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

const SERVER_URL = "http://localhost:8000";

export default {
  name: "ReviewEdit",
  props: {
    review: Object,
    movie_id: Number,
  },
  data() {
    return {
      config: {
        headers: {
          Authorization: `Token ${this.$cookies.get("auth-token")}`,
        },
      },
      reviewData: {
        content: this.review.content,
        rank: this.review.rank,
      },
    };
  },
  methods: {
    EditReview(review_id) {
      event.preventDefault();
      axios
        .put(
          SERVER_URL +
            "/movies/" +
            this.movie_id +
            "/review/" +
            review_id +
            "/",
          this.reviewData,
          this.config
        )
        .then(() => {
          this.$emit("edit-review");
        })
        .catch((err) => console.error(err.response));
    },
  },
};
</script>

<style>
</style>