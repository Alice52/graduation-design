<template>
  <div v-if="showComponent">
    <section>
      <div class="wp">
        <ul class="crumbs">
          <li>
            <a  @click="$router.push(`/`)" >首页</a>>
          </li>
          <li>公开课</li>
        </ul>
      </div>
    </section>
    <section class="content">
      <div class="wp">
        <div class="list" style="margin-top:0;">
          <div class="left layout">
            <div class="head">
              <ul class="tab_header">
                <li v-if="sort==''" class="active">  <a @click="sortType('')" >最新</a> </li>
                <li v-if="sort!=''" >  <a @click="sortType('')" >最新</a> </li>
                <li v-if="sort=='click_num'" class="active"> <a @click="sortType('click_num')" >最热门</a> </li>
                <li v-if="sort!='click_num'"> <a @click="sortType('click_num')" >最热门</a> </li>
                <li v-if="sort=='study_num'" class="active"> <a @click="sortType('study_num')" >参与人数</a> </li>
                <li v-if="sort!='study_num'"> <a @click="sortType('study_num')" >参与人数</a> </li>
              </ul>
            </div>
            <div id="inWindow">
              <div class="tab_cont" id="content">
                <div class="group_list">
                  <div v-for="(course, index) in pages" :index="index" :key="index" class="box">
                    <a @click="$router.push(`/courses/course_detail/${course.pk}`)">
                      <img
                        width="280"
                        height="350"
                        class="scrollLoading"
                        :src="getImgUrl(course.fields.image)"
                      >
                    </a>
                    <div class="des">
                      <a @click="$router.push(`/courses/course_detail/${course.pk}`)">
                        <h2>{{course.fields.name}}</h2>
                      </a>
                      <span class="fl">
                        时长：
                        <i class="key">{{course.fields.study_time}}</i>
                      </span>
                      <span class="fr">学习人数：{{course.fields.study_num}}&nbsp;&nbsp;</span>
                    </div>
                    <div class="bottom">
                      <a @click="$router.push(`/courses/course_detail/${course.pk}`)">
                        <span class="browse fl" title="浏览次数">{{course.fields.click_num}}</span>
                        <span class="star fr" title="收藏人数">{{course.fields.love_num}}</span>
                      </a>
                    </div>
                  </div>
                </div>
                <div class="pageturn">
                  <ul class="pagelist">
                    <li v-if="has_previous" class="long">
                      <a @click="previousPage(current_page_number, keyword, sort)">上一页</a>
                    </li>
                    <li v-for="(item, index) in page_range"  :index="index" :key="index">
                      <a v-if="current_page_number==(index+1)" class="activePage" @click="goPage(index+1, keyword)">{{index + 1}}</a>
                      <a v-if="current_page_number!=(index+1)" @click="goPage(index+1, keyword, sort)">{{index + 1}}</a>
                    </li>
                    <li v-if="has_next" class="long">
                      <a @click="nextPage(current_page_number, keyword, sort)">下一页</a>
                    </li>
                  </ul>
                </div>
              </div>
            </div>
          </div>
          <div class="right layout">
            <div class="head">热门课程推荐</div>
            <div class="group_recommend">
              <dl v-for="(course, index) in recommend_courses" :index="index" :key="index">
                <dt>
                  <a target="_blank" @click="$router.push(`/courses/course_detail/${course.pk}`)">
                    <img
                      width="240"
                      height="135"
                      class="scrollLoading"
                      :src="getImgUrl(course.fields.image)"
                    >
                  </a>
                </dt>
                <dd>
                  <a target="_blank" @click="$router.push(`/courses/course_detail/${course.pk}`)">
                    <h2>{{course.fields.name}}</h2>
                  </a>
                  <span class="fl">
                    难度：
                    <i v-if="course.fields.level == 'gj'" class="key">高级</i>
                    <i v-if="course.fields.level == 'zj'" class="key">中级</i>
                    <i v-if="course.fields.level == 'cj'" class="key">初级</i>
                  </span>
                </dd>
              </dl>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
  import axios from 'axios'

  export default {
    name: "CourseList",
    data() {
      return {
        pages: [],
        recommend_courses: [],
        sort:'',
        keyword: '',
        // 分页信息
        has_previous: false,
        has_next: true,
        current_page_number: '',
        page_range: '',
        showComponent: false,
      };
    },
    methods: {
      getImgUrl: (bannerUrl) => {
        return "../../static/media/" + bannerUrl
      },
      previousPage(current_page_number, keyword, sort) {
        axios({
          url: '/api/courses/course_list/',
          method: 'GET',
          params: {"pagenum": current_page_number - 1, "keyword": keyword, 'sort': sort},
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
      nextPage(current_page_number, keyword, sort) {
        axios({
          url: '/api/courses/course_list/',
          method: 'GET',
          params: {"pagenum": current_page_number + 1, "keyword": keyword, 'sort': sort},
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
      goPage(targetPage, keyword, sort) {
        axios({
          url: '/api/courses/course_list/',
          method: 'GET',
          params: {"pagenum": targetPage, "keyword": keyword, 'sort': sort},
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
      sortType(type) {
          axios({
            url: '/api/courses/course_list/',
            method: 'GET',
            params: {"keyword": this.keyword, 'sort': type},
          }).then(response => {
            var res = response.data
            this.pages = JSON.parse(res.pages)
            this.has_previous = res.has_previous
            this.has_next = res.has_next
            this.current_page_number = res.current_page_number
            this.page_range = res.page_range
            this.sort = res.sort
            this.keyword = res.keyword
          }).catch(err => {
            console.log(err)
          })
      },
      getInitAndSearchData() {
        this.keyword = this.$route.query.keyword
        axios({
          url: '/api/courses/course_list/',
          params: {'keyword': this.keyword},
          method: 'GET'
        }).then(response => {
          var res = response.data
          this.recommend_courses = JSON.parse(res.recommend_courses)
          this.pages = JSON.parse(res.pages)
          this.has_previous = res.has_previous
          this.has_next = res.has_next
          this.current_page_number = res.current_page_number
          this.page_range = res.page_range
          this.keyword = res.keyword
          this.showComponent = true
        }).catch(err => {
          console.log(err)
        })
      }
    },
    mounted() {
      this.getInitAndSearchData()
    },
    watch:{
      $route(from, to) {
        this.getInitAndSearchData()
      }
    }
  }
</script>

<style>
  a {
    cursor: pointer;
  }

  .group_list .bottom .browse {
    cursor: pointer;
    background: lightgrey url(../../../static/images/browse.png) no-repeat 20px center;
    background-size: 25px 20px;
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


  .activePage{
    background-color: #eaeaea;
  }
</style>
