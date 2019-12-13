<template>
  <div class="game">
    <h4 class="text-center"><b> Game Statistics </b></h4>
    <b-row align-h="center">
      <b-list-group horizontal="md">
        <b-list-group-item>Number of moves made: {{statistics.numTurns}}</b-list-group-item>
        <b-list-group-item>Number of black pieces: {{statistics.numBlack}}</b-list-group-item>
        <b-list-group-item>Number of white pieces: {{statistics.numWhite}}</b-list-group-item>
        <b-list-group-item v-if="winner === 'B'">Winner: Black</b-list-group-item>
        <b-list-group-item v-else-if="winner === 'W'">Winner: White</b-list-group-item>
        <b-list-group-item v-else>Tie game!</b-list-group-item>
      </b-list-group>
    </b-row>
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
        statistics: json.statistics,
        winner: json.winner
      }
    },
    methods: {
    }
  }
</script>

<style>

</style>
