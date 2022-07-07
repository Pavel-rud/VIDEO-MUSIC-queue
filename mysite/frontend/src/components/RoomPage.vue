<template>
  <header class="p-3 mb-3 border-bottom">
<table class="alltable">
  <tr>
    <td>
      <label for="id"><h6>Room id</h6></label>
    </td>
    <td>
      <InputText class="p-inputtext" type="text" v-model="inputid" id="id"/>
    </td>
    <td>
      <label for="pass"><h6>Password</h6></label>
    </td>
    <td>
      <InputText class="p-inputtext" :type="showPassword ? 'text' : 'password'" v-model="password" id="pass"/>
    </td>
    <td>
      <Button @click="connect" >Connect room</Button>
    </td>
    <td>
      {{ textResponse }}
    </td>
    <td>
      <Button style="margin-left: 30px" @click="myroom" >My room</Button>
    </td>
  </tr>
</table>
  </header>





<div class="roomvue">

  <div class="queue">
    <table class="btq">
      <tr>
        <td><Button>Pause/Resume</Button></td>
        <td><Button>Next</Button></td>
      </tr>
    </table>
    <table class="table">
      <tr>
        <td>Author</td>
        <td>Link</td>
      </tr>
      <tbody>
      <tr v-for="link in listLinks" v-bind:key="link">
        <td>
          {{ link.author }}
        </td>
        <td>
          {{ link.text }}
        </td>
      </tr>
      </tbody>
    </table>

  </div>

  <table>
    <tr>
      <td>
        <h6>Room id: {{RoomId}}</h6>
      </td>
      <td>
        <InputText style="margin-left:50px; width:300px" class="p-inputtext" type="text" v-model="inputlink" id="id"/>
      </td>
      <td>
        <Button style="margin-left: 2px" @click="addlink" >Add link</Button>
      </td>
    </tr>
    <tr>
      <td>
        <h6 class="roomname">{{NameRoom}}</h6>
      </td>

    </tr>
  </table>


  <iframe  align="left" width="854" height="480"
          src="https://www.youtube.com/embed/tgbNymZ7vqY">
  </iframe>
</div>


</template>

<script>
import Button from 'primevue/button'
import InputText from 'primevue/inputtext'
import axios from "axios";

//import Checkbox from 'primevue/checkbox'
//import axios from "axios";

export default {
  name: "RoomPage",
  title() {
    return "Room"
  },
  components: {
    Button,
    InputText,
  },
  data() {
    return {
      RoomId: '',
      NameRoom: '',
      password: '',
      inputid: '',
      inputlink: '',
      textResponse: '',
      room: '',
      listlinks: [],
      list_of_links: '',
    }
  },
  async created() {
    try {
      this.room = await axios.get(`http://127.0.0.1:8000/api/room/room/` + localStorage.getItem('active_roomW') + '/',
          {headers: {'Authorization':"Token " + localStorage.getItem("tokenW")}})
      this.NameRoom = this.room.data.name_room
      this.RoomId = localStorage.getItem('active_roomW')
    } catch (error) {
      console.log(error.response.data)
    }
  },
  methods:{
    async connect() {
      await axios.post(`http://127.0.0.1:8000/api/room/add_to_room/`, {
        id_room: this.inputid,
        password_room: this.password,
        username: localStorage.getItem('usernameW'),
      }, {headers: {'Authorization':"Token " + localStorage.getItem("tokenW")}}).then(() =>{
        localStorage.setItem('active_roomW', this.inputid)
        this.textResponse = 'Success!'
        this.$router.push('/room')
      }).catch(error => {
        console.log(error)
        this.textResponse = Object.values( error.response.data ).map(x => x[0]).join('\r\n')
        if (this.textResponse.length > 5) {
          this.textResponse = "Error"
        }
        console.log(this.textResponse)
      })
    },
    async addlink() {
      await axios.post(`http://127.0.0.1:8000/api/room/room/` + localStorage.getItem('active_roomW') + '/', {
        link: this.inputlink,
        username: localStorage.getItem('usernameW'),
      }, {headers: {'Authorization':"Token " + localStorage.getItem("tokenW")}}).then(() =>{
        this.textResponse = 'Success!'
      }).catch(error => {
        console.log(error)
        this.textResponse = Object.values( error.response.data ).map(x => x[0]).join('\r\n')
        if (this.textResponse.length > 5) {
          this.textResponse = "Error"
        }
        console.log(this.textResponse)
      })
    },
    async myroom(){
      if (localStorage.getItem('my_active_roomW') === ''){
        console.log("no_my_room")
      }
      else{
        localStorage.setItem('active_roomW', localStorage.getItem('my_active_roomW'))
      }
    },
    async get_links(){

      try {
        this.list_of_links = await axios.get(`http://127.0.0.1:8000/api/room/links/` + localStorage.getItem('active_roomW') + '/',
            {headers: {'Authorization':"Token " + localStorage.getItem("tokenW")}})
        this.list_of_links = this.list_of_links.data.result
        let list = []
        for (let index = 0; index < this.rooms.length; index++) {
          const element = this.rooms[index]
          list.push({
            author: element.username_add,
            text: element.link,
          })
          this.listlinks = list
        }
      } catch (error) {
        console.log(error.response.data)
      }
    }
  }
}
</script>

<style scoped>
.alltable{
  margin-left: 30px;
}

.p-inputtext {
  padding: 4px;
  margin-left: 10px;
  margin-right: 15px;
}
.roomvue{
  margin-top: 10px;
  margin-left: 30px;
  text-align: left;
}
.roomname{
  font-size: 35px;
  color: black;
  text-align: left;
}

.queue{
  float: right;
  margin-right:20px;
}
.btq{
  text-align: right;
}
.table {
  width: 100%;
  border: none;
  border-collapse: separate;
  background-color: rgba(112, 129, 183, 0.51);
  border-radius: 10px;
}
</style>