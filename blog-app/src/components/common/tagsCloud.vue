<template>
  <div class="tags-wrapper">
    <div ref="tagBox" class="tags-box">
      <a
        class="tag"
        ref="tag"
        @mousemove="mouseMove"
        v-for="(item, index) in tagList"
        :key="index"
        :style="{
                  fontSize: size[index] + 'px',
                  opacity: opacitys[index],
                  color: colors[index],
                  zIndex: zIndexs[index],
                  left: (posList[index] ? posList[index][0] : '0') + 'px',
                  top: (posList[index] ? posList[index][1] : '0') + 'px'
                }"
      >{{item.name}}({{item.count}})</a>
      
    </div>
  </div>
</template>

<script>
import { setInterval, setTimeout } from "timers";
import { constants } from "crypto";
export default {
  data() {
    return {
      tagList: [
        {
          name: "那些看戏",
          count: 5
        },
        {
          name: "没下实现",
          count: 2
        },
        {
          name: "明星爱丽丝",
          count: 4
        },
        {
          name: "麦克拉",
          count: 3
        },
        {
          name: "没你看下啦",
          count: 5
        },
        {
          name: "没打算",
          count: 5
        },
        {
          name: "栏目开播",
          count: 2
        },
        {
          name: "对联储",
          count: 4
        },
        {
          name: "吧发v",
          count: 3
        },
        {
          name: "科伦坡",
          count: 5
        }
      ],
      size: [],
      opacitys: [],
      colors: [],
      zIndexs: [],
      pos: [],
      posList: [],
      angleX: 0,
      angleY: 0,
      r: 0,
      tags: [],
      tagBox: "",
      width: 0,
      height: 0,
      animationTime: 5
    };
  },
  created() {
    this.init();
  },
  methods: {
    init() {
      this.tags = this.$refs.tag;
      this.tagBox = this.$refs.tagBox;
      if (this.tags && this.tagBox) {
        let tagLen = this.tags.length;
        this.width = this.tagBox.offsetWidth;
        this.height = this.tagBox.offsetHeight;
        this.r = this.width / 3;
        this.angleY = Math.PI / this.width;
        this.angleX = Math.PI / this.width
        for (let i = 0; i < tagLen; i++) {
          let theta = Math.acos(-1 + (2 * (i + 1) - 1) / tagLen), 
            phi = theta * Math.sqrt(tagLen * Math.PI), // Φ = θ*sqrt(all * π)
            x = this.r * Math.sin(theta) * Math.cos(phi), // x轴坐标: x=r*sinθ*cosΦ
            y = this.r * Math.sin(theta) * Math.sin(phi), // y轴坐标: x=r*sinθ*cosΦ
            z = this.r * Math.cos(theta); // z轴坐标: z=r*cosθ
          this.colors.splice(i, 1, "rgb(" + parseInt(Math.random() * 255) + "," + parseInt(Math.random() * 255) + "," + parseInt(Math.random() * 255) + ")");
          this.pos.splice(i, 1, [x, y, z]);
        }
        this.move();
        this.animate();
      } else {
        setTimeout(this.init, 20);
      }
    },
    animate() {
      this.rotateX();
      this.rotateY();
      this.move();
      requestAnimationFrame(this.animate);
    },
    rotateX() {
      let cos = Math.cos(this.angleX);
      let sin = Math.sin(this.angleX);
      this.pos.forEach((p, i) => {
        let y = p[1] * cos - p[2] * sin;
        let z = p[2] * cos + p[1] * sin;
        this.pos.splice(i, 1, [p[0], y, z]);
      });
    },
    rotateY() {
      let cos = Math.cos(this.angleY);
      let sin = Math.sin(this.angleY);
      this.pos.forEach((p, i) => {
        let x = p[0] * cos - p[2] * sin;
        let z = p[2] * cos + p[0] * sin;
        this.pos.splice(i, 1, [x, p[1], z]);
      });
    },
    move() {
      this.pos.forEach((p, i) => {
        let scale = this.width / (this.width - p[2]);
        let alpha = (p[2] + this.r) / (2 * this.r);

        let left = p[0] + this.width / 2 - this.tags[i].offsetWidth / 2;
        let top = p[1] + this.height / 2 - this.tags[i].offsetHeight / 2;
        
        this.size.splice(i, 1, 12 * scale)
        this.opacitys.splice(i, 1, alpha + 0.5);
        this.zIndexs.splice(i, 1, parseInt(scale * 100));
        this.posList.splice(i, 1, [left, top, p[2]]);
      });
    },
    mouseMove(e) {
      let x = e.clientX - this.tagBox.offsetLeft - this.width;
      let y = e.clientY - this.tagBox.offsetTop - this.height;
      this.angleY = x * 0.00005;
      this.angleX = y * 0.00005;
    }
  }
};
</script>

<style lang="less">
@import "../../assets/css/common/tagsCloud.less";
</style>