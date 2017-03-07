<template>
  <div class="panel panel-default category">
    <div class="panel-heading" style="background-color:rgba(255, 255, 255, 0.5);">
      <b>Friends</b>
    </div>
    <div class="panel-body bottom-line">
      <div class="row">
        <div class="col-md-3" style="margin-bottom:5px;" v-for="item in items.slice(0,2)">
          <div class="media">
            <a class="media-left" :href="item.href" target="_blank">
              <img :src="item.img" style="width:64px;" class="img-circle" />
            </a>
            <div class="media-body"  style="padding-top:9px;">
              <h5 class="media-heading"><b>{{ item.title }}</b></h5>
              <small>
                {{ item.dep }}
              </small>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="panel-body">
      <div class="row">
        <div class="col-md-3" style="margin-bottom:5px;" v-for="item in items.slice(2,3)">
          <div class="media">
            <a class="media-left" :href="item.href" target="_blank">
              <img :src="item.img" style="width:64px;" class="img-circle" />
            </a>
            <div class="media-body"  style="padding-top:9px;">
              <h5 class="media-heading"><b>{{ item.title }}</b></h5>
              <small>
                {{ item.dep }}
              </small>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script type="text/javascript">
 export default {
     data () {
         return {
             items:[
                 {
                     title:'honmaple论坛',
                     dep:'爱生活，更爱自由',
                     img:'static/images/header.png',
                     href:'https://forums.honmaple.org'
                 },
                 {
                     title:"honmaple'blog",
                     dep:'自由',
                     img:'static/images/header.png',
                     href:'http://honmaple.org'
                 },
                 {
                     title:"创造狮",
                     dep:'创意工作者导航',
                     img:'static/images/header.png',
                     href:'http://chuangzaoshi.com/'
                 },
             ]
         }
     }
 }
</script>

<style>
 .bottom-line {
     border-bottom:1px solid #eee;
 }
</style>
