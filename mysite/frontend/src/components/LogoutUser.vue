<template>
  <a></a>
</template>

<script>
export default {
  mounted() {
    localStorage.clear('usernameW')
    localStorage.clear('tokenW')
    this.$router.push('/login')
  },
}
</script>