<template>
  <div>
    <h1>수정</h1>
    <form>
      <div class="form-group">
        <label for="title">제목</label>
        <input
          v-model="article.title"
          type="text"
          class="form-control"
          id="title"
        />
      </div>
      <div class="form-group">
        <label for="content">내용</label>
        <textarea
          v-model="article.content"
          class="form-control"
          id="content"
          rows="3"
        ></textarea>
      </div>
      <button @click="articleEdit" type="submit" class="btn btn-primary">
        제출
      </button>
    </form>
  </div>
</template>

<script>
import axios from "axios";

const SERVER_URL = "http://localhost:8000";

export default {
  name: "CommunityEdit",
  data() {
    return {
      article_id: this.$route.params.article_id,
      user: "",
      article: {
        title: null,
        content: null,
      },
      config: {
        headers: {
          Authorization: `Token ${this.$cookies.get("auth-token")}`,
        },
      },
    };
  },
  methods: {
    articleEdit(event) {
      event.preventDefault(event);
      axios
        .put(
          SERVER_URL + "/community/" + this.article_id + "/",
          this.article,
          this.config
        )
        .then(() => {
          // console.log('수정성공')
          this.$router.push({ name: "Community" });
        })
        .catch((err) => console.error(err.response));
    },
    articleDetail() {
      axios
        .get(SERVER_URL + "/community/" + this.article_id + "/", this.config)
        .then((res) => {
          this.article.title = res.data.title;
          this.article.content = res.data.content;
        })
        .catch((err) => {
          console.error(err);
        });
    },

    checkLoggedIn() {
      if (!this.$cookies.isKey("auth-token")) {
        this.$router.push({ name: "Login" });
      }
    },
    checkUser() {
      console.log("this.config");
      this.user = localStorage.getItem("username");
      axios
        .get(
          SERVER_URL +
            "/community/" +
            this.article_id +
            "/check/" +
            this.user +
            "/",
          this.config
        )
        .then((res) => {
          console.log(
            "🚀 ~ file: CommunityEdit.vue ~ line 69 ~ .then ~ res",
            res
          );
        })
        .catch((err) => {
          console.error(err.response);
          console.log(err);
          // alert('작성한 본인만 가능합니다.')
        });
    },
  },
  created() {
    this.articleDetail();
    this.checkUser();
  },
};
</script>

<style>
</style>