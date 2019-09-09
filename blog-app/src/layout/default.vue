<template>
  <div class="default-page">
    <div class="nav-wrapper">
      <div class="container">
        <router-link class="logo" :to="{name: 'index'}">XXX的个人博客</router-link>
        <div @click="onClick" :class="isShow ? 'show' : ''" class="nav-menu">
          <router-link :to="{name: 'index'}" class="link index">
            <span class="icon-home">首页</span>
          </router-link>
          <router-link :to="{name: 'archives'}" class="link">
            <span class="icon-single">文章归档</span>
          </router-link>
          <router-link :to="{name: 'friends'}" class="link">
            <span class="icon-link">友情链接</span>
          </router-link>
          <router-link :to="{name: 'about'}" class="link">
            <span class="icon-user">关于本站</span>
          </router-link>
          <router-link :to="{name: 'messages'}" class="link">
            <span class="icon-comment">留言板</span>
          </router-link>
        </div>
        <div class="btn" @click="showMenu">
          <span :class="isShow ? 'icon-close' : 'icon-category'"></span>
        </div>
      </div>
    </div>


      <router-view />


    <div class="footer-wrapper">
      <div class="container">
        <div class="foot-t">
          <router-link class="foot-icon" :to="{name: 'index'}">
            <span class="icon-user1"></span>
          </router-link>
          <a class="foot-icon icon-mail" href="mailto:1986436987@qq.com"></a>
          <a class="foot-icon icon-weixin" @click="onShow"></a>
          <a class="foot-icon icon-github" href="https://github.com/LGlory" target="_blank"></a>
        </div>
        <div class="foot-b">
          <span>Copyright©2019</span>
          <router-link class="name" :to="{name: 'index'}">XXX的个人博客</router-link>
        </div>
      </div>
    </div>

    <mask-box @close="onMask" width="" title="微信扫一扫" v-if="isShowMask">
      <img class="wechat-img" src="/images/weixin.png" alt="">
    </mask-box>
  </div>
</template>

<script>
import maskBox from '../components/common/maskBox.vue'
export default {
  data() {
    return {
      isShow: false,
      isShowMask: false
    };
  },
  components: {
    maskBox
  },
  methods: {
    showMenu() {
      this.isShow = !this.isShow;
    },
    onClick() {
      this.isShow = !this.isShow;
    },
    onMask() {
      this.isShowMask = false;
    },
    onShow() {
      this.isShowMask = true;
    }
  }
};
</script>

<style lang="less">
@import "../assets/css/default.less";
</style>