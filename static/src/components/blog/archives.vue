<template>
  <div>
    <div class="panel panel-default transparency7">
      <div class="panel-heading" style="background-color:rgba(255, 255, 255, 0.3);">
        Archives of honmaple
      </div>
      <div class="panel-body">
        <template v-for="item in items">
          <span class="glyphicon glyphicon-calendar" aria-hidden="true"></span>
          <span>{{ item.created_at | timesince }}</span>
          <router-link :to="{name:'blog',params:{blogId:item.id}}">{{ item.title }}</router-link>
          <br/>
        </template>
      </div>
    </div>
    <PageInfo :pageinfo="pageinfo"></PageInfo>
  </div>
</template>

<script>
 import api from 'api'
 import PageInfo from 'components/common/pageinfo'

 export default {
     components: {
         PageInfo,
     },
     data () {
         return {
             items:[],
             pageinfo:{}
         }
     },
     created () {
         this.getBlogList()
     },
     watch: {
         // 如果路由有变化，会再次执行该方法
         '$route': 'getBlogList'
     },
     methods: {
         getBlogList: function() {
             var query = this.$root.$route.query
             query['number'] = 30
             this.$http.get(api.bloglist,{params:query})
                 .then((response) => {
                     this.items = response.body.data
                     this.pageinfo = response.body.pageinfo
                 })
                 .catch(function(response) {
                     console.log(response)
                 })
         },
     }
 }
</script>
