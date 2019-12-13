<template>
  <b-container class="board">
    <b-table striped hover :items="items"></b-table>
  </b-container>
</template>

<script>
  import json from "../../../../output.json"

  export default {
    name : 'Board',
    data() {
      return {
        items: json.turns
      }
    }
  }
</script>

<style>
</style>
