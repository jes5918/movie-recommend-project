<template>
  <main class="community-article">
    <section class="realarticle">
      <h2>{{ article.title }}</h2>
      <p>{{ article.content }}</p>
      <br />
      <div class="datetime float-right">
        <p>{{ article.user.username }}</p>
        작성 : {{ article.created_at }} | 수정 : {{ article.updated_at }}
      </div>
    </section>

    <div class="enemy-controller">
      <button>
        <router-link :to="{ name: 'CreateArticle' }">새 리뷰</router-link>
      </button>
      <button v-if="this.user === article.user.username">
        <router-link
          :to="{ name: 'EditArticle', params: { article_id: article_id } }"
          >수정</router-link
        >
      </button>
      <button v-if="this.user === article.user.username" @click="articleDelete">
        삭제
      </button>
    </div>

    <CommentList :article_id="article_id" />
  </main>
</template>

<script>
import axios from "axios";
import CommentList from "@/components/communityDetail/CommentList.vue";

const SERVER_URL = "http://localhost:8000";

export default {
  name: "CommunityDetail",
  data() {
    return {
      article: {},
      user: "",
      article_id: this.$route.params.article_id,
      config: {
        headers: {
          Authorization: `Token ${this.$cookies.get("auth-token")}`,
        },
      },
    };
  },
  components: {
    CommentList,
  },
  methods: {
    articleDetail() {
      axios
        .get(SERVER_URL + "/community/" + this.article_id + "/", this.config)
        .then((res) => {
          this.article = res.data;
        })
        .catch((err) => {
          console.error(err.response);
        });
    },

    articleDelete() {
      this.checkUser();
      axios
        .delete(SERVER_URL + "/community/" + this.article_id + "/", this.config)
        .then(() => {
          this.$router.push({ name: "Community" });
        })
        .catch((err) => console.error(err.response));
    },
    checkUser() {
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
        .then(() => {})
        .catch((err) => {
          console.error(err);
          // console.log(err);
          // alert("작성한 본인만 가능합니다.");
        });
    },
    loginuser() {
      this.user = localStorage.getItem("username");
    },
  },
  created() {
    this.loginuser();
    this.articleDetail();
  },
};
</script>

<style>
h2 {
  margin: 10px 20px;
}
</style>