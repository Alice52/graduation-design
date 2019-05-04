<template>
  <div v-if="showComponent">
    <div class="right companycenter layout grouping">
      <div class="head">
        <h1>全部课程</h1>
        <a class="green fr more" @click="$router.push(`/courses/course_list/`)" 查看更多 > </a>
      </div>
      <div class="brief group_list">
        <!--{% for course in org.courseinfo_set.all %}-->
        <div v-for="(course, index) in all_courses" :index="index" :key="index" class="module1_5 box">
          <a @click="$router.push(`/courses/course_detail/${course.pk}`)" >
            <img width="214" :src="getImgUrl(course.fields.image)"/></a>
          <div class="des">
            <a @click="$router.push(`/courses/course_detail/${course.pk}`)" ><h2>{{course.fields.name}}</h2></a>
            <span class="fl">课时：<i class="key">{{course.fields.study_time}}</i></span>
            <span class="fr">参加人数：{{course.fields.study_num}}</span>
          </div>
          <div class="bottom">
            <span class="fl">{{org.fields.name}}</span>
            <span class="star fr  notlogin " data-favid="13" data-fav-type="4"> {{course.fields.love_num}} </span>
          </div>
        </div>
      </div>
    </div>
    <div class="right companycenter layout">
      <div class="head">
        <h1>机构教师</h1>
        <a class="green fr more" @click="$router.push(`/orgs/teacher_list`)" > >查看更多 > </a>
      </div>
      <div class="diarys">
        <div v-for="teacher in all_teacher" class="module5 share company-diary-box" style="padding:10px 0;">
          <div class="left">
            <img class="pic" :src="getImgUrl(teacher.image)"/>
            <p>昵称：{{teacher.name}}</p>
          </div>
          <div class="right course-zack">
            <div class="top">
              <div class="fl">
                <a @click="$router.push(`/courses/course_detail/${teacher.pop_course_id}`)" ><h1>{{teacher.pop_course_name}}</h1></a>
                <span>发表于：{{teacher.pop_course_addtime.substring(0,19).replace('-', '年').replace('-', '月').replace(' ', '日 ')}}</span>
              </div>
            </div>
            <div class="middle" style="border-bottom:0;">{{teacher.pop_course_desc}}</div>
          </div>
        </div>
      </div>
    </div>
    <div class="right companycenter layout">
      <div class="head">
        <h1>机构介绍</h1>
        <a class="green fr more" @click="$router.push(`/orgs/org_list`)"> 查看更多 > </a>
      </div>
      <div class="cont">
        <p>{{org.fields.desc}}</p>
      </div>
    </div>
  </div>
</template>

<script>
  import axios from 'axios'

  export default {
    name: "OrgDetail",
    data() {
      return{
        all_courses: [],
        all_teacher: [],
        showComponent: false,
      };
    },
    mounted() {
      axios({
        url: `/api/orgs/org_detail/${this.$route.params.pathMatch}/`,
        method: 'GET'
      }).then(response => {
        var res = response.data
        this.all_courses = JSON.parse(res.all_courses)
        this.all_teacher = JSON.parse(res.all_teacher)
        this.showComponent =true
      }).catch(err=> {
        console.log(err)
      })
    },
    methods: {
      getImgUrl: (bannerUrl) =>{
        return "../../static/media/" + bannerUrl
      }
    },
    props:[
      'org'
    ]

  }
</script>

<style scoped>
  .course-zack{
    border: none;
  }
</style>
