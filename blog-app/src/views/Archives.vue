<template>
  <div class="page-archives">
    <h2>文章归档</h2>
    <timeline class="timeline-box" :total="total" />
  </div>
</template>

<script>
import Timeline from '../components/archives/timeline';
import api from '../api'
export default {
  data() {
    return {
      articles: [
        // {
        //   id: 1,
        //   timestamp: "Sun, 25 Aug 2019 07:16:59 GMT",
        //   name: "你哦四川麻将哦第四"
        // },
        // {
        //   id: 2,
        //   timestamp: "Sun, 26 Aug 2019 07:16:59 GMT",
        //   name: "面对市场的"
        // },
        // {
        //   id: 3,
        //   timestamp: "Sun, 27 Aug 2019 07:16:59 GMT",
        //   name: "的时刻里面的"
        // },
        // {
        //   id: 4,
        //   timestamp: "Sun, 28 Oct 2019 07:16:59 GMT",
        //   name: "的看了上面的"
        // }
      ],
      total: {}
    };
  },
  created() {
      api.getArchives().then((res) => {
        // console.log(res.data.posts)
        this.articles = res.data.posts;
        this.getTotal();
      })
  },
  components: {
      Timeline
  },
  methods: {
      getTotal() {
          let total = {};
          this.articles.forEach((item) => {
              let date = new Date(item.timestamp);
              let mouth = date.getFullYear() + '年' + (date.getMonth() + 1) + '月';
              let day = mouth + date.getDate() + '日';
              item.day = day;
              if (!total[mouth]) {
                  total[mouth] = {
                      articles: [item]
                    };
              }else {
                  total[mouth].articles.push(item);
              }
          })
          this.total = total;
          // console.log(this.total)
      },

  }
};
</script>

<style lang="less">
@import "../assets/css/archives/archives.less";
</style>