<template>
    <div class="category" style="padding:0 15px;">
        <h1 class="text-center" style="font-size:30px;">{{ item.title }}</h1>
        <BlogHeader :item="item" :category="category" :author="author"></BlogHeader>
        <div class="blog-content" id="org-mode-parser">
            {{ item.content }}
        </div>
    </div>
</template>

<script>
 import api from 'api'
 import BlogHeader from './item_header'

 export default {
     components: {
         BlogHeader,
     },
     data () {
         return {
             item:{},
             author:{},
             category:{},
             tags:[]
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
                     this.author = this.item.author
                     this.category = this.item.category
                     this.tags = this.item.tags
                 })
                 .catch(function(response) {
                     console.log(response)
                 })
         }}
 }
</script>
