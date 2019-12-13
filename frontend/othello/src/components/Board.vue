<template>
  <b-container>
    <h4 class="text-center"><b>Game Board</b></h4>
    <p class="text-center">Current move: {{stateCount + 1}}</p>
    <br/>
    <b-table thead-class="d-none" tbody-class="text-center" bordered :items="gameStates[stateCount]"></b-table>
    <b-row>
      <b-col offset="2">
        <button v-if="stateCount < totalMoves-1" v-on:click="stateCount++">Next move</button>
      </b-col>
      <b-col offset="4">
        <button v-if="stateCount > 0" v-on:click="stateCount--">Previous move</button>
      </b-col>
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
