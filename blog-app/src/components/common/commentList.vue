<template>
    <div class="comment-list">
        <div v-for="(item, index) in comments" 
            :key="index" 
            class="comment-box">
            <div class="head">
                <a class="head-img" :href="item.website">
                    <img :src="item.head_img" alt="">
                </a>
                <div class="name-box">
                    <a class="name" :href="item.website">{{item.username}}</a>
                    <div class="time">{{item.timestamp}}</div>
                </div>
            </div>
            <div class="content">
                {{item.content}}
            </div>
        </div>
    </div>
</template>

<script>
export default {
    props: ['comments']
}
</script>

<style lang="less">
    @import "../../assets/css/article/commentList.less"; 
</style>