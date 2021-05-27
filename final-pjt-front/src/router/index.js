import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Stock from '../views/Stock.vue'
import Login from '../views/accounts/Login.vue'
import Signup from '../views/accounts/Signup.vue'
import MovieDetail from '../views/movies/MovieDetail.vue'
import MovieTMDBdetail from '../views/movies/MovieTMDBdetail.vue'
import CommunityList from '../views/community/CommunityList.vue'
import CommunityDetail from '../views/community/CommunityDetail.vue'
import CommunityCreate from '../views/community/CommunityCreate.vue'
import CommunityEdit from '../views/community/CommunityEdit.vue'
import NavSearchResult from '../views/NavSearchResult.vue'

Vue.use(VueRouter)

const routes = [{
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/navsearchresult',
    name: 'NavSearchResult',
    component: NavSearchResult,
  },
  {
    path: '/accounts/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/accounts/signup',
    name: 'Signup',
    component: Signup
  },
  {
    path: '/stock',
    name: 'Stock',
    component: Stock
  },
  {
    path: '/movies/detail',
    name: 'MovieDetail',
    component: MovieDetail
  },
  {
    path: '/movies/tmdbdetail',
    name: 'MovieTMDBdetail',
    component: MovieTMDBdetail
  },
  {
    path: '/community',
    name: 'Community',
    component: CommunityList
  },
  {
    path: '/community/article',
    name: 'ArticleDetail',
    component: CommunityDetail
  },
  {
    path: '/community/new',
    name: 'CreateArticle',
    component: CommunityCreate
  },
  {
    path: '/community/article/new',
    name: 'EditArticle',
    component: CommunityEdit
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router