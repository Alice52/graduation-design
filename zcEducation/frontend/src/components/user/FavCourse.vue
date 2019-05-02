<template>
  <div class="companycenter">
    <div class="group_list brief">
      <div v-for="(course, index) in course_list" :index="index" :key="index" class="module1_5 box">
        <a @click="$router.push(`/courses/course_detail/${course.pk}`)" >
          <img width="214" height="190" :src="getImgUrl(course.fields.image)">
        </a>
        <div class="des">
          <a @click="$router.push(`/courses/course_detail/${course.pk}`)">
            <h2>{{course.fields.name}}</h2>
          </a>
          <span class="fl">
            时长：
            <i class="key">{{course.fields.study_time}}</i>
          </span>
          <span class="fr">学习人数：{{course.fields.study_num}}</span>
        </div>
        <div class="bottom">
          <span class="browse fl" title="浏览次数">{{course.fields.click_num}}</span>
          <span class="delete-group fr jsDeleteFav_course" @click="deleteLove(course.pk, index)"></span>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
  import axios from 'axios'
  export default {
    data() {
      return {
        course_list:[],
      }
    },
    methods:{
      getImgUrl: (bannerUrl) =>{
        console.log(bannerUrl)
        return "../../static/media/" + bannerUrl
      },
      deleteLove(favId, index) {
        axios({
          url: `/api/operations/user_deletelove/?loveid=${favId}&lovetype=2`,
          method: 'GET'
        }).then((response)=>{
          var res = response.data
          console.log(res)
          if (res.status == 'ok') {
            this.course_list.splice(index, 1)
          } else {
            alert(res.msg)
          }
        })
      }
    },
    mounted() {
      axios({
        url:'/api/users/user_lovecourse/',
        method: 'GET'
      }).then((response)=>{
        var res = response.data
        console.log(res)
        this.course_list = JSON.parse(res.course_list)
      })
    },
  };
</script>
<style scoped>
  .group_list .bottom .browse {
    cursor: pointer;
    background: lightgrey url(../../../static/images/browse.png) no-repeat 20px center;
    background-size: 21px 17px;
  }
</style>
