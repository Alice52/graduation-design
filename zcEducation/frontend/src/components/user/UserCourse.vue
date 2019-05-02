<template>
  <div class="right">
    <div class="personal_des Releasecont">
      <div class="head">
        <h1>我的课程</h1>
      </div>
    </div>
    <div class="personal_des permessage">
      <div class="companycenter">
        <div class="group_list brief">
          <!--{% for course in course_list %}-->
          <div v-for="(course, index) in course_list" :key='index' :index='index' class="module1_5 box">
            <a @click="$router.push(`/courses/course_detail/${course.pk}`)" >
              <img
                width="214"
                height="190"
                class="scrollLoading"
                :src="getImgUrl(course.fields.image)">
            </a>
            <div class="des">
              <a @click="$router.push(`/courses/course_detail/${course.pk}`)" >
                <h2>{{course.fields.name}}</h2>
              </a>
              <span class="fl">
                课时：
                <i class="key">{{course.fields.study_time}}</i>
              </span>
              <span class="fr">学习人数：{{ course.fields.study_num }}</span>
            </div>
            <div class="bottom">
              <span class="browse fl" title="浏览次数">{{course.fields.click_num}}</span>
              <span class="star fr" title="收藏人数">{{course.fields.love_num}}</span>
            </div>
            <!--<div class="bottom">-->
              <!--<span class="fl">{{ course.fields.name }}</span>-->
              <!--<span class="star fr notlogin" data-favid="15">{{ course.fields.love_num }}</span>-->
            <!--</div>-->
          </div>
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
  mounted() {
    axios({
      url:'/api/users/user_course/',
      method: 'GET',
    }).then((response)=>{
      var res = response.data
      console.log(res)
      this.course_list = JSON.parse(res.course_list)
      console.log(this.course_list[0])
      console.log(this.course_list[0].fields)
      console.log(this.course_list[0].fields.image)
    }).catch((err)=> {
      console.log(err)
    })
  },
  methods:{
    getImgUrl: (bannerUrl) =>{
      console.log(bannerUrl)
      return "../../static/media/" + bannerUrl
    }
  },
};
</script>
<style scoped>
  .group_list .bottom .browse {
    cursor: pointer;
    background: lightgrey url(../../../static/images/browse.png) no-repeat 20px center;
    background-size: 21px 17px;
  }

  .group_list .bottom .fl {
    width: 50.5%;
  }

  .group_list .bottom .fr {
    width: 49%;
    text-indent: 10px;
    cursor: pointer;
  }

  .group_list .bottom .star {
    cursor: pointer;
    background: lightgrey url(../../../static/images/star.png) no-repeat 38px center;
  }
</style>
