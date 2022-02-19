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
        <tr class="bg-gray-300">
          <td><input type="date" form="newEntry" /></td>
          <td>
            <select form="newEntry" class="w-36">
              <option>FOO</option>
              <option>Bar</option>
              <option>bAz</option>
            </select>
          </td>
          <td>
            <input type="number" form="newEntry" value="0.00" class="text-right" />
          </td>
          <td><input type="text" form="newEntry" value="..." /></td>
          <td><input type="text" form="newEntry" value="..." /></td>
        </tr>
      </tbody>
    </table>
    <form id="newEntry" class="m-auto mt-5">
      <button type="button" onclick="javascript:console.log(document.getElementById('newEntry').data)">Submit</button>
    </form>
  </div>
</template>

<script>
export default {
  props: {
    tableData: Array,
  },
  data() {
    return {
      tableHeaders: ['Date', 'Account', 'Amount (PHP)', 'Category', 'Description'],
    }
  },
}
</script>
