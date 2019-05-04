<template>
  <section class="headerwrap">
    <header>
      <div class="header">
        <div class="top">
          <div class="wp">
            <!-- TODO 判断用户是否登录状态 -->
            <div v-if="user!=null" class="personal">
              <dl @mouseenter="enter()" @mouseleave="leave()" class="user fr">
                <dd >
                  {{ user.username }}
                </dd>
                <dt>
                  <img width="30" height="30" :src="getImgUrl(user.image)">
                </dt>
              </dl>
              <div @mouseenter="enter()" @mouseleave="leave2()" v-show="showUserScale" class="userdetail">
                <dl>
                  <dt>
                    <img width="80" height="80" :src="getImgUrl(user.image)">
                  </dt>
                  <dd>
                    <p>{{ user.username }}</p>
                  </dd>
                </dl>
                <div class="btn">
                  <a class="personcenter fl" @click="$router.push(`/users/user_info`)" >进入个人中心</a>
                  <a class="fr"  @click="userLogout">退出</a>
                </div>
              </div>
            </div>
            <a
              v-if="user==null"
              style="color:white"
              class="fr registerbtn"
              @click="$router.push(`/users/user_register`)"
            >注册</a>
            <a
              v-if="user==null"
              style="color:white"
              class="fr loginbtn"
              @click="$router.push(`/users/user_login`)"
            >登录</a>
          </div>
        </div>
        <div class="middle">
          <div class="wp">
            <a  @click="$router.push(`/`)" ><img class="fl" src="../../../static/images/logo1.png"></a>
            <h1>617室 ZC在线学习平台</h1>
          </div>
        </div>
        </div>
    </header>
  </section>
</template>

<script>
  import axios from 'axios'
  export default {
    data() {
      return {
        showUserScale: false,
        timer: '',
      }
    },
    methods: {
      enter(){
        this.showUserScale = true
        if (this.timer != null){
          clearTimeout(this.timer);
        }
      },
      leave(){
        this.timer = setTimeout(()=>{
          this.showUserScale = false
        }, 100)
      },
      leave2(){
        this.showUserScale = false
      },
      userLogout() {
        axios({
          url: "/api/users/user_logout/",
          method: "GET",
        })
          .then(respanse => {
            let res = respanse.data;
            if (res.errMsg == "ok") {
              // this.$router.push(`/`);
              location.reload()
            } else {
              alert(res.errMsg);
            }
          })
          .catch(function(error) {
            console.log(error);
          });
      },
      getImgUrl: (bannerUrl) =>{
        return "../../static/media/" + bannerUrl
      },
    },
    props:[
      'user'
    ],
  };
</script>
<style >
  /*@import "../../../static/css/reset.css";*/
  /*@import "../../../static/css/animate.css";*/
  /*@import "../../../static/css/style.css";*/
  a{
    cursor:pointer;
  }
  [v-cloak] {
    display:none !important;
  }
</style>
