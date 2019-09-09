<template>
  <table>
    <tbody>
      <tr>
        <th>名称</th>
        <th>描述</th>
      </tr>
      <tr v-for="item in friends" :key="item.id">
        <td>
          <a :href="item.website" target="_blank">{{item.username}}</a>
        </td>
        <td>{{item.description}}</td>
      </tr>
    </tbody>
  </table>
</template>

<script>
export default {
    props: ['friends']
}
</script>

<style lang="less" scoped>
@import "../../assets/css/friends/unitTable.less";
</style>