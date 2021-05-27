<template>
  <div>
    <div
      class="modal fade"
      :id="`comment_${comment.id}`"
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
              v-html="`댓글 수정`"
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
                v-model="commentData.content"
                class="form-control"
                placeholder="댓글을 작성하세요."
                id="content"
                rows="3"
              />
              <button
                @click="EditComment(comment.id)"
                type="submit"
                data-dismiss="modal"
              >
                댓글 수정
              </button>
            </div>
          </div>
          <div class="modal-footer">
            <button type="button" data-dismiss="modal">취소</button>
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
  name: "CommentEdit",
  props: {
    comment: Object,
    article_id: Number,
  },
  data() {
    return {
      config: {
        headers: {
          Authorization: `Token ${this.$cookies.get("auth-token")}`,
        },
      },
      commentData: {
        content: this.comment.content,
      },
    };
  },
  methods: {
    EditComment(comment_id) {
      event.preventDefault();
      axios
        .put(
          SERVER_URL +
            "/community/" +
            this.article_id +
            "/comment/" +
            comment_id +
            "/",
          this.commentData,
          this.config
        )
        .then(() => {
          this.$emit("edit-comment");
        })
        .catch((err) => console.error(err.response));
    },
  },
};
</script>

<style>
</style>