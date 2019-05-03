<template>
  <div>
    <div id="js-pub-container" class="issques clearfix js-form">
      <div class="wgt-ipt-wrap pub-editor-wrap " id="js-pl-input-fake">
        <textarea id="js-pl-textarea" class="" placeholder="扯淡、吐槽、表扬、鼓励……想说啥就说啥！" ></textarea>
      </div>
      <input type="button" id="js-pl-submit" class="pub-btn" data-cid="452" value="发表评论">
      <p class="global-errortip js-global-error"></p>
    </div>
    <div id="course_note">
      <ul class="mod-post" id="comment-list">
        <li v-for="comment in comment_vo" class="post-row">
          <div class="media">
            <span target="_blank"><img :src='getImgUrl(comment.image)' width='40' height='40' /></span>
          </div>
          <div class="bd">
            <div class="tit">
              <span target="_blank">{{comment.nick_name}}</span>
            </div>
            <p class="cnt">{{comment.comment_content}}</p>
            <div class="footer clearfix">
              <span title="创建时间" class="l timeago">时间：{{comment.add_time}}</span>
            </div>
          </div>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
    import axios from 'axios'
    export default {
        name: "Comment",
        data() {
          return {
            course: {},
            comment_vo: [],
          };
        },
        mounted() {
          axios({
            url: `/api${this.$route.fullPath}/`,
            method: 'GET'
          }).then(response => {
            var res = response.data
            console.log(res)
            this.course = JSON.parse(res.course)[0]
            this.comment_vo = JSON.parse(res.comment_vo)
          }).catch(err => {
            console.log(err)
          })
        },
        methods:{
          getImgUrl: (bannerUrl) => {
            return "../../static/media/" + bannerUrl
          }
        }
    }
</script>

<style scoped>
  @import "../../../static/css/zc-education/course/learn-less.css";
  @import "../../../static/css/zc-education/course/course-comment.css";
  /*@import "../../../static/css/zc-education/course/learn-less.css";*/
  /*@import "../../../static/css/zc-education/course/learn-less.css";*/
  /*@import "../../../static/css/zc-education/course/learn-less.css";*/
  /*@import "../../../static/css/zc-education/course/learn-less.css";*/
  /*<link rel="stylesheet" type="text/css" href="{% static 'css/zc-education/course/course-comment.css' %}" />*/
    /*<link rel="stylesheet" type="text/css" href="{% static 'css/zc-education/base.css' %}">*/
                                /*<link rel="stylesheet" type="text/css" href="{% static 'css/zc-education/common-less.css' %}">*/
                                   /*<link rel="stylesheet" type="text/css" href="{% static 'css/zc-education/course/common-less.css' %}">*/
  /*<link rel="stylesheet" type="text/css" href="{% static 'css/mooc.css' %}" />*/

  .pub-editor-wrap{
    border: none;
  }
</style>
