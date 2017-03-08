<template>
  <div class="row">
    <div class="col-md-9">
      <router-view></router-view>
    </div>
    <div class="col-md-3 blog-no-margin" v-if="$route.path == '/blog/archives'">
      <keep-alive>
        <ArchivePanel></ArchivePanel>
      </keep-alive>
    </div>
    <div class="col-md-3 blog-no-margin" v-else>
      <keep-alive>
        <BlogPanel></BlogPanel>
      </keep-alive>
    </div>
  </div>
</template>

<script>
 import {lazyload} from 'globals'

 export default {
     components: {
         BlogPanel:lazyload('blog/panel'),
         ArchivePanel:lazyload('blog/archives_panel')
     }
 }
</script>

<style>
 .blog-no-margin {
     padding-left:0px;
 }
 .blog-no-padding {
     padding-left:0px;
     padding-right:0px;
 }
 .blog {
     margin-bottom:15px;
     background-color:rgba(255, 255, 255, 0.3);
     padding:5px 30px;
     border:1px solid #ddd;
     box-shadow:0px 0px 1px #ddd;
     border-radius: 3px;
 }
 .blog:hover {
     background-color:rgba(255, 255, 255, 0.5);
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
     max-width: 640px;
     width:100%;
     height: auto;
     display: block;
 }
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
</style>
