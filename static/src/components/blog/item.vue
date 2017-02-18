<template>
    <div class="category" style="padding:0 15px;">
        <h1 class="text-center" style="font-size:30px;">{{ item.title }}</h1>
        <BlogHeader :item="item" :category="category" :author="author" class="text-left pull-right"></BlogHeader>
        <div class="blog-content text-left">
            <span v-html="item.content"></span>
        </div>
    </div>
</template>

<script>
 import api from 'api'
 import BlogHeader from './header'
 import markup from './markup'

 export default {
     components: {
         BlogHeader,
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
