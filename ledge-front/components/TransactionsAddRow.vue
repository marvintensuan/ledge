<template>
  <tr class="bg-gray-300">
    <td><input type="date" form="newEntry" /></td>
    <td>
      <select form="newEntry" class="w-36">
        <option v-for="account in bankAccounts">{{ account }}</option>
      </select>
    </td>
    <td>
      <input type="number" form="newEntry" value="0.00" class="text-right" />
    </td>
    <td><input type="text" form="newEntry" value="..." /></td>
    <td><input type="text" form="newEntry" value="..." /></td>
  </tr>
</template>

<script>
export default {
  computed: {
    bankAccounts() {
      let accounts = this.$store.state.tables.transactions.map((bank) => bank.account)
      return [...new Set(accounts)]
    },
  },
}
</script>
