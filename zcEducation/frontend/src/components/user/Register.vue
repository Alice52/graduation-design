<template>
  <section class="loginbg">
    <div class="c-box bg-box">
      <div class="login-box clearfix">
        <div class="hd-login clearfix">
          <h1>用户注册</h1>
          <a class="index-font" href="/">回到首页</a>
        </div>
        <div class="fl slide">
          <div class="imgslide">
            <ul class="imgs">
              <li>
                <a href>
                  <img width="483" height="472" src="../../../static/images/mysql.jpg">
                </a>
              </li>

              <li>
                <a href>
                  <img width="483" height="472" src="../../../static/images/mongoDB.jpg">
                </a>
              </li>

              <li>
                <a href>
                  <img width="483" height="472" src="../../../static/images/mysql.jpg">
                </a>
              </li>
            </ul>
          </div>
          <div class="unslider-arrow prev"></div>
          <div class="unslider-arrow next"></div>
        </div>
        <div class="fl form-box">
          <div class="tab">
            <h2>邮箱注册</h2>
          </div>

          <div class="tab-form">
            <form
              id="email_register_form"
              autocomplete="off"
            >
              <!--{% csrf_token %}-->
              <div class="form-group marb20">
                <label>邮&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;箱</label>
                <input type="text" id="id_email" name="email" placeholder="请输入您的邮箱地址" v-model="email">
              </div>
              <div class="form-group marb8">
                <label>密&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;码</label>
                <input
                  type="password"
                  id="id_password"
                  name="password"
                  placeholder="请输入6-20位非中文字符密码"
                  v-model="password"
                >
              </div>
              <div class="form-group marb8 captcha1">
                <label>验&nbsp;证&nbsp;码</label>
                <input v-model="verifyCode" autocomplete="off" id="id_captcha_1_1" name="captcha_1" type="text" />
                <div class="code" @click="refreshCode">
                  <s-idintity :identifyCode="identifyCode"></s-idintity>
                </div>
              </div>
              <div class="error btns" id="jsEmailTips">
                {{ errMsg }}
              </div>
              <div class="auto-box marb8"></div>
              <input class="btn btn-green" id="jsEmailRegBtn" @click="userRegister" value="注册并登录">
            </form>
          </div>
          <p class="form-p">
            已有账号？
            <a @click="$router.push(`/users/user_login`)">[立即登录]</a>
          </p>
        </div>
      </div>
    </div>
  </section>
</template>
<script>
  import '../../../static/js/validateDialog.js'
  import '../../../static/js/login.js'
  import axios from 'axios'
  import Qs from 'qs'
  import SIdintity from '../identity'

  export default {
    components:{
      SIdintity
    },
    data() {
      return {
        captcha:'',
        errMsg:'',
        email: '',
        password:'',
        identifyCodes: "1234567890",
        identifyCode: "", // os
        verifyCode: '', // manual
      }
    },

    mounted() {
      this.identifyCode = "";
      this.makeCode(this.identifyCodes, 4);
    },

  methods:{
    userRegister(){
        this.errMsg = ''
        if (this.verifyCode === this.identifyCode) {
          var data = Qs.stringify({"email":this.email, "password":this.password});
          axios({
            url: "/api/users/user_register/",
            method: "POST",
            data: data,
            headers: {
              "Content-Type": "application/x-www-form-urlencoded"
            }
          })
            .then(respanse => {
              let res = respanse.data;
              this.errMsg = res.errMsg
            })
            .catch(function(error) {
              console.log(error);
            });
        } else {
          this.errMsg = '验证码错误'
        }
      },

      randomNum(min, max) {
        return Math.floor(Math.random() * (max - min) + min);
      },
      refreshCode() {
        this.identifyCode = "";
        this.makeCode(this.identifyCodes, 4);
      },
      makeCode(o, l) {
        for (let i = 0; i < l; i++) {
          this.identifyCode += this.identifyCodes[
            this.randomNum(0, this.identifyCodes.length)
            ];
        }
        console.log(this.identifyCode);
      }
    }
  };
</script>
<style scoped>
  @import "../../../static/css/reset.css";
  @import "../../../static/css/login.css";

  #jsEmailRegBtn{
   text-indent: 108px;
  }
  .loginbg{
    background-color: green;
    width: 100%;
    height: 100%;
  }
</style>
