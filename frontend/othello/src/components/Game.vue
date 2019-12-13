<template>
  <div class="game">
    <Board></Board>
    <br/>
    <Statistics></Statistics>
  </div>
</template>

<script>
  import Statistics from './Statistics.vue'
  import Board from './Board.vue'

  export default {
    name: 'Game',
    components : {
      Board,
      Statistics
    }
  }
</script>

<style>

</style>
