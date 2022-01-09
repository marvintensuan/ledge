from decimal import Decimal
from enum import Enum

from sqlmodel import SQLModel, Field

class Transactions(SQLModel):
    date: date
    account: str
    amount: Decimal = Field(decimal=2)
    category: TransactionCategory
    description: str

class TransactionCategory(str, Enum):
    PERSONAL_EXPENSE = 'Personal Expense'
    MAJOR_EXPENSE = 'Major Expense'
    FINANCE_CHARGE = 'Finance Charge'
    INTEREST_EXPENSE = 'Interest Expense'
    INTEREST_REVENUE = 'Interest Revenue'
    WTH_TAX = 'Withholding Taxes'
    BILLS = 'Bills'
    CASH_TRANSFER = 'Cash Transfer'
    INSURANCE = 'Insurance'
    INVESTMENT_DEPOSIT = 'Investment Deposit'
    PAYROLL = 'Payroll'
