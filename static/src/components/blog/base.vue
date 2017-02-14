<template>
    <div class="blog">
        <nav class="navbar navbar-inverse navbar-fixed-top">
            <div class="container-fluid col-md-offset-1 col-md-10">
                <div class="navbar-header">
                    <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#nav-header" aria-expanded="false">
                        <span class="sr-only">Toggle navigation</span>
                        <span class="icon-bar"></span>
                        <span class="icon-bar"></span>
                        <span class="icon-bar"></span>
                    </button>
                    <a class="navbar-brand" href="/" style="padding:0px">
                        <img src="https://honmaple.com/static/images/snow.jpg" style="width:120px;height:51px">
                    </a>
                    <p class="navbar-text visible-xs-block">
                        HELLO WORLD
                    </p>
                </div>
                <div class="collapse navbar-collapse" id="nav-header">
                    <ul class="nav navbar-nav navbar-left" v-for="item in items">
                        <li><router-link :to="{name:'bloglist',params:{category:item.name}}">{{ item.name }}</router-link></li>
                    </ul>
                    <form class="navbar-form navbar-right" style="margin-top:10px;" >
                        <div class="form-group has-feedback">
                            <input class="form-control input-sm" id="search" name="search" placeholder="Search" type="text" value="">
                            <i class="fa fa-search form-control-feedback"></i>
                        </div>
                    </form>
                </div>
            </div>
        </nav>
        <div class="row">
            <div class="col-md-9">
                <router-view></router-view>
            </div>
            <div class="col-md-3">
                <BlogPanel></BlogPanel>
            </div>
        </div>
    </div>
</template>

<script>
 import api from 'api'
 import BlogPanel from './panel'

 export default {
     components: {
         BlogPanel
     },
     data () {
         return {
             items:[],
             categories:[],
         }
     },
     created () {
         this.getCategoryList(),
         this.getTagList()
     },
     methods: {
         getCategoryList: function() {
             this.$http.get(api.categorylist)
                 .then((response) => {
                     this.items = response.body.data
                     this.pageinfo = response.body.pageinfo
                 })
                 .catch(function(response) {
                     console.log(response)
                 })
         },
         getTagList: function() {
             this.$http.get(api.taglist)
                 .then((response) => {
                     this.items = response.body.data
                     this.pageinfo = response.body.pageinfo
                 })
                 .catch(function(response) {
                     console.log(response)
                 })
         }
     }
 }
</script>
