<template>
  <nav class="navbar navbar-default navbar-fixed-top">
    <div class="col-md-offset-1 col-md-10">
      <div class="navbar-header">
        <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#nav-header" aria-expanded="true">
          <span class="sr-only">Toggle navigation</span>
          <span class="icon-bar"></span>
          <span class="icon-bar"></span>
          <span class="icon-bar"></span>
        </button>
        <router-link :to="{name:'index'}" class="navbar-brand" style="padding:0px">
          <img src="/static/images/header.png" style="width:72px;height:72px">
        </router-link>
        <p class="navbar-text visible-xs-block text-center">
          HELLO WORLD
        </p>
      </div>
      <div class="collapse navbar-collapse" id="nav-header">
        <ul class="nav navbar-nav navbar-left">
          <li v-for="category in categories.slice(0,4)">
            <router-link :to="{name:'bloglist',query:{category:category.name}}">{{ category.name }}</router-link>
          </li>
          <li v-if="categories.length > 4">
            <a href="#" class="dropdown-toggle" id="dropdown-more" data-toggle="dropdown">······</a>
            <ul class="dropdown-menu" role="menu" aria-labelledby="dropdown-more">
              <li role="presentation" v-for="category in categories.slice(start=4)">
                <router-link :to="{name:'bloglist',query:{category:category.name}}">{{ category.name }}</router-link>
              </li>
            </ul>
          </li>
          <li><router-link :to="{name:'blogarchives'}">归档</router-link></li>
          <li><router-link :to="{name:'blogarchives'}">Rss</router-link></li>
        </ul>
        <form class="navbar-form navbar-right" style="margin-top:10px;" >
          <div class="form-group has-feedback">
            <input class="form-control input-sm" id="search" name="search" placeholder="搜索" type="text">
            <i class="fa fa-search form-control-feedback"></i>
          </div>
        </form>
      </div>
    </div>
  </nav>
</template>

<script>
 import api from 'api'

 export default {
     data () {
         return {
             categories:[]
         }
     },
     created () {
         this.getCategoryList()
     },
     methods: {
         getCategoryList: function() {
             this.$http.get(api.categorylist)
                 .then((response) => {
                     this.categories = response.body.data
                 })
                 .catch(function(response) {
                     console.log(response)
                 })
         }
     }
 }
</script>

<style>
 .navbar .nav > li .dropdown-menu {
     margin: 0;
 }
 .navbar .nav > li:hover .dropdown-menu {
     display: block;
 }
</style>
