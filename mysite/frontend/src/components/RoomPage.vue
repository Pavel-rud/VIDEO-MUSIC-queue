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
          <Button @click="connect">Connect room</Button>
        </td>
        <td>
          {{ textResponse }}
        </td>
        <!--    <td>-->
        <!--      <Button style="margin-left: 30px" @click="myroom" >My room</Button>-->
        <!--    </td>-->
      </tr>
    </table>
  </header>


  <div class="roomvue">

    <div class="queue">
      <table class="btq">
        <tr>
          <td>
            <Button @click="restart">Restart</Button>
          </td>
          <td>
            <Button @click="pauseorresume">Pause/Resume</Button>
          </td>
          <td>
            <Button @click="next_link">Next</Button>
          </td>
        </tr>
      </table>
      <table class="table">
        <tr>
          <td>Author</td>
          <td>Link</td>
        </tr>
        <tbody>
        <tr v-for="link in listRooms" v-bind:key="link">
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
          <h6>Room id: {{ RoomId }}</h6>
        </td>
        <td>
          <InputText style="margin-left:50px; width:300px" class="p-inputtext" type="text" v-model="inputlink" id="id"/>
        </td>
        <td>
          <Button style="margin-left: 2px" @click="addlink">Add link</Button>
        </td>
      </tr>
      <tr>
        <td>
          <h6 class="roomname">{{ NameRoom }}</h6>
        </td>

      </tr>
    </table>


    <div>
      <!--      <div>-->
      <!--        video_id : <input type="text" v-model="temp.video_id"/><br/>-->
      <!--        <button @click="applyConfig">Apply</button>-->
      <!--      </div>-->
      <YoutubeVue3 ref="youtube" :videoid="play.video_id" :loop="play.loop" :width="854" :height="480"
                   @ended="onEnded" @paused="onPaused" @played="onPlayed"/>
    </div>
  </div>


</template>

