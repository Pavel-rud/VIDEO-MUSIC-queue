<template>
  <link rel="canonical" href="https://getbootstrap.com/docs/5.1/examples/headers/">
  <header class="p-3 mb-3 border-bottom">
    <div class="container">
      <div class="d-flex flex-wrap align-items-center justify-content-center justify-content-lg-start">
        <router-link class="nav-link" to="/home" >
          <a class="d-flex align-items-center mb-2 mb-lg-0 text-dark text-decoration-none">
            <img class="bi me-2" width="40" height="40" role="img" aria-label="Bootstrap" src="@/assets/img/logo.png" >
          </a>
        </router-link>
        <ul class="nav col-12 col-lg-auto me-lg-auto mb-2 justify-content-center mb-md-0">
          <li><router-link class="nav-link" to="/home" ><a class="nav-link px-2 link-dark">Home</a></router-link></li>
          <li><router-link class="nav-link" to="/home" ><a class="nav-link px-2 link-dark">Room</a></router-link></li>
          <li><router-link class="nav-link" to="/createroom" ><a class="nav-link px-2 link-dark">Create room</a></router-link></li>
          <li><router-link class="nav-link" to="/profile" ><a class="nav-link px-2 link-dark">Profile</a></router-link></li>
        </ul>
        <form class="d-flex" role="search">
          <router-link class="nav-link" to="/logout"><h5>Logout</h5></router-link>
        </form>
      </div>
    </div>
  </header>

  <div class="content">
    <router-view></router-view>
  </div>
</template>

<script>

export default {
  name: 'App',
  title() {
    return "App Page"
  },
  data() {
    return {
      check: false,
    }
  },
  created() {
    if (!localStorage.getItem('usernameW')) {
      this.$router.push('/login')
    } else if (localStorage.getItem('usernameW') && (this.isLogin)) {
      this.$router.push('/home')
    }
  },
  computed: {
    isLogin() {
      return this.$route.path === '/login' || this.$route.path === '/register' || this.$route.path === '/'
    }
  },
  watch: {
    $route() {
      if (!localStorage.getItem('usernameW') && this.$route.path !== '/register') {
        this.$router.push('/login')
      } else if (localStorage.getItem('usernameW') && (this.isLogin)) {
        this.$router.push('/home')
      }
    }
  }
}
</script>

<style>
@import url('~bootstrap/dist/css/bootstrap.min.css');

#app {
  font-family: Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #000000;
}

.bd-placeholder-img {
  font-size: 1.125rem;
  text-anchor: middle;
  -webkit-user-select: none;
  -moz-user-select: none;
  user-select: none;
}

@media (min-width: 768px) {
  .bd-placeholder-img-lg {
    font-size: 3.5rem;
  }
}
</style>
