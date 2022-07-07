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
        <Button @click="create_room" >Create room</Button>
      </td>
    </tr>
    <tr style="text-align: center; white-space: pre;">
      <td>
        {{ textResponse }}
      </td>
    </tr>
    </tbody>
  </table>
  <div class="your_room">
    <p class="tit">
      Your rooms
    </p>
    <table class="table">
      <tr>
        <td><h6>ID</h6></td>
        <td><h6>Room name</h6></td>
        <td><h6>Is music</h6></td>
        <td><h6>Is active</h6></td>
      </tr>
      <tbody>
      <tr v-for="room in listRooms" v-bind:key="room">
        <td>
          {{ room.id }}
        </td>
        <td>
          {{ room.name }}
        </td>
        <td>
          {{ room.is_mus}}
        </td>
        <td>
          <Button @click="setact(room.id)">{{ room.is_active }}</Button>
        </td>
      </tr>
      </tbody>
    </table>
  </div>

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
      rooms: '',
      active: '',
    }
  },
  title() {
    return "Create room"
  },
  async created() {
    try {
      this.rooms = await axios.post(`http://127.0.0.1:8000/api/room/my_rooms/`, {username: localStorage.getItem("usernameW")},
          {headers: {'Authorization':"Token " + localStorage.getItem("tokenW")}})
      this.rooms = this.rooms.data.result
    } catch (error) {
      console.log(error.response.data)
    }
  },
  computed: {
    listRooms() {
      let list = []
      for (let index = 0; index < this.rooms.length; index++) {
        const element = this.rooms[index]
        let active = "Set active";
        if (element.id_room.toString() === localStorage.getItem('my_active_roomW').toString()){
          active = "Is active";
        }
        list.push({
          id: element.id_room,
          name: element.name_room,
          is_mus: element.is_music,
          is_active: active,
        })
      }
      return list
    }
  },
  methods: {
    async create_room() {
      await axios.post(`http://127.0.0.1:8000/api/room/new/`, {
        username: localStorage.getItem('usernameW'),
        name_room: this.NameRoom,
        password_room: this.password,
        is_music: this.is_music,
      }, {headers: {'Authorization':"Token " + localStorage.getItem("tokenW")}}).then(response =>{
        localStorage.setItem('active_roomW', response.data.id)
        localStorage.setItem('my_active_roomW', response.data.id)
        this.textResponse = 'Success!'
        this.$router.push('/createroom')
      }).catch(error => {
        console.log(error)
        this.textResponse = Object.values( error.response.data ).map(x => x[0]).join('\r\n')
        if (this.textResponse.length > 5) {
          this.textResponse = "Error"
        }
        console.log(this.textResponse)
      })
    },
    async setact(id_act){
      localStorage.setItem('active_roomW', id_act)
      localStorage.setItem('my_active_roomW', id_act)
      this.$router.push('/createroom')
    }
  },

}
</script>

<style scoped>
.add {
  text-align: left;
  margin-top: 5px;
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
.table {
  width: 98%;
  border: none;
  border-collapse: separate;
  background-color: rgba(112, 129, 183, 0.51);
  border-radius: 10px;
}
.your_room{
  text-align: left;
  margin-left: 50px;
}
</style>