<template>
    <div class="row">
        <div class="col-md-offset-2 col-md-8">
            <ul class="media-list" v-for="item in items">
                {{ item.content }}
                <li><hr/></li>
            </ul>
            <PageInfo :pageinfo="pageinfo"></PageInfo>
        </div>
    </div>
</template>

<script>
 import PageInfo from 'components/common/pageinfo'
 import api from 'api'

 export default {
     components: {
         PageInfo,
     },
     data () {
         return {
             items:[1,2,3,4,5],
             pageinfo:{}
         }
     },
     created () {
         this.getTimeLineList()
     },
     methods: {
         getTimeLineList: function() {
             var query = this.$root.$route.query
             this.$http.get(api.timeline,{params:query})
                             .then((response) => {
                                 this.items = response.body.data
                                 this.pageinfo = response.body.pageinfo
                             })
                             .catch(function(response) {
                                 console.log(response)
                             })
         },
     }
 }
</script>
