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
import CourseList from '../components/CourseList'
import TeacherList from '../components/TeacherList'
import OrgList from '../components/OrgList'


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
          component: CourseList
        },
        {
          path: '/teachers/teacher_list',
          component: TeacherList
        },
        {
          path: '/orgs/org_list',
          component: OrgList
        }
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
    {
      path: '/courses/course_list'
    }
  ]
})
