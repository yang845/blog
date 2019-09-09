<template>
  <div class="hot-articles">
    <ul class="hot-box">
      <li class="hot" v-for="(item, index) in hotArticleList" :key="index">
        <div class="msg-box">
          <span class="number"
            :style="{backgroundColor: (colorsArray[index] ? colorsArray[index] : '#0bf')}"  
          >{{index}}</span>
          <span class="title">{{item.title}}</span>
        </div>
        <span class="count">{{item.search}}</span>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  data() {
    return {
      hotArticleList: [
        { title: "8岁孩独自吃火锅", search: 46731, hisSearch: 41076 },
        { title: "父亲开车撞死儿子", search: 44950, hisSearch: 47232 },
        { title: "国足战胜乌兹别克", search: 24954, hisSearch: 23492 },
        { title: "中国研发高速列车", search: 11334, hisSearch: 39224 },
        { title: "狐狸被养成怪物", search: 6134, hisSearch: 4282 },
        { title: "杨坤被骚扰发飙", search: 5207, hisSearch: 4342 },
        { title: "陈冠希怒怼女主持", search: 5204, hisSearch: 9831 },
        { title: "王俊凯室友曝光", search: 4921, hisSearch: 2832 },
        { title: "中国海军击溃海盗", search: 4351, hisSearch: 8271 },
        { title: "美团再遭举报", search: 4293, hisSearch: 9824 },
        { title: "德国现巨型炸弹", search: 2985, hisSearch: 6823 },
      ],
      colorsArray: ['#f54545', '#ff8547', '#ffac38']
    };
  }
};
</script>

<style lang="less">
@import "../../assets/css/common/hotArticles.less";
</style>