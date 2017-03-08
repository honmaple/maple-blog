<template>
  <div class="category" style="padding:15px;">
    <h1 class="text-center" style="font-size:30px;">{{ item.title }}</h1>
    <hr style="max-width:none" />
    <BlogInfo :item="item" :category="category" :author="author" class="pull-right"></BlogInfo>
    <div class="blog-content text-left">
      <span v-html="item.content" v-highlight></span>
    </div>
  </div>
</template>

<script>
 import api from 'api'
 import BlogInfo from './info'
 import markup from './markup'
 import blogmixin from 'services/blog'
 import { callback } from 'globals'

 export default {
     mixins: [blogmixin],
     components: {
         BlogInfo,
     },
     data () {
         return {
             item:{},
             author:{},
             category:{}
         }
     },
     created () {
         this.getItem(this.$route.params.blogId).then((response) => {
             return  callback(
                 this,
                 response.body,
                 function(_this) {
                     _this.item = response.body.data
                     _this.item.content = markup(_this.item.content_type,_this.item.content)
                     _this.author = _this.item.author
                     _this.category = _this.item.category
                 }
             )
         }).catch(function(response) {
             console.log(response)
         })
     },
 }
</script>
