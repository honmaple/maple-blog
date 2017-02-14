<template>
    <div class="book">
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
            honmaple's blog
                </p>
            </div>
            <div class="collapse navbar-collapse" id="nav-header">
            <ul class="nav navbar-nav navbar-left">
            <li><router-link :to="{name:'bloglist'}">博客</router-link></li>
            <li><router-link :to="{name:'bloglist'}">WIKI</router-link></li>
            <li><router-link :to="{name:'timelinelist'}">时间轴</router-link></li>
            <li><router-link :to="{name:'booklist'}">书籍</router-link></li>
            <li><router-link :to="{name:'about'}">关于</router-link></li>
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
        <router-view></router-view>
    </div>
</template>

<script>
 export default {
     data () {
         return {
             title: 'HonMaple',
             description: 'asda'
         }
     }
 }
</script>
