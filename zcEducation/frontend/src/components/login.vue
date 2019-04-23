<template>
  <section>
    <div class="c-box bg-box">
      <div class="login-box clearfix">
        <div class="hd-login clearfix">
          <a class="index-logo" href="/"></a>
          <h1>用户登录</h1>
          <a class="index-font" href="/">回到首页</a>
        </div>
        <div class="fl slide">
          <div class="imgslide">
            <ul class="imgs">
              <li>
                <a href>
                  <img width="483" height="472" src="../../static/images/mysql.jpg">
                </a>
              </li>
              <li>
                <a href>
                  <img width="483" height="472" src="../../static/images/mongoDB.jpg">
                </a>
              </li>
            </ul>
          </div>
          <div class="unslider-arrow prev"></div>
          <div class="unslider-arrow next"></div>
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
              <!-- {% for key, err in user_login_from.errors.items %}
                {{ err }}
              {% endfor %}-->
            </div>
            <div class="auto-box marb38">
              <a class="fr" href="http://www.zc-education.top:8000/users/user_forget">忘记密码？</a>
            </div>
            <input class="btn btn-green btlogin" id="jsLoginBtn" @click="login" value="立即登录 > ">
          </div>
          <p class="form-p">
            没有617室 ZC在线学习平台？
            <a href="http://www.zc-education.top:8000/users/user_register">[立即注册]</a>
          </p>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import "../../static/js/unslider.js";
import "../../static/js/login.js";
// import "../../static/js/ajax_post_csrf.js";
import axios from "axios";
export default {
  name: "login",
  data() {
    return {
      errMsg: "",
      username: "",
      password: ""
    };
  },
  methods: {
    login() {
      // 发送请求，提交登录数据
      // OK, 跳转 index
      // failed 显示本界面
      var userInfo = {
        username: this.username,
        password: this.password
      };

      axios({
        url: "http://www.zc-education.top:8000/users/user_login/",
        method: "POST",
        data: userInfo,
        headers: {
          "Content-Type": "application/x-www-form-urlencoded"
        }
      })
        .then(respanse => {
          let res = respanse.data;
          if (res.errMsg == "ok") {
            let url = res.url;
            window.location.href = "http://www.zc-education.top:8000/";
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
.btlogin {
  text-indent: 108px;
}
</style>
