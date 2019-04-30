<template>
  <div>
    <section>
      <div class="wp">
        <div class="crumbs">
          <ul>
            <li>
              <a href="/">首页</a>>
            </li>
            <li>
              <a href="{% url 'courses:course_list' %}">公开课程</a>>
            </li>
            <li>课程详情</li>
          </ul>
        </div>
      </div>
    </section>
    <section>
      <div class="wp">
        <div class="groupPurchase_detail detail">
          <div class="toppro">
            <div class="left">
              <div class="picbox">
                <div class="tb-booth tb-pic">
                  <img
                    width="440"
                    height="445"
                    src="{{ MEDIA_URL }}{{ course.image }}"
                    class="jqzoom"
                  >
                </div>
              </div>
              <div class="des">
                <h1 title="{{ course.name }}">{{ course.name }}</h1>
                <span class="key">{{ course.desc }}</span>
                <div class="prize">
                  <span class="fl">
                    难度：
                    <i class="key">
                      {% if course.level == 'cj' %}
                      初级
                      {% elif course.level == 'zj' %}
                      中级
                      {% else %}
                      高级
                      {% endif %}
                    </i>
                  </span>
                  <span class="fr">学习人数：{{ course.study_num }}</span>
                </div>
                <ul class="parameter">
                  <li>
                    <span class="pram word3">时&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;长：</span>
                    <span>{{ course.study_time }}</span>
                  </li>
                  <li>
                    <span class="pram word3">章&nbsp;节&nbsp;数：</span>
                    <span>{{ course.lessoninfo_set.count }}</span>
                  </li>
                  <li>
                    <span class="pram word3">课程类别：</span>
                    <span title>
                      {% if course.category == 'qd' %}
                      前端开发
                      {% else %}
                      后端开发
                      {% endif %}
                    </span>
                  </li>
                  <li class="piclist">
                    <span class="pram word4">学习用户：</span>
                    {% for usercourse in course.usercourse_set.all|slice:":6" %}
                    <span
                      class="pic"
                    >
                      <img
                        width="40"
                        height="40"
                        src="{{ MEDIA_URL }}{{ usercourse.study_man.image }}"
                      >
                    </span>
                    {% endfor %}
                  </li>
                </ul>
                <div class="btns">
                  <div
                    class="btn colectgroupbtn"
                    id="jsLeftBtn"
                  >{% if lovecourse %}取消收藏{% else %}收藏{% endif %}</div>
                  <div class="buy btn">
                    <a style="color: white" href="{% url 'courses:course_video' course.id %}">开始学习</a>
                  </div>
                </div>
              </div>
            </div>
            <div class="right">
              <div class="head">
                <h1>授课机构</h1>
                <p>世界名校，课程权威</p>
              </div>
              <div class="pic">
                <a href="{% url 'orgs:org_detail' course.orginfo.id %}">
                  <img
                    width="130"
                    height="130"
                    style="margin-left: 10px"
                    src="{{ MEDIA_URL }}{{ course.orginfo.image }}"
                  >
                </a>
              </div>
              <a href="{% url 'orgs:org_detail' course.orginfo.id %}">
                <h2 class="center" title="{{ course.orginfo.name }}">{{ course.orginfo.name }}</h2>
              </a>
              <div
                class="btn notlogin"
                data-favid="14"
                id="jsRightBtn"
              >{% if loveorg %}取消收藏{% else %}收藏{% endif %}</div>
              <div class="clear">
                <ul>
                  <li>
                    <span>课 &nbsp;程&nbsp; 数：&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; {{ course.orginfo.course_num }}</span>
                  </li>
                  <li>
                    <span>教 &nbsp;师&nbsp; 数：&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; {{ course.orginfo.teacherinfo_set.count }}</span>
                  </li>
                  <li>所在地区：&nbsp;&nbsp;{{ course.orginfo.cityinfo.name }}</li>
                </ul>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
    <section>
      <div class="wp">
        <div class="list groupPurchase_detail_pro">
          <div class="left layout">
            <div class="head">
              <ul class="tab_header">
                <li class="active">课程详情</li>
              </ul>
            </div>
            <div class="tab_cont tab_cont1">
              <p>{{ course.detail }}</p>
            </div>
          </div>
          <div class="right layout">
            <div class="head">相关课程推荐</div>
            <div class="group_recommend">
              {% for relate in relate_courses %}
              <dl>
                <dt>
                  <a target="_blank" href="{% url 'courses:course_detail' relate.id %}">
                    <img
                      width="170"
                      height="130"
                      class="scrollLoading"
                      src="{{ MEDIA_URL }}{{ relate.image }}"
                    >
                  </a>
                </dt>
                <dd>
                  <a target="_blank" href="{% url 'courses:course_detail' relate.id %}">
                    <h2>{{ relate.name }}</h2>
                  </a>
                  <span class="fl">
                    学习时长：
                    <i class="key">{{ relate.study_time }}</i>
                  </span>
                </dd>
              </dl>
              {% endfor %}
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>
<script>
import HeaderWithSearch from "../HeaderWithSearch";
export default {
  components: {
    HeaderWithSearch
  }
};
</script>
<style scoped>
</style>
