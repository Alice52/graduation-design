<template>
  <div v-if="showComponent">
    <section>
      <div class="wp">
        <div class="crumbs">
          <ul>
            <li><a @click="$router.push(`/`)">首页</a>&gt;</li>
            <li><a @click="$router.push(`/courses/course_list`)">公开课程</a>&gt;</li>
            <li><a @click="$router.push(`/courses/course_detail/${course.pk}`)">课程详情</a>&gt;</li>
            <li>课程评论</li>
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
                  <li><router-link :to="'/courses/course_video/'+course.pk"><span>章节</span></router-link></li>
                  <li><router-link :to="'/courses/course_comment/'+course.pk"><span>评论</span></router-link></li>
                </ul>
              </div>
              <keep-alive>
              <router-view :course="course" :lesson_list="lesson_list"></router-view>
              </keep-alive>
            </div>
            <div class="aside r vedioright">
              <div class="bd">
                <div class="box mb40">
                  <h4>课程信息</h4>
                  <div class="course-info-tip">
                    <dl class="first">
                      <dt>课程名称：{{course.fields.name}}</dt>
                    </dl>
                    <dl class="first">
                      <dt>课程时长：{{course.fields.study_time}}分钟</dt>
                    </dl>
                    <dl class="first">
                      <dt>学习人数： {{course.fields.study_num}}</dt>
                    </dl>
                    <dl class="first">
                      <dt>如何学习:</dt>
                      <dd class="autowrap">&nbsp;&nbsp;&nbsp;{{course.fields.teacher_tell}}</dd>
                    </dl>
                  </div>
                </div>
                <div class="box mb40">
                  <h4>资料下载</h4>
                  <ul class="downlist">
                    <li v-for="(source, index) in course_sources" :index="index" :key="index">
                      <span><i class="aui-iconfont aui-icon-file"></i>&nbsp;&nbsp;{{source.fields.name}}</span>
                      <a :href="getSourceUrl(source.fields.down_load)" class="downcode"
                         :title="source.fields.name">下载</a>
                    </li>
                  </ul>
                </div>

                <div class="cp-other-learned  js-comp-tabs">
                  <div class="cp-header clearfix">
                    <h2 class="cp-tit l">学过该课的同学还学过</h2>
                  </div>
                  <div class="cp-body">
                    <div class="cp-tab-pannel js-comp-tab-pannel" data-pannel="course"
                         style="display: block">
                      <!-- img 200 x 112 -->
                      <ul class="other-list">
                        <li v-for="(course1, index) in course_list" :index="index" :key="index" class="curr">
                          <a @click="$router.push(`/courses/course_detail/${course1.pk}`)" target="_blank">
                            <img width="240" :src="getImgUrl(course1.fields.image)">
                            <span class="name autowrap">{{course1.fields.name}}</span>
                          </a>
                        </li>
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
  import axios from 'axios'
  import Qs from 'qs'

  export default {
    data() {
      return {
        course: {},
        course_list: [],
        course_sources: [],
        lesson_list: [],
        showComponent: false,
      };
    },
    mounted() {
      axios({
        url: `/api/courses/course_video/${this.$route.params.pathMatch}/`,
        method: 'GET'
      }).then(response => {
        var res = response.data
        this.course = JSON.parse(res.course)[0]
        this.course_list = JSON.parse(res.course_list)
        this.course_sources = JSON.parse(res.course_sources)
        this.lesson_list = JSON.parse(res.lesson_list)
        this.showComponent = true
      }).catch(err => {
        console.log(err)
      })
    },
    methods: {
      getSourceUrl: (bannerUrl) => {
        return "../../static/media/" + bannerUrl
      },
      getImgUrl: (bannerUrl) => {
        return "../../static/media/" + bannerUrl
      }
    },
  };
</script>
<style>
  @import "../../../static/css/zc-education/course/learn-less.css";
  @import "../../../static/css/zc-education/course/common-less.css";
  .router-link-active {
    border-bottom: 2px solid #f01400;
    color: #f01400;
    height: 55px;
    font-weight: bold;
  }
  .course-info-tip:before{
    content: '';
    display: block;
    position: absolute;
    left: 0px;
    top: 0px;
    width: 0;
    height: 0;
    border: 10px solid transparent;
    border-top: 0 none;
    border-bottom-color: #edf1f2;
  }
</style>
