<template>
  <div v-if="showComponent">
    <section v-cloak class="headerwrap">
    <header>
      <div class="header">
        <div class="top">
          <div class="wp">
            <!-- TODO 判断用户是否登录状态 -->
            <div v-if="user!=null" class="personal">
              <dl @mouseenter="enter(1)" @mouseleave="leave()" class="user fr">
                <dd >
                  {{user.username}}
                </dd>
                <dt>
                  <img width="30" height="30" :src="getImgUrl(user.image)">
                </dt>
              </dl>
              <div @mouseenter="enter(1)" @mouseleave="leave2()" v-show="showUserScale" class="userdetail">
                <dl>
                  <dt>
                    <img width="80" height="80" :src="getImgUrl(user.image)">
                  </dt>
                  <dd>
                    <p>{{user.username}}</p>
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
              style="color:white; text-decoration: none;"
              class="fr registerbtn"
              @click="$router.push(`/users/user_register`)"
            >注册</a>
            <a
              v-if="user==null"
              style="color:white; text-decoration: none;"
              class="fr loginbtn"
              @click="$router.push(`/users/user_login`)"
            >登录</a>
          </div>
        </div>
        <div class="middle">
          <div class="wp">
            <a  @click="$router.push(`/`)" >
              <img class="fl logo" src="../../static/images/logo1.png">
            </a>
            <div class="searchbox fr">
              <div class="selectContainer fl">
                <span class="selectOption" id="jsSelectOption" data-value="course" @mouseenter="enter(2)" @mouseleave="leave()">公开课</span>
                <ul v-if="showDropdownList" class="selectMenu"  @mouseenter="enter(2)" @mouseleave="leave2()">
                  <li  @click="selectType('course')">公开课</li>
                  <li  @click="selectType('org')">课程机构</li>
                  <li  @click="selectType('teacher')">授课老师</li>
                </ul>
              </div>
              <input id="search_keywords" class="fl" type="text" value placeholder="请输入搜索的课程" v-model="keyword">
              <img class="search_btn fr" id="jsSearchBtn" src="../../static/images/search_btn.png" @click="SearchCourse">
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
    <keep-alive>
      <router-view></router-view>
    </keep-alive>
  </div>
</template>

<script>
  import axios from 'axios'
export default {
  data() {
    return {
      showUserScale: false,
      timer: '',
      keyword: '',
      user : null,
      showDropdownList: false,
      showComponent: false,
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
        this.showComponent = true
      })
      .catch(function(error) {
        console.log(error);
      });
  },
  methods: {

    getImgUrl: (bannerUrl) =>{
      return "../../static/media/" + bannerUrl
    },
    enter(type){
      if (type == 1) {
        this.showUserScale = true
      } else {
        this.showDropdownList = true
      }
      if (this.timer != null){
        clearTimeout(this.timer);
      }
    },
    leave(){
      this.timer = setTimeout(()=>{
          this.showUserScale = false
          this.showDropdownList = false
      }, 100)
    },
    leave2(){
        this.showUserScale = false
        this.showDropdownList = false
    },
    userLogout() {
      axios({
        url: "/api/users/user_logout/",
        method: "GET",
      })
        .then(respanse => {
          let res = respanse.data;
          if (res.errMsg == "ok") {
            this.user=null
          } else {
            alert(res.errMsg);
          }
        })
        .catch(function(error) {
          console.log(error);
        });
    },
    selectType(type) {
      var targetDom = document.querySelector('#jsSelectOption');
      targetDom.setAttribute('data-value', type)
      if (type == 'course') {
        targetDom.innerHTML = '公开课'
        this.showDropdownList = !this.showDropdownList
      } else if (type == 'org'){
        targetDom.innerHTML = '课程机构'
        this.showDropdownList = !this.showDropdownList
      } else {
        // teacher
        targetDom.innerHTML = '授课老师'
        this.showDropdownList = !this.showDropdownList
      }
    },

    SearchCourse() {
      var targetDom = document.querySelector('#jsSelectOption');
      var type = targetDom.getAttribute('data-value')
      if (type == 'course') {
        // this.$router.push({name: 'courseList', params: {keyword: this.keyword}}) // 被路由器分配之后, 当前路由没有变化
        this.$router.push({path: '/courses/course_list', query: {keyword: this.keyword}}) // 被路由器分配之后, 当前路由变化
      } else if (type == 'org'){
        this.$router.push({path: '/orgs/org_list', query: {keyword: this.keyword}}) // 被路由器分配之后, 当前路由变化
      } else {
        // teacher
        this.$router.push({path: '/orgs/teacher_list', query: {keyword: this.keyword}}) // 被路由器分配之后, 当前路由变化
      }
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
  .router-link-exact-active {
    background: #3D9328 !important;
  }
  .selectOption {
    color: black;
    background: url(../../static/images/select_arrow.png) no-repeat 93% 50%;
    display: block;
    cursor: pointer;
    text-align: center;
  }
  .selectMenu {
     width: 91px;
     border: 1px solid black;
     background: #fff;
     display: block;
    overflow: hidden;
    margin-left: -7px;
    margin-top: 6px;
    position: relative;
    z-index: 99;
  }
</style>
