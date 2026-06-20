import pandas as pd
import streamlit as st

from account import SavingAccount
from bank import Bank


st.set_page_config(
    page_title="Bank Of Balaghat",
    page_icon=":material/account_balance:",
    layout="wide",
)


def money(value):
    return f"Rs {value:,.2f}"


def render_styles():
    st.markdown(
        """
        <style>
            :root {
                --bg: #f6f8fb;
                --panel: #ffffff;
                --ink: #172033;
                --muted: #657187;
                --line: #dde5f0;
                --brand: #175cd3;
                --brand-dark: #123f91;
                --good: #079455;
                --warn: #d92d20;
                --note: #daf5d9;
                --note-border: #46a758;
            }

            .stApp {
                background:
                    radial-gradient(circle at top left, rgba(23, 92, 211, 0.12), transparent 28rem),
                    linear-gradient(180deg, #f9fbff 0%, var(--bg) 44%, #eef3fa 100%);
                color: var(--ink);
            }

            [data-testid="stSidebar"] {
                background: #0f1d34;
            }

            [data-testid="stSidebar"] * {
                color: #e6edf7;
            }

            .block-container {
                padding-top: 2rem;
                padding-bottom: 3rem;
                max-width: 1180px;
            }

            .app-shell {
                display: grid;
                gap: 1.25rem;
            }

            .hero {
                border: 1px solid var(--line);
                border-radius: 8px;
                background:
                    linear-gradient(135deg, rgba(23, 92, 211, 0.94), rgba(18, 63, 145, 0.96)),
                    linear-gradient(45deg, rgba(255,255,255,0.14), transparent);
                color: #ffffff;
                padding: 2rem;
                overflow: hidden;
                position: relative;
                min-height: 220px;
            }

            .hero:after {
                content: "";
                position: absolute;
                width: 360px;
                height: 360px;
                border: 1px solid rgba(255,255,255,0.20);
                border-radius: 50%;
                right: -120px;
                top: -120px;
            }

            .hero h1 {
                font-size: 2.45rem;
                line-height: 1.08;
                margin: 0 0 .7rem 0;
                letter-spacing: 0;
            }

            .hero p {
                max-width: 650px;
                color: #dbe8ff;
                font-size: 1.03rem;
                margin: 0;
            }

            .hero-stats {
                display: grid;
                grid-template-columns: repeat(3, minmax(0, 1fr));
                gap: .75rem;
                margin-top: 1.5rem;
                max-width: 720px;
            }

            .stat-card,
            .panel,
            .account-card {
                background: var(--panel);
                border: 1px solid var(--line);
                border-radius: 8px;
                box-shadow: 0 12px 28px rgba(23, 32, 51, 0.06);
            }

            .hero .stat-card {
                background: rgba(255,255,255,0.12);
                border-color: rgba(255,255,255,0.24);
                box-shadow: none;
                color: #ffffff;
                padding: .9rem 1rem;
            }

            .stat-label {
                color: inherit;
                opacity: .78;
                font-size: .78rem;
                text-transform: uppercase;
                letter-spacing: .04em;
                margin-bottom: .25rem;
            }

            .stat-value {
                font-size: 1.45rem;
                font-weight: 750;
            }

            .panel {
                padding: 1.25rem;
            }

            .section-title {
                font-size: 1.25rem;
                font-weight: 750;
                margin: 0 0 .25rem 0;
                color: var(--ink);
            }

            .section-subtitle {
                color: var(--muted);
                margin: 0 0 1rem 0;
            }

            .account-grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(230px, 1fr));
                gap: .85rem;
                margin-top: .25rem;
            }

            .account-card {
                padding: 1rem;
            }

            .account-number {
                color: var(--muted);
                font-size: .82rem;
                margin-bottom: .35rem;
            }

            .account-name {
                color: var(--ink);
                font-weight: 750;
                font-size: 1rem;
                margin-bottom: .75rem;
            }

            .account-balance {
                color: var(--brand-dark);
                font-size: 1.55rem;
                font-weight: 800;
            }

            .empty-state {
                border: 1px dashed #b9c6d8;
                border-radius: 8px;
                padding: 1.3rem;
                color: var(--muted);
                background: rgba(255,255,255,0.72);
            }

            .success-pop {
                position: relative;
                display: inline-flex;
                align-items: center;
                gap: .6rem;
                padding: .8rem 1rem;
                border-radius: 8px;
                background: #ecfdf3;
                border: 1px solid #abefc6;
                color: #067647;
                font-weight: 750;
                animation: popIn .42s ease-out both;
                overflow: hidden;
                margin: .75rem 0;
            }

            .success-pop:after {
                content: "";
                position: absolute;
                inset: -4px;
                border-radius: 10px;
                border: 2px solid rgba(7, 148, 85, .28);
                animation: ringPop .75s ease-out both;
            }

            .success-dot {
                width: 12px;
                height: 12px;
                border-radius: 50%;
                background: var(--good);
                box-shadow: 0 0 0 6px rgba(7, 148, 85, .13);
            }

            .money-stage {
                position: relative;
                height: 210px;
                border: 1px solid var(--line);
                border-radius: 8px;
                background:
                    linear-gradient(180deg, #ffffff 0%, #f4f8ff 100%);
                overflow: hidden;
                margin: 1rem 0;
            }

            .vault {
                position: absolute;
                left: 50%;
                top: 50%;
                transform: translate(-50%, -50%);
                width: 170px;
                height: 108px;
                border-radius: 8px;
                background: linear-gradient(135deg, #172033, #344054);
                box-shadow: 0 18px 40px rgba(23, 32, 51, .18);
            }

            .vault:before {
                content: "";
                position: absolute;
                left: 20px;
                right: 20px;
                top: 20px;
                height: 52px;
                border-radius: 6px;
                background: #eef4ff;
                border: 4px solid #c7d7f3;
            }

            .vault:after {
                content: "";
                position: absolute;
                left: 50%;
                top: 46px;
                transform: translate(-50%, -50%);
                width: 34px;
                height: 34px;
                border-radius: 50%;
                background: #175cd3;
                box-shadow: 0 0 0 7px #d8e7ff;
            }

            .slot {
                position: absolute;
                left: 36px;
                right: 36px;
                bottom: 18px;
                height: 10px;
                border-radius: 99px;
                background: #101828;
            }

            .bill {
                position: absolute;
                width: 86px;
                height: 40px;
                border-radius: 5px;
                background: var(--note);
                border: 1px solid var(--note-border);
                box-shadow: 0 8px 18px rgba(23, 32, 51, .12);
                color: #087443;
                font-weight: 800;
                display: flex;
                align-items: center;
                justify-content: center;
            }

            .bill:before,
            .bill:after {
                content: "";
                position: absolute;
                width: 10px;
                height: 10px;
                border-radius: 50%;
                border: 1px solid rgba(70, 167, 88, .55);
            }

            .bill:before { left: 8px; }
            .bill:after { right: 8px; }

            .deposit .bill {
                left: 50%;
                top: -54px;
                transform: translateX(-50%);
                animation: depositBill 1.25s ease-in forwards;
            }

            .withdraw .bill {
                left: 50%;
                top: 92px;
                transform: translateX(-50%);
                animation: withdrawBill 1.35s ease-out forwards;
            }

            .bill.b2 { animation-delay: .12s; margin-left: -58px; }
            .bill.b3 { animation-delay: .24s; margin-left: 58px; }

            .spark {
                position: absolute;
                left: 50%;
                top: 50%;
                width: 8px;
                height: 8px;
                border-radius: 50%;
                background: #fdb022;
                opacity: 0;
                animation: spark .8s ease-out .55s both;
            }

            .spark.s2 { margin-left: -86px; margin-top: -58px; animation-delay: .62s; }
            .spark.s3 { margin-left: 78px; margin-top: -42px; animation-delay: .68s; }
            .spark.s4 { margin-left: 92px; margin-top: 48px; animation-delay: .74s; }

            @keyframes depositBill {
                0% { transform: translate(-50%, -10px) rotate(-9deg); opacity: 0; }
                18% { opacity: 1; }
                70% { transform: translate(-50%, 98px) rotate(2deg); opacity: 1; }
                100% { transform: translate(-50%, 132px) scale(.55) rotate(0); opacity: 0; }
            }

            @keyframes withdrawBill {
                0% { transform: translate(-50%, 24px) scale(.55) rotate(0); opacity: 0; }
                20% { opacity: 1; }
                100% { transform: translate(-50%, -128px) scale(1) rotate(8deg); opacity: 0; }
            }

            @keyframes popIn {
                0% { transform: scale(.92); opacity: 0; }
                70% { transform: scale(1.03); opacity: 1; }
                100% { transform: scale(1); }
            }

            @keyframes ringPop {
                0% { transform: scale(.84); opacity: .8; }
                100% { transform: scale(1.18); opacity: 0; }
            }

            @keyframes spark {
                0% { transform: scale(.2); opacity: 0; }
                35% { opacity: 1; }
                100% { transform: scale(8); opacity: 0; }
            }

            div.stButton > button {
                border-radius: 8px;
                border: 1px solid var(--brand);
                background: var(--brand);
                color: #ffffff;
                font-weight: 700;
                padding: .6rem 1rem;
            }

            div.stButton > button:hover {
                border-color: var(--brand-dark);
                background: var(--brand-dark);
                color: #ffffff;
            }

            [data-testid="stDataFrame"] {
                border: 1px solid var(--line);
                border-radius: 8px;
                overflow: hidden;
            }

            @media (max-width: 760px) {
                .hero { padding: 1.25rem; }
                .hero h1 { font-size: 1.85rem; }
                .hero-stats { grid-template-columns: 1fr; }
                .money-stage { height: 190px; }
            }
        </style>
        """,
        unsafe_allow_html=True,
    )


