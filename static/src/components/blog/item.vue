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

 export default {
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
         this.getBlog()
     },
     methods: {
         getBlog: function() {
             this.$http.get(api.bloglist + this.$root.$route.params.blogId)
                 .then((response) => {
                     this.item = response.body.data
                     this.item.content = markup(this.item.content_type,this.item.content)
                     this.author = this.item.author
                     this.category = this.item.category
                 })
                 .catch(function(response) {
                     console.log(response)
                 })
         },
     },
 }
</script>
