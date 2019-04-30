<template>
  <div>
    <Header/>
    <section>
      <div class="wp">
        <ul class="crumbs">
          <li>
            <a href="/">首页</a>>
          </li>
          <li>
            <a href="{% url 'users:user_info' %}">个人中心</a>>
          </li>
          <li>{% block breach %}{% endblock %}</li>
        </ul>
      </div>
    </section>
    <section>
      <div class="wp list personal_list">
        <div class="left">
          <ul>
            <li class="active2">
              <a href="{% url 'users:user_info' %}">个人资料</a>
            </li>
            <li class="active2">
              <a href="{% url 'users:user_course' %}">我的课程</a>
            </li>
            <li class="active2">
              <a href="{% url 'users:user_loveorg' %}">我的收藏</a>
            </li>
          </ul>
        </div>

        <router-view></router-view>
      </div>
    </section>
  </div>
</template>

<script>
import Header from "./Header";
export default {
  components: {
    Header
  }
};
</script>

<style scoped>
</style>
