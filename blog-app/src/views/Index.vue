<template>
    <div class="page-index">
        <slider class="slider" :images="images" >
            <h1>离你越近的地方，路途越远；</h1>
            <h1>最简单的音调，需要最艰苦的练习。</h1>
            <a class="go-buttom" href="#article-list">
                <span class="icon-gobuttom"></span>
            </a>
        </slider>
        <article-list :articleList="articleList" id="article-list" />
        <pagination @click="getPage" :len="len" :pagination="pagination" />
    </div>
</template>

<script>
import Slider from '../components/index/slider';
import articleList from '../components/index/articleList';
import Pagination from '../components/common/pagination';
import api from '../api.js';
export default {
    data() {
        return {
            len: 7,
            pageSize: 12,
            pagination: {},
            articleList: [],
            images: ['images/banner1.jpg','images/banner2.jpg','images/banner3.jpg','images/banner4.jpg']
        }
    },
    created() {
        this.getPage(1);
    },
    components: {
        Slider,
        articleList,
        Pagination
    },
    methods: {
        getPage(page) {
            api.getArticles({
                page,
                size: this.pageSize
            }).then((res) => {
                // console.log(res)
                this.pagination = res.data;
                this.articleList = res.data.posts;
            })
        }
    }
}
</script>

<style lang="less">
@import "../assets/css/index/index.less";
</style>