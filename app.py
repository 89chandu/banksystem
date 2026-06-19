import streamlit as st
import pandas as pd

from bank import Bank
from account import SavingAccount

bank = Bank()

st.title("Banking System")

menu = st.sidebar.selectbox(
    "Menu",
    [
        "Create Account",
        "View Account",
        "Deposit",
        "Withdraw"
    ]
)

# Create Account

if menu == "Create Account":
    st.header("Create Account")

    account_no = st.text_input("Account Number")
    name = st.text_input("Customer Name")
    balance = st.number_input("Opening Balance",min_value=0)

    if st.button("Create"):

        account = SavingAccount(
            account_no,
            name,
            balance
        )

        bank.create_account(account)
        st.success("Account Created Successfully")


# View Accounts

elif menu == "View Account":

    data = []

    for account in bank.accounts:

        data.append(
            {
                "Account No":account.account_no,
                "Name":account.name,
                "Balance":account.get_balance()
            }
        ) 

        if data:
            st.dataframe(pd.DataFrame(data))


# Deposit

elif menu == "Deposit":
    account_no = st.text_input("Account Number")

    amount = st.number_input(
        "Amount",
        min_value=1
    )

    if st.button("Deposit"):
        account = bank.find_account(account_no)

        if account :

            account.deposit(amount)
            bank.save_accounts()
            st.success("Amount Deposited")

        else:
            st.error("Account Not Found")


#Withdraw

elif menu == "Withdraw":
    account_no = st.text_input("Account Number")

    amount = st.number_input(
        "Amount",
        min_value=1
    ) 

    if st.button("withdraw"):
        account = bank.find_account(account_no)

        if account:
            result = account.withdraw(amount)

            if result:
                bank.save_accounts()

                st.success("Amount Withdrawn")

            else:
                st.error("Insufficient Balance")

        else:
            st.error("Account Not Found")            


