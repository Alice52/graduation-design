<template>
  <div class="right">
    <div class="personal_des Releasecont">
      <div class="head">
        <h1>我的收藏</h1>
      </div>
    </div>
    <div class="personal_des permessage">
      <div class="head" style="boder:0">
        <ul class="tab_header messagehead">
          <li>
            <router-link to="/users/user_loveorg">课程机构</router-link>
          </li>
          <li>
            <router-link to="/users/user_loveteacher">授课教师</router-link>
          </li>
          <li >
            <router-link to="/users/user_lovecourse">公开课程</router-link>
          </li>
        </ul>
      </div>
      <router-view></router-view>
    </div>
  </div>
</template>
<script>
  export default {

  }
</script>
<style scoped>
</style>
