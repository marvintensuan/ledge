<script>
import Table from '~/components/TransactionsTable.vue'
export default {
  async fetch() {
    let isEmpty = this.$store.state.tables.transactions
    if (!isEmpty.length) {
      let results = await this.$axios.get(
        'http://127.0.0.1:8000/tables/transactions'
      )
      this.$store.commit('tables/addTransaction', results.data)
    }
  },
  computed: {
    transactions() {
      return this.$store.state.tables.transactions
    },
  },
  components: { Table },
}
</script>

<template>
  <main>
    <TransactionsTable :tableData="transactions" />
  </main>
</template>
