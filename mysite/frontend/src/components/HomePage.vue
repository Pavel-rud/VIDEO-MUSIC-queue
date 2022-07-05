<template>
  <div class="home">
    <h2>
      Здесь вы можете всей компанией смотреть видео/слушать музыку!
    </h2>
    <h2>
      Вы можете добавлять видео/музыку в очередь при помощи телеграмм бота: <a href="">@DjangoVueProjBot</a>
    </h2>
    <img src="@/assets/img/logo.png" class="logovm">
  </div>
</template>

<script>
export default {
  methods: {
  },
  title() {
    return "Home"
  },
}
</script>

<style scoped>
.logovm {
  margin-top: 20px;
  height: 300px;
  width: 300px;
  margin-right: auto;
  margin-left: auto;
}

.home {
  margin-top:40px;
}
</style>