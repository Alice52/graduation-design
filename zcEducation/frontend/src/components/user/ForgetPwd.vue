<template>
  <section>
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
                  <img width="483" height="472" src="{% static 'images/mysql.jpg' %}">
                </a>
              </li>
              <li>
                <a href>
                  <img width="483" height="472" src="{% static 'images/mongoDB.jpg' %}">
                </a>
              </li>
              <li>
                <a href>
                  <img width="483" height="472" src="{% static 'images/mysql.jpg' %}">
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
            method="post"
            action="{% url 'users:user_forget' %}"
            autocomplete="off"
          >
            {% csrf_token %}
            <div class="form-group marb20">
              <label>帐&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;号</label>
              {#
              <input type="text" id="account" name="email" value="None" placeholder="邮箱">#}
              <input type="text" id="account" name="email" placeholder="请输入邮箱账号">
            </div>
            <div class="form-group captcha1 marb38">
              <label>验&nbsp;证&nbsp;码</label>
              {{ user_forget_form.captcha }}
            </div>
            <div class="error btns" id="jsForgetTips">
              {{ msg }}
              {% for key, err in user_forget_form.errors.items %}
              {{ err }}
              {% endfor %}
            </div>
            <input type="hidden" name="sms_type" value="1">
            <input class="btn btn-green" id="jsFindPwdBtn" type="submit" value="提交">
            <p class="form-p" style="bottom:40px;">
              您还可以
              <a href="{% url 'users:user_login' %}">[直接登录]</a>
            </p>
          </form>
        </div>
      </div>
    </div>
  </section>
</template>
<script>
export default {};
</script>
<style scoped>
</style>
