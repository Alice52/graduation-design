<template>
  <div v-if="showComponent">
    <div id="js-pub-container" class="issques clearfix js-form">
      <div class="wgt-ipt-wrap pub-editor-wrap" id="js-pl-input-fake">
        <textarea
          id="js-pl-textarea"
          v-model="comment_content"
          class
          placeholder="请自觉遵守互联网相关的政策法规，严禁发布色情、暴力、反动的言论。"
        ></textarea>
      </div>
      <input type="button" @click="pushComment" class="pub-btn" value="发表评论">
      <p class="global-errortip js-global-error"></p>
    </div>
    <div id="course_note">
      <ul class="mod-post" id="comment-list">
        <li v-for="(comment, index) in comment_vo" :key="index" class="post-row">
          <div class="media">
            <span target="_blank">
              <img :src="getImgUrl(comment.image)" width="40" height="40">
            </span>
          </div>
          <div class="bd">
            <div class="tit">
              <span target="_blank">{{comment.nick_name}}</span>
            </div>
            <p class="cnt">{{comment.comment_content}}</p>
            <div class="footer clearfix">
              <span
                title="创建时间"
                class="l timeago"
              >时间：{{comment.add_time.substring(0,19).replace('-', '年').replace('-', '月').replace(' ', '日 ')}}</span>
            </div>
          </div>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import Qs from "qs";
export default {
  name: "Comment",
  data() {
    return {
      course: {},
      comment_vo: [],
      comment_content: "",
      showComponent: false
    };
  },
  mounted() {
    axios({
      url: `/api${this.$route.fullPath}/`,
      method: "GET"
    })
      .then(response => {
        var res = response.data;
        this.course = JSON.parse(res.course)[0];
        this.comment_vo = JSON.parse(res.comment_vo);
        this.showComponent = true;
      })
      .catch(err => {
        console.log(err);
      });
  },
  methods: {
    getImgUrl: bannerUrl => {
      return "../../static/media/" + bannerUrl;
    },
    pushComment() {
      var data = Qs.stringify({
        course: this.course.pk,
        content: this.comment_content
      });
      axios({
        url: "/api/operations/user_comment/",
        method: "POST",
        data: data,
        headers: {
          "Content-Type": "application/x-www-form-urlencoded"
        }
      })
        .then(respanse => {
          let res = respanse.data;
          if (res.status == "ok") {
            this.comment_vo.unshift(res.comment_info);
            this.comment_content = "";
          } else {
            alert(res.msg);
          }
          this.showComponent = true;
        })
        .catch(function(error) {
          console.log(error);
        });
    }
  }
};
</script>

<style scoped>
@import "../../../static/css/zc-education/course/learn-less.css";
@import "../../../static/css/zc-education/course/course-comment.css";
.pub-editor-wrap {
  border: none;
}
</style>
