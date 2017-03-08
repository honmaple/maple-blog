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
 import blogmixin from 'services/blog'
 import {callback,lazyload} from 'globals.js'

 export default {
     mixins: [blogmixin],
     components: {
         PageInfo:lazyload('common/pageinfo.vue')
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
         '$route': 'getBlogList'
     },
     methods: {
         getBlogList: function() {
             var query = this.$root.$route.query
             query['number'] = 30
             this.getItemList(query).then(response => {
                 return callback(
                     this,response.body,
                     function(_this) {
                         _this.items = response.body.data
                         _this.pageinfo = response.body.pageinfo
                     }
                 )
             })
         },
     }
 }
</script>
