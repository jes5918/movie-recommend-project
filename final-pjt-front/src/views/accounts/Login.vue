<template>
  <div class="fckncenter notheader-login_color">
    <main class="main-login">
      <img style="width: 150px; height: auto" src="@/assets/logo.png" alt="" />
      <h2>로그인</h2>
      <form action="" @keypress.enter="login">
        <input
          class="input-login"
          v-model="loginData.username"
          type="text"
          id="username"
          required
          placeholder=" 아이디"
        />
        <input
          class="input-login"
          v-model="loginData.password"
          type="password"
          id="password"
          required
          placeholder=" 비밀번호"
        />
        <input
          @click="login"
          type="submit"
          class="signup_button"
          value="로그인"
        />
      </form>
      <p v-if="!isLoggedIn">
        계정이 없으신가요?

        <router-link :to="{ name: 'Signup' }">회원가입</router-link>
      </p>

      <div></div>
    </main>
  </div>
</template>

<script>
export default {
  name: "Login",
  data() {
    return {
      loginData: {
        username: null,
        password: null,
      },
    };
  },
  methods: {
    login(event) {
      event.preventDefault();
      this.$emit("submitlogin", this.loginData);
    },
  },
};
</script>

<style>
</style>