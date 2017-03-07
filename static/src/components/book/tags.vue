<template>
    <div>
        <span class="label label-info book-tag" v-for="item in items">
            <router-link :to="{name:'booklist',query:{tag:item.tag}}">{{ item.tag }}</router-link>
        </span>
    </div>
</template>

<script>
 import api from 'api'
 export default {
     data () {
         return {
             items:[],
         }
     },
     created () {
         this.getBookTags()
     },
     methods: {
         getBookTags: function() {
             this.$http.get(api.book + 'tags')
                 .then((response) => {
                     this.items = response.body.data
                 })
                 .catch(function(response) {
                     console.log(response)
                 })
         },
     }
 }
</script>

<style>
 .book-tag {
     display: inline-block;
 }
 .book-tag a{
     color:#fff;
 }
</style>
