<template>
  <div class="page-about">
    <h2>{{pageAbout.title}}</h2>
    <div class="author-box">
      <img class="author-head" :src="pageAbout.author.imgUrl" alt />
      <div
        class="describe"
        v-for="(item, index) in pageAbout.author.describe"
        :key="index"
      >{{item.name}}：{{item.text}}</div>
    </div>
    <div class="text">简介：{{pageAbout.text}}</div>
  </div>
</template>

<script>
import twoCols from "../components/common/twoCols";
export default {
  data() {
    return {
      pageAbout: {
        title: "关于本站",
        author: {
          imgUrl: "images/banner1.jpg",
          describe: [
            {
              name: "邮箱",
              text: "1986436987@qq.com"
            },
            {
              name: "github",
              text: "www.baidu.com"
            }
          ]
        },
        text: "分享生活，分享知识，工作等方面，欢迎到来的朋友！"
      }
    };
  },
  components: {
    twoCols
  }
};
</script>

<style lang="less">
@import "../assets/css/about/about.less";
</style>