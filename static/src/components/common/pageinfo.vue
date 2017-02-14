<template>
    <div class="page">
        <ul class="pagination" style="margin-top:0px;">
            <li v-if="pageinfo.has_prev == true">
                <router-link :to="{path:path,query:{page:current_page - 1}}" aria-label="Previous">
                    <span aria-hidden="true">&laquo;</span>
                </router-link>
            </li>
            <li v-else class="disabled">
                <span aria-hidden="true">&laquo;</span>
            </li>
            <template v-for="page in pageinfo.iter_pages">
                <li>
                    <router-link :to="{path:path,query:{page:page}}">{{ page }}</router-link>
                </li>
            </template>
            <li v-if="pageinfo.has_next == true">
                <router-link :to="{path:path,query:{page:current_page + 1}}" aria-label="Next">
                    <span aria-hidden="true">&raquo;</span>
                </router-link>
            </li>
            <li v-else class="disabled">
                <span aria-hidden="true">&raquo;</span>
            </li>
        </ul>
    </div>
</template>


<script>
 export default {
     props: ['pageinfo'],
     data () {
         var path = this.$root.$route.fullPath
         console.log(path)
         return {
             path:path,
             current_page: parseInt(this.$root.$route.query.page)
         }
     },
 }
</script>