def account_rows(accounts):
    return [
        {
            "Account No": account.account_no,
            "Name": account.name,
            "Balance": account.get_balance(),
        }
        for account in accounts
    ]


def account_summary(accounts):
    total_balance = sum(account.get_balance() for account in accounts)
    return len(accounts), total_balance


def render_success(message):
    st.markdown(
        f"""
        <div class="success-pop">
            <span class="success-dot"></span>
            <span>{message}</span>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_money_animation(kind):
    stage_class = "deposit" if kind == "deposit" else "withdraw"
    st.markdown(
        f"""
        <div class="money-stage {stage_class}">
            <div class="vault"><div class="slot"></div></div>
            <div class="bill b1">Rs 100</div>
            <div class="bill b2">Rs 50</div>
            <div class="bill b3">Rs 20</div>
            <div class="spark s1"></div>
            <div class="spark s2"></div>
            <div class="spark s3"></div>
            <div class="spark s4"></div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_dashboard(bank):
    account_count, total_balance = account_summary(bank.accounts)
    largest_balance = max((account.get_balance() for account in bank.accounts), default=0)

    st.markdown(
        f"""
        <div class="hero">
            <h1>Banking System</h1>
            <p>Manage customer accounts, deposits, and withdrawals from a clean professional dashboard.</p>
            <div class="hero-stats">
                <div class="stat-card">
                    <div class="stat-label">Accounts</div>
                    <div class="stat-value">{account_count}</div>
                </div>
                <div class="stat-card">
                    <div class="stat-label">Total Balance</div>
                    <div class="stat-value">{money(total_balance)}</div>
                </div>
                <div class="stat-card">
                    <div class="stat-label">Highest Balance</div>
                    <div class="stat-value">{money(largest_balance)}</div>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.write("")
    render_accounts_preview(bank.accounts)


def render_accounts_preview(accounts):
    st.markdown(
        """
        <div class="panel">
            <div class="section-title">Recent Accounts</div>
            <div class="section-subtitle">Quick view of customer balances.</div>
        """,
        unsafe_allow_html=True,
    )

    if not accounts:
        st.markdown(
            '<div class="empty-state">No accounts yet. Create an account to start banking operations.</div>',
            unsafe_allow_html=True,
        )
    else:
        cards = ['<div class="account-grid">']
        for account in accounts[-6:]:
            cards.append(
                f"""
                <div class="account-card">
                    <div class="account-number">Account {account.account_no}</div>
                    <div class="account-name">{account.name}</div>
                    <div class="account-balance">{money(account.get_balance())}</div>
                </div>
                """
            )
        cards.append("</div>")
        st.markdown("".join(cards), unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)


def account_selector(bank, key):
    options = [account.account_no for account in bank.accounts]
    if not options:
        return None
    return st.selectbox("Account Number", options, key=key)


bank = Bank()
render_styles()

with st.sidebar:
    st.markdown("### Banking System")
    st.caption("Professional account operations")
    menu = st.radio(
        "Menu",
        [
            "Home",
            "Create Account",
            "View Accounts",
            "Deposit",
            "Withdraw",
        ],
    )

if menu == "Home":
    render_dashboard(bank)

elif menu == "Create Account":
    st.markdown('<div class="panel">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Create Account</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-subtitle">Open a new savings account with an initial balance.</div>',
        unsafe_allow_html=True,
    )

    with st.form("create_account_form", clear_on_submit=True):
        col1, col2 = st.columns(2)
        with col1:
            account_no = st.text_input("Account Number")
        with col2:
            name = st.text_input("Customer Name")
        balance = st.number_input("Opening Balance", min_value=0, step=100)
        submitted = st.form_submit_button("Create Account")

    if submitted:
        account_no = account_no.strip()
        name = name.strip()

        if not account_no or not name:
            st.error("Account number and customer name are required.")
        elif bank.find_account(account_no):
            st.error("An account with this number already exists.")
        else:
            account = SavingAccount(account_no, name, balance)
            bank.create_account(account)
            render_success("Account created successfully")

    st.markdown("</div>", unsafe_allow_html=True)

elif menu == "View Accounts":
    st.markdown('<div class="panel">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">All Accounts</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-subtitle">Search and review every saved bank account.</div>',
        unsafe_allow_html=True,
    )

    data = account_rows(bank.accounts)
    if data:
        df = pd.DataFrame(data)
        df["Balance"] = df["Balance"].map(money)
        st.dataframe(df, use_container_width=True, hide_index=True)
    else:
        st.markdown(
            '<div class="empty-state">No accounts found. Create your first account from the sidebar.</div>',
            unsafe_allow_html=True,
        )

    st.markdown("</div>", unsafe_allow_html=True)

elif menu == "Deposit":
    st.markdown('<div class="panel">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Deposit Money</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-subtitle">Add funds to a customer account and watch the success pop.</div>',
        unsafe_allow_html=True,
    )

    if not bank.accounts:
        st.markdown(
            '<div class="empty-state">Create an account before making a deposit.</div>',
            unsafe_allow_html=True,
        )
    else:
        with st.form("deposit_form"):
            account_no = account_selector(bank, "deposit_account")
            amount = st.number_input("Deposit Amount", min_value=1, step=100)
            submitted = st.form_submit_button("Deposit")

        if submitted:
            account = bank.find_account(account_no)
            if account and account.deposit(amount):
                bank.save_accounts()
                render_money_animation("deposit")
                render_success(f"Deposit successful. New balance: {money(account.get_balance())}")
            else:
                st.error("Deposit failed. Please check the account and amount.")

    st.markdown("</div>", unsafe_allow_html=True)

elif menu == "Withdraw":
    st.markdown('<div class="panel">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Withdraw Money</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-subtitle">Withdraw funds with a visible money-out animation.</div>',
        unsafe_allow_html=True,
    )

    if not bank.accounts:
        st.markdown(
            '<div class="empty-state">Create an account before making a withdrawal.</div>',
            unsafe_allow_html=True,
        )
    else:
        with st.form("withdraw_form"):
            account_no = account_selector(bank, "withdraw_account")
            amount = st.number_input("Withdrawal Amount", min_value=1, step=100)
            submitted = st.form_submit_button("Withdraw")

        if submitted:
            account = bank.find_account(account_no)
            if not account:
                st.error("Account not found.")
            elif account.withdraw(amount):
                bank.save_accounts()
                render_money_animation("withdraw")
                render_success(f"Withdrawal successful. New balance: {money(account.get_balance())}")
            else:
                st.error("Insufficient balance.")

    st.markdown("</div>", unsafe_allow_html=True)
