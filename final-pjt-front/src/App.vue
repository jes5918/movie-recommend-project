<template>
  <div>
    <header>
      <div class="header_column header_column_left">
        <router-link to="/">
          <img src="@/assets/logo.png" class="header-logo" alt="" />
        </router-link>
      </div>
      <div class="header_column header_column_right">
        <div v-show="isLoggedIn">
          <form @submit="navsearch">
            <input
              v-model="keyword"
              class="input-header"
              type="text"
              required
              placeholder=" 작품 제목을 검색해보세요."
            />
          </form>
        </div>
        <div v-if="isLoggedIn">
          <router-link :to="{ name: 'Community' }">커뮤니티</router-link>
        </div>
        <!-- <div v-if="isLoggedIn">
          <router-link :to="{ name: 'Stock' }">주식기반 영화추천</router-link>
        </div> -->
        <div v-if="!isLoggedIn">
          <router-link class="nav-link" :to="{ name: 'Login' }"
            >로그인
          </router-link>
        </div>
        <div v-if="!isLoggedIn">
          <router-link class="nav-link" :to="{ name: 'Signup' }"
            >회원가입</router-link
          >
        </div>
        <div v-if="isLoggedIn">
          <router-link
            class="nav-link"
            to="/accounts/logout"
            @click.native="logout"
            >로그아웃</router-link
          >
        </div>
      </div>
    </header>

    <div class="notheader">
      <router-view
        @submitlogin="login"
        @submitsignup="signup"
        :key="$route.fullPath"
      />
      <footer>
        <section class="footer-section footer_section_left">
          <p>
            고객센터 |
            <a href="mailto:tbs01215@gmail.com">tbs01215@gmail.com</a>
          </p>
          <p>대표 수&영</p>
          <div><img src="@/assets/logo.png" alt="" /></div>
          <p>© 2020 Rising Cinema. Inc</p>
        </section>
        <section></section>
      </footer>
    </div>
  </div>
</template>

<script>
import axios from "axios";

const SERVER_URL = "http://127.0.0.1:8000";

export default {
  name: "App",
  data() {
    return {
      isLoggedIn: false,
      keyword: "",
      username: "",
    };
  },
  methods: {
    navsearch() {
      event.preventDefault();
      if (!this.keyword) {
        alert("검색어를 입력하세요");
      } else {
        this.$router.push({
          name: "NavSearchResult",
          query: { keyword: this.keyword },
        });
      }
    },
    setCookie(token) {
      this.$cookies.set("auth-token", token);
      this.isLoggedIn = true;
    },

    signup(signupData) {
      axios
        .post(SERVER_URL + "/rest-auth/signup/", signupData)
        .then((res) => {
          let userstr = res.config.data
          let userAry = userstr.split('&')
          let userAry2 = userAry[0].split('=')
          let user = userAry2[1]
          this.username = user
          this.setCookie(res.data.key);
          localStorage.username = user
          this.$router.push({ name: "Home" });
        })
        .catch(() => {
          alert("입력된 정보를 확인해주세요.");
        });
    },

    login(loginData) {
      axios
        .post(SERVER_URL + "/rest-auth/login/", loginData)
        .then((res) => {
          let userstr = res.config.data
          let userAry = userstr.split('&')
          let userAry2 = userAry[0].split('=')
          let user = userAry2[1]
          this.username = user
          this.setCookie(res.data.key);
          localStorage.username = user
          this.$router.push({ name: "Home" });
        })
        .catch(() => {
          alert("아이디와 비밀번호를 확인하고 다시 로그인 해주세요.");
        });
    },

    logout() {
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get("auth-token")}`,
        },
      };
      axios
        .post(SERVER_URL + "/rest-auth/logout/", null, config)
        .catch((err) => console.log(err.response))
        .finally(() => {
          this.$cookies.remove("auth-token");
          this.isLoggedIn = false;
          localStorage.removeItem('username')
          this.$router.push({ name: "Home" });
        });
    },
  },
  mounted() {
    this.isLoggedIn = this.$cookies.isKey("auth-token");
  },
};
</script>

<style>
</style>
