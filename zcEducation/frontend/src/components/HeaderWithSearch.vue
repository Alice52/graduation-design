<template>
  <section class="headerwrap">
    <header>
      <div class="header">
        <div class="top">
          <div class="wp">
            <!-- TODO 判断用户是否登录状态 -->
            <div v-if="user!=null" class="personal">
              <dl class="user fr">
                <dd>
                  {{ user.username }}
                  <img
                    class="down fr"
                    src="../../static/images/top_down.png"
                  >
                </dd>
                <dt>
                  <img width="30" height="30" :src="getImgUrl(user.image)">
                </dt>
              </dl>
              <div class="userdetail">
                <dl>
                  <dt>
                    <img width="80" height="80" :src="getImgUrl(user.image)">
                  </dt>
                  <dd>
                    <p>{{ user.username }}</p>
                  </dd>
                </dl>
                <div class="btn">
                  <a class="personcenter fl" @click="$router.push(`/user/user_info`)" >进入个人中心</a>
                  <a class="fr"  @click="$router.push(`/user/user_logout`)">退出</a>
                </div>
              </div>
            </div>
            <a
              v-if="user==null"
              style="color:white"
              class="fr registerbtn"
              @click="$router.push(`/user/user_register`)"
            >注册</a>
            <a
              v-if="user==null"
              style="color:white"
              class="fr loginbtn"
              @click="$router.push(`/user/user_login`)"
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
                <ul class="selectMenu" id="jsSelectMenu">
                  <li data-value="course">公开课</li>
                  <li data-value="org">课程机构</li>
                  <li data-value="teacher">授课老师</li>
                </ul>
              </div>
              <input id="search_keywords" class="fl" type="text" value placeholder="请输入搜索内容">
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
                <li class="active">
                  <a href="/">首页</a>
                </li>
                <li class="active">
                  <a @click="$router.push(`/courses/course_list`)">
                    公开课
                  </a>
                </li>
                <li class="active">
                  <a @click="$router.push(`/orgs/teacher_list`)" >授课教师</a>
                </li>
                <li class="active">
                  <a @click="$router.push(`/orgs/org_list`)" >授课机构</a>
                </li>
              </ul>
            </div>
          </div>
        </nav>
      </div>
    </header>
  </section>
</template>

<script>
export default {
  data() {
    return {
    }
  },
  methods: {
    getImgUrl: (bannerUrl) =>{
      return "../../static/media/" + bannerUrl
    }
  },
  props:[
    'user'
  ],
};
</script>
<style scoped>
</style>
