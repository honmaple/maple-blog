<template>
    <div class="blog-panel">
        <Aplayer></Aplayer>
        <ul class="list-group">
            <li class="list-group-item hidden-xs" style="text-align:center;">
                <img src="static/images/header.png" width="60%" style="max-width:270px;" /> <br />
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
                <a href="https://github.com/honmaple" target="_blank" title="GitHub"><i class="fa fa-github" aria-hidden="true"></i></a>
                <a href="https://honmaple.com/blog/" target="_blank" title="Blog"><i class="fa fa-leaf" aria-hidden="true"></i></a>
                <a href="https://honmaple.com/books/" target="_blank" title="Book"><i class="fa fa-book" aria-hidden="true"></i></a>
                <a href="xiyang0807@gmail.com" target="_blank" title="Gmail"><i class="fa fa-envelope" aria-hidden="true"></i></a>
                <a href="https://www.facebook.com/honmaple" target="_blank" title="FaceBook"><i class="fa fa-facebook" aria-hidden="true"></i></a>
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
            <div class="panel-body panel-body-border">
                <TimeLineList></TimeLineList>
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
 import TimeLineList from 'components/timeline/itemlist'

 export default {
     components: {
         Aplayer,
         TimeLineList
     },
     data () {
         return {
             tags:[],
         }
     },
     created () {
         this.getTagList()
     },
     methods: {
         getTagList: function() {
             this.$http.get(api.taglist)
                 .then((response) => {
                     this.tags = response.body.data
                 })
                 .catch(function(response) {
                     console.log(response)
                 })
         }
     }
 }
</script>
