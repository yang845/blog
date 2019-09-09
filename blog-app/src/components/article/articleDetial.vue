<template>
  <div class="article-box">
    <div class="title">{{article.name}}</div>
    <div class="author-box">
      <span class="author">作者: {{article.author ? article.author : '佚名'}}</span>
      <span class="date">{{article.timestamp}}</span>
      <div class="tags">
        <span v-for="(item, index) in article.tags" :key="index" class="tag">{{item}}</span>
      </div>
    </div>
    <editor-show :content="article.body" />
    <div class="bottom-btn">
      <span class="icon-icon-dollar">&nbsp;打赏</span>
      <span @click="onLike" class="like icon-heart">&nbsp;喜欢&nbsp;|&nbsp;{{article.likes}}</span>
    </div>
    <!-- <div class="pages">
      <router-link :to="{name: 'article', params: {id: 2}}">
        <span class="prev">上一页：ksadmsadscds</span>
      </router-link>
      <router-link :to="{name: 'article', params: {id: 2}}">
        <span class="next">下一页：ksadmsadscds</span>
      </router-link>
    </div> -->

    
  </div>
</template>

<script>
import editorShow from "../common/editorShow.vue";

export default {
  data() {
    return {
      // comments: [
      //     {
      //       content:
      //         "\u6027\u80fd\u8003\u8bd5\u7684\u6ca1\u8010\u5fc3\u770b\u5565\u5b50\u8f9b\u82e6\u6d12\u4e0b\u63a5\u9001\u718a\u732b\u7ec6\u8282\u4e0a\u62c9\u5f00\u5e8f\u5e55\u770b\u6765\u6d12\u4e0b",
      //       email: "1986437987@qq.com",
      //       head_img: "/static/gravatar/img6.jpg",
      //       timestamp: "Sun, 25 Aug 2019 07:08:52 GMT",
      //       username: "\u6211\uff0c\u7684\u7f57\u9a6c\u4e3a",
      //       website: "www.baidu.com"
      //     },
      //     {
      //       content:
      //         "\u6027\u80fd\u8003\u8bd5\u7684\u6ca1\u8010\u5fc3\u770b\u5565\u5b50\u8f9b\u82e6\u6d12\u4e0b\u63a5\u9001\u718a\u732b\u7ec6\u8282\u4e0a\u62c9\u5f00\u5e8f\u5e55\u770b\u6765\u6d12\u4e0b",
      //       email: "1986437987@qq.com",
      //       head_img: "/static/gravatar/img6.jpg",
      //       timestamp: "Sun, 25 Aug 2019 07:08:52 GMT",
      //       username: "\u6211\uff0c\u7684\u7f57",
      //       website: "www.baidu.com"
      //     }
      // ]
    };
  },
  components: {
    editorShow,
  },
  props: ["article", "comments"],
  methods: {
    onLike() {
      this.$emit('like');
    },
  }
};
</script>

<style lang="less" scoped>
@import "../../assets/css/article/articleDetial.less";
</style>