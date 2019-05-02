<template>
  <div>
    <UserHeader :user="user"/>
    <section>
      <div class="wp">
        <ul  class="crumbs">
          <li><a href="/">首页</a>></li>
          <li><a @click="$router.push(`/users/user_info/`)" > 个人中心</a></li>
          <li> > 个人信息</li>
        </ul>
      </div>
    </section>
    <section>
      <div class="wp list personal_list">
        <div class="left">
          <ul>
            <!--<li class="active2"><a @click="$router.push(`/users/user_info/`)"  >个人资料</a></li>-->
            <!--<li ><a @click="$router.push(`/users/user_courses/`)" >我的课程</a></li>-->
            <!--<li ><a href="usercenter-fav-course.html">我的收藏</a></li>-->
            <li ><router-link to="/users/user_info" class="list-group-item">个人资料</router-link> </li>
            <li ><router-link to="/users/user_courses" class="list-group-item">我的课程</router-link> </li>
            <li ><router-link to="/users/user_favors" class="list-group-item">我的收藏</router-link> </li>
          </ul>
        </div>
        <router-view :user="user"></router-view>
      </div>
    </section>
  </div>
</template>
<script>
  import UserHeader from './UserHeader'
  import axios from 'axios'

  export default {
    data() {
      return {
        user: null,
      }
    },
    mounted: function () {
      // 发送请求获取 data
      axios({
        url: "/api/users/user_info/",
        method: "GET",
      })
        .then(respanse => {
          let res = respanse.data;
          console.log(res)
          if (res.user!=null){
            this.user = JSON.parse(res.user)[0].fields
          }

          console.log(this.user)
          console.log(this.user.image)
        })
        .catch(function(error) {
          console.log(error);
        });
    },
    methods:{
      getUserImgUrl: (bannerUrl) =>{
        console.log(bannerUrl)
        return "../../static/media/" + bannerUrl
      }
    },
    components:{
      UserHeader
    }
  };
</script>
<style >
  @import "../../../static/css/reset.css";
  @import "../../../static/css/animate.css";
  @import "../../../static/css/style.css";
  .personal_list .left li{
    width: 100%;
    height: 60px;
    line-height: 60px;
    font-size: 16px;
    color: #3a3a3a;
    background: url(../../../static/images/arrow_g.png) no-repeat 95% center;
  }
  .router-link-active {
    color: red !important;
  }
</style>
