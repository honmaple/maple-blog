<template>
    <div class="row">
        <div class="col-md-9">
            <router-view></router-view>
        </div>
        <div class="col-md-3">
            <BlogPanel></BlogPanel>
        </div>
    </div>
</template>

<script>
 import BlogPanel from './panel'

 export default {
     components: {
         BlogPanel
     }
 }
</script>
