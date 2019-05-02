<template>
  <div class="right">
    <div class="personal_des ">
      <div class="head">
        <h1>个人信息</h1>
      </div>
      <div class="inforcon">
        <div class="left" style="width:240px;">
          <span id="avatardiv" class="pic">
            <img @click="alertInput" width="100" height="100" class="js-img-show" id="avatarShow" v-if="user!=null"
                 :src="getUserImgUrl(user.image)"/>
          </span>
          <input @change="UserChangeImage" type="file" id="file"
                 style="filter:alpha(opacity=0);opacity:0;width: 0;height: 0;"/>
          <span class="button btn-green btn-w100" id="jsAvatarBtn" @click="alertInput">修改头像</span>
        </div>
        <form class="perinform" id="jsEditUserForm" autocomplete="off">
          <ul class="right">
            <li>昵&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;称：
              <input type="text" name="nick_name" id="nick_name" maxlength="10" v-if="user!=null"
                     v-model="user.nick_name">
              <i class="error-tips"></i>
            </li>
            <li>生&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;日：
              <input type="date" id="birth_day" name="birday" v-if="user!=null" v-model="user.birthday"/>
              <i class="error-tips"></i>
            </li>
            <li>性&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;别：
              <label>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<input :checked="user.gender=='boy'?'checked':''" type="radio"
                                                          name="gender" value="boy" v-if="user!=null"
                                                          v-model="user.gender">男</label>
              <label>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<input :checked="user.gender=='girl'?'checked':''" type="radio"
                                                          name="gender" value="girl" v-if="user!=null"
                                                          v-model="user.gender">女</label>
            </li>
            <li class="p_infor_city">地&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;址：
              <input type="text" name="address" id="address" placeholder="请输入你的地址" v-if="user!=null"
                     v-model="user.address" maxlength="10">
              <i class="error-tips"></i>
            </li>
            <li>手&nbsp;&nbsp;机&nbsp;&nbsp;号：
              <input type="text" name="mobile" id="mobile" placeholder="请输入你的手机号码" v-if="user!=null"
                     v-model="user.phone" maxlength="11">
            </li>
            <!--<li>邮&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;箱：-->
              <!--<input class="borderno" type="text" name="email" readonly="readonly" v-if="user!=null"-->
                     <!--v-model="user.email"/>-->
              <!--<span class="green changeemai_btn" @click="userChangeEmail">[修改]</span>-->
            <!--</li>-->
            <li class="button heibtn">
              <input class="button btn-green btn-w100" type="button" id="jsEditUserBtn" @click="UserChangeInfo"
                     value="保存">
            </li>
          </ul>
          <input type='hidden' name='csrfmiddlewaretoken' value='799Y6iPeEDNSGvrTu3noBrO4MBLv6enY'/>
        </form>
      </div>
    </div>
  </div>
</template>
<script>
  import axios from 'axios';
  import Qs from 'qs'

  export default {
    props: [
      'user'
    ],
    data() {
      return {}
    },

    methods: {
      getUserImgUrl: (bannerUrl) => {
        console.log(bannerUrl)
        return "../../static/media/" + bannerUrl
      },
      UserChangeInfo() {
        var data = Qs.stringify(this.user)

        axios({
          url: '/api/users/user_changeinfo/',
          method: 'POST',
          data: data,
          headers: {
            "Content-Type": "application/x-www-form-urlencoded"
          }
        }).then(response => {
          var res = response.data
          console.log(res)
          if (res.status == 'ok') {

          } else {
            alert('修改失败，请重试')
          }
        }).catch(err => {
          console.log(err)
        })
      },
      alertInput() {
        document.getElementById('file').click();
      },
      UserChangeImage() {
        // let reader =new FileReader();
        let img1 = event.target.files[0];
        let size = img1.size;//文件的大小，判断图片的大小
        if (size > 3145728) {
          alert('请选择3M以内的图片！');
          return false;
        }

        var uri = ''
        let form = new FormData();
        form.append('image', img1, img1.name);
        axios({
          url: '/api/users/user_changeimage/',
          method: "POST",
          data: form,
          headers: {
            "Content-Type": "application/x-www-form-urlencoded"
          }
        }).then(response => {
          var res = response.data
          console.log(res)
          if (res.status == 'ok') {
            this.user.image = 'user/' + img1.name
          }
        }).catch(err => {
          console.log(err)
        })
      },
      userChangeEmail() {

      },
    },
  }
</script>
<style>
  @import "../../../static/css/reset.css";
  @import "../../../static/css/animate.css";
  @import "../../../static/css/style.css";
  .personal_list .inforcon .right li input[type=date] {
    color: #3d3d3d;
    height: 30px;
    line-height: 30px;
    margin-left: 20px;
    text-indent: 10px;
    width: 300px;
    background: #fafafa;
  }
  .personal_list .inforcon .right > li, .inputs li {
    height: 55px;
    line-height: 50px;
    border-bottom: 1px solid #eaeaea;
    text-indent: 20px;
    color: #a9a9a9;
    position: relative;
  }
</style>
