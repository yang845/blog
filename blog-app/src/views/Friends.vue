<template>
  <div class="page-friends">
    <h2>友情链接</h2>
    <unit-table :friends="friends" />
    <div class="friend-btn">
      <button @click="showForm" class="apply-btn">申请成为我的朋友</button>
    </div>
    <unit-form v-if="isShowForm" @click="onSubmit" />

    <mask-box @close="onMask" width="" title="提示" v-if="isShowMask">
      <p>友链申请已提交，请等待管理员审核！</p>
      <div class="mask-btn" slot="footer">
        <button @click="onMask">确定</button>
      </div>
    </mask-box>
  </div>
</template>

<script>
import unitTable from "../components/friends/unitTable";
import unitForm from "../components/common/unitForm";
import maskBox from "../components/common/maskBox"
import api from "../api";
export default {
  data() {
    return {
      isShowForm: false,
      isShowMask: false,
      friends: []
    };
  },
  components: {
    unitTable,
    unitForm,
    maskBox
  },
  created() {
    api.getFriends().then(res => {

      this.friends = res.data.friends;
    });
  },
  methods: {
    onSubmit(form) {
      api
        .postFriend({
          ...form
        })
        .then(res => {
          if (res.data.status == 1) {
            this.isShowMask = true;
          }
        });
    },
    showForm() {
      this.isShowForm = !this.isShowForm;
    },
    onMask() {
      this.isShowMask = false;
    }
  }
};
</script>

<style lang="less">
@import "../assets/css/friends/friends.less";
</style>
