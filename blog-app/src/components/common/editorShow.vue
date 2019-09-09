<template>
    <div class="content" v-html="content">{{content}}</div>
</template>

<script>

export default {
    props: ['content']
}
</script>

<style lang="less">
    @import "../../assets/css/markdown/dark.less";  
</style>