<template>
  <div class="blog-panel">
    <Aplayer style="margin-left:0;margin-right:0;"></Aplayer>
    <ul class="list-group">
      <li class="list-group-item hidden-xs" style="text-align:center;">
        <img src="/static/images/header.png" width="60%" style="max-width:270px;" /> <br />
        <span style="display: inline-block;width:80%;" class="label label-default">
          <router-link :to="{name:'about'}" style="color:#fff">Author</router-link>
        </span>
        <span style="display: inline-block;width:80%;" class="label label-primary">
          About me
        </span>
        <br/>
        <span>
          <i>I like solitude, yearning for freedom</i>
        </span>
      </li>
      <li class="list-group-item text-center" style="font-size:24px;">
        <template v-for="social in socials">
          <a :href="social.url" target="_blank" :title="social.title"><i class="fa" :class="'fa-' + social.icon" aria-hidden="true"></i></a>
        </template>
      </li>
      <li class="list-group-item">
        <span class="label label-primary" style="display: inline-block;" v-for="tag in tags">
          <router-link :to="{name:'bloglist',query:{tag:tag.name}}"  style="color:#fff;">
            {{ tag.name }}
          </router-link>
        </span>
      </li>
    </ul>
    <div class="panel panel-default transparency7">
      <div class="panel-heading" style="background-color:rgba(255, 255, 255, 0.3);">
        <i class="fa fa-calendar" aria-hidden="true" style="color:#a40000"></i>
        TimeLine
      </div>
      <div class="panel-body panel-body-border" v-for="timeline in timelines">
        {{ timeline.content }}
        <footer><small style="color:#999;">{{ timeline.created_at | timesince }}</small></footer>
      </div>
    </div>
    <ul class="list-group">
      <li class="list-group-item text-center">
        <router-link :to="{name:'friend'}">
          <span class="glyphicon glyphicon-link"></span>
          Friends
        </router-link>
      </li>
    </ul>
    <div style="position:fixed; bottom:0;left:30%;width:100%;">
      <ul class="pager">
        <li><a href="#"><i class="fa fa-hand-o-up" aria-hidden="true"></i></a></li>
      </ul>
    </div>
  </div>
</template>

<script>
 import api from 'api'
 import Aplayer from 'components/aplayer'

 export default {
     components: {
         Aplayer,
     },
     data () {
         return {
             tags:[],
             timelines:[],
             socials:[
                 {
                     url:'https://github.com/honmaple',
                     icon:'github',
                     title:'GitHub'
                 },
                 {
                     url:'https://honmaple.com/blog/',
                     icon:'leaf',
                     title:'Blog'
                 },
                 {
                     url:'https://honmaple.com/books/',
                     icon:'book',
                     title:'Book'
                 },
                 {
                     url:'xiyang0807@gmail.com',
                     icon:'envelope',
                     title:'Gmail'
                 },
                 {
                     url:'https://www.facebook.com/honmaple',
                     icon:'facebook',
                     title:'FaceBook'
                 }
             ]
         }
     },
     created () {
         this.getTagList(),
         this.getTimeLineList()
     },
     methods: {
         getTagList: function() {
             var query = {number:20}
             this.$http.get(api.taglist,{params:query})
                 .then((response) => {
                     this.tags = response.body.data
                 })
                 .catch(function(response) {
                     console.log(response)
                 })
         },
         getTimeLineList: function() {
             this.$http.get(api.timeline)
                 .then((response) => {
                     this.timelines = response.body.data
                 })
                 .catch(function(response) {
                     console.log(response)
                 })
         },
     }
 }
</script>
