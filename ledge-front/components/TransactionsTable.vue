<template>
  <div class="flex flex-col m-auto">
    <table class="divide-x divide-y">
      <thead class="bg-gray-50">
        <tr>
          <th scope="col" v-for="item in tableHeaders" :key="item">
            {{ item }}
          </th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="transaction in tableData" :key="transaction.id" class="divide-y divide-gray-200">
          <td>{{ transaction.date }}</td>
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
        <TransactionsAddRow />
      </tbody>
    </table>
    <form id="newEntry" class="m-auto mt-5">
      <button type="button" @click="submitTable">Submit</button>
    </form>
  </div>
</template>

<script>
import TransactionsAddRow from './TransactionsAddRow.vue'
export default {
  props: {
    tableData: Array,
  },
  data() {
    return {
      tableHeaders: ['Date', 'Account', 'Amount (PHP)', 'Category', 'Description'],
    }
  },
  components: { TransactionsAddRow },
  methods: {
    submitTable() {
      let f = document.querySelector('form')
      console.log(f)
    },
  },
}
</script>
