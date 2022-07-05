<template>
  <a></a>
</template>

<script>
export default {
  mounted() {
    localStorage.clear('usernameW')
    this.$router.push('/login')
  },
}
</script>