<template>
  <section class="loginbg">
    <div class="c-box bg-box">
      <div class="login-box clearfix">
        <div class="hd-login clearfix">
          <a class="index-logo"  @click="$router.push(`/`)" ></a>
          <h1>用户登录</h1>
          <a class="index-font"  @click="$router.push(`/`)" >回到首页</a>
        </div>
        <div class="fl slide">
          <div class="imgslide">
            <ul class="imgs">
              <li>
                  <img width="483" height="472" src="../../../static/images/mysql.jpg">
              </li>
            </ul>
          </div>
        </div>
        <div class="fl form-box">
          <h2>帐号登录</h2>
          <div autocomplete="off">
            <!-- {% csrf_token %} -->
            <div class="form-group marb20">
              <label>邮 箱</label>
              <input
                name="username"
                id="account_l"
                type="text"
                v-model="username"
                placeholder="请输入您的邮箱"
              >
            </div>
            <div class="form-group marb8">
              <label>密&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;码</label>
              <input
                name="password"
                id="password_l"
                type="password"
                v-model="password"
                placeholder="请输入您的密码"
              >
            </div>
            <div class="error btns login-form-tips" id="jsLoginTips">
              {{ errMsg }}
            </div>
            <div class="auto-box marb38">
              <a class="fr"  @click="$router.push(`/users/user_forget`)">忘记密码？</a>
            </div>
            <input class="btn btn-green btlogin" id="jsLoginBtn" @click="login" value="立即登录 > ">
          </div>
          <p class="form-p">
            没有617室 ZC在线学习平台？
            <a  @click="$router.push(`/users/user_register`)">[立即注册]</a>
          </p>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import axios from "axios";
import Qs from 'qs'

export default {
  data() {
    return {
      errMsg: "",
      username: "",
      password: ""
    };
  },
  methods: {
    login () {
      var data = Qs.stringify({"username":this.username, "password":this.password});
      axios({
        url: "/api/users/user_login/",
        method: "POST",
        data: data,
        headers: {
          "Content-Type": "application/x-www-form-urlencoded"
        }
      })
        .then(respanse => {
          let res = respanse.data;
          if (res.errMsg == "ok") {
            let url = res.url;
            this.$router.push(`${url}`);
          } else {
            this.errMsg = res.errMsg;
          }
        })
        .catch(function(error) {
          console.log(error);
        });
    }
  }
};
</script>

<style scoped>
.loginbg{
  background-color: green;
  width: 100%;
  height: 100%;
}
.btlogin {
  text-indent: 108px;
}
</style>
