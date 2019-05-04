<template>
  <div class="messagelist" v-if="showComponent">
    <div v-for="(teacher, index) in teacher_list" :index="index" :key="index" class="butler_list butler-fav-box">
      <dl class="des users">
        <dt>
          <a @click="$router.push(`/orgs/teacher_detail/${teacher.pk}`)"  >
            <img width="100" height="100" :src="getImgUrl(teacher.fields.image)">
          </a>
        </dt>
        <dd>
          <h1>
            <a @click="$router.push(`/orgs/teacher_detail/${teacher.pk}`)" >
              {{teacher.fields.name}}
            </a>
          </h1>
          <ul class="cont clearfix">
            <li class="time">
              工作年限：
              <span>{{teacher.fields.work_year}}年</span>
            </li>
            <li class="c7">
              课程数：
              <span>{{ teacher.fields.click_num }}</span>
            </li>
          </ul>
          <ul class="cont clearfix">
            <li class="time">
              工作公司：
              <span>{{ teacher.fields.gender}}</span>
            </li>
            <li class="c7">
              公司职位：
              <span>{{ teacher.fields.love_num }}</span>
            </li>
          </ul>
        </dd>
        <div class="delete jsDeleteFav_teacher" @click="deleteLove(teacher.pk, index)"></div>
      </dl>
    </div>
  </div>
</template>
<script>
  import axios from 'axios'
  export default {
    mounted() {
      axios({
        url:'/api/users/user_loveteacher/',
        method: 'GET'
      }).then((response)=>{
        var res = response.data
        this.teacher_list = JSON.parse(res.teacher_list)
        this.showComponent = true
      })
    },
    data() {
      return {
        teacher_list:[],
        showComponent: false,
      }
    },
    methods:{
      getImgUrl: (bannerUrl) =>{
        return "../../static/media/" + bannerUrl
      },
      deleteLove(favId, index) {
        axios({
          url: `/api/operations/user_deletelove/?loveid=${favId}&lovetype=3`,
          method: 'GET'
        }).then((response)=>{
          var res = response.data
          if (res.status == 'ok') {
            this.teacher_list.splice(index, 1)
          } else {
            alert(res.msg)
          }
        })
      }
    },
  };
</script>
<style scoped>
</style>
