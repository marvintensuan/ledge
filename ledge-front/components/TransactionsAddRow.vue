<template>
  <tr class="bg-gray-300">
    <td><input type="date" form="newEntry" v-model="dateToday" /></td>
    <td>
      <select form="newEntry" class="w-36" v-model="selectedAccount">
        <option v-for="account in bankAccounts">{{ account }}</option>
      </select>
    </td>
    <td>
      <input type="number" form="newEntry" v-model.number="amt" class="text-right" />
    </td>
    <td><input type="text" form="newEntry" v-model="category" /></td>
    <td><input type="text" form="newEntry" v-model="desc" /></td>
  </tr>
</template>

<script>
export default {
  data: function () {
    return {
      dateToday: new Date().toISOString().split('T')[0],
      selectedAccount: '',
      amt: 0,
      category: 'Personal Exponses',
      desc: 'Please provide a description.',
    }
  },
  computed: {
    bankAccounts() {
      let accounts = this.$store.state.tables.transactions.map((bank) => bank.account)
      return [...new Set(accounts)]
    },
  },
}
</script>
