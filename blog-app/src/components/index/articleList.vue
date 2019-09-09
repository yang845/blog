<template>
  <div class="article-list">
    <div class="container">
      <router-link :to="{name: 'article', params: {id: item.id}}" v-for="item in articleList" :key="item.id">
        <div class="article">
          <div class="img" :style="{backgroundImage:'url('+ item.img_url +')'}"></div>
          <h4>{{item.name}}</h4>
          <p class="content">{{item.description}}...</p>
          <div class="bottom">
            <span class="author">{{item.author ? item.author : '佚名'}}</span>
            <div class="article-icon">
              <span class="icon-view">{{item.watched}}</span>
              <span class="icon-comment">{{item.comment_count}}</span>
              <span class="icon-heart">{{item.likes}}</span>
            </div>
          </div>
        </div>
      </router-link>

      <div v-for="item in 4" :key="'empty_' + item" class="article-empty"></div>
    </div>
  </div>
</template>
<script>
export default {
  data() {
    return {
    };
  },
  props: ['articleList']
};
</script>

<style lang="less">
@import "../../assets/css/index/articleList.less";
</style>