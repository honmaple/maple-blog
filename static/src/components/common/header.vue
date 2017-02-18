<template>
    <nav class="navbar navbar-default navbar-fixed-top">
        <div class="container-fluid col-md-offset-1 col-md-10">
            <div class="navbar-header">
                <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#nav-header" aria-expanded="false">
                    <span class="sr-only">Toggle navigation</span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                </button>
                <router-link :to="{name:'index'}" class="navbar-brand" style="padding:0px">
                    <img src="static/images/storm-bg.jpg" style="width:120px;height:51px">
                </router-link>
                <p class="navbar-text visible-xs-block">
                    HELLO WORLD
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
