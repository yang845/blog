<template>
    <div class="body-wrapper">
        <div class="container">
            <two-cols>
                <router-view />
            </two-cols>
        </div>
    </div>
</template>

<script>
import twoCols from "../components/common/twoCols";
export default {
    components: {
        twoCols
    }
}
</script>

<style lang="less">
    @import "../assets/css/defaultBody.less";
</style>