<template>
<div class="profile">
  <p class="nameuser">{{ username }}</p>
  <table>
    <tr>
      <td>
        <label for="mail"><h6>Mail: </h6></label>
      </td>
      <td>
        <InputText class="p-inputtext" type="text" v-model="NameRoom" id="mail"/>
      </td>
    </tr>
    <tr>
      <td>
        <label for="tg"><h6>Telegram: </h6></label>
      </td>
      <td>
        <InputText class="p-inputtext" type="text" v-model="NameRoom" id="tg"/>
      </td>
    </tr>
  </table>
  <Button class="bt" @click="login" >Save changes</Button>

</div>
</template>

<script>
import Button from 'primevue/button'
import InputText from 'primevue/inputtext'

export default {
  name: "ProfilePage",
  components: {
    Button,
    InputText,
  },
  data() {
    return {
      username: 'example',
      tg: '',
      mail: '@asdasdasd',
      textResponse: '',
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
</style>