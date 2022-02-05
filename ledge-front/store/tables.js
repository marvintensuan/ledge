export const state = () => ({ transactions: [] })

export const mutations = {
  addTransaction(state, txn) {
    state.transactions = [...state.transactions, ...txn]
  },
}
