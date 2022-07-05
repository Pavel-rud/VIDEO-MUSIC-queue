<template>
  <img src="@/assets/img/laptomusicvideo.png" class="laptop">

  <table class="left">
    <p class="tit">Registration</p>
    <tbody style="text-align: left">
    <tr>
      <td>
        <label for="usr"><h6>Username</h6></label>
      </td>
    </tr>
    <tr>
      <td>
        <InputText class="p-inputtext" type="text" v-model="username" id="usr"/>
      </td>
    </tr>
    <tr>
      <td>
        <label for="email"><h6>Email</h6></label>
      </td>
    </tr>
    <tr>
      <td>
        <InputText class="p-inputtext" type="email" v-model="email" id="email"/>
      </td>
    </tr>
    <tr>
      <td>
        <label for="pass"><h6>Password</h6></label>
      </td>
    </tr>
    <tr>
      <td>
        <InputText class="p-inputtext" :type="showPassword ? 'text' : 'password'" v-model="password" id="pass"/>
      </td>
    </tr>
    <tr>
      <td>
        <Checkbox class="align-middle" v-model="showPassword" title="show pass" id="showpass" :binary="true"  />
        <label for="showpass"><h6>&nbsp;Show Password</h6></label>
      </td>
    </tr>
    <tr style="text-align: center">
      <td>
        <Button @click="register">Register</Button>
      </td>
    </tr>
    <tr style="text-align: center">
      <td>
        <router-link to="/login">
          <Button>Or login</Button>
        </router-link>
      </td>
    </tr>
    <tr style="text-align: center; white-space: pre;">
      <td>{{ textResponse }}</td>
    </tr>
    </tbody>
  </table>
</template>

<script>
import Button from 'primevue/button'
import InputText from 'primevue/inputtext'
import Checkbox from 'primevue/checkbox'

import axios from 'axios'

export default {
  components: {
    Button,
    InputText,
    Checkbox
  },
  data() {
    return {
      email: '',
      username: '',
      password: '',
      showPassword: false,
      textResponse: '',
    }
  },
  title() {
    return "Register"
  },
  methods: {
    async register() {
      await axios.post('/api/users/', {
        username: this.username,
        password: this.password,
        email: this.email
      }).then(response => {
        console.log(response)
        this.textResponse = 'Success!'
      }).catch(error => {
        console.log(error)
        this.textResponse = Object.values( error.response.data ).map(x => x[0]).join('\r\n')
        console.log(this.textResponse)
      })
    }
  },
}
</script>

<style scoped>
.left {
  text-align: left;
  margin-top: 40px;
  margin-left: 150px;
}

.p-inputtext {
  padding: 4px;
}

.tit{
  font-size: 30px;
  color: black;
}

router-link {
  text-decoration: none;
}
.laptop {
  height: 600px;
  width: 600px;
  float: right; /* Выравнивание по правому краю */
  margin-right: 300px;
}
</style>