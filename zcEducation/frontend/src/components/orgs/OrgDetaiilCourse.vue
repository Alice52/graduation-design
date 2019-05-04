<template>
  <div class="right companycenter layout" v-if="showComponent">
    <div class="head">
      <h1>机构课程</h1>
    </div>
    <div class="brief group_list">
      <!--{% for course in pages %}-->
      <div v-for="course in pages" class="module1_5 box">
        <a class="comp-img-box" @click="$router.push(`/courses/course_detail/${course.pk}`)" >
          <img width="214" height="195" :src="getImgUrl(course.fields.image)"/>
        </a>
        <div class="des">
          <a @click="$router.push(`/courses/course_detail/${course.pk}`)" ><h2>{{course.fields.name}}</h2></a>
          <span class="fl">课时：<i class="key">{{course.fields.study_time}}</i></span>
          <span class="fr">学习人数：{{course.fields.study_num}}</span>
        </div>
        <div class="bottom">
          <span class="fl">{{org.fields.name}}</span>
          <span class="star fr  notlogin " > {{course.fields.love_num}} </span>
        </div>
      </div>
    </div>
    <div class="pageturn">
      <ul class="pagelist">
        <li v-if="has_previous" class="long">
          <a @click="previousPage(current_page_number)">上一页</a>
        </li>
        <li v-for="(item, index) in page_range"  :index="index" :key="index">
          <a v-if="current_page_number==(index+1)" class="activePage" @click="goPage(index+1)">{{index + 1}}</a>
          <a v-if="current_page_number!=(index+1)" @click="goPage(index+1)">{{index + 1}}</a>
        </li>
        <li v-if="has_next" class="long">
          <a @click="nextPage(current_page_number)">下一页</a>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
    import axios from 'axios'

    export default {
      name: "OrgDetaiilCourse",
      props:[
        'org'
      ],
      data() {
        return {
          pages: [],
          has_previous: false,
          has_next: true,
          current_page_number: '',
          page_range: '',
          showComponent: false,
        }
      },
      mounted() {
        axios({
          url: `/api/orgs/org_detail_course/${this.$route.params.pathMatch}/`,
          method: 'GET'
        }).then(response => {
          var res = response.data
          this.pages = JSON.parse(res.pages)
          this.has_previous = res.has_previous
          this.has_next = res.has_next
          this.current_page_number = res.current_page_number
          this.page_range = res.page_range
          this.showComponent = true
        }).catch(err => {
          console.log(err)
        })
      },
      methods: {
        getImgUrl: (bannerUrl) => {
          return "../../static/media/" + bannerUrl
        },
        previousPage(current_page_number) {
          axios({
            url: `/api/orgs/org_detail_course/${this.$route.params.pathMatch}/`,
            method: 'GET',
            params: {"pagenum": current_page_number - 1},
          }).then(response => {
            var res = response.data
            this.pages = JSON.parse(res.pages)
            this.has_previous = res.has_previous
            this.has_next = res.has_next
            this.current_page_number = res.current_page_number
            this.page_range = res.page_range
          }).catch(err => {
            console.log(err)
          })
        },
        nextPage(current_page_number) {
          axios({
            url: `/api/orgs/org_detail_course/${this.$route.params.pathMatch}/`,
            method: 'GET',
            params: {"pagenum": current_page_number + 1},
          }).then(response => {
            var res = response.data
            this.pages = JSON.parse(res.pages)
            this.has_previous = res.has_previous
            this.has_next = res.has_next
            this.current_page_number = res.current_page_number
            this.page_range = res.page_range
          }).catch(err => {
            console.log(err)
          })
        },
        goPage(targetPage) {
          axios({
            url: `/api/orgs/org_detail_course/${this.$route.params.pathMatch}/`,
            method: 'GET',
            params: {"pagenum": targetPage},
          }).then(response => {
            var res = response.data
            this.pages = JSON.parse(res.pages)
            this.has_previous = res.has_previous
            this.has_next = res.has_next
            this.current_page_number = res.current_page_number
            this.page_range = res.page_range
          }).catch(err => {
            console.log(err)
          })
        },
      }
    }
</script>

<style scoped>
  .activePage{
    background-color: #eaeaea;
  }
</style>
