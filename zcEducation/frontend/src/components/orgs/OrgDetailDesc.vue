<template>
  <div class="right companycenter layout">
    <div class="head">
      <h1>机构介绍</h1>
    </div>
    <div class="des">

      <p class="org-detail"></p>

    </div>
  </div>
</template>

<script>
    export default {
      data() {
        return{
        }
      },
      props:[
        'org'
      ],
      mounted() {
        this.$nextTick(function(){
          var dom = document.querySelector('.org-detail');
          dom.innerHTML = this.org.fields.detail;
        });
      }
    }
</script>

<style scoped>

</style>
