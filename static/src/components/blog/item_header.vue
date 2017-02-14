<template>
    <div class="blog-header">
        <footer class="pull-right">
            <span class="glyphicon glyphicon-time"></span>
            <abbr :title="item.created_at">
                <span class="label label-success">{{ item.created_at | timesince }}</span>
            </abbr>
            <address style="margin-top:8px">
                <span class="glyphicon glyphicon-user"></span>
                <router-link :to="{name:'bloglist',query:{author:author.username}}" class="label label-primary">{{ author.username }}</router-link>
            </address>
            <address style="margin-top:-12px">
                <span class="glyphicon glyphicon-leaf"></span>
                <router-link :to="{name:'bloglist',query:{category:category.name}}" class="label label-primary" style="display:inline-block;">{{ category.name }}</router-link>
            </address>
            <address style="margin-top:-12px">
                <span class="glyphicon glyphicon-tags"></span>
                <template v-for="tag in item.tags">
                    <router-link :to="{name:'bloglist',query:{tag:tag.name}}" class="label label-primary" style="display:inline-block;">{{ tag.name }}</router-link>
                </template>
            </address>
            <address style="margin-top:-12px">
                <span class="glyphicon glyphicon-eye-open"></span>
                <span class="label label-info">{{ item.id }}</span>
            </address>
        </footer>
    </div>
</template>

<script>
 export default {
     props: ['item','author','category'],
 }
</script>
