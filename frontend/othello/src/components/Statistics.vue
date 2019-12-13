<template>
  <div class="statistics">
    <h4 class="text-center"><b> Game Statistics </b></h4>
    <b-row align-h="center">
      <b-list-group horizontal="md">
        <b-list-group-item>Total moves made: {{statistics.numTurns}}</b-list-group-item>
        <b-list-group-item>Black pieces: {{statistics.numBlack}}</b-list-group-item>
        <b-list-group-item>White pieces: {{statistics.numWhite}}</b-list-group-item>
        <b-list-group-item v-if="winner === 'B'">Winner: Black</b-list-group-item>
        <b-list-group-item v-else-if="winner === 'W'">Winner: White</b-list-group-item>
        <b-list-group-item v-else>Tie game!</b-list-group-item>
      </b-list-group>
    </b-row>
    <b-container>
      <b-table striped hover :items="turns"></b-table>
    </b-container>
  </div>
</template>

<script>
  import json from '../../../../output.json'

  export default {
    name: 'Statistics',
    data() {
      return {
        statistics: json.statistics,
        turns: json.turns,
        winner: json.winner
      }
    }
  }
</script>

<style>

</style>
