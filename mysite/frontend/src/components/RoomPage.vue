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
    </table>

  </div>

  <table>
    <tr>
      <td>
        <h6>Room id: {{RoomId}}</h6>
      </td>
      <td>
        <InputText style="margin-left:50px; width:300px" class="p-inputtext" type="text" v-model="inputid" id="id"/>
      </td>
      <td>
        <Button style="margin-left: 2px" @click="Create" >Add link</Button>
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