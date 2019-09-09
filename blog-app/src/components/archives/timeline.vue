<template>
  <div class="timeline"> 
    <div v-for="(item, mouth) in total" :key="mouth" class="archives">
      <div class="circle-box">
        <div :data-mouth="mouth" @click="show" class="circle">{{isShowList[mouth] ? '-': '+'}}</div>
        <div class="line"></div>
      </div>
      <div class="message-box">
        <div class="time-box">
          <span :data-mouth="mouth" @click="show" class="time">{{mouth}}({{item.articles.length}}篇)</span>
        </div>
        <!-- <img src="images/banner2.jpg" alt /> -->
        <template v-if="isShowList[mouth]">
          <router-link
            v-for="article in item.articles"
            :key="article.id"
            :to="{name: 'article', params: {id: article.id}}"
          >{{article.day}}：{{article.name}}</router-link>
        </template>
      </div>
    </div>
  </div>
</template>

<script>
import { setTimeout } from 'timers';
export default {
  data() {
    return {
      isShowList: {}
    };
  },
  props: ["total"],
  methods: {
    show(e) {
      let mouth = e.target.dataset.mouth;
      this.isShowList[mouth] = this.$set(this.isShowList, mouth, !this.isShowList[mouth]);;
    }
  }
};
</script>

<style lang="less">
    @import "../../assets/css/archives/timeline.less";
</style>