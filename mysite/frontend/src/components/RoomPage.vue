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
      <Button @click="Create" >Connect room</Button>
    </td>
    <td>
      {{ textResponse }}
    </td>
    <td>
      <Button style="margin-left: 30px" @click="Create" >My room</Button>
    </td>
  </tr>
</table>
  </header>

<div class="roomvue">
  <h6>Room id: {{RoomId}}</h6>
  <h6 class="roomname">{{NameRoom}}</h6>
  <video src="https://youtu.be/nirqhEOLiCY" autoplay>
  </video>
  <iframe  width="420" height="315"
          src="https://www.youtube.com/embed/tgbNymZ7vqY">
  </iframe>
</div>


</template>

<script>
import Button from 'primevue/button'
import InputText from 'primevue/inputtext'

//import Checkbox from 'primevue/checkbox'
//import axios from "axios";

export default {
  name: "RoomPage",
  components: {
    Button,
    InputText,
  },
  data() {
    return {
      RoomId: 'sdfsdfdsf',
      NameRoom: 'lol',
      password: '',
      inputid: '',
    }
  },
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
</style>