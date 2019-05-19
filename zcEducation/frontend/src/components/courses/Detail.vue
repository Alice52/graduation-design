<template>
    <div v-if="showComponent">
      <section>
        <div class="wp">
          <div class="crumbs">
            <ul>
              <li><a @click="$router.push(`/`)" >首页</a>></li>
              <li><a @click="$router.push(`/courses/course_list`)" >公开课程</a>></li>
              <li>课程详情</li>
            </ul>
          </div>
        </div>
      </section>
      <section>
        <div class="wp">
          <div class="groupPurchase_detail detail">
            <div class="toppro">
              <div class="left">
                <div class="picbox">
                  <div class="tb-booth tb-pic">
                    <img width="440" height="445" :src="getImgUrl(course.fields.image)" class="jqzoom" />
                  </div>
                </div>
                <div class="des">
                  <h1 :title="course.fields.name">{{course.fields.name}}</h1>
                  <span class="key ">{{course.fields.desc}}</span>
                  <ul class="parameter">
                    <li>
                      <span class="study-num">
                        难&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;度：
                        <i v-if="course.fields.level == 'gj'" class="key">高级</i>
                        <i v-if="course.fields.level == 'zj'" class="key">中级</i>
                        <i v-if="course.fields.level == 'cj'" class="key">初级</i>
                      </span>
                    </li>
                    <li><span class="pram word3">时&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;长：</span><span>{{course.fields.study_time}}</span></li>
                    <li><span class="pram word3">章&nbsp;节&nbsp;数：</span><span>{{course_lessoninfo_count}}</span></li>
                    <li>
                      <span class="pram word3">课程类别：</span>
                      <span v-if="course.fields.category=='qd'" title="前端开发">前端开发</span>
                      <span v-if="course.fields.category=='hd'" title="后端开发">后端开发</span>
                    </li>
                    <span class="study-num">学习人数：{{course.fields.study_num}}</span>
                  </ul>
                  <div class="btns">
                    <div v-if="lovecourse" class="btn colectgroupbtn" @click="CancelLove(course.pk, 2)" > 取消收藏</div>
                    <div v-else class="btn colectgroupbtn" @click="CancelLove(course.pk, 2)"  > 收藏 </div>
                    <div class="buy btn"><a style="color: white; text-decoration: none;" @click="$router.push(`/courses/course_video/${course.pk}`)" >开始学习</a></div>
                  </div>
                </div>
              </div>
              <div class="right">
                <div class="head">
                  <h1>授课机构</h1>
                  <p>举世瞩目的高级名校</p>
                </div>
                <div class="pic">
                  <a @click="$router.push(`/orgs/org_detail/${org.pk}`)">
                    <img width="130" height="130" style="margin-left: 10px" :src="getImgUrl(org.fields.image)"/>
                  </a>
                </div>
                <a @click="$router.push(`/orgs/org_detail/${org.pk}`)">
                  <h2 class="center" :title="org.fields.name">{{org.fields.name}}</h2>
                </a>
                <div v-if="loveorg" class="btn  notlogin"   @click="CancelLove(org.pk, 1)" >取消收藏</div>
                <div v-else  class="btn  notlogin"   @click="CancelLove(org.pk, 1)" >收藏</div>
                <div class="clear">
                  <ul>
                    <li>
                      <span>课 &nbsp;程&nbsp; 数：&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   {{org.fields.course_num}}</span>
                    </li>
                    <li>
                      <span>教 &nbsp;师&nbsp; 数：&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  {{org_teacher_num}}</span>
                    </li>
                    <li>所在地区：&nbsp;&nbsp;{{city_name}}</li>
                  </ul>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>
      <section>
        <div class="wp">
          <div class="list groupPurchase_detail_pro">
            <div class="left layout">
              <div class="head">
                <ul class="tab_header">
                  <li class="active">课程详情</li>
                </ul>
              </div>
              <div class="tab_cont tab_cont1">
                <p>
                  {{course.fields.detail}}
                </p>

              </div>
            </div>
            <div class="right layout">
              <div class="head">相关课程推荐</div>
              <div class="group_recommend">
                <dl v-for="(relate, index) in relate_courses" :index="index" :key="index">
                  <dt>
                    <a target="_blank" @click="$router.push(`/courses/course_detail/${relate.pk}`)" >
                      <img width="170" height="130" class="scrollLoading" :src="getImgUrl(relate.fields.image)"/>
                    </a>
                  </dt>
                  <dd>
                    <a target="_blank"@click="$router.push(`/courses/course_detail/${relate.pk}`)" ><h2> {{relate.fields.name}}</h2></a>
                    <span class="fl">学习时长：<i class="key">{{relate.fields.study_time}}</i></span>
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
    import Qs from 'qs'

    export default {
        name: "Detail",
        data() {
          return {
            course: {},
            relate_courses:[],
            lovecourse:'',
            loveorg:'',
            course_lessoninfo_count:0,
            org:'',
            org_teacher_num: '',
            city_name:'',
            showComponent: false,
          };
        },
        mounted() {
          axios({
            url: `/api/courses/course_detail/${this.$route.params.pathMatch}/`,
            methods: 'GET'
          }).then(response=> {
            var res = response.data
            this.course = JSON.parse(res.course)[0]
            this.relate_courses = JSON.parse(res.relate_courses)
            this.org = JSON.parse(res.org)[0]
            this.lovecourse = res.lovecourse
            this.loveorg = res.loveorg
            this.course_lessoninfo_count = res.course_lessoninfo_count
            this.org_teacher_num = res.org_teacher_num
            this.city_name = res.city_name
            this.showComponent = true
          }).catch(err=> {
            console.log(err)
          })
        },

        methods: {
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
                } else if(type == 2) {
                  this.lovecourse = !this.lovecourse
                } else {
                  alert(res.msg)
                }
              } else {
                alert(res.msg)
              }
            }).catch(err=>{
              if (err.message == "Request failed with status code 404")
                alert("登录之后才能收藏")
              else
                console.log(err)
            })
          }
        },
        watch: {
          '$route' (to, from1) {
            this.showComponent = false
            axios({
              url: `/api${this.$route.path}/`,
              methods: 'GET'
            }).then(response=> {
              var res = response.data
              this.course = JSON.parse(res.course)[0]
              this.relate_courses = JSON.parse(res.relate_courses)
              this.org = JSON.parse(res.org)[0]
              this.lovecourse = res.lovecourse
              this.loveorg = res.loveorg
              this.course_lessoninfo_count = res.course_lessoninfo_count
              this.org_teacher_num = res.org_teacher_num
              this.city_name = res.city_name
              this.showComponent = true
            }).catch(err=> {
              console.log(err)
            })
          }
      }
    }
</script>

<style scoped>
.study-num{
  letter-spacing: 2px;
  color: #9f9f9f;
}
.groupPurchase_detail .toppro .btns {
  left: 45px;
  bottom: 0;
  position: absolute;
}

.groupPurchase_detail .toppro .left .colectgroupbtn:hover{
  background: red;
}
.groupPurchase_detail .toppro .buy:hover{
  background: red;
}
</style>
