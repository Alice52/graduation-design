import Vue from 'vue'
import Router from 'vue-router'
import Login from '../components/user/Login'
import Home from '../components/Home'
import UserInfo from '../components/user/UserInfo'
import UserForget from '../components/user/ForgetPwd'
import UserLogout from '../components/user/UserLogout'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    // {
    //   path: '*',
    //   name: 'error',
    //   component: Home
    // },
    {
      path: '/',
      component: Home
    },
    // 用户
    {
      path: '/user/user_info',
      component: UserInfo
    },
    {
      path: '/user/user_logout',
      component: UserLogout
    },
    {
      path: '/user/user_register',
      component: UserForget
    },
    {
      path: '/user/user_login',
      component: Login
    },
    {
      path: '/courses/course_list'
    }
  ]
})
