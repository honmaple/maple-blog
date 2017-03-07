<template>
  <div class="archive">
    <div class="panel panel-default transparency7">
      <div class="panel-heading"  style="background-color:rgba(255, 255, 255, 0.3);">
        按时间归档
      </div>
      <div class="panel-body" style="padding:1px 16px;" v-for="time in times.slice(0,10)">
        <router-link :to="{name:'blogarchives',query:{year:time[0],month:time[1]}}">
          {{ time[0] }}年{{ time[1] }}月
        </router-link>
        <small>({{ time[2] }})</small>
      </div>
      <template v-if="times.length > 10">
        <div class="panel-body collapse" id="archive-time" style="padding:1px 16px;" v-for="time in times.slice(10)">
          <router-link :to="{name:'blogarchives',query:{year:time[0],month:time[1]}}">
            {{ time[0] }}年{{ time[1] }}月
          </router-link>
          <small>({{ time[2] }})</small>
        </div>
        <div class="panel-footer archives transparency3">
          <i class="fa fa-angle-double-down text-center" data-toggle="collapse" data-target="#archive-time" aria-hidden="true" style="width:100%;"></i>
        </div>
      </template>
    </div>
    <div class="panel panel-default transparency7">
      <div class="panel-heading"  style="background-color:rgba(255, 255, 255, 0.3);">
        按分类归档
      </div>
      <div class="panel-body">
        <template v-for="category in categoies">
          <router-link :to="{name:'blogarchives',query:{category:category.name}}" class="label label-primary" style="display:inline-block;color:#fff;">
            {{ category.name }}
            <span class="badge" style="background-color:#fff;color:#337ab7;">{{ category.count }}</span>
          </router-link>
        </template>
      </div>
    </div>
    <div class="panel panel-default transparency7">
      <div class="panel-heading"  style="background-color:rgba(255, 255, 255, 0.3);">
        按节点归档
      </div>
      <div class="panel-body">
        <template v-for="tag in tags.slice(0,20)">
          <router-link :to="{name:'blogarchives',query:{tag:tag.name}}" class="label label-primary" style="display:inline-block;color:#fff;">
            {{ tag.name }}
            <span class="badge" style="background-color:#fff;color:#337ab7;">{{ tag.count }}</span>
          </router-link>
        </template>
      </div>
      <template v-if="tags.length > 20">
        <div class="panel-body collapse" id="archive-tag" style="padding:1px 16px;">
          <template v-for="tag in tags.slice(20)">
            <router-link :to="{name:'blogarchives',query:{tag:tag.name}}" class="label label-primary" style="display:inline-block;color:#fff;">
              {{ tag.name }}
              <span class="badge" style="background-color:#fff;color:#337ab7;">{{ tag.count }}</span>
            </router-link>
          </template>
        </div>
        <div class="panel-footer archives transparency3">
          <i class="fa fa-angle-double-down text-center" data-toggle="collapse" data-target="#archive-tag" aria-hidden="true" style="width:100%;"></i>
        </div>
      </template>
    </div>
  </div>
</template>

<script>
 import api from 'api'

 export default {
     data () {
         return {
             categoies:[],
             tags:[],
             times:[]
         }
     },
     created () {
         this.getTagList(),
         this.getCategoryList(),
         this.getTimeList()
     },
     methods: {
         getCategoryList: function() {
             this.$http.get(api.categorylist)
                 .then((response) => {
                     this.categoies = response.body.data
                 })
                 .catch(function(response) {
                     console.log(response)
                 })
         },
         getTagList: function() {
             var query = {number:60}
             this.$http.get(api.taglist,{params:query})
                 .then((response) => {
                     this.tags = response.body.data
                 })
                 .catch(function(response) {
                     console.log(response)
                 })
         },
         getTimeList: function() {
             this.$http.get(api.blogtimelist)
                 .then((response) => {
                     this.times = response.body.data
                 })
                 .catch(function(response) {
                     console.log(response)
                 })
         },
     }
 }
</script>
