<template>
  <div class="messagelist">
    {% for teacher in teacher_list %}
    <div class="butler_list butler-fav-box">
      <dl class="des users">
        <dt>
          <a href="{% url 'orgs:teacher_detail' teacher.id %}">
            <img width="100" height="100" src="{{ MEDIA_URL }}{{ teacher.image }}">
          </a>
        </dt>
        <dd>
          <h1>
            <a href="{% url 'orgs:teacher_detail' teacher.id %}">
              {# {{ teacher.name }}
              <span class="key">认证教师</span>
              #}
              {{ teacher.name }}
            </a>
          </h1>
          <ul class="cont clearfix">
            <li class="time">
              工作年限：
              <span>{{ teacher.work_year }}年</span>
            </li>
            <li class="c7">
              课程数：
              <span>{{ teacher.courseinfo_set.count }}</span>
            </li>
          </ul>
          <ul class="cont clearfix">
            <li class="time">
              工作公司：
              <span>{{ teacher.work_company.name }}</span>
            </li>
            <li class="c7">
              公司职位：
              <span>{{ teacher.work_position }}</span>
            </li>
          </ul>
        </dd>
        <div class="delete jsDeleteFav_teacher" data-favid="{{ teacher.id }}"></div>
      </dl>
    </div>

    {% endfor %}
  </div>
</template>
<script>
export default {};
</script>
<style scoped>
</style>
