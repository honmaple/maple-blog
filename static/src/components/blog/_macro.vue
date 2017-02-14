<template>
    <div class="blog-header">
        <span class="glyphicon glyphicon-calendar" aria-hidden="true"></span>:
        <small style="color:#999">{{ item.created_at | timesince }} </small> |
        <span class="glyphicon glyphicon-tags" aria-hidden="true"></span> :
        <small v-for="tag in item.tags">
            <router-link :to="{name:'bloglist',query:{tag:tag.name}}" style="color:#eb5424;margin-left:3px;">{{ tag.name }}</router-link>
        </small> |
        <span class="glyphicon glyphicon-book" aria-hidden="true"></span>:
        <small style="color:#999">{{ item.id }}</small>
    </div>
</template>

<script>
 export default {
     props: ['item']
 }
</script>
