<script>

let formatter = new Intl.NumberFormat('en-US')

export default {
  async fetch(){
    let isEmpty = this.$store.state.tables.transactions
    if (!isEmpty.length) {
      let results = await this.$axios.get("http://127.0.0.1:8000/tables/transactions")
      this.$store.commit('tables/addTransaction', results.data)
    }
  },
  computed: {
    transactions() { return this.$store.state.tables.transactions } 
  },
  filters: {
    accounting(n) {
      return formatter.format(n)
    }
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
          <td >{{ transaction.amount | accounting }}</td>
          <td>{{ transaction.category }}</td>
          <td>{{ transaction.description }}</td>
        </tr>
      </tbody>
    </table>
  </main>
</template>