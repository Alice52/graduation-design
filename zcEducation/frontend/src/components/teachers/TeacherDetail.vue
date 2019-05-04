<template>
  <div v-if="showComponent">
    <section>
      <div class="wp">
        <ul  class="crumbs">
          <li><a @click="$router.push(`/`)">首页</a>></li>
          <li><a @click="$router.push(`/orgs/teacher_list`)">授课讲师</a>></li>
          <li>讲师详情</li>
        </ul>
      </div>
    </section>
    <section>
      <div class="wp butler-detail-box butler-diaryd-box clearfix">
        <div class="fl list">
          <div class="butler_detail_list clearfix">
            <div class="brief">
              <dl class="des">
                <dt>
                  <div class="picpic">
                    <img width="100" height="100" :src="getImgUrl(teacher.fields.image)"/>
                  </div>
                  <div class="btn">
                    <div v-if="loveteacher" class="zack zc-btn" @click="CancelLove(teacher.pk, 3)">取消收藏 </div>
                    <div v-else class="zack zc-btn"  @click="CancelLove(teacher.pk, 3)">收藏 </div>
                    <div class="fr btn2 shareBtn bdsharebuttonbox zc-btn">
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
                    <li>工作年限：<span>{{teacher.fields.work_year}}年</span></li>
                    <li>就职公司：<span>{{org_name}}</span></li>
                    <li>工作职位：<span>{{org_address}}&nbsp;</span></li>
                    <li>教学特点：<span>{{teacher.fields.work_style}}</span></li>
                  </ul>
                </dd>
              </dl>
            </div>
          </div>
          <div class="butler_detail_cont clearfix">
            <div class="left layout">
              <div class="head">
                <ul class="tab_header">
                  <li class="active"><a @click="$router.push(`/courses/course_list`)"  >全部课程</a> </li>
                </ul>
              </div>
              <div class="companycenter">
                <div class="group_list brief">
                  <div v-for="(course, index) in all_courses" :index="index" :key="index" class="module1_5 box">
                    <a @click="$router.push(`/courses/course_detail/${course.pk}`)" >
                      <img width="214" height="190" class="scrollLoading" :src="getImgUrl(course.fields.image)"/>
                    </a>
                    <div class="des">
                      <a @click="$router.push(`/courses/course_detail/${course.pk}`)"><h2>{{course.fields.name}}</h2></a>
                      <span class="fl">时长：<i class="key">{{course.fields.study_time}}</i></span>
                      <span class="fr">学习人数：{{course.fields.study_num}}</span>
                    </div>
                    <div class="bottom">
                      <span class="browse fl" title="浏览次数">{{course.fields.click_num}}</span>
                      <span class="star fr  notlogin" data-favid="15">{{course.fields.love_num}}</span>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="fr list">
          <div class="butler_detail_list">
            <div class="right butler-company-box">
              <div class="head">
                <h1>{{org_name}}</h1>
                <p>{{org_desc}}</p>
              </div>
              <div class="pic">
                <a @click="$router.push(`/orgs/org_detail/${org_id}`)" >
                  <img width="150" height="80" :src="getImgUrl(org_img)"/>
                </a>
              </div>
              <a @click="$router.push(`/orgs/org_detail/${org_id}`)" >
                <h2 class="center">{{org_name}}</h2>
              </a>
              <p class="center tell">地址：{{org_address}}</p>
              <a v-if="loveorg" class="btn" @click="CancelLove(org_id, 1)">取消收藏</a>
              <a v-else class="btn" @click="CancelLove(org_id, 1)">收藏</a>
            </div>
          </div>
          <div class="butler_detail_cont">
            <div class="butler_list_box">
              <div class="right layout">
                <div class="head">讲师排行榜</div>
                <dl v-for="(teacher1, index) in sort_teachers" :index="index" :key="index" class="des">
                  <span class="num fl">{{index+1}}</span>
                  <a @click="$router.push(`/orgs/teacher_detail/${teacher1.pk}`)" >
                    <dt>
                      <img width="50" height="50" class="scrollLoading" :src="getImgUrl(teacher1.fields.image)"/>
                    </dt>
                  </a>
                  <dd>
                    <a @click="$router.push(`/orgs/teacher_detail/${teacher1.pk}`)" >
                      <h1 :title="teacher1.fields.name">{{teacher1.fields.name}}</h1>
                    </a>
                    <p>工作年限：<span>{{teacher1.fields.work_year}}年</span></p>
                  </dd>
                </dl>
              </div>
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
        name: "TeacherDetail",
        data() {
          return {
            teacher : {},
            sort_teachers: [],
            all_courses: [],
            loveteacher: '',
            loveorg: '',
            org_name: '',
            org_desc:'',
            org_id: '',
            org_img: '',
            org_address: '',
            showComponent: false,
          };
        },
        mounted() {
          axios({
            url: `/api${this.$route.fullPath}/`,
            method: 'GET'
          }).then(response => {
            var res = response.data
            this.sort_teachers = JSON.parse(res.sort_teachers)
            this.teacher = JSON.parse(res.teacher)[0]
            this.all_courses = JSON.parse(res.all_courses)
            this.loveteacher = res.loveteacher
            this.loveorg = res.loveorg
            this.org_name = res.org_name
            this.org_desc = res.org_desc
            this.org_id =res.org_id
            this.org_img = res.org_img
            this.org_address =res.org_address
            this.showComponent = true
          }).catch(err => {
            console.log(err)
          })
        },
        methods:{
          getImgUrl: (bannerUrl) =>{
            return "../../static/media/" + bannerUrl
          },
          CancelLove(favId, type){
            // 1: 机构
            // 2： 课程
            // 3： 老师
            axios({
              url: '/api/operations/user_love/',
              method: 'GET',
              params: {"loveid": favId,"lovetype": type}
            }).then((response)=>{
              var res = response.data
              if (res.status == 'ok') {
                if (type == 1) {
                  this.loveorg = !this.loveorg
                } else if(type == 3) {
                  this.loveteacher = !this.loveteacher
                } else {
                  alert(res.msg)
                }
              } else {
                alert(res.msg)
              }
            })
          }
        },
      watch: {
        '$route' (to, from1) {
          axios({
            url: `/api${this.$route.fullPath}/`,
            method: 'GET'
          }).then(response => {
            var res = response.data
            this.sort_teachers = JSON.parse(res.sort_teachers)
            this.teacher = JSON.parse(res.teacher)[0]
            this.all_courses = JSON.parse(res.all_courses)
            this.loveteacher = res.loveteacher
            this.loveorg = res.loveorg
            this.org_name = res.org_name
            this.org_desc = res.org_desc
            this.org_id =res.org_id
            this.org_img = res.org_img
            this.org_address =res.org_address
          }).catch(err => {
            console.log(err)
          })
        }
      }
    }
</script>

<style scoped>
  a{
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
  .butler_detail_list .btn .btn1{
    background: #717171 no-repeat 15px center;
  }
  .zc-btn:hover{
    background: #00ad29;
  }
  .zack{
    background: #717171;
    width: 90px;
    display: inline-block;
    text-align: center;
    cursor: pointer;
    color: #fff;
  }

  .bdsharebuttonbox{
    color: #717171;
     margin-right: 0 ;
     margin-top: 0;
    float: right;
    line-height: 30px;
  }

</style>
