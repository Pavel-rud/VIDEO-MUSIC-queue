<template>
  <div class="home">
    <h2>
      Here you can watch video / listen to music with the friends!
    </h2>
    <h2>
      You can add video/music to the queue using telegram bot:
    </h2>
    <h2></h2>
    <h2><a class="blue-link" href="http://t.me/VIDEO_MUSIC_QUEUE_bot">@VIDEO_MUSIC_QUEUE_bot</a></h2>
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

.blue-link{
  color: #006fff;
}

.home {
  margin-top:40px;
}
</style>