<template>
  <div>
    <div id="notice" class="clearfix">
      <div class="l tnotice"><strong>课程须知:</strong> <a
        href="javascript:void(0)">{{course.fields.course_need}}</a></div>
    </div>
    <div class="mod-chapters">
      <div v-for="(lesson, index) in lesson_list" :index="index" :key="index" class="chapter chapter-active">
        <h3>
          <strong><i class="state-expand"></i>{{lesson.name}}</strong>
        </h3>
        <ul class="video">
          <li v-for="(video, index) in lesson.video" :index="index" :key="index">
            <a target="_blank" :href='getImgUrl(video.url)'
               class="J-media-item studyvideo">{{video.name}}
              ({{video.study_time}})
              <i class="study-state"></i>
            </a>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
    export default {
        name: "Chapter",
        props:[
          'lesson_list',
          'course'
        ],
        methods:{
          getImgUrl: (bannerUrl) => {
            return "../../static/media/" + bannerUrl
          }
        }

    }
</script>

<style scoped>

</style>
