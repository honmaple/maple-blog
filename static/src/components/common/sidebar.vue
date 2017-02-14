<template>
    <div class="nav-side-menu" style="margin-top:50px;">
        <div class="brand"><a href="/console">管理控制台</a></div>
        <i class="fa fa-bars fa-2x toggle-btn" data-toggle="collapse" data-target="#menu-content"></i>
        <div class="menu-list">
            <ul id="menu-content" class="menu-content collapse out">
                <li>
                    <a href=""><i class="icon icon-home icon-lg"></i>个人资料</a>
                </li>
                <li>
                    <a data-toggle="collapse" href="#topic"><i class="icon icon-gift icon-lg"></i>主题管理<span class="arrow"></span></a>
                    <ul class="sub-menu collapse in" id="topic">
                        <li class="active"><a href="/console/topic">项目管理</a></li>
                        <li><a href="/console/topic/identity">身份管理</a></li>
                        <li><a href="/console/topic/strategy">策略管理</a></li>
                        <li><a href="/console/topic/hardware">设备管理</a></li>
                    </ul>
                </li>
                <li>
                    <a data-toggle="collapse"  href="#rule"><i class="icon icon-globe icon-lg"></i>规则管理<span class="arrow"></span></a>
                    <ul class="sub-menu collapse" id="rule">
                        <li><a href="/console/rule">规则列表</a></li>
                        <li>新建规则</li>
                    </ul>
                </li>
                <li><hr/></li>
                <li class="active">
                    <a href="/console/message">站内信管理</a>
                </li>
                <li>
                    <a data-toggle="collapse" href="#ticket"><i class="icon icon-home icon-lg"></i>工单管理<span class="arrow"></span></a>
                    <ul class="sub-menu collapse" id="ticket">
                        <li><a href="/console/ticket">工单列表</a></li>
                        <li><a href="/console/ticket/new">新建工单</a></li>
                    </ul>
                </li>
            </ul>
        </div>
    </div>
</template>

<script>
 export default {
     props: ['sidebar']
 }
</script>


<style>
 .nav-side-menu {
     overflow: auto;
     font-family: verdana;
     font-weight: 200;
     background-color: #222;
     position: fixed;
     top: 0px;
     width: 300px;
     height: 100%;
     color: #e1ffff;
 }
 .nav-side-menu .brand {
     background-color: #23282e;
     line-height: 50px;
     display: block;
     text-align: center;
 }
 .nav-side-menu .brand a{
     text-decoration: none;
     color: #e1ffff;
 }
 .nav-side-menu .toggle-btn {
     display: none;
 }
 .nav-side-menu ul,
 .nav-side-menu li {
     list-style: none;
     padding: 0px;
     margin: 0px;
     line-height: 35px;
     cursor: pointer;
 }
 .nav-side-menu ul :not(collapsed) .arrow:before,
 .nav-side-menu li :not(collapsed) .arrow:before {
     font-family: FontAwesome;
     content: "\f078";
     display: inline-block;
     padding-left: 16px;
     padding-right: 10px;
     vertical-align: middle;
     float: right;
 }
 .nav-side-menu ul .active,
 .nav-side-menu li .active {
     border-left: 3px solid #d19b3d;
     background-color: #4f5b69;
 }
 .nav-side-menu ul .sub-menu li.active,
 .nav-side-menu li .sub-menu li.active {
     color: #d19b3d;
 }
 .nav-side-menu ul .sub-menu li.active a,
 .nav-side-menu li .sub-menu li.active a {
     color: #d19b3d;
 }
 .nav-side-menu ul .sub-menu li,
 .nav-side-menu li .sub-menu li {
     background-color: #181c20;
     border: none;
     line-height: 28px;
     border-bottom: 1px solid #23282e;
     margin-left: 0px;
 }
 .nav-side-menu ul .sub-menu li:hover,
 .nav-side-menu li .sub-menu li:hover {
     background-color: #020203;
 }
 .nav-side-menu ul .sub-menu li:before,
 .nav-side-menu li .sub-menu li:before {
     font-family: FontAwesome;
     content: "\f105";
     display: inline-block;
     padding-left: 10px;
     padding-right: 10px;
     vertical-align: middle;
 }
 .nav-side-menu li {
     padding-left: 0px;
     border-left: 3px solid #2e353d;
     border-bottom: 1px solid #23282e;
 }
 .nav-side-menu li a {
     padding-left: 10px;
     text-decoration: none;
     color: #e1ffff;
 }
 .nav-side-menu li a i {
     padding-left: 10px;
     width: 20px;
     padding-right: 20px;
 }
 .nav-side-menu li:hover {
     border-left: 3px solid #d19b3d;
     background-color: #4f5b69;
     -webkit-transition: all 1s ease;
     -moz-transition: all 1s ease;
     -o-transition: all 1s ease;
     -ms-transition: all 1s ease;
     transition: all 1s ease;
 }
 @media (max-width: 767px) {
     .nav-side-menu {
         position: relative;
         width: 100%;
         margin-bottom: 10px;
     }
     .nav-side-menu .toggle-btn {
         display: block;
         cursor: pointer;
         position: absolute;
         right: 10px;
         top: 10px;
         z-index: 10 !important;
         padding: 3px;
         background-color: #ffffff;
         color: #000;
         width: 40px;
         text-align: center;
     }
     .brand {
         text-align: left !important;
         padding-left: 20px;
         line-height: 50px !important;
     }
 }
 @media (min-width: 767px) {
     .nav-side-menu .menu-list .menu-content {
         display: block;
     }
     .nav-side-content {
         width:calc(100% - 300px);
         float: right;
     }
 }
</style>
