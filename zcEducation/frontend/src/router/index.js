import Vue from 'vue'
import Router from 'vue-router'
import Login from '../components/user/Login'
import Home from '../components/Home'
import UserInfo from '../components/user/UserInfo'
import UserForget from '../components/user/ForgetPwd'
import UserLogout from '../components/user/UserLogout'
import UserRegister from '../components/user/Register'
import UserActive from '../components/user/UserActive'
import UserReset from '../components/user/PasswordReset'



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
      path: '/users/user_info',
      component: UserInfo
    },
    {
      path: '/users/user_courses',
      // component: UserActive
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
