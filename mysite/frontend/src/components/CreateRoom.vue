<template>

  <table class="add">
    <tbody style="text-align: left">
    <tr>
      <td>
        <p class="tit">
          You can create a new room with music or video
        </p>
        <label for="usr"><h6>Room name</h6></label>
      </td>
    </tr>
    <tr>
      <td>
        <InputText class="p-inputtext" type="text" v-model="NameRoom" id="usr"/>
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
        <Checkbox class="align-middle" v-model="is_music" title="show pass" id="ismusic" :binary="true"  />
        <label for="ismusic" style="padding-left: 7px"><h6>Is music</h6></label>
      </td>
    </tr>
    <tr style="text-align: left">
      <td>
        <Button @click="Create" >Create room</Button>
      </td>
    </tr>
    <tr style="text-align: center; white-space: pre;">
      <td>
        {{ textResponse }}
      </td>
    </tr>
    </tbody>
  </table>
</template>

<script>
import Button from 'primevue/button'
import InputText from 'primevue/inputtext'
import Checkbox from 'primevue/checkbox'
import axios from "axios";


export default {
  name: "CreateRoom",
  components: {
    Button,
    InputText,
    Checkbox
  },
  data() {
    return {
      NameRoom: '',
      password: '',
      is_music: false,
    }
  },
  methods: {
    async login() {
      await axios.put(`/api/users/`, {
        NameRoom: this.NameRoom,
        password: this.password,
        is_music: this.is_music,
      }).then(() =>{
        localStorage.setItem('usernameW', this.username)
        this.textResponse = 'Success!'
        this.$router.push('/home')
      }).catch(error => {
        console.log(error)
        this.textResponse = Object.values( error.response.data ).map(x => x[0]).join('\r\n')
        if (this.textResponse.length > 5) {
          this.textResponse = "Server error"
        }
        console.log(this.textResponse)
      })
    }
  },

}
</script>

<style scoped>
.add {
  text-align: left;
  margin-top: 40px;
  margin-left: 50px;
}
.p-inputtext {
  padding: 4px;
}
.tit{
  font-size: 30px;
  color: black;
  text-align: left;
}
</style>