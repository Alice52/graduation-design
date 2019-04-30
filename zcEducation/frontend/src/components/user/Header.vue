<template>
  <!--<section class="headerwrap">-->
    <!--<header>-->
      <!--<div class="header">-->
        <!--<div class="top">-->
          <!--<div class="wp">-->
            <!--&lt;!&ndash; TODO 判断用户是否登录状态 &ndash;&gt;-->
            <!--<div v-if="request.user.is_authenticated" class="personal">-->
              <!--<dl class="user fr">-->
                <!--<dd>-->
                  <!--{{ request.user.username }}-->
                  <!--<img-->
                    <!--class="down fr"-->
                    <!--src="{% static 'images/top_down.png' %}"-->
                  <!--&gt;-->
                <!--</dd>-->
                <!--<dt>-->
                  <!--<img width="30" height="30" src="{{ MEDIA_URL }}{{ request.user.image }}">-->
                <!--</dt>-->
              <!--</dl>-->
              <!--<div class="userdetail">-->
                <!--<dl>-->
                  <!--<dt>-->
                    <!--<img width="80" height="80" src="{{ MEDIA_URL }}{{ request.user.image }}">-->
                  <!--</dt>-->
                  <!--<dd>-->
                    <!--<p>{{ request.user.username }}</p>-->
                  <!--</dd>-->
                <!--</dl>-->
                <!--<div class="btn">-->
                  <!--<a class="personcenter fl" href="{% url 'users:user_info' %}">进入个人中心</a>-->
                  <!--<a class="fr" href="{% url 'users:user_logout' %}">退出</a>-->
                <!--</div>-->
              <!--</div>-->
            <!--</div>-->
            <!--<a-->
              <!--v-if="没有登录"-->
              <!--style="color:white"-->
              <!--class="fr registerbtn"-->
              <!--href="{% url 'users:user_register' %}"-->
            <!--&gt;注册</a>-->
            <!--<a-->
              <!--v-if="没有登录"-->
              <!--style="color:white"-->
              <!--class="fr loginbtn"-->
              <!--href="{% url 'users:user_login' %}"-->
            <!--&gt;登录</a>-->
          <!--</div>-->
        <!--</div>-->
        <!--<div class="middle">-->
        <!--<div class="wp">-->
            <!--<a href="/"><img class="fl" src="{% static 'images/logo1.png' %}"/></a>-->
            <!--<h1>617室 ZC在线学习平台</h1>-->
        <!--</div>-->
    <!--</div>-->
    <!--</header>-->
  <!--</section>-->
</template>

<script>
export default {
};
</script>
<style scoped>
</style>
