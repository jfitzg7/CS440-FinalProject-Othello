<template>
  <div class="game">
    <h4 class="text-center"><b> Game Statistics </b></h4>
    <b-container>
      <b-list-group>
        <b-list-group-item>Number of moves made: {{statistics.numTurns}}</b-list-group-item>
        <b-list-group-item>Number of black pieces: {{statistics.numBlack}}</b-list-group-item>
        <b-list-group-item>Number of white pieces: {{statistics.numWhite}}</b-list-group-item>
      </b-list-group>
    </b-container>
    <Board></Board>
  </div>
</template>

<script>
  import json from '../../../../output.json'
  import Board from './Board.vue'

  export default {
    name: 'Game',
    components : {
      Board
    },
    data() {
      return {
        statistics: json.statistics
      }
    },
    methods: {
    }
  }
</script>

<style>

</style>
