<template>
  <div>
    <section class="headerwrap">
      <header>
        <div class="header">
          <div class="top">
            <div class="wp">
              <!-- TODO 判断用户是否登录状态 -->
              <div v-if="user!=null" class="personal">
                <dl @mouseenter="enter()" @mouseleave="leave()" class="user fr">
                  <dd>
                    {{user.username}}
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
                      <p>{{user.username}}</p>
                    </dd>
                  </dl>
                  <div class="btn">
                    <a class="personcenter fl" @click="$router.push(`/users/user_info`)">进入个人中心</a>
                    <a class="fr" @click="userLogout">退出</a>
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
          <div class="middle companyheader">
            <div class="wp">
              <img class="fl" style="width: 112px;height: 103px" :src="getImgUrl(org.fields.image)"/>
              <div class="head fl">
                <h1>
                  {{org.fields.name}}
                </h1>
                <p class="fl">
                  <span class="fl" style="margin-top:8px;color:#848484;">推荐指数： </span>
                  <span class="precision company-credit" data-star-scope="5.0" title="非常满意" style="width: 140px;">
                    <img src="../../../static/images/r_star.png" alt="1" title="非常满意">&nbsp;
                    <img src="../../../static/images/r_star.png" alt="2" title="非常满意">&nbsp;
                    <img src="../../../static/images/r_star.png" alt="3" title="非常满意">&nbsp;
                    <img src="../../../static/images/r_star.png" alt="4" title="非常满意">&nbsp;
                    <img src="../../../static/images/r_star.png" title="非常满意">
                    <input type="hidden" name="score" value="5" readonly="readonly">
                  </span>
                  <span class="key">5.0</span>
                </p>
              </div>
              <div v-if="lovestatus" class="btn fr collectionbtn  notlogin" @click="CancelLove(org.pk, 1)">取消收藏</div>
              <div v-else class="btn fr collectionbtn  notlogin" @click="CancelLove(org.pk, 1)">收藏</div>
            </div>
          </div>
        </div>
      </header>
    </section>
    <section>
      <div class="wp">
        <ul class="crumbs">
          <li><a href="/">首页</a>></li>
          <li><a @click="$router.push(`/orgs/org_list`)">课程机构</a>></li>
        </ul>
      </div>
    </section>
    <section>
      <div class="wp list personal_list comp">
        <div class="left">
          <ul>
            <li>
              <router-link  :to="'/orgs/org_detail_home/'+org.pk">机构首页</router-link>
            </li>
            <li>
              <router-link   :to="'/orgs/org_detail_course/'+org.pk">机构课程</router-link>
            </li>
            <li>
              <router-link   :to="'/orgs/org_detail_desc/'+org.pk">机构介绍</router-link>
            </li>
            <li>
              <router-link   :to="'/orgs/org_detail_teacher/'+org.pk">机构讲师</router-link>
            </li>
          </ul>
        </div>
        <router-view></router-view>
      </div>
    </section>
  </div>
</template>

<script>
  import axios from 'axios'

  export default {
    name: "OrgHeader",
    data() {
      return {
        org: '',
        showUserScale: false,
        timer: '',
        lovestatus: '',
        user: "",
        org: '',
      }
    },
    methods: {
      getImgUrl: (bannerUrl) => {
        return "../../static/media/" + bannerUrl
      },
      enter() {
        this.showUserScale = true
        if (this.timer != null) {
          clearTimeout(this.timer);
        }
      },
      leave() {
        this.timer = setTimeout(() => {
          this.showUserScale = false
        }, 100)
      },
      leave2() {
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
              this.user = null
            } else {
              alert(res.errMsg);
            }
          })
          .catch(function (error) {
            console.log(error);
          });
      },
      CancelLove(favId, type){
        // 1: 机构
        // 2： 课程
        // 3： 老师
        axios({
          url: '/api/operations/user_love/',
          method: 'GET',
          params: {"loveid": favId,"lovetype": type}
        }).then((response)=>{
          var res = response.data
          console.log(res)
          if (res.status == 'ok') {
            if (type == 1) {
              this.lovestatus = !this.lovestatus
            } else {
              alert(res.msg)
            }
          } else {
            alert(res.msg)
          }
        })
      }
    },
    mounted() {
      axios({
        url: `/api/orgs/org_header/${this.$route.params.pathMatch}/`,
        method: "GET",
      })
        .then(respanse => {
          let res = respanse.data;
          if (res.user != null) {
            this.user = JSON.parse(res.user)[0].fields
          }
          this.lovestatus = res.lovestatus
          this.org = JSON.parse(res.org)[0]

          console.log(this.user)
          console.log(this.org_id)
        })
        .catch(function (error) {
          console.log(error);
        });
    }

  }
</script>

<style scoped>
.router-link-active{
  background: #fff url(../../../static/images/arrow_g.png) no-repeat 85% center;
  color: red !important;
}
.personal_list .left a{
  width: 100%;
  padding: 0 5%;
  height: 100%;
  display: block;
  color: #3a3a3a;
  margin: 0;

}
</style>
