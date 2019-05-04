<template>
  <div v-if="showComponent">
    <section>
      <div class="wp">
        <ul  class="crumbs">
          <li><a @click="$router.push(`/`)">首页</a>></li>
          <li>课程讲师</li>
        </ul>
      </div>
    </section>
    <section class="content">
      <div class="wp butler_list_box list">
        <div class='left'>
          <div class="butler_list layout">
            <div class="head">
              <ul class="fl tab_header">
                <li v-if="sort==''" class="active"><a @click="sortType('')" >全部</a> </li>
                <li v-if="sort!=''"><a @click="sortType('')">全部</a> </li>
                <li v-if="sort=='click_num'" class="active"><a @click="sortType('click_num')" >人气 &#8595;</a></li>
                <li v-if="sort!='click_num'"><a @click="sortType('click_num')" >人气 &#8595;</a></li>
              </ul>
              <div class="fr butler-num">共<span class="key">{{all_teachers_count}}</span>人&nbsp;&nbsp;&nbsp;</div>
            </div>
            <dl v-for="(teacher, index) in pages" :index="index" :key="index" class="des">
              <dt>
                <a @click="$router.push(`/orgs/teacher_detail/${teacher.pk}`)">
                  <div class="picpic">
                    <img width="100" height="100" class="scrollLoading" :src="getImgUrl(teacher.fields.image)"/>
                  </div>
                </a>
                <div class="btn">
                  <div class="fr btn2 bdsharebuttonbox">
                    <span class="fl">分享</span>
                    <a href="#" class="bds_more" data-cmd="more"></a>
                  </div>
                </div>
              </dt>
              <dd>
                <a @click="$router.push(`/orgs/teacher_detail/${teacher.pk}`)">
                  <h1>{{teacher.fields.name}}</h1>
                </a>
                <ul class="cont">
                  <li>工作年限：<span>{{ teacher.fields.work_year }}年</span></li>
                  <li>工作职位：<span>{{ teacher.fields.work_position }}</span></li>
                  <li>就职公司：<span>南通大学</span></li>
                  <li>年龄：<span>{{teacher.fields.age}}岁</span></li>
                  <li>教学特点：<span>{{teacher.fields.work_style}}</span></li>
                </ul>
              </dd>
            </dl>
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
        <div class="right layout">
          <div class="head">讲师排行榜</div>
          <dl v-for="(teacher, index) in sort_teachers" :index="index" :key="index" class="des">
            <span class="num fl">{{index+1}}</span>
            <a @click="$router.push(`/orgs/teacher_detail/${teacher.pk}`)">
              <dt>
                <img width="50" height="50" class="scrollLoading"  :src="getImgUrl(teacher.fields.image)"/>
              </dt>
            </a>
            <dd>
              <a @click="$router.push(`/orgs/teacher_detail/${teacher.pk}`)">
                <h1 :title="teacher.fields.name">{{teacher.fields.name}}</h1>
              </a>
              <p>工作年限：<span>{{teacher.fields.work_year}}年</span></p>
            </dd>
          </dl>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
    import axios from 'axios'

    export default {
      name: "TeacherList",
      data() {
        return {
          all_teachers_count:0,
          sort_teachers: [],
          pages: [],
          sort:'',
          keyword: '',
          // 分页信息
          has_previous: false,
          has_next: true,
          current_page_number: '',
          page_range: '',
          showComponent: false
        };
      },
      methods: {
        getImgUrl: (bannerUrl) => {
          return "../../static/media/" + bannerUrl
        },
        previousPage(current_page_number, keyword, sort) {
          axios({
            url: '/api/orgs/teacher_list/',
            method: 'GET',
            params: {"pagenum": current_page_number - 1, "keyword": keyword, 'sort': sort},
          }).then(response => {
            var res = response.data
            this.pages = JSON.parse(res.pages)
            this.has_previous = res.has_previous
            this.has_next = res.has_next
            this.current_page_number = res.current_page_number
            this.page_range = res.page_range
            this.all_teachers_count = res.all_teachers_count
          }).catch(err => {
            console.log(err)
          })
        },
        nextPage(current_page_number, keyword, sort) {
          axios({
            url: '/api/orgs/teacher_list/',
            method: 'GET',
            params: {"pagenum": current_page_number + 1, "keyword": keyword, 'sort': sort},
          }).then(response => {
            var res = response.data
            this.pages = JSON.parse(res.pages)
            this.has_previous = res.has_previous
            this.has_next = res.has_next
            this.current_page_number = res.current_page_number
            this.page_range = res.page_range
            this.all_teachers_count = res.all_teachers_count
          }).catch(err => {
            console.log(err)
          })
        },
        goPage(targetPage, keyword, sort) {
          axios({
            url: '/api/orgs/teacher_list/',
            method: 'GET',
            params: {"pagenum": targetPage, "keyword": keyword, 'sort': sort},
          }).then(response => {
            var res = response.data
            this.pages = JSON.parse(res.pages)
            this.has_previous = res.has_previous
            this.has_next = res.has_next
            this.current_page_number = res.current_page_number
            this.page_range = res.page_range
            this.all_teachers_count = res.all_teachers_count
          }).catch(err => {
            console.log(err)
          })
        },
        sortType(type) {
          axios({
            url: '/api/orgs/teacher_list/',
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
            this.all_teachers_count = res.all_teachers_count
            this.keyword = res.keyword
          }).catch(err => {
            console.log(err)
          })
        },
        getInitAndSearchData() {
          this.keyword = this.$route.query.keyword
          axios({
            url: '/api/orgs/teacher_list/',
            params: {'keyword': this.keyword},
            method: 'GET'
          }).then(response => {
            var res = response.data
            this.sort_teachers = JSON.parse(res.sort_teachers)
            this.pages = JSON.parse(res.pages)
            this.has_previous = res.has_previous
            this.has_next = res.has_next
            this.current_page_number = res.current_page_number
            this.page_range = res.page_range
            this.all_teachers_count = res.all_teachers_count
            this.keyword = res.keyword
            this.showComponent = true
          }).catch(err => {
            console.log(err)
          })
        },
      },
      mounted() {
        this.getInitAndSearchData()
      },
      watch:{
        $route(from, to) {
          this.getInitAndSearchData()
        }
      },
    }
</script>

<style scoped>

  .butler_list_box .right {
    width: 210px;
    height: auto;
    overflow: hidden;
    float: right;
  }

</style>
