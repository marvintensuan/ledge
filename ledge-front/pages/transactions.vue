<script>
export default {
  data(){ return{ transactions: [] } },
  async fetch(){
      this.transactions = await fetch("http://127.0.0.1:8000/tables/transactions")
        .then(response => response.json())
  },
  computed: {
    transactions() { return this.$store.state.tables.transactions} 
  }
}
</script>

<template>
  <main>
    <h1>Transactions</h1>
    <table>
      <thead>
        <tr>
          <th>Date</th>
          <th>Account</th>
          <th>Amount (PHP)</th>
          <th>Category</th>
          <th>Description</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="transaction in transactions" :key="transaction.id">
          <td>{{ transaction.date }}</td>
          <td>{{ transaction.account }}</td>
          <td>{{ transaction.amount }}</td>
          <td>{{ transaction.category }}</td>
          <td>{{ transaction.description }}</td>
        </tr>
      </tbody>
    </table>
  </main>
</template>