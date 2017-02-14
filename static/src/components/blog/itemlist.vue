<template>
    <div class="blog-list">
        <ul class="category" style="padding:0 15px" v-for="item in items">
            <li>
                <h3><router-link :to="{name:'blog',params:{blogId:item.id}}" target="_blank">{{ item.title }}</router-link></h3>
                <BlogHeader :item="item"></BlogHeader>
                <div>
                    <span class="content">
                        {{ item.content }}
                    </span>
                </div>
            </li>
            <li style="display:block;text-align:right;width:100%;">
                <router-link :to="{name:'blog',params:{blogId:item.id}}">more >></router-link>
            </li>
        </ul>
        <PageInfo :pageinfo="pageinfo"></PageInfo>
    </div>
</template>


<script>
 import api from 'api'
 import BlogHeader from './_macro'
 import PageInfo from 'components/common/pageinfo'

 export default {
     components: {
         PageInfo,
         BlogHeader,
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
         // 如果路由有变化，会再次执行该方法
         '$route': 'getBlogList'
     },
     methods: {
         getBlogList: function() {
             var query = this.$root.$route.query
             this.$http.get(api.bloglist,{params:query})
                             .then((response) => {
                                 this.items = response.body.data
                                 this.pageinfo = response.body.pageinfo
                             })
                             .catch(function(response) {
                                 console.log(response)
                             })
         }}
 }
</script>

<style>
 img {width:100%}
 li {
     list-style-type:none;
 }
 .category {
     margin-bottom:15px;
     background:#fff;
     border:1px solid #ddd;
     box-shadow:0px 0px 1px #ddd;
     border-radius: 3px;
 }
 .category:hover {
     background-color:rgba(255, 255, 255, 0.6);
 }
</style>
