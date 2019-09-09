<template>
  <div class="unit-form">
    <form>
      <div v-if="error" class="error-box">
        <span class="error">{{error[0]}}</span>
      </div>
      <div class="input-box nick-addr">
        <div class="nickname">
          <label for="username">名称</label>
          <input
            type="text"
            @blur="checkUserName"
            id="username"
            name="username"
            placeholder="名称（必填）"
          />
        </div>
        <div class="address">
          <label for="email">邮箱</label>
          <input
            type="text"
            @blur="checkEmail"
            id="email"
            name="email"
            placeholder="邮箱（必填，方便联系，不会公开）"
          />
        </div>
      </div>
      <div class="input-box">
        <div class="website">
          <label for="website">网站</label>
          <input type="text" @blur="checkWebsite" id="website" name="website" placeholder="http://" />
        </div>
      </div>
      <textarea
        name="content"
        @blur="checkContent"
        maxlength="150"
        id="content"
        placeholder="写下你想说的话吧!"
      ></textarea>
      <div class="comment-sub">
        <input type="reset" id="reset" style="display:none" />
        <input @click.prevent="onSubmit" id="submit" type="submit" value="发布评论" />
      </div>
    </form>
  </div>
</template>

<script>
import { setTimeout } from "timers";
export default {
  data() {
    return {
      error: []
    };
  },
  methods: {
    onSubmit(e) {
      // console.log(this.error)
      if (this.error.length != 0) {
        return;
      }
      let form = {};
      form.username = e.target.form.username.value;
      form.email = e.target.form.email.value;
      form.website = e.target.form.website.value;
      form.content = e.target.form.content.value;
      if (this.checkNull(form)) {
        let str = "请填入必填项！";
        this.error.push(str);
        setTimeout(() => {
          this.removeArrayOne(this.error, str);
        }, 5000);
      } else {
        this.$emit("click", form);
        e.target.form.reset.click();
      }
    },
    checkNull(form) {
      if (form.username && form.email && form.content) {
        return false;
      } else {
        return true;
      }
    },
    getStrLen(str) {
      var len = 0;
      for (var i = 0; i < str.length; i++) {
        var c = str.charCodeAt(i);
        if ((c >= 0x0001 && c <= 0x007e) || (0xff60 <= c && c <= 0xff9f)) {
          len++;
        } else {
          len += 2;
        }
      }
      return len;
    },
    checkArrayHave(array, value) {
      let index = array.indexOf(value);
      if (index > -1) {
        return true;
      } else {
        return false;
      }
    },
    removeArrayOne(array, value) {
      let index = array.indexOf(value);
      array.splice(index, 1);
    },
    checkUserName(e) {
      let value = e.target.value;
      let str = "名称必须在12个字符以内！";
      if (!value || this.getStrLen(value) > 12) {
        this.checkArrayHave(this.error, str) ? "" : this.error.push(str);
      } else if (this.checkArrayHave(this.error, str)) {
        this.removeArrayOne(this.error, str);
      }
    },
    checkEmail(e) {
      let value = e.target.value;
      let str = "请输入正确的邮箱！";
      let mailReg = /^(\w-*\.*)+@(\w-?)+(\.\w{2,})+$/;
      if (!value || !mailReg.test(value)) {
        this.checkArrayHave(this.error, str) ? "" : this.error.push(str);
      } else if (this.checkArrayHave(this.error, str)) {
        this.removeArrayOne(this.error, str);
      }
    },
    checkWebsite(e) {
      let value = e.target.value;
      let str = "请输入正确的网址！";
      let websiteReg = /^((https|http){0,1}(:\/\/){0,1})www\.(([A-Za-z0-9-~]+)\.)+([A-Za-z0-9-~\/])+$/i;
      if (value && !websiteReg.test(value)) {
        this.checkArrayHave(this.error, str) ? "" : this.error.push(str);
      } else if (this.checkArrayHave(this.error, str)) {
        this.removeArrayOne(this.error, str);
      }
    },
    checkContent(e) {
      let value = e.target.value;
      let str = "请输入评论内容！";
      if (!value) {
        this.checkArrayHave(this.error, str) ? "" : this.error.push(str);
      } else if (this.checkArrayHave(this.error, str)) {
        this.removeArrayOne(this.error, str);
      }
    }
  }
};
</script>

<style lang="less">
@import "../../assets/css/common/unitForm.less";
</style>