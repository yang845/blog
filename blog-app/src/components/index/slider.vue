<template>
  <div class="slider-wrapper" :style="{height: height, width: width}">
    <div class="img-box"
      :style="{
                    transition: 'transform '+ transitionTime +'s ease-in-out',
                    transform: 'translateX(' + getTranslate + ')'    
                }"
      >
      <img
        v-for="(img,index) in images"
        :key="index"
        :src="img"
        :data-index="index"
        
      />
      <img
        :src="images[0]"
        :data-index="images.length"
      />
    </div>
    <span @click="prev" class="btn prev icon-back"></span>
    <span @click="next" class="btn next icon-go"></span>
    <div class="circle-box">
        <span 
            :class="{active: index == activeIndex }"
            class="circle-btn" 
            :data-index="index" 
            @click="changeImg"
            v-for="(img,index) in images"
            :key="index"
        ></span>
    </div>
    <div class="text-box">
      <slot></slot>
    </div>
  </div>
</template>
<script>
import { clearInterval } from "timers";
import { constants } from 'crypto';
export default {
  data() {
    return {
      currIndex: 0,
      transitionTime: 0.4,
      sliderTimer: null
    };
  },
  props: ["images", "height", "width"],
  computed: {
    getTranslate() {
      return "-" + 100 * this.currIndex + "%";
    },
    activeIndex() {
        return this.currIndex % this.images.length;
    }
  },
  mounted() {
    this.begin();
  },
  methods: {
    begin() {
      this.sliderTimer = setInterval(this.goRight, 2000);
    },
    stop() {
      clearTimeout(this.sliderTimer);
    },
    goRight() {
      this.currIndex++;
      if (this.currIndex > this.images.length) {
        this.transitionTime = 0;
        this.currIndex = 0;
      } else if (!this.transitionTime) {
        this.transitionTime = 0.5;
      }
    },
    goLeft() {
      this.currIndex--;
      if (this.currIndex < 0) {
        this.transitionTime = 0;
        this.currIndex = this.images.length;
      } else if (!this.transitionTime) {
        this.transitionTime = 0.5;
      }
    },
    prev() {
      this.stop();
      this.goLeft();
      this.begin();
    },
    next() {
      this.stop();
      this.goRight();
      this.begin();
    },
    changeImg(e) {
        this.stop();
        this.currIndex = e.target.dataset.index;
        this.begin();
    }
  }
};
</script>

<style lang="less">
@import "../../assets/css/index/slider.less";
</style>