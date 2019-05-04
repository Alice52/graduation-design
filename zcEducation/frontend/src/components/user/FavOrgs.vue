<template>
  <div class="messagelist" v-if="showComponent">
    <div v-for="(org, index) in org_list" :index="index" :key="index" class="messages butler_list company company-fav-box">
      <dl class="des fr">
        <dt>
          <a @click="$router.push(`/orgs/org_detail/${org.pk}`)" >
            <img width="160" height="90" :src="getImgUrl(org.fields.image)">
          </a>
        </dt>
        <dd>
          <h1>
            <a @click="$router.push(`/orgs/org_detail/${org.pk}`)">{{ org.fields.name }}</a>
          </h1>
          <div class="pic fl" style="width:auto;"></div>
          <span class="c8 clear">{{ org.fields.address }}</span>
          <div class="delete jsDeleteFav_org" @click="deleteLove(org.pk, index)"></div>
        </dd>
      </dl>
    </div>
  </div>
</template>
<script>
  import axios from 'axios'
export default {
  mounted() {
    axios({
      url: '/api/users/user_loveorg/',
      method: 'GET'
    }).then((response)=>{
      var res = response.data
      this.org_list = JSON.parse(res.org_list)
      this.showComponent=true
    }).catch((err)=> {
      console.log(err)
    })
  },
  data() {
    return {
      org_list:[],
      showComponent: false,
    }
  },
  methods:{
    getImgUrl: (bannerUrl) =>{
      return "../../static/media/" + bannerUrl
    },
    deleteLove(favId, index) {
      axios({
        url: `/api/operations/user_deletelove/?loveid=${favId}&lovetype=1`,
        method: 'GET'
      }).then((response)=>{
        var res = response.data
        if (res.status == 'ok') {
          this.org_list.splice(index, 1)
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
