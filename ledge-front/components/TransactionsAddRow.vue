<template>
  <tr class="bg-gray-300">
    <td><input type="date" v-model="formData.dateToday" /></td>
    <td>
      <select class="w-36" v-model="formData.selectedAccount">
        <option v-for="account in bankAccounts">{{ account }}</option>
      </select>
    </td>
    <td>
      <input type="number" v-model.number="formData.amt" class="text-right" />
    </td>
    <td><input type="text" v-model="formData.category" /></td>
    <td><input type="text" v-model="formData.desc" /></td>
  </tr>
</template>

<script>
export default {
  data: function () {
    return {
      formData: {
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
    this.$emit('formData', this.formData)
  },
}
</script>
