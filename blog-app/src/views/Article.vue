<template>
  <div class="page-article">
    <!-- <mavon-editor 
            ref="md" 
            @change="change" 
            v-model="value"
    />-->
    <article-detial @submit="onSubmit" @like="onLike" :comments="comments" :article="article" />

    <div class="comment-box">
      <h3>发布评论</h3>
      <unit-form @click="onSubmit" />
      <comment-list :comments="comments" />
      <pagination class="pagination" @click="getPage" :len="len" :pagination="pagination" />
    </div>

    <mask-box @close="onMask" width title="提示" v-if="isShowMask">
      <p>评论已提交，请等待管理员审核！</p>
      <div class="mask-btn" slot="footer">
        <button @click="onMask">确定</button>
      </div>
    </mask-box>
  </div>
</template>

<script>
import articleDetial from "../components/article/articleDetial.vue";
import commentList from "../components/common/commentList.vue";
import unitForm from "../components/common/unitForm.vue";
import Pagination from '../components/common/pagination';
import maskBox from "../components/common/maskBox.vue";
import api from "../api.js";
export default {
  data() {
    return {
      len: 7,
      pageSize: 12,
      pagination: {},
      article: {},
      comments: [],
      isShowMask: false
    };
  },
  created() {
    const id = this.$route.params.id;
    api.getArticle(id).then(res => {
      // console.log(res.data)
      this.article = res.data;
    });
    this.getPage(1);
  },
  components: {
    articleDetial,
    maskBox,
    commentList,
    unitForm,
    Pagination
  },
  methods: {
    // change(value, render) {
    //   this.html = render;
    // }
    onLike() {
      api
        .likeArticle({
          id: this.article.id
        })
        .then(res => {
          // console.log(res.data);
          if (res.data.status == 1) {
            this.article.likes++;
          }
        });
    },
    getPage(page) {
      api
        .getComments(this.$route.params.id, {
          page,
          size: this.pageSize
        })
        .then(res => {
          // console.log(res.data);
          this.pagination = res.data;
          this.comments = res.data.comments;
        });
    },
    onSubmit(form) {
      // console.log(form);
      api
        .postComment(this.article.id, {
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
@import "../assets/css/article/article.less";
</style>