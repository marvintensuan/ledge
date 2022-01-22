export const state = () => {
  let tables = {
    'transactions': []
  }
  return tables
}

export const mutations = {
  addTransaction(state, txn) {
    state.transactions = [...state.transactions, ...txn]
  }
}