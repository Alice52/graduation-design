<template>
  <div>
    <UserHeader :user="user"/>
    <section>
      <div class="wp">
        <ul  class="crumbs">
          <li><a href="/">首页</a>></li>
          <li><a @click="$router.push(`/users/user_info/`)" >个人中心</a></li>
          <li>个人信息</li>
        </ul>
      </div>
    </section>
    <section>
      <div class="wp list personal_list">
        <div class="left">
          <ul>
            <li class="active2"><a @click="$router.push(`/users/user_info/`)"  >个人资料</a></li>
            <li ><a @click="$router.push(`/users/user_courses/`)" >我的课程</a></li>
            <li ><a href="usercenter-fav-course.html">我的收藏</a></li>
            <!--<li >-->
              <!--<a href="usercenter-message.html" style="position: relative;">-->
                <!--我的消息-->
              <!--</a>-->
            <!--</li>-->
          </ul>
        </div>
        <div class="right">
          <div class="personal_des ">
            <div class="head" >
              <h1>个人信息</h1>
            </div>
            <div class="inforcon">
              <div class="left" style="width:240px;">
                <iframe id='frameFile' name='frameFile' style='display: none;'></iframe>
                <form class="clearfix" id="jsAvatarForm" enctype="multipart/form-data" autocomplete="off" method="post" action="{% url 'users:user_changeimage' %}" target='frameFile'>
                  <label class="changearea" for="avatarUp">
                      <span id="avatardiv" class="pic">
                          <img width="100" height="100" class="js-img-show" id="avatarShow" v-if="user!=null" :src="getUserImgUrl(user.image)"/>
                      </span>
                      <span class="fl upload-inp-box" style="margin-left:70px;">
                          <span class="button btn-green btn-w100" id="jsAvatarBtn">修改头像</span>
                          <input type="file" name="image" id="avatarUp" class="js-img-up"/>
                      </span>
                  </label>
                </form>
                <div style="border-top:1px solid #eaeaea;margin-top:30px;">
                  <a class="button btn-green btn-w100" id="jsUserResetPwd" style="margin:80px auto;width:100px;">修改密码</a>
                </div>
              </div>
              <form class="perinform" id="jsEditUserForm" autocomplete="off">
                <ul class="right">
                  <li>昵&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;称：
                    <input type="text" name="nick_name" id="nick_name" maxlength="10" v-if="user!=null" v-model="user.nike_name">
                    <i class="error-tips"></i>
                  </li>
                  <li>生&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;日：
                    <input type="text" id="birth_day" name="birday"  readonly="readonly" v-if="user!=null" v-model="user.birthday"/>
                    <i class="error-tips"></i>
                  </li>
                  <li>性&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;别：
                    <label>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<input :checked="isBoy" type="radio"  name="gender" value="boy" v-if="user!=null" v-model="user.gender">男</label>
                    <label>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<input :checked="isGirl" type="radio" name="gender" value="girl" v-if="user!=null" v-model="user.gender" >女</label>
                  </li>
                  <li class="p_infor_city">地&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;址：
                    <input type="text" name="address" id="address" placeholder="请输入你的地址" v-if="user!=null" v-model="user.address" maxlength="10">
                    <i class="error-tips"></i>
                  </li>
                  <li>手&nbsp;&nbsp;机&nbsp;&nbsp;号：
                    <input type="text" name="mobile" id="mobile" placeholder="请输入你的手机号码" v-if="user!=null" v-model="user.phone" maxlength="11">
                  </li>
                  <li>邮&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;箱：
                    <input class="borderno" type="text" name="email" readonly="readonly" v-if="user!=null" v-model="user.email"/>
                    <span class="green changeemai_btn">[修改]</span>
                  </li>
                  <li class="button heibtn">
                    <input type="button" id="jsEditUserBtn" value="保存">
                  </li>
                </ul>
                <input type='hidden' name='csrfmiddlewaretoken' value='799Y6iPeEDNSGvrTu3noBrO4MBLv6enY' />
              </form>
            </div>
          </div>
        </div>
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
        isBoy: '', // checked
        isGirl: '',
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
          // 得到 user 设置 isBody
          if(this.user.gender == 'boy') {
            this.isBody = 'checked'
            this.isGirl = ''
          } else {
            this.isGirl = 'checked'
            this.isBody = ''
          }
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
</style>
