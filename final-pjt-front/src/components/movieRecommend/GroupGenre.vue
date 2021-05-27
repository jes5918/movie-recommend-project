<template>
  <div class="padding">
    <h2 style="margin-left: 40px">장르별</h2>
    <div class="form-group">
      <label for="ControlSelect">장르를 선택하세요</label>
      <select
        @click="selectGenre"
        v-model="genreKeyword"
        class="custom-select"
        id="ControlSelect"
      >
        <option v-for="genre in genres" :key="genre">{{ genre }}</option>
      </select>
    </div>
  </div>
</template>

<script>
export default {
  name: "GroupGenre",
  data: function () {
    return {
      genres: [
        "드라마",
        "판타지",
        "공포",
        "로맨스",
        "모험",
        "스릴러",
        "느와르",
        "다큐멘터리",
        "코미디",
        "가족",
        "전쟁",
        "애니메이션",
        "범죄",
        "뮤지컬",
        "SF",
        "액션",
      ],
      genreKeyword: "",
    };
  },
  methods: {
    selectGenre: function () {
      this.$emit("search-genre", this.genreKeyword);
    },
  },
};
</script>

<style scoped>
.padding {
  margin: 40px 60px;
}
.padding * {
  margin: 5px 20px;
}
</style>