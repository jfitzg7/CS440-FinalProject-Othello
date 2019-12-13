<template>
  <b-container>
    <h4 class="text-center"><b>Game Board</b></h4>
    <b-row align-h="center">
      <b-list-group horizontal="md">
        <b-list-group-item cols="2">Current move: {{stateCount + 1}}</b-list-group-item>
        <b-list-group-item cols="2">Black pieces: {{countBlackPieces()}}</b-list-group-item>
        <b-list-group-item cols="2">White pieces: {{countWhitePieces()}}</b-list-group-item>
      </b-list-group>
    </b-row>
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
    },
    methods: {
      countWhitePieces() {
        var count = 0
        var game_state = this.gameStates[this.stateCount]
        for (let i = 0;i < 8;i++) {
          for(let j = 0;j < 8;j++) {
            if (game_state[i][j] == 'W') {
              count = count + 1
            }
          }
        }
        return count
      },
      countBlackPieces() {
        var count = 0
        var game_state = this.gameStates[this.stateCount]
        for (let i = 0;i < 8;i++) {
          for(let j = 0;j < 8;j++) {
            if (game_state[i][j] == 'B') {
              count = count + 1
            }
          }
        }
        return count
      }
    }
  }
</script>

<style>

</style>
