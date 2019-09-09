<template>
  <div class="mask-box">
    <div :style="{width: width}" class="content-box">
      <div class="header">
        <span class="title">{{title}}</span>
        <span @click="onClose" class="icon-close"></span>
      </div>
      <div class="content">
        <slot></slot>
      </div>
      <div class="footer">
        <slot name="footer"></slot>
      </div>
    </div>
  </div>
</template>

<script>
export default {
    props: ['title', 'width'],
    methods: {
        onClose() {
            this.$emit('close');
        }
    }
};
</script>

<style lang="less">
@import "../../assets/css/common/maskBox.less";
</style>