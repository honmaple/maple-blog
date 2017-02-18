<template>
    <div class="row">
        <div class="col-sm-9">
            <div class="row" style="padding:0">
                <div class="col-xs-4 col-sm-2 text-center" v-for="item in items">
                    <div style="height:160px;width:auto">
                        <img src="" alt="book" style="width:80px;height:120px;"/>
                        <br />
                        <router-link :to="{name:'book',params:{bookId:item.id}}">{{ item.name }}</router-link>
                    </div>
                </div>
            </div>
        </div>
        <div class="col-sm-3" id="book-tags">
        </div>
    </div>
</template>

<script>
 import api from 'api'
 export default {
     data () {
         return {
             table:{
                 'th':['规则名称','主题','创建时间','操作']
             },
             items:[],
             pageinfo:{}
         }
     },
     created () {
         this.getBookList()
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
