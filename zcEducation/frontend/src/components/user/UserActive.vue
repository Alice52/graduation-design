<template>

</template>

<script>
  import axios from 'axios'
  export default {
    mounted() {
      axios({
        url: `/api/${this.$router.history.current.fullPath}`,
        method: "GET",
      })
        .then(respanse => {
          let res = respanse.data;
          console.log(res)
          if (res.errMsg == "ok") {
            this.$router.push(`/users/user_login`);
          } else {
            alert(res.errMsg);
          }
        })
        .catch(function(error) {
          console.log(error);
        });
    }
  }
</script>
<style scoped></style>
