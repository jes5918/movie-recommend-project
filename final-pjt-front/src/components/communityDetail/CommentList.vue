<template>
  <div class="fckncenter" style="margin-bottom: 30px">
    <input
      class="article-comment"
      type="text"
      placeholder=" 댓글을 작성해 보세요!"
      v-model="commentData.content"
      id="content"
      rows="3"
      @keypress.enter="createComment"
    />

    <section
      class="notarticle"
      v-for="comment in comments.slice().reverse()"
      :key="`comment_${comment.id}`"
    >
      <main class="community-article-flex">
        <CommentEdit
          @edit-comment="getComments"
          :comment="comment"
          :article_id="article_id"
        />
        <div class="community-flex-column">
          <div class="community-flex-column-item">
            {{ comment.user.username }}
          </div>
        </div>
        <div class="community-flex-column and_title">
          <div class="community-flex-column-item">{{ comment.content }}</div>
        </div>
        <div class="community-flex-column">
          <div class="community-flex-column-item">
            작성: {{ comment.created_at }}
          </div>
        </div>
        <div class="community-flex-column">
          <div class="community-flex-column-item putfcknbutton">
            수정: {{ comment.updated_at }}
            <div v-if="user == comment.user.username" class="fcknbutton">
              <button
                class="pd1"
                @click="checkUser(comment.id)"
                data-toggle="modal"
                :data-target="`#comment_${comment.id}`"
              >
                <i
                  data-v-111a0ca8=""
                  class="fas fa-edit"
                  aria-hidden="true"
                ></i>
              </button>

              <button class="pd1" @click="DeleteComment(comment.id)">
                <i
                  data-v-111a0ca8=""
                  class="far fa-trash-alt"
                  aria-hidden="true"
                ></i>
              </button>
            </div>
          </div>
        </div>
      </main>
    </section>
  </div>
</template>

<script>
import axios from "axios";
import CommentEdit from "./CommentEdit";

const SERVER_URL = "http://localhost:8000";

export default {
  name: "CommentList",
  components: {
    CommentEdit,
  },
  props: {
    article_id: Number,
  },
  data() {
    return {
      comments: [],
      user: "",
      config: {
        headers: {
          Authorization: `Token ${this.$cookies.get("auth-token")}`,
        },
      },
      commentData: {
        content: null,
        // article: this.article_id,
      },
    };
  },
  computed: {},
  methods: {
    getComments() {
      axios
        .get(
          SERVER_URL + "/community/" + this.article_id + "/comment/",
          this.config
        )
        .then((res) => {
          this.comments = res.data;
        })
        .catch((err) => {
          console.error(err.response);
        });
    },
    createComment() {
      event.preventDefault();
      axios
        .post(
          SERVER_URL + "/community/" + this.article_id + "/comment/",
          this.commentData,
          this.config
        )
        .then(() => {
          // this.$router.push({ name: 'Community' })
          this.getComments();
          this.commentData.content = null;
          // alert('댓글 작성됨')
        })
        .catch((err) => console.log(err.response.data));
    },

    DeleteComment(comment_id) {
      this.checkUser(comment_id);
      axios
        .delete(
          SERVER_URL +
            "/community/" +
            this.article_id +
            "/comment/" +
            comment_id +
            "/",
          this.config
        )
        .then(() => {
          this.getComments();
          // alert('댓글 삭제됨')
        })
        .catch((err) => console.error(err.response));
    },
    checkUser(comment_id) {
      axios
        .get(
          SERVER_URL +
            "/community/" +
            this.article_id +
            "/comment/" +
            comment_id +
            "/check/",
          this.config
        )
        .then(() => {})
        .catch(() => {
          // alert("작성한 본인만 가능합니다.");
        });
    },
  },
  created() {
    this.user = localStorage.getItem("username");
  },
  mounted() {
    this.getComments();
  },
};
</script>

<style scoped>
.community-flex-column {
  display: flex;
  flex-direction: column;
}
</style>