<script>
import Button from 'primevue/button'
import InputText from 'primevue/inputtext'
import axios from "axios";
import {YoutubeVue3} from 'youtube-vue3'
// import {computed} from "vue";
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
    YoutubeVue3,
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
      list_of_id: [],

      pause: false,
      end_videos: false,
      temp: {video_id: "", loop: 1},
      play: {video_id: "", loop: 1},
    }
  },
  async created() {
    try {
      this.room = await axios.get(`http://127.0.0.1:8000/api/room/room/` + localStorage.getItem('active_roomW') + '/',
          {headers: {'Authorization': "Token " + localStorage.getItem("tokenW")}})
      this.NameRoom = this.room.data.name_room
      this.RoomId = localStorage.getItem('active_roomW')
    } catch (error) {
      console.log(error.response.data)
    }
    try {
      this.list_of_links = await axios.get(`http://127.0.0.1:8000/api/room/links/` + localStorage.getItem('active_roomW') + '/',
          {headers: {'Authorization': "Token " + localStorage.getItem("tokenW")}})
      this.list_of_links = this.list_of_links.data.result

      let list_id = []
      for (let index = 0; index < this.list_of_links.length; index++) {
        const element = this.list_of_links[index]
        list_id.push(element.link.substr(-11))
      }
      this.list_of_id = list_id
      console.log(this.list_of_id)
      if (this.list_of_id.length === 0) {
        this.end_videos = true
      }
    } catch (error) {
      console.log(error.response.data)
    }
    try {
      this.list_of_links = await axios.get(`http://127.0.0.1:8000/api/room/delete_first_link/` + localStorage.getItem('active_roomW') + '/',
          {headers: {'Authorization': "Token " + localStorage.getItem("tokenW")}})
      this.list_of_links = this.list_of_links.data.result
    } catch (error) {
      console.log(error.response.data)
    }
    this.temp = {video_id: this.list_of_id[0], loop: 1}
    this.play = {video_id: this.list_of_id[0], loop: 1}
    this.play = Object.assign(this.play, this.temp)
  },
  computed: {
    listRooms() {
      let list = []
      //let list_id = []
      for (let index = 0; index < this.list_of_links.length; index++) {
        const element = this.list_of_links[index]
        //list_id.push(element.link.substr(-11))
        list.push({
          author: element.username_add,
          text: element.link,
        })
      }
      //this.list_of_id = list_id
      return list
    }
  },
  methods: {
    async connect() {
      await axios.post(`http://127.0.0.1:8000/api/room/add_to_room/`, {
        id_room: this.inputid,
        password_room: this.password,
        username: localStorage.getItem('usernameW'),
      }, {headers: {'Authorization': "Token " + localStorage.getItem("tokenW")}}).then(() => {
        localStorage.setItem('active_roomW', this.inputid)
        this.textResponse = 'Success!'
        this.$router.push('/room')
      }).catch(error => {
        console.log(error)
        this.textResponse = Object.values(error.response.data).map(x => x[0]).join('\r\n')
        if (this.textResponse.length > 5) {
          this.textResponse = "Error"
        }
        console.log(this.textResponse)
      })
      try {
        this.room = await axios.get(`http://127.0.0.1:8000/api/room/room/` + localStorage.getItem('active_roomW') + '/',
            {headers: {'Authorization': "Token " + localStorage.getItem("tokenW")}})
        this.NameRoom = this.room.data.name_room
        this.RoomId = localStorage.getItem('active_roomW')
      } catch (error) {
        console.log(error.response.data)
      }
      try {
        this.list_of_links = await axios.get(`http://127.0.0.1:8000/api/room/links/` + localStorage.getItem('active_roomW') + '/',
            {headers: {'Authorization': "Token " + localStorage.getItem("tokenW")}})
        this.list_of_links = this.list_of_links.data.result
      } catch (error) {
        console.log(error.response.data)
      }
    },
    async addlink() {
      await axios.post(`http://127.0.0.1:8000/api/room/room/` + localStorage.getItem('active_roomW') + '/', {
        link: this.inputlink,
        username: localStorage.getItem('usernameW'),
      }, {headers: {'Authorization': "Token " + localStorage.getItem("tokenW")}}).then(() => {
        this.textResponse = 'Success!'
      }).catch(error => {
        console.log(error)
        this.textResponse = Object.values(error.response.data).map(x => x[0]).join('\r\n')
        if (this.textResponse.length > 5) {
          this.textResponse = "Error"
        }
        console.log(this.textResponse)
      })
      try {
        this.list_of_links = await axios.get(`http://127.0.0.1:8000/api/room/links/` + localStorage.getItem('active_roomW') + '/',
            {headers: {'Authorization': "Token " + localStorage.getItem("tokenW")}})
        this.list_of_links = this.list_of_links.data.result
        let list_id = []
        for (let index = 0; index < this.list_of_links.length; index++) {
          const element = this.list_of_links[index]
          list_id.push(element.link.substr(-11))
        }
        this.list_of_id = list_id
        // computed()
      } catch (error) {
        console.log(error.response.data)
      }
      if (this.end_videos) {
        this.end_videos = false
        console.log('uifveduhfeduhfd')
        try {
          this.list_of_links = await axios.get(`http://127.0.0.1:8000/api/room/links/` + localStorage.getItem('active_roomW') + '/',
              {headers: {'Authorization': "Token " + localStorage.getItem("tokenW")}})
          this.list_of_links = this.list_of_links.data.result

          let list_id = []
          for (let index = 0; index < this.list_of_links.length; index++) {
            const element = this.list_of_links[index]
            list_id.push(element.link.substr(-11))
          }
          this.list_of_id = list_id
        } catch (error) {
          console.log(error.response.data)
        }
        this.temp = {video_id: this.list_of_id[0], loop: 1}
        this.play = {video_id: this.list_of_id[0], loop: 1}
        this.play = Object.assign(this.play, this.temp)
      }
    },
    async myroom() {
      if (localStorage.getItem('my_active_roomW') === '') {
        console.log("no_my_room")
      } else {
        localStorage.setItem('active_roomW', localStorage.getItem('my_active_roomW'))
      }
      try {
        this.list_of_links = await axios.get(`http://127.0.0.1:8000/api/room/links/` + localStorage.getItem('active_roomW') + '/',
            {headers: {'Authorization': "Token " + localStorage.getItem("tokenW")}})
        this.list_of_links = this.list_of_links.data.result
      } catch (error) {
        console.log(error.response.data)
      }
    },
    async get_links() {
      try {
        this.list_of_links = await axios.get(`http://127.0.0.1:8000/api/room/links/` + localStorage.getItem('active_roomW') + '/',
            {headers: {'Authorization': "Token " + localStorage.getItem("tokenW")}})
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
    },
    applyConfig() {
      this.play = Object.assign(this.play, this.temp)
    },
    playCurrentVideo() {
      this.$refs.youtube.player.playVideo();
    },
    stopCurrentVideo() {
      this.$refs.youtube.player.stopVideo();
    },
    pauseCurrentVideo() {
      this.$refs.youtube.player.pauseVideo();
    },
    pauseorresume() {
      if (this.pause) {
        this.$refs.youtube.player.playVideo();
        this.pause = !this.pause
      } else {
        this.pause = !this.pause
        this.$refs.youtube.player.pauseVideo();
      }
    },
    restart() {
      this.$refs.youtube.player.stopVideo();
      this.$refs.youtube.player.playVideo();
    },

    async next_link() {
      if (this.list_of_id.length > 1) {
        try {
          this.list_of_links = await axios.delete(`http://127.0.0.1:8000/api/room/delete_first_link/` + localStorage.getItem('active_roomW') + '/',
              {headers: {'Authorization': "Token " + localStorage.getItem("tokenW")}})
          this.list_of_links = this.list_of_links.data.result
        } catch (error) {
          console.log(error.response.data)
        }
      }
      try {
        this.list_of_links = await axios.get(`http://127.0.0.1:8000/api/room/links/` + localStorage.getItem('active_roomW') + '/',
            {headers: {'Authorization': "Token " + localStorage.getItem("tokenW")}})
        this.list_of_links = this.list_of_links.data.result

        let list_id = []
        for (let index = 0; index < this.list_of_links.length; index++) {
          const element = this.list_of_links[index]
          list_id.push(element.link.substr(-11))
        }
        this.list_of_id = list_id
      } catch (error) {
        console.log(error.response.data)
      }
      this.temp = {video_id: this.list_of_id[0], loop: 1}
      this.play = {video_id: this.list_of_id[0], loop: 1}
      this.play = Object.assign(this.play, this.temp)
    },
    async onEnded() {
      console.log("## OnEnded")
      try {
        this.list_of_links = await axios.delete(`http://127.0.0.1:8000/api/room/delete_first_link/` + localStorage.getItem('active_roomW') + '/',
            {headers: {'Authorization': "Token " + localStorage.getItem("tokenW")}})
        this.list_of_links = this.list_of_links.data.result
      } catch (error) {
        console.log(error.response.data)
      }
      try {
        this.list_of_links = await axios.get(`http://127.0.0.1:8000/api/room/links/` + localStorage.getItem('active_roomW') + '/',
            {headers: {'Authorization': "Token " + localStorage.getItem("tokenW")}})
        this.list_of_links = this.list_of_links.data.result

        let list_id = []
        for (let index = 0; index < this.list_of_links.length; index++) {
          const element = this.list_of_links[index]
          list_id.push(element.link.substr(-11))
        }
        this.list_of_id = list_id
      } catch (error) {
        console.log(error.response.data)
      }
      if (this.list_of_id.length === 0) {
        this.end_videos = true
      }
      this.temp = {video_id: this.list_of_id[0], loop: 1}
      this.play = {video_id: this.list_of_id[0], loop: 1}
      this.play = Object.assign(this.play, this.temp)
    },
    onPaused() {
      this.pause = true
      console.log("## OnPaused")
    },
    onPlayed() {
      this.pause = false
      console.log("## OnPlayed")
    }
  }
}
</script>

<style scoped>
.alltable {
  margin-left: 30px;
}

.p-inputtext {
  padding: 4px;
  margin-left: 10px;
  margin-right: 15px;
}

.roomvue {
  margin-top: 10px;
  margin-left: 30px;
  text-align: left;
}

.roomname {
  font-size: 35px;
  color: black;
  text-align: left;
}

.queue {
  float: right;
  margin-right: 20px;
}

.btq {
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