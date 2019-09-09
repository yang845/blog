<template>
    <div class="cols-wrapper">
        <div class="left-col">
            <slot></slot>
        </div>
        <div class="right-col">
            <h3>全部标签</h3>
            <tags-cloud class="tags-cloud" />
            <h3>热门文章</h3>
            <hot-articles />
        </div>
    </div>
</template>

<script>
import tagsCloud from './tagsCloud';
import hotArticles from './hotArticles';
export default {
    components: {
        tagsCloud,
        hotArticles
    }
}
</script>

<style lang="less">
    @import "../../assets/css/common/twoCols.less";
</style>