<template>
  <div class="community">
    <h2 class="community-h2">커뮤니티</h2>

    <main class="community-flex1">
      <div class="community-flex-column">
        <div class="community-flex-column-item">작성자</div>
      </div>
      <div class="community-flex-column and_title">
        <div class="community-flex-column-item">작성글</div>
      </div>
      <div class="community-flex-column">
        <div class="community-flex-column-item">작성일</div>
      </div>
      <div class="community-flex-column">
        <div class="community-flex-column-item">수정일</div>
      </div>
    </main>
    <main class="community-flex2">
      <div class="community-flex-column">
        <div
          class="community-flex-column-item"
          v-for="article in articles.slice().reverse()"
          :key="`article_${article.id}`"
        >
          {{ article.user.username }}
        </div>
      </div>
      <div class="community-flex-column and_title">
        <div
          class="community-flex-column-item"
          v-for="article in articles.slice().reverse()"
          :key="`article_${article.id}`"
        >
          <router-link
            :to="{
              name: 'ArticleDetail',
              params: { article_id: article.id },
            }"
          >
            {{ article.title }}
          </router-link>
        </div>
      </div>
      <div class="community-flex-column">
        <div
          class="community-flex-column-item"
          v-for="article in articles.slice().reverse()"
          :key="`article_${article.id}`"
        >
          {{ article.created_at }}
        </div>
      </div>
      <div class="community-flex-column">
        <div
          class="community-flex-column-item"
          v-for="article in articles.slice().reverse()"
          :key="`article_${article.id}`"
        >
          {{ article.updated_at }}
        </div>
      </div>
    </main>

    <div class="community-bottom">
      <router-link style="color: white" :to="{ name: 'CreateArticle' }"
        ><button>글쓰기</button></router-link
      >
    </div>
  </div>
</template>

<script>
import axios from "axios";

const SERVER_URL = "http://localhost:8000";

export default {
  name: "CommunityList",
  components: {},
  data() {
    return {
      articles: [],
    };
  },
  methods: {
    fetchArticles() {
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get("auth-token")}`,
        },
      };
      axios
        .get(SERVER_URL + "/community/", config)
        .then((res) => (this.articles = res.data))
        .catch((err) => console.error(err));
    },
    checkLoggedIn() {
      if (!this.$cookies.isKey("auth-token")) {
        alert("로그인 후 사용가능합니다");
        this.$router.push({ name: "Login" });
      }
    },
  },
  created() {
    this.checkLoggedIn(), this.fetchArticles();
  },
  mounted() {
    // this.isLoggedIn = this.$cookies.isKey('auth-token')
  },
};
</script>

<style scoped>
</style>
