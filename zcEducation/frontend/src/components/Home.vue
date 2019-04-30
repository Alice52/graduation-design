<template>
  <div>
    <HeaderWithSearch :user="user"/>
    <div class="banner">
      <div class="wp">
        <div class="fl">
          <div class="imgslide">
            <ul class="imgs">
              <li v-for="(banner, index) in all_banners" :key="index" :index="index">
                <a :href="banner.fields.url">
                  <img width="1200" height="478" :src="getImgUrl(banner.fields.image)"/>
                </a>
              </li>
            </ul>
          </div>
          <div class="unslider-arrow prev"></div>
          <div class="unslider-arrow next"></div>
        </div>
      </div>
    </div>
    <section>
      <div class="module">
        <div class="wp">
          <h1>公开课程</h1>
          <div class="module1 eachmod">
            <div class="module1_1 left">
              <img width="228" height="614" src="../../static/images/module5_1.jpg">
              <p class="fisrt_word">
                名师授课
                <br>专业权威
              </p>
              <a class="more" @click="$router.push(`/courses/course_list`)">查看更多课程 ></a>
            </div>
            <div class="right group_list">
              <div class="module1_2 box">
                <div class="imgslide2">
                  <ul class="imgs">
                    <li v-for="(banner , index) in banner_courses" :key="index" :index="index">
                      <a @click="$router.push(`/courses/course_detail/{{banner.fields.id}}`)">
                        <img width="470" height="300" :src="getImgUrl(banner.fields.image)">
                      </a>
                    </li>
                  </ul>
                </div>
                <div class="unslider-arrow2 prev"></div>
                <div class="unslider-arrow2 next"></div>
              </div>
              <div v-for="(course, index) in all_courses" :key="index" :index="index">
                <a @click="$router.push(`/courses/course_detail/{{course.fields.id}}`)">
                  <img width="233" height="190" :src="getImgUrl(course.fields.image)">
                </a>
                <div class="des">
                  <a @click="$router.push(`/courses/course_detail/{{banner.fields.id}}`)">
                    <h2 :title="course.fields.name">{{course.fields.name}}</h2>
                  </a>
                  <span class="fl">
                    难度：
                    <i v-if="course.fields.level == 'gj'" class="key">高级</i>
                    <i v-if="course.fields.level == 'zj'" class="key">中级</i>
                    <i v-else class="key">初级</i>
                  </span>
                  <span class="fr">学习人数：{{course.fields.study_num}}</span>
                </div>
                <div class="bottom">
                  <!--<span class="fl" title={{ course.orginfo.name }}>{{ course.orginfo.name }}</span>-->
                  <!--<span class="star fr">{{ course.love_num }}</span>-->
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
    <section>
      <div class="module greybg">
        <div class="wp">
          <h1>课程机构</h1>
          <div class="module3 eachmod">
            <div class="module3_1 left">
              <img width="228" height="463" src="../../static/images/module6_1.jpg">
              <p class="fisrt_word">
                名校来袭
                <br>权威认证
              </p>
              <a class="more" @click="$router.push(`/orgs/org_list/`)">查看更多机构 ></a>
            </div>
            <div class="right">
              <ul>
                <li v-for="(org, index) in all_orgs " :key="index" :index="index" class="five">
                  <a @click="$router.push(`/orgs/org_detail/{{org.id}}`)">
                    <div class="company">
                      <img
                        width="120"
                        height="96"
                        style="margin-top: 2px"
                        :src="getImgUrl(org.fields.image)"
                      >
                    </div>
                    <p>
                      <span class="key" :title="org.fields.name">{{org.fields.name}}</span>
                    </p>
                  </a>
                </li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </section>
    <Footer/>
    <ToTop/>
  </div>
</template>
<script>
import HeaderWithSearch from "./HeaderWithSearch";
import ToTop from "./ToTop";
import Footer from "./Footer";
import axios from "axios";


export default {
  data() {
    return {
      user : null,
      all_banners: [],
      banner_courses: [],
      all_courses:[],
      all_orgs:[],
    };
  },

  mounted: function () {
   // 发送请求获取 data
    axios({
      url: "/api/",
      method: "GET",
    })
      .then(respanse => {
        let res = respanse.data;
        if (res.user!=null){
          this.user = JSON.parse(res.user)[0].fields
        }
        this.all_banners = JSON.parse(res.all_banners)
        this.banner_courses = JSON.parse(res.banner_courses)
        this.all_courses = JSON.parse(res.all_courses)
        this.all_orgs = JSON.parse(res.all_orgs)
        console.log(this.all_courses[0].fields)
        console.log(this.all_courses[0].fields.orginfo)
        console.log(this.all_courses[0].fields.orginfo.name)
      })
      .catch(function(error) {
        console.log(error);
      });
  },
  methods: {
    getImgUrl: (bannerUrl) =>{
        return "../../static/media/" + bannerUrl
    }
  },
  computed: {},
  // 将头组件映射为标签
  components: {
    HeaderWithSearch,
    ToTop,
    Footer
  }
};
</script>
