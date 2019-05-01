<template>
  <section class="loginbg">
    <div class="c-box bg-box">
      <div class="login-box clearfix">
        <div class="hd-login clearfix">
          <a class="index-logo" href="/"></a>
          <h1>修改密码</h1>
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
          <h2>通过验证，请修改密码</h2>
          <form id="reset_password_form" >
            <div class="form-group marb20">
              <label>新 密 码</label>
              <input name="password" id="pwd" type="password" placeholder="6-20位非中文字符" v-model="password">
            </div>
            <div class="form-group marb20">
              <label>确定密码</label>
              <input name="password1" id="repwd" type="password" placeholder="6-20位非中文字符" v-model="password1">
            </div>
            <div class="error btns login-form-tips" id="jsLoginTips">
              {{ errMsg }}
            </div>
            <input class="btn btn-green" id="jsEmailRegBtn" value="确认修改" @click="userRest">
          </form>

          <p class="form-p">
            立即登录
            <a @click="$router.push(`/users/user_login`)">[立即登录]</a>
          </p>
        </div>
      </div>
    </div>
  </section>
</template>
<script>
  import axios from 'axios'
  import Qs from 'qs'

  export default {
    data() {
      return {
        errMsg:'',
        password:'',
        password1:'',
      }
    },
    methods:{
      userRest() {
        if(this.password == this.password1){
          var data = Qs.stringify({"password": this.password,"password1": this.password1})
          axios({
            url: `/api/${this.$router.history.current.fullPath}`,
            method: "POST",
            data: data,
            headers: {
              "Content-Type": "application/x-www-form-urlencoded"
            }
          }).then(respanse => {
            let res = respanse.data;
            console.log(res)
            if (res.errMsg == 'ok'){
              this.$router.push('/users/user_login')
            } else {
              this.errMsg = res.errMsg
            }
          }).catch(function(error) {
              console.log(error);
            });
        } else {
          this.errMsg = '两次输入密码不同'
        }
      }
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
  #jsEmailRegBtn {
    text-indent: 108px;
  }
</style>
