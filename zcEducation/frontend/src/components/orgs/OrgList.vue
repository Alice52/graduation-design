<template>
<div>
  <section>
    <div class="wp">
      <ul class="crumbs">
        <li><a @click="$router.push(`/home`)" >首页</a>></li>
        <li>课程机构</li>
      </ul>
    </div>
  </section>
  <section class="content">
    <div class="wp butler_list_box list">
      <div class='left'>
        <div class="listoptions">
          <ul>
            <li>
              <h2>机构类别</h2>
              <div class="cont">
                <a v-if="cate==''" @click="sortType(sort, cityid, '')" ><span  class="active2"  >全部</span></a>
                <a v-if="cate!=''"  @click="sortType(sort, cityid, '')"><span  >全部</span></a>
                <a v-if="cate=='pxjg'" @click="sortType(sort, cityid, 'pxjg')"><span class="active2"  >培训机构</span></a>
                <a v-if="cate!='pxjg'" @click="sortType(sort, cityid, 'pxjg')"><span >培训机构</span></a>
                <a v-if="cate=='gx'" @click="sortType(sort, cityid, 'gx')"><span class="active2">高校</span></a>
                <a v-if="cate!='gx'" @click="sortType(sort, cityid, 'gx')"><span >高校</span></a>
                <a v-if="cate=='gr'" @click="sortType(sort, cityid, 'gr')"><span class="active2">个人</span></a>
                <a v-if="cate!='gr'" @click="sortType(sort, cityid, 'gr')"><span >个人</span></a>
              </div>
            </li>
            <li>
              <h2>所在地区</h2>
              <div class="cont">
                <a v-if="cityid==''" @click="sortType(sort, '', cate)"><span class="active2">全部</span></a>
                <a v-if="cityid!=''" @click="sortType(sort, '', cate)"><span >全部</span></a>
                <a v-for="(city, index) in all_citys" :index="index" :key="index"  @click="sortType(sort, city.pk, cate)">
                  <span v-if="cityid==city.pk" class="active2">{{city.fields.name}}</span>
                  <span v-if="cityid!=city.pk" >{{city.fields.name}}</span>
                </a>
              </div>
            </li>
          </ul>
        </div>
        <div class="all">共<span class="key">{{all_orgs_count}}</span>家</div>
        <div class="butler_list company list">
          <div class="layout">
            <div class="head">
              <ul class="tab_header">
                <li v-if="sort==''" class="active" ><a @click="sortType('', cityid, cate)">全部</a></li>
                <li v-if="sort!=''"  ><a @click="sortType('', cityid, cate)">全部</a></li>
                <li v-if="sort=='study_num'" class="active"  ><a @click="sortType('study_num', cityid, cate)">学习人数</a></li>
                <li v-if="sort!='study_num'"  ><a @click="sortType('study_num', cityid, cate)">学习人数</a></li>
                <li v-if="sort=='course_num'" class="active"  ><a @click="sortType('course_num', cityid, cate)">课程数</a></li>
                <li v-if="sort!='course_num'"  ><a @click="sortType('course_num', cityid, cate)">课程数</a></li>
              </ul>
            </div>
            <dl v-for="(org, index) in pages" :index="index" :key="index" class="des difdes">
              <dt>
                <a @click="$router.push(`/orgs/org_detail/${org.pk}`)" >
                  <img width="200" height="120" class="scrollLoading"
                       :src="getImgUrl(org.fields.image)"/>
                </a>
              </dt>
              <dd>
                <div class="clearfix">
                  <a @click="$router.push(`/orgs/org_detail/${org.pk}`)">
                    <h1>{{org.fields.name}}</h1>
                    <div class="pic fl">
                    </div>
                  </a>
                </div>
                <ul class="cont">
                  <li class="first"><p class="pic9">课程数：<span>{{org.fields.course_num}}</span></p>
                    <p class="c7">学习人数：<span>{{org.fields.study_num}}</span></p></li>
                  <li class="c8" style="padding-left:18px;">{{org.fields.address}}</li>
                  <li class="pic10" style="padding-left:18px;">简介：{{org.fields.desc}}</li>
                </ul>
              </dd>
              <div class="buy start_groupbuy jsShowPerfect2" data-id="22"><br/>优秀<br/>分享</div>
            </dl>
          </div>
          <div class="pageturn">
            <ul class="pagelist">
              <li v-if="has_previous" class="long">
                <a @click="previousPage(current_page_number, keyword, sort, cityid, cate)">上一页</a>
              </li>
              <li v-for="(item, index) in page_range"  :index="index" :key="index">
                <a v-if="current_page_number==(index+1)" class="activePage" @click="goPage(index+1, keyword, cityid, cate)">{{index + 1}}</a>
                <a v-if="current_page_number!=(index+1)" @click="goPage(index+1, keyword, sort, cityid, cate)">{{index + 1}}</a>
              </li>
              <li v-if="has_next" class="long">
                <a @click="nextPage(current_page_number, keyword, sort, cityid, cate)">下一页</a>
              </li>
            </ul>
          </div>
        </div>
      </div>
      <div class="right companyrank layout">
        <div class="head">授课机构排名</div>
        <dl v-for="(org, index) in sort_orgs" :index="index" :key="index" class="des">
          <dt class="num fl">{{index+1}}</dt>
          <dd>
            <a @click="$router.push(`/orgs/org_list/${org.pk}`)" ><h1>{{org.fields.name}}</h1></a>
            <p>{{org.fields.address}}</p>
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
      name: "OrgList",
      data() {
        return {
          all_orgs_count: 0,
          all_citys:[],
          sort_orgs: [],
          pages: [],
          cate: '',
          cityid:'',
          sort:'',
          keyword: '',
          // 分页信息
          has_previous: false,
          has_next: true,
          current_page_number: '',
          page_range: '',
        };
      },
      methods: {
        getImgUrl: (bannerUrl) => {
          return "../../static/media/" + bannerUrl
        },
        previousPage(current_page_number, keyword, sort, cityid, cate) {
          axios({
            url: '/api/orgs/org_list/',
            method: 'GET',
            params: {"pagenum": current_page_number - 1, "keyword": keyword, 'sort': sort, 'cityid': cityid, 'cate': cate},
          }).then(response => {
            var res = response.data
            console.log(res)
            this.pages = JSON.parse(res.pages)
            this.all_citys = JSON.parse(res.all_citys)
            this.sort_orgs = JSON.parse(res.sort_orgs)
            this.has_previous = res.has_previous
            this.has_next = res.has_next
            this.current_page_number = res.current_page_number
            this.page_range = res.page_range

          }).catch(err => {
            console.log(err)
          })
        },
        nextPage(current_page_number, keyword, sort, cityid, cate) {
          axios({
            url: '/api/orgs/org_list/',
            method: 'GET',
            params: {"pagenum": current_page_number + 1, "keyword": keyword, 'sort': sort, 'cityid': cityid, 'cate': cate},
          }).then(response => {
            var res = response.data
            console.log(res)
            this.pages = JSON.parse(res.pages)
            this.all_citys = JSON.parse(res.all_citys)
            this.sort_orgs = JSON.parse(res.sort_orgs)
            this.has_previous = res.has_previous
            this.has_next = res.has_next
            this.current_page_number = res.current_page_number
            this.page_range = res.page_range
          }).catch(err => {
            console.log(err)
          })
        },
        goPage(targetPage, keyword, sort, cityid, cate) {
          axios({
            url: '/api/orgs/org_list/',
            method: 'GET',
            params: {"pagenum": targetPage, "keyword": keyword, 'sort': sort, 'cityid': cityid, 'cate': cate},
          }).then(response => {
            var res = response.data
            console.log(res)
            this.pages = JSON.parse(res.pages)
            this.all_citys = JSON.parse(res.all_citys)
            this.sort_orgs = JSON.parse(res.sort_orgs)
            this.has_previous = res.has_previous
            this.has_next = res.has_next
            this.current_page_number = res.current_page_number
            this.page_range = res.page_range
          }).catch(err => {
            console.log(err)
          })
        },
        sortType(type, cityid, cate) {
          axios({
            url: '/api/orgs/org_list/',
            method: 'GET',
            params: {"keyword": this.keyword, 'sort': type, 'cityid': cityid, 'cate': cate},
          }).then(response => {
            var res = response.data
            this.pages = JSON.parse(res.pages)
            this.all_citys = JSON.parse(res.all_citys)
            this.sort_orgs = JSON.parse(res.sort_orgs)
            this.has_previous = res.has_previous
            this.has_next = res.has_next
            this.current_page_number = res.current_page_number
            this.page_range = res.page_range
            this.sort = res.sort
            this.cate = res.cate
            this.cityid = res.cityid
            this.keyword = res.keyword
          }).catch(err => {
            console.log(err)
          })
        },
      },
      mounted() {
        axios({
          url: '/api/orgs/org_list/',
          method: 'GET'
        }).then(response => {
          var res = response.data
          console.log(res)
          this.pages = JSON.parse(res.pages)
          this.all_citys = JSON.parse(res.all_citys)
          this.sort_orgs = JSON.parse(res.sort_orgs)
          this.has_previous = res.has_previous
          this.has_next = res.has_next
          this.current_page_number = res.current_page_number
          this.page_range = res.page_range
          this.all_orgs_count = res.all_orgs_count
          this.keyword = res.keyword
        }).catch(err => {
          console.log(err)
        })
      },
    }
</script>

<style scoped>

</style>
