<template>
<div class="profile">
  <a>name</a>
</div>
</template>

<script>
//import Button from 'primevue/button'
//import InputText from 'primevue/inputtext'

export default {
  name: "ProfilePage",
  components: {
    //Button,
    //InputText,
  },
  data() {
    return {
      username: '',
      tg: '',
      textResponse: '',
    }
  },
}
</script>

<style scoped>
.profile {
  text-align: left;
  margin-top: 40px;
  margin-left: 50px;
}
</style>