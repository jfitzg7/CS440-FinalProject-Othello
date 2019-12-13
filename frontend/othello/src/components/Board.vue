<template>
  <b-container>
    <h4 class="text-center"><b>Game Board</b></h4>
    <p class="text-center">Current move: {{stateCount + 1}}</p>
    <br/>
    <b-table :items="gameStates[stateCount]"></b-table>
    <b-row align-h="center">
      <button v-if="stateCount < totalMoves-1" v-on:click="stateCount++">Next move</button>
      <button v-if="stateCount > 0" v-on:click="stateCount--">Previous move</button>
    </b-row>
  </b-container>
</template>

<script>
  import json from "../../../../output.json"

  export default {
    name : 'Board',
    data() {
      return {
        gameStates: json.gameStates,
        stateCount: 0,
        totalMoves: json.statistics.numTurns
      }
    }
  }
</script>

<style>
</style>
