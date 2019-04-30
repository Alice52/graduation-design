<template>

</template>

<script>
  import axios from "axios";
  export default {
    mounted: () => {
      axios({
        url: "/api/users/user_logout",
        method: "GET",
      })
        .then(respanse => {
          let res = respanse.data;
          console.log(res)
          if (res.errMsg == "ok") {
            let url = res.url;
            this.$router.push(`${url}`);
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
