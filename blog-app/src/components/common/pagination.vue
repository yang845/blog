<template>
  <ul class="page-box">
    <template v-if="pagination.prev_url">
      <li class="page-count">
        <span @click="getPage(pagination.curr_page - 1)" class="icon-back"></span>
      </li>
    </template>

    <template v-for="(item,index) in pages">
      <li class="page-curr" v-if="item == pagination.curr_page" :key="index">
        <span @click="getPage(item)">{{ item }}</span>
      </li>
      <li class="page-count" v-else-if="item != '...'" @click="getPage(item)" :key="index">
        <span>{{ item }}</span>
      </li>
      <li class="page-count" v-else :key="index">
        <span>{{ item }}</span>
      </li>
    </template>

    <template v-if="pagination.next_url">
      <li class="page-count">
        <span @click="getPage(pagination.curr_page + 1)" class="page-count icon-go"></span>
      </li>
    </template>
  </ul>
</template>

<script>
export default {
  props: ["pagination", "len"],
  computed: {
    pages() {
      const curr = this.pagination.curr_page;
      const count = this.pagination.page_count;
      let pageList = this.pagination.page_list;
      let pages = [];
      if (count <= this.len) {
        return pageList;
      } else if (curr <= Math.ceil(this.len / 2)) {
        return [1, 2, 3, 4, 5, 6, 7];
      } else if (curr + 3 <= count) {
        let pages = [];
        for (let i = curr - 3; i <= count; i++) {
          pages.push(i);
        }
        return pages;
      } else {
        let pages = [];
        for (let i = curr; i <= count; i++) {
          pages.push(i);
        }
        let last = this.len - pages.length;
        for (let i = 1; i <= last; i++) {
          pages.unshift(curr - i);
        }
        return pages;
      }
    }
  },
  methods: {
    getPage(page) {
      this.$emit("click", page);
    }
  }
};
</script>

<style lang="less">
@import "../../assets/css/common/pagination.less";
</style>