import Vue from 'vue'
import Router from 'vue-router'
import Login from '../components/user/Login'
import Home from '../components/Home'
import UserCenter from '../components/user/UserCenter'
import UserInfo from '../components/user/UserInfo'
import UserForget from '../components/user/ForgetPwd'
import UserLogout from '../components/user/UserLogout'
import UserRegister from '../components/user/Register'
import UserActive from '../components/user/UserActive'
import UserReset from '../components/user/PasswordReset'
import  UserCourses from '../components/user/UserCourse'
import UserFav from '../components/user/UserFav'
import FavOrgs from '../components/user/FavOrgs'
import FavCourse from '../components/user/FavCourse'
import FavTeacher from '../components/user/FavTeacher'
import HeaderWithSearch from '../components/HeaderWithSearch'
import CourseList from '../components/courses/CourseList'
import TeacherList from '../components/teachers/TeacherList'
import OrgList from '../components/orgs/OrgList'
import Detail from '../components/courses/Detail'
import Vedio from '../components/courses/Vedio'
import TeacherDetail from '../components/teachers/TeacherDetail'
import VideoChapter from '../components/courses/Chapter'
import VideoComment from '../components/courses/Comment'
import OrgHeader from '../components/orgs/OrgHeader'
import OrgDetaiilCourse from '../components/orgs/OrgDetaiilCourse'
import OrgDetail from '../components/orgs/OrgDetail'
import OrgDetailDesc from '../components/orgs/OrgDetailDesc'
import OrgDetailTeacher from '../components/orgs/OrgDetailTeacher'


Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    // {
    //   path: '*',
    //   name: 'error',
    //   component: Home
    // },

    // 首页 nav
    {
      path: '/',
      component: HeaderWithSearch,
      redirect: '/home',
      children:[
        {
          path: '/home',
          component: Home
        },
        {
          path: '/courses/course_list',
          name: 'courseList',
          component: CourseList,
        },
        {
          path: '/orgs/teacher_list',
          name: 'teacherList',
          component: TeacherList
        },
        {
          path: '/orgs/org_list',
          name: 'orgList',
          component: OrgList
        },
        {
          path: '/courses/course_detail/(\\d+)',
          component: Detail,

        },
        {
          path: '/courses/course_video/(\\d+)',
          component: Vedio,
          redirect: '/courses/course_chapter/(\\d+)',
          children: [
            {
              path: '/courses/course_chapter/(\\d+)',
              component: VideoChapter
            },
            {
              path: '/courses/course_comment/(\\d+)',
              component: VideoComment
            },
          ],

        },
        {
          path: '/orgs/teacher_detail/(\\d+)',
          component: TeacherDetail
        },
      ]
    },
    // 用户
    {
      path: '/users/user_center',
      component: UserCenter,
      redirect:'/users/user_info',
      children:[
        {
          path: '/users/user_info',
          component: UserInfo
        },
        {
          path: '/users/user_courses',
          component: UserCourses
        },
        {
          path: '/users/user_favors',
          component: UserFav,
          redirect: '/users/user_loveorg',
          children:[
            {
              path: '/users/user_loveorg',
              component: FavOrgs
            },
            {
              path: '/users/user_loveteacher',
              component: FavTeacher
            },
            {
              path: '/users/user_lovecourse',
              component: FavCourse,
            }
          ]
        }
      ]
    },
    {
      path: 'users/user_logout',
      component: UserLogout
    },
    {
      path: '/users/user_register',
      component: UserRegister
    },
    {
      path: '/users/user_login',
      component: Login
    },
    {
      path: '/users/user_forget',
      component: UserForget
    },
    {
      path: '/users/user_active/(\\w+)',
      component: UserActive
    },
    {
      path: '/users/user_reset/(\\w+)',
      component: UserReset
    },

    // org-detail
    {
      path: '/orgs/org_detail/(\\d+)',
      component: OrgHeader,
      redirect: '/orgs/org_detail_home/(\\d+)',
      children: [
        {
          path: '/orgs/org_detail_home/(\\d+)',
          component: OrgDetail
        },
        {
          path: '/orgs/org_detail_course/(\\d+)',
          component: OrgDetaiilCourse
        },
        {
          path: '/orgs/org_detail_desc/(\\d+)',
          component: OrgDetailDesc
        },
        {
          path: '/orgs/org_detail_teacher/(\\d+)',
          component: OrgDetailTeacher
        },
      ]
    },

  ]
})
