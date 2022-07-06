<template>
<table class="alltable">
  <tr>
    <td>
      <label for="usr"><h6>Room name</h6></label>
    </td>
    <td>
      <InputText class="p-inputtext" type="text" v-model="NameRoom" id="usr"/>
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
  </tr>
</table>


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
      NameRoom: '',
      password: '',
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
</style>