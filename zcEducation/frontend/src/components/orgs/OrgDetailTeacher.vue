<template>
  <div v-if="showComponent" class="right companycenter layout">
    <div class="head">
      <h1>机构讲师</h1>
    </div>
    <div class="messagelist">
      <div class=" butler_list butler-fav-box">
        <dl v-for="teacher in pages" class="des users">
          <dt>
            <a @click="$router.push(`/orgs/teacher_detail/${teacher.id}`)" >
              <img width="100" height="100" class="scrollLoading" :src="getImgUrl(teacher.image)"/>
            </a>
          </dt>
          <dd>
            <h1>
              <a  @click="$router.push(`/orgs/teacher_detail/${teacher.id}`)" >
                {{teacher.name}}
              </a>
            </h1>
            <ul class="cont clearfix">
              <li class="time">工作年限：<span>{{teacher.work_year}}年</span></li>
              <li class="c7" style="padding-left: 21px">课程数：<span>{{teacher.count}}</span></li>
            </ul>
          </dd>
        </dl>
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
    name: "OrgDetailTeacher",
    data() {
      return {
        pages: [],
        has_previous: false,
        has_next: true,
        current_page_number: '',
        page_range: '',
        showComponent: false,
      };
    },
    mounted() {
      axios({
        url: `/api/orgs/org_detail_teacher/${this.$route.params.pathMatch}/`,
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
          url: `/api/orgs/org_detail_teacher/${this.$route.params.pathMatch}/`,
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
          url: `/api/orgs/org_detail_teacher/${this.$route.params.pathMatch}/`,
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
          url: `/api/orgs/org_detail_teacher/${this.$route.params.pathMatch}/`,
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
