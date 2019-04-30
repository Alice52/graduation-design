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
            <li>
              <a href="{% url 'courses:course_detail' course.id %}">课程详情</a>>
            </li>
            <li>章节信息</li>
          </ul>
        </div>
      </div>
    </section>
    <div id="main">
      <div class="course-info-main clearfix w has-progress">
        <div class="info-bar clearfix">
          <div class="content-wrap clearfix">
            <div class="content">
              <div class="mod-tab-menu">
                <ul class="course-menu clearfix">
                  <li>
                    <a
                      class="ui-tabs-active active"
                      id="learnOn"
                      href="{% url 'courses:course_video' course.id %}"
                    >
                      <span>章节</span>
                    </a>
                  </li>
                  <li>
                    <a id="commentOn" class href="{% url 'courses:course_comment' course.id %}">
                      <span>评论</span>
                    </a>
                  </li>
                </ul>
              </div>
              <div id="notice" class="clearfix">
                <div class="l tnotice">
                  <strong>课程须知:</strong>
                  <a href="javascript:void(0)">{{ course.course_need }}</a>
                </div>
              </div>

              <div class="mod-chapters">
                {% for lesson in course.lessoninfo_set.all %}
                <div class="chapter chapter-active">
                  <h3>
                    <strong>
                      <i class="state-expand"></i>
                      {{ lesson.name }}
                    </strong>
                  </h3>
                  <ul class="video">
                    {% for video in lesson.videoinfo_set.all %}
                    <li>
                      <a
                        target="_blank"
                        href="{{MEDIA_URL }}{{ video.url }}"
                        class="J-media-item studyvideo"
                      >
                        {{ video.name }}
                        ({{ video.study_time }})
                        <i
                          class="study-state"
                        ></i>
                      </a>
                    </li>
                    {% endfor %}
                  </ul>
                </div>
                {% endfor %}
              </div>
            </div>
            <div class="aside r vedioright">
              <div class="bd">
                <div class="box mb40">
                  <h4>课程信息</h4>
                  <div class="course-info-tip">
                    <dl class="first">
                      <dt>课程名称：{{ course.name }}</dt>
                    </dl>
                    <dl class="first">
                      <dt>课程时长：{{ course.study_time }}分钟</dt>
                    </dl>
                    <dl class="first">
                      <dt>学习人数： {{ course.study_num }}</dt>
                    </dl>
                    <dl class="first">
                      <dt>如何学习:</dt>
                      <dd class="autowrap">&nbsp;&nbsp;&nbsp;{{ course.teacher_tell }}</dd>
                    </dl>
                  </div>
                </div>
                <div class="box mb40">
                  <h4>资料下载</h4>
                  <ul class="downlist">
                    {% for source in course.sourceinfo_set.all %}
                    <li>
                      <span>
                        <i class="aui-iconfont aui-icon-file"></i>
                        &nbsp;&nbsp;{{ source.name }}
                      </span>
                      <a
                        href="{{ MEDIA_URL }}{{ source.down_load }}"
                        class="downcode"
                        target="_blank"
                        download
                        data-id="274"
                        title
                      >下载</a>
                    </li>
                    {% endfor %}
                  </ul>
                </div>

                <div class="cp-other-learned js-comp-tabs">
                  <div class="cp-header clearfix">
                    <h2 class="cp-tit l">学过该课的同学还学过</h2>
                  </div>
                  <div class="cp-body">
                    <div
                      class="cp-tab-pannel js-comp-tab-pannel"
                      data-pannel="course"
                      style="display: block"
                    >
                      <!-- img 200 x 112 -->
                      <ul class="other-list">
                        {% for course1 in course_list %}
                        <li class="curr">
                          <a href="{% url 'courses:course_detail' course1.id %}" target="_blank">
                            <img width="240" src="{{ MEDIA_URL }}{{ course1.image }}">
                            <span class="name autowrap">{{ course1.name }}</span>
                          </a>
                        </li>
                        {% endfor %}
                      </ul>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="clear"></div>
        </div>
      </div>
    </div>
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
