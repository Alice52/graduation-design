<template>
  <section>
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
          <h2>通过验证，请修改密码</h2>
          <form id="reset_password_form" action="{% url 'users:user_reset' code %}" method="post">
            {% csrf_token %}
            <div class="form-group marb20">
              <label>新 密 码</label>
              <input name="password" id="pwd" type="password" placeholder="6-20位非中文字符">
            </div>
            <div class="form-group marb20">
              <label>确定密码</label>
              <input name="password1" id="repwd" type="password" placeholder="6-20位非中文字符">
            </div>
            <input class="btn btn-green" type="submit" value="确认修改">
            <div class="error btns login-form-tips" id="jsLoginTips">
              {{ msg }}
              {% for key, err in user_reset_from.errors.items %}
              {{ err }}
              {% endfor %}
            </div>
          </form>

          <p class="form-p">
            立即登录
            <a href="{% url 'users:user_login' %}">[立即登录]</a>
          </p>
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
