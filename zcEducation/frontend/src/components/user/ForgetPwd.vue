<template>
  <section class="loginbg">
    <div class="c-box bg-box">
      <div class="login-box clearfix">
        <div class="hd-login clearfix">
          <a class="index-logo" href="/"></a>
          <h1>忘记密码</h1>
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
          <h2>忘记密码</h2>
          <form
            id="jsFindPwdForm"
            autocomplete="off"
          >
            <div class="form-group marb20">
              <label>帐&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;号</label>
              <input type="text" id="account" name="email" placeholder="请输入邮箱账号" v-model="email">
            </div>
            <div class="form-group captcha1 marb38">
              <label>验&nbsp;证&nbsp;码</label>
              <input v-model="verifyCode" autocomplete="off" id="id_captcha_1_1" name="captcha_1" type="text" />
              <div class="code" @click="refreshCode">
                <s-idintity :identifyCode="identifyCode"></s-idintity>
              </div>
            </div>
            <div class="error btns" id="jsForgetTips">
              {{ errMsg }}
            </div>
            <input type="hidden" name="sms_type" value="1">
            <input class="btn btn-green" id="jsFindPwdBtn" @click="userForget" value="提交">
            <p class="form-p" style="bottom:40px;">
              您还可以
              <a @click="$router.push(`/users/user_login`)" >[直接登录]</a>
            </p>
          </form>
        </div>
      </div>
    </div>
  </section>
</template>
<script>
  import SIdintity from '../identity'
  import axios from 'axios'
  import Qs from 'qs'

  export default {
    components:{
      SIdintity
    },
    data() {
      return {
        errMsg:'',
        email: '',
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
      },
      userForget() {
        this.errMsg = ''
        console.log(this.email)
        if (this.verifyCode === this.identifyCode) {
          var data = Qs.stringify({"email":this.email});
          axios({
            url: "/api/users/user_forget/",
            method: "POST",
            data: data,
            headers: {
              "Content-Type": "application/x-www-form-urlencoded"
            }
          })
            .then(respanse => {
              let res = respanse.data;
              console.log(res)
              this.errMsg = res.errMsg
              console.log(this.errMsg)
            })
            .catch(function(error) {
              console.log(error);
            });
        } else {
          this.errMsg = '验证码错误'
        }
      },
    }
  };
</script>
<style scoped>
  @import "../../../static/css/login.css";
  @import "../../../static/css/reset.css";
  .loginbg{
    background-color: green;
    width: 100%;
    height: 100%;
  }
  #jsFindPwdBtn {
    text-indent: 108px;
  }
</style>
