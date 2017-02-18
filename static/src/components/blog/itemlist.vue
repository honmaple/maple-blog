<template>
    <div class="blog-list">
        <ul class="media-list" style="margin:0">
            <template v-for="item in items">
                <li class="media category">
                    <h3 class="text-left"><router-link :to="{name:'blog',params:{blogId:item.id}}" target="_blank">{{ item.title }}</router-link></h3>
                    <hr style="max-width:none" />
                    <div class="media-left">
                        <BlogHeader :item="item" :author="item.author" :category="item.category" class="text-left"></BlogHeader>
                    </div>
                    <div class="media-body" style="width: 79%;">
                        <span class="blog-content text-left" v-html="markup(item.content_type,item.content.slice(0,255))"></span>
                        <div class="media-footer text-right" style="margin-top:auto;display:block;text-align:right;width:100%;">
                            <router-link :to="{name:'blog',params:{blogId:item.id}}">read more</router-link>
                        </div>
                    </div>
                </li>
            </template>
        </ul>
        <PageInfo :pageinfo="pageinfo"></PageInfo>
    </div>
</template>


<script>
 import api from 'api'
 import BlogHeader from './header'
 import PageInfo from 'components/common/pageinfo'
 import markup from './markup'

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
         markup,
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
         },
     }
 }
</script>

<style>
 img {width:100%}
 li {
     list-style-type:none;
 }
 .padding {padding:0}
 .margin {margin:0}
 .padgin {padding:0;margin:0}
 .font-small {font-size:12px}
 .font-big {font-size:16px}
 .header-color {color:#eb5424}
 .header-back {background:#fff;padding:0;margin-bottom:10px;}
 .category {
     margin-bottom:15px;
     /* background:#fff; */
     padding:5px 30px;
     border:1px solid #ddd;
     box-shadow:0px 0px 1px #ddd;
     border-radius: 3px;
 }
 .category:hover {
     background-color:rgba(255, 255, 255, 0.6);
 }
 .tags {
     color:#777;
 }
 .question {
     display: inline-block;
     background-color: #a40000;
     padding: 2px;
     border: 1px solid #a40000;
     font-size: 12px;
     line-height: 12px;
     font-weight: 400;
     border-radius: 2px;
     margin-right: 5px;
     vertical-align: 1px;
     text-decoration: none;
     color: #FBFBFB;
 }
 .font-color1 {
     color:#eb5424;
 }
 .font-color2 {
     color: #ad1616;
 }
 .answer {
     color: #ad1616;
 }
 .cate {
     padding:0 4px;
 }
 span.content h1 {
     font-size:25px;
 }
 span.content h2 {
     font-size:22px;
 }
 span.content h3 {
     font-size:19px;
 }
 span.content blockquote {
     font-size:14px;
     color:#666;
 }
 span.content ul {
     padding-left:16px;
 }
 span.content ol {
     padding-left:16px;
 }
 span.content li {
     list-style-type:circle;
 }
 .blog-content {
     color: #333;
 }
 .blog-content h1 {
     font-size:25px;
     font-weight:bold;
 }
 .blog-content h2 {
     font-size:22px;
     font-weight:bold;
 }
 .blog-content h3 {
     font-size:19px;
     font-weight:bold;
 }
 .blog-content blockquote {
     font-size:16px;
     color:#666;
 }
 .blog-content ul {
     padding-left:16px;
 }
 .blog-content ol {
     padding-left:16px;
 }
 .blog-content li {
     list-style-type:circle;
 }
 .blog-content img {
     max-width: 480px;
     width:100%;
     height: auto;
     display: block;
 }
 code.hljs {
     padding: 6px 16px;
 }
 /* .blog-content pre,.blog-content .highlight,span.content pre, span.content .highlight {
    margin: 0;
    padding: 0;
    border-style: solid;
    border-color: #eceff2;
    border-width: 1px 0;
    overflow: auto;
    line-height: 22.400000000000002px;
    } */
 .label-tag {
     background-color: #ab5424;
 }
 .tag-badge {
     background-color:#fff;
     color:#337ab7;
     padding:2px 6px;
     font-size: 10px;
 }
 a {
     color: #333;
 }
 a:focus, a:hover {
     color:#EB5455;
     text-decoration: none;
 }
 .a-blue {
     color: #369;
 }
 div.category,ul.category,ul.list-group,li.list-group-item,nav.navbar,ul.dropdown-menu {
     filter:progid:DXImageTransform.Microsoft.gradient(startColorstr='#3f000000',endColorstr='#3f000000');
     background-color:rgba(255, 255, 255, 0.5);
 }
 .navbar-default .navbar-nav > li > a {
     color: #555;
 }
 .transparency1 {
     background-color:rgba(255, 255, 255, 0.1);
 }
 .transparency2 {
     background-color:rgba(255, 255, 255, 0.2);
 }
 .transparency3 {
     background-color:rgba(255, 255, 255, 0.3);
 }
 .transparency4 {
     background-color:rgba(255, 255, 255, 0.4);
 }
 .transparency5 {
     background-color:rgba(255, 255, 255, 0.5);
 }
 .transparency6 {
     background-color:rgba(255, 255, 255, 0.6);
 }
 .transparency7 {
     background-color:rgba(255, 255, 255, 0.7);
 }
 .panel-body-border {
     border-bottom:1px solid #eea;
 }
 .archives {
     padding: 0 0 0 24px;
     color: #666;
     cursor: pointer;
 }
 .hidelist {
     display:none;
 }
</style>
