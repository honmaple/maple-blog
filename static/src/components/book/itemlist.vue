<template>
  <div class="row">
    <div class="col-sm-9" style="padding:0">
      <div class="row">
        <div class="col-xs-4 col-sm-2 text-center" v-for="item in items">
          <div style="height:160px;width:auto">
            <img :src="'/static/books/'+item.name + '.jpg'" style="width:80px;height:120px;"/>
            <br />
            <router-link :to="{name:'book',params:{bookId:item.id}}">{{ item.name }}</router-link>
          </div>
        </div>
      </div>
      <PageInfo :pageinfo="pageinfo"></PageInfo>
    </div>
    <div class="col-sm-3">
      <BookTags></BookTags>
    </div>
  </div>
</template>

<script>
 import api from 'api'
 import {lazyload} from 'globals'

 export default {
     components: {
         PageInfo:lazyload('common/pageinfo.vue'),
         BookTags:lazyload('book/tags.vue')
     },
     data () {
         return {
             items:[],
             pageinfo:{}
         }
     },
     created () {
         this.getBookList()
     },
     watch: {
         '$route': 'getBookList'
     },
     methods: {
         getBookList: function() {
             var query = this.$root.$route.query
             this.$http.get(api.book,{params:query})
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
