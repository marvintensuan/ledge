from datetime import date
from decimal import Decimal
from enum import Enum

from pydantic import condecimal
from sqlmodel import SQLModel, Field


class TransactionCategory(str, Enum):
    PERSONAL_EXPENSE = "Personal Expense"
    MAJOR_EXPENSE = "Major Expense"
    FINANCE_CHARGE = "Finance Charge"
    INTEREST_EXPENSE = "Interest Expense"
    INTEREST_REVENUE = "Interest Revenue"
    WTH_TAX = "Withholding Taxes"
    BILLS = "Bills"
    CASH_TRANSFER = "Cash Transfer"
    INSURANCE = "Insurance"
    INVESTMENT_DEPOSIT = "Investment Deposit"
    PAYROLL = "Payroll"


class Transactions(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    date: date
    account: str
    amount: float
    category: TransactionCategory | None = None
    description: str
