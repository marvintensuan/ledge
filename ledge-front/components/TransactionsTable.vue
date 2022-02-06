<template>
  <table>
    <thead>
      <tr>
        <th v-for="item in tableHeaders" :key="item" class="capitalize">
          {{ item }}
        </th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="transaction in tableData" :key="transaction.id">
        <td>{{ transaction.date }}</td>
        <td>{{ transaction.account }}</td>
        <td>
          {{
            transaction.amount.toLocaleString('en-US', {
              minimumFractionDigits: 2,
            })
          }}
        </td>
        <td>{{ transaction.category }}</td>
        <td>{{ transaction.description }}</td>
      </tr>
    </tbody>
  </table>
</template>

<script>
export default {
  props: {
    tableData: Array,
  },
  data() {
    return {
      tableHeaders: [
        'Date',
        'Account',
        'Amount (PHP)',
        'Category',
        'Description',
      ],
    }
  },
}
</script>
