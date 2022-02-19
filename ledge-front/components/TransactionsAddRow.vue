<template>
  <tr class="bg-gray-300">
    <td><input type="date" form="newEntry" v-model="addRow.dateToday" /></td>
    <td>
      <select form="newEntry" class="w-36" v-model="addRow.selectedAccount">
        <option v-for="account in bankAccounts">{{ account }}</option>
      </select>
    </td>
    <td>
      <input type="number" form="newEntry" v-model.number="addRow.amt" class="text-right" />
    </td>
    <td><input type="text" form="newEntry" v-model="addRow.category" /></td>
    <td><input type="text" form="newEntry" v-model="addRow.desc" /></td>
  </tr>
</template>

<script>
export default {
  data: function () {
    return {
      addRow: {
        dateToday: new Date().toISOString().split('T')[0],
        selectedAccount: '',
        amt: 0,
        category: 'Personal Expenses',
        desc: 'Please provide a description.',
      },
    }
  },
  computed: {
    bankAccounts() {
      let accounts = this.$store.state.tables.transactions.map((bank) => bank.account)
      return [...new Set(accounts)]
    },
  },
  mounted() {
    console.log('Emitting...')
    console.log(this.addRow)
    this.$emit('formData', this.addRow)
  },
}
</script>
