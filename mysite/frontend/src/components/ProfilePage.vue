<template>
<div class="profile">
  <img class="rounded-circle"  width="250" height="250" src="{{ avatar }} " style="cursor: pointer; border: 2px solid black; "/>
  <p class="nameuser">{{ username }}</p>
  <table>
    <tr>
      <td>
        <label for="mail"><h6>Mail: </h6></label>
      </td>
      <td>
        <InputText class="p-inputtext" type="text" v-model="mail" id="mail"/>
      </td>
    </tr>
    <tr>
      <td>
        <label for="tg"><h6>Telegram: </h6></label>
      </td>
      <td>
        <InputText class="p-inputtext" type="text" v-model="tg" id="tg"/>
      </td>
    </tr>
    <tr>
      <td>
        <label for="av"><h6>Avatar: </h6></label>
      </td>
      <td>
        <FileUpload  style="margin-top:5px; margin-left:10px" mode="basic" name="demo[]" url="./upload" accept="image/*" v-model="avatar" id="av"/>
      </td>
    </tr>
  </table>
  <Button class="bt" @click="save_changes" >Save changes</Button>
  <p>{{textResponse}}</p>
</div>
</template>

<script>
import Button from 'primevue/button'
import InputText from 'primevue/inputtext'
import FileUpload from 'primevue/fileupload';
import axios from "axios";

export default {
  name: "ProfilePage",
  title() {
    return "Profile"
  },
  components: {
    Button,
    InputText,
    FileUpload,
  },
  data() {
    return {
      username: '',
      tg: '',
      mail: '',
      textResponse: '',
      avatar: '',
    }
  },

  async created() {
    this.username = localStorage.getItem('usernameW')
    try{
      this.response = await axios.get(`http://127.0.0.1:8000/api/sait/auth/users/me/`,
          {headers: {'Authorization':"Token " + localStorage.getItem("tokenW")}})
      this.tg = this.response.data.tg_name
      this.mail = this.response.data.email
      this.avatar = this.response.data.avatar
    } catch (error) {
      console.log(error.response.data)
      this.textResponse = "Error loading data"
    }
  },
  methods: {
    async save_changes() {
      await axios.put(`http://127.0.0.1:8000/api/sait/auth/users/me/ `, {
        tg_name: this.tg,
        email: this.mail,
        avatar: this.avatar
      }, {headers: {'Authorization':"Token " + localStorage.getItem("tokenW")}}).then(response =>{
        response
      }).catch(error => {
        console.log(error)
        this.textResponse = Object.values( error.response.data ).map(x => x[0]).join('\r\n')
        if (this.textResponse.length > 10) {
          this.textResponse = "Data sending error"
        }
        console.log(this.textResponse)
      })
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
.nameuser{
  font-size: 35px;
  color: black;
  text-align: left;
}
.p-inputtext {
  padding: 4px;
  margin-top:5px;
  margin-left: 10px;
}
.bt {
  margin-top: 10px;
}
.rounded-circle {
  border-radius: 50%!important;
}
.fileu{
  margin-top:20px;
}
</style>