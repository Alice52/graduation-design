<template>
  <section>
    <ul class="sidebar">
      <li class="totop"></li>
    </ul>
  </section>
</template>
<script>
export default {};
</script>
<style scoped>
  .sidebar {
    display: block;
    width: 80px;
    height: 360px;
    position: fixed;
    right: 0;
    top: 50%;
    z-index: 99;
  }
  .sidebar .totop {
    background: lightgray url(../../static/images/side4.png) no-repeat center center;
  }

  .sidebar li {
    float: left;
    width: 60px;
    height: 60px;
    border-radius: 50%;
    background: #e1e1e1;
    margin: 5px;
    cursor: pointer;
    position: relative;
  }

</style>
