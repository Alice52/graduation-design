<template>
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
            <a @click="previousPage(current_page_number, keyword)">上一页</a>
          </li>
          <li v-for="(item, index) in page_range"  :index="index" :key="index">
            <a v-if="current_page_number==(index+1)" class="activePage" @click="goPage(index+1, keyword)">{{index + 1}}</a>
            <a v-if="current_page_number!=(index+1)" @click="goPage(index+1, keyword)">{{index + 1}}</a>
          </li>
          <li v-if="has_next" class="long">
            <a @click="nextPage(current_page_number, keyword)">下一页</a>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
    export default {
        name: "ListCourse"
    }
</script>

<style scoped>

</style>
