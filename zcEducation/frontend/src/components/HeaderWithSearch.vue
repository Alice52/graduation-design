<template>
  <div>
    <section v-cloak class="headerwrap">
    <header>
      <div class="header">
        <div class="top">
          <div class="wp">
            <!-- TODO 判断用户是否登录状态 -->
            <div v-if="user!=null" class="personal">
              <dl @mouseenter="enter()" @mouseleave="leave()" class="user fr">
                <dd >
                  {{ user.username }}
                  <!--<img-->
                    <!--class="down fr"-->
                    <!--src="../../static/images/top_down.png"-->
                  <!--&gt;-->
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
                  <a class="personcenter fl" @click="$router.push(`/users/user_center`)" >进入个人中心</a>
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
            <a href="/">
              <img class="fl logo" src="../../static/images/logo1.png">
            </a>
            <div class="searchbox fr">
              <div class="selectContainer fl">
                <span class="selectOption" id="jsSelectOption" data-value="course">公开课</span>
                <ul  class="selectMenu" id="jsSelectMenu">
                  <li data-value="course">公开课</li>
                  <li data-value="org">课程机构</li>
                  <li data-value="teacher">授课老师</li>
                </ul>
              </div>
              <input id="search_keywords" class="fl" type="text" value placeholder="请输入搜索内容" v-model="searchKeywords">
              <img
                class="search_btn fr"
                id="jsSearchBtn"
                src="../../static/images/search_btn.png"
              >
            </div>
          </div>
        </div>
        <nav>
          <div class="nav">
            <div class="wp">
              <ul>
                <li  >
                  <router-link to="/" class="list-group-item">首页</router-link>
                </li>
                <li  >
                  <router-link to="/courses/course_list" class="list-group-item">公开课</router-link>
                </li>
                <li  >
                  <router-link to="/orgs/teacher_list" class="list-group-item">授课教师</router-link>
                </li>
                <li  >
                  <router-link to="/orgs/org_list" class="list-group-item">授课机构</router-link>
                </li>
              </ul>
            </div>
          </div>
        </nav>
      </div>
    </header>
  </section>
    <router-view ></router-view>
  </div>
</template>

<script>
  import axios from 'axios'
export default {
  data() {
    return {
      showUserScale: false,
      timer: '',
      searchKeywords: '',
      user : null,
    }
  },
  mounted: function () {
    // 发送请求获取 data
    axios({
      url: "/api/users/get_user/",
      method: "GET",
    })
      .then(respanse => {
        let res = respanse.data;
        if (res.user!=null){
          this.user = JSON.parse(res.user)[0].fields
        }
      })
      .catch(function(error) {
        console.log(error);
      });
  },
  methods: {

    getImgUrl: (bannerUrl) =>{
      return "../../static/media/" + bannerUrl
    },
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
          console.log(res)
          if (res.errMsg == "ok") {
            // this.$router.push(`/`);
            // location.reload()
            this.user=null
          } else {
            alert(res.errMsg);
          }
        })
        .catch(function(error) {
          console.log(error);
        });
    },
  },
};
</script>
<style scoped>

  a{
    cursor:pointer;
  }
  [v-cloak] {
    display:none !important;
  }
</style>
