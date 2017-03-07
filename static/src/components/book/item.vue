<template>
    <div class="media">
        <div class="media-left media-middle">
            <a href="">
                <img :src="'/static/books/'+item.name + '.jpg'" class="media-object" style="width:80px;height:120px;"/>
            </a>
        </div>
        <div class="media-body">
            <p><b>书籍名称:</b>  {{ item.name }}</p>
            <p><b>类型:</b>  {{ item.tag }}</p>
            <p><b>title:</b>  {{ item.title }}</p>
        </div>
        <p><b>作者简介:</b>  {{ item.author }}</p>
        <p><b>内容概要:</b>  {{ item.content }}</p>
</template>


<script>
 import api from 'api'

 export default {
     data () {
         return {
             item:{}
         }
     },
     created () {
         this.getBook()
     },
     watch: {
         '$route': 'getBook'
     },
     methods: {
         getBook: function() {
             this.$http.get(api.book +this.$root.$route.params.bookId)
                 .then((response) => {
                     this.item = response.body.data
                 })
                 .catch(function(response) {
                     console.log(response)
                 })
         },
     }
 }
</script>
