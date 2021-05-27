<template>
  <div class="fckncenter notheader-login_color">
    <main class="main-login">
      <img src="logo.png" alt="" />
      <h2>회원가입</h2>
      <form action="" @keypress.enter="signup">
        <input
          class="input-login"
          v-model="signupData.username"
          type="text"
          id="username"
          required
          placeholder=" 아이디"
        />
        <input
          class="input-login"
          v-model="signupData.password1"
          type="password"
          id="password1"
          required
          placeholder=" 비밀번호"
        />
        <input
          class="input-login"
          v-model="signupData.password2"
          type="password"
          id="password2"
          required
          placeholder=" 비밀번호 확인"
        />
        <input
          type="submit"
          @click="signup"
          class="signup_button"
          value="회원가입"
        />
      </form>
    </main>
  </div>
</template>

<script>
export default {
  name: "Signup",
  data() {
    return {
      signupData: {
        username: null,
        password1: null,
        password2: null,
      },
    };
  },
  methods: {
    signup(event) {
      event.preventDefault();
      this.$emit("submitsignup", this.signupData);
      this.$router("/login");
    },
  },
};
</script>

<style>
</style>