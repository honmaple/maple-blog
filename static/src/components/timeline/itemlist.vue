<template>
    <div class="row">
        <div class="col-md-offset-2 col-md-8">
            <ul class="media-list" v-for="item in items">
                <li>{{ item.content }}</li>
                <li>
                    <footer><small style="color:#999;">{{ item.created_at | timesince }}</small></footer>
                    <hr/>
                </li>
            </ul>
            <PageInfo :pageinfo="pageinfo"></PageInfo>
        </div>
    </div>
</template>

<script>
 import api from 'api'
 import PageInfo from 'components/common/pageinfo'

 export default {
     components: {
         PageInfo,
     },
     data () {
         return {
             items:[],
             pageinfo:{}
         }
     },
     created () {
         this.getTimeLineList()
     },
     watch: {
         '$route': 'getTimeLineList'
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
