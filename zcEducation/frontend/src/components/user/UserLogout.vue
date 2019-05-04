<template>

</template>

<script>
  import axios from "axios";
  export default {
    mounted() {
      axios({
        url: "/api/users/user_logout/",
        method: "GET",
      })
        .then(respanse => {
          let res = respanse.data;
          if (res.errMsg == "ok") {
            this.$router.push(`/`);
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

<style>

</style>
