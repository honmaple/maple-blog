<template>
    <div class="row">
        <div class="col-md-offset-2 col-md-8">
            <ul class="media-list" v-for="item in items">
                sssssj
                <li><hr/></li>
            </ul>
            <PageInfo :pageinfo="pageinfo"></PageInfo>
        </div>
    </div>
</template>

<script>
 import PageInfo from 'components/common/pageinfo'

 export default {
     components: {
         PageInfo,
     },
     data () {
         return {
             table:{
                 'th':['规则名称','主题','创建时间','操作']
             },
             items:[1,2,3,4,5],
             pageinfo:{}
         }
     },
     created () {
         this.getBlogList()
     },
     methods: {
         getBlogList: function() {
             this.$http.get('http://127.0.0.1:8000/message/',{params:{cloud_token:'MQ.C3hMJA.5NFkzsF2fErXKYHXWFefi9SYVFc'}})
                 .then((response) => {
                     this.items = response.body.data
                     this.pageinfo = response.body.pageinfo
                 })
                 .catch(function(response) {
                     console.log(response)
                 })
         }}
 }
</script>
