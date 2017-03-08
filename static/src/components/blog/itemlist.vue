<template>
  <div class="blog-list">
    <ul class="media-list">
      <li class="media blog" v-for="item in items">
        <h3><router-link :to="{name:'blog',params:{blogId:item.id}}">{{ item.title }}</router-link></h3>
        <hr style="max-width:none" />
        <div class="media-left">
          <BlogInfo :item="item" :author="item.author" :category="item.category" class="text-left"></BlogInfo>
        </div>
        <div class="media-body" style="width: 79%;">
          <span class="blog-content text-left" v-html="markup(item.content_type,item.content.slice(0,255))" v-highlight></span>
          <div class="media-footer text-right" style="margin-top:auto;display:block;text-align:right;width:100%;">
            <router-link :to="{name:'blog',params:{blogId:item.id}}">read more</router-link>
          </div>
        </div>
      </li>
    </ul>
    <PageInfo :pageinfo="pageinfo"></PageInfo>
  </div>
</template>


<script>
 import api from 'api'
 import BlogInfo from './info'
 import PageInfo from 'components/common/pageinfo'
 import markup from './markup'
 import blogmixin from 'services/blog'
 import {callback} from 'globals'

 export default {
     mixins: [blogmixin],
     components: {
         PageInfo,
         BlogInfo,
     },
     data () {
         return {
             items:[],
             pageinfo:{}
         }
     },
     created () {
         this._getBlogList()
     },
     watch: {
         // 如果路由有变化，会再次执行该方法
         '$route': '_getBlogList'
     },
     methods: {
         markup,
         _getBlogList: function() {
             var query = this.$route.query
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
