<template>
  <div>
    <table class="m-auto divide-x divide-y">
      <thead class="bg-gray-50">
        <tr>
          <th scope="col" v-for="item in tableHeaders" :key="item">
            {{ item }}
          </th>
        </tr>
      </thead>
      <tbody>
        <tr
          v-for="transaction in tableData"
          :key="transaction.id"
          class="divide-y divide-gray-200"
        >
          <td class="w-36">{{ transaction.date }}</td>
          <td class="w-36">{{ transaction.account }}</td>
          <td class="w-32 text-right">
            {{
              transaction.amount.toLocaleString('en-US', {
                minimumFractionDigits: 2,
              })
            }}
          </td>
          <td class="w-36">{{ transaction.category }}</td>
          <td class="w-36">{{ transaction.description }}</td>
        </tr>
      </tbody>
    </table>
  </div>
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
