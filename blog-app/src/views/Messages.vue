<template>
  <div class="page-messages">
      <h2>留言板</h2>
    <div class="message-box">
      <unit-form @click="onSubmit" />
      <comment-list :comments="comments" />
       <pagination class="pagination" @click="getPage" :len="len" :pagination="pagination" />
    </div>

    <mask-box @close="onMask" width="" title="提示" v-if="isShowMask">
      <p>留言已提交，请等待管理员审核！</p>
      <div class="mask-btn" slot="footer">
        <button @click="onMask">确定</button>
      </div>
    </mask-box>
  </div>
</template>
<script>
import unitForm from "../components/common/unitForm.vue";
import commentList from "../components/common/commentList.vue";
import Pagination from '../components/common/pagination';
import maskBox from "../components/common/maskBox.vue";
import api from '../api'
export default {
  data() {
    return {
      len: 7,
      pageSize: 12,
      pagination: {},
      comments: [],
      isShowMask: false
    };
  },
  created() {
    this.getPage(1);
  },
  components: {
    unitForm,
    commentList,
    Pagination,
    maskBox
  },
  methods: {
    getPage(page) {
      api.getMessages({
          page,
          size: this.pageSize
        })
        .then(res => {
          console.log(res.data);
          this.pagination = res.data;
          this.comments = res.data.messages;
        });
    },
    onSubmit(form) {
      // console.log(form);
      api
        .postMessage({
          ...form
        })
        .then(res => {
          // console.log(res.data);
          if (res.data.status == 1) {
            this.isShowMask = true;
          }
        });
    },
    onMask() {
      this.isShowMask = false;
    }
  }
};
</script>

<style lang="less" scoped>
  @import "../assets/css/messages/messages.less";
</style>