<script>
export default {
  computed: {
    transactions() { return this.$store.state.tables.tables.transactions}
  }
}
</script>

<template>
  <main>
    <h1>Transactions</h1>
    <table>
      <thead>{{ transactions.Head }}</thead>
      <tbody>
        <tr>
          <td>{{ transactions.Body }}</td>
        </tr>
      </tbody>
    </table>
  </main>
</template>