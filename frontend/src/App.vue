<template>
  <div id="app">
    <el-menu :default-active="actibeIndex" mode="horizontal" router>
      <el-menu-item index="home" :route="{ name:'home' }">Home</el-menu-item>
      <el-menu-item index="about" :route="{ name:'about'}">About</el-menu-item>
      <el-menu-item>
        <a href="https://element.eleme.io" target="_blank">Link</a>
      </el-menu-item>
    </el-menu>
    <router-view />
<!-- VueCliのデフォルト処理
    <img src="./assets/logo.png">
    <div>
      <p>
        If Element is successfully added to this project, you'll see an
        <code v-text="'<el-button>'"></code>
        below
      </p>
      <el-button>el-button</el-button>
    </div>
    <HelloWorld msg="Welcome to Your Vue.js App"/> -->

  </div>
</template>

<script>
export default {
  name: 'app',
  data(){
    return {
      activeIndex: this.$route.name
    }
  }
}
// VueCliのデフォルト処理
// import HelloWorld from './components/HelloWorld.vue'

// export default {
//   name: 'app',
//   components: {
//     HelloWorld
//   }
// }
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, Helvetica, sans-serif;
  text-align: center;
  color: #2c3e50;
}
a {
  text-decoration: none;
}
/* VueCliのデフォルト処理
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
} */
</style>
