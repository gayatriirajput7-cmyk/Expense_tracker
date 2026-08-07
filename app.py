import streamlit as st
import pandas as pd

# Set page configuration for a professional look
st.set_page_config(page_title="Expense Tracker", page_icon="💸", layout="centered")

# Initialize session state to store the list of dictionary expenses
if 'expenses_list' not in st.session_state:
    st.session_state['expenses_list'] = []

st.title("💸 Personal Expense Tracker")
st.write("Track your daily *kharcha* cleanly and professionally.")

# Create tabs for navigation instead of a terminal menu
tab1, tab2, tab3 = st.tabs(["➕ Add Expense", "📋 View All", "📊 Total Spending"])

# --- TAB 1: ADD EXPENSE ---
with tab1:
    st.subheader("Log a New Expense")
    
    # Using a form ensures the app only updates when the user clicks 'Save'
    with st.form("expense_form", clear_on_submit=True):
        date = st.date_input("When did you make this purchase?")
        category = st.selectbox("Category", ["Food", "Travel", "Makeup", "Books", "Education", "Other"])
        description = st.text_input("Additional Details")
        amount = st.number_input("Amount (₹)", min_value=0.0, format="%.2f", step=10.0)
        
        submitted = st.form_submit_button("Save Expense")

        if submitted:
            if amount > 0:
                # Storing data in the exact dictionary format you established
                expense = {
                    "Date": date.strftime("%Y-%m-%d"),
                    "Category": category,
                    "Description": description,
                    "Amount": amount
                }
                st.session_state['expenses_list'].append(expense)
                st.success("Done bro! Expense added successfully.")
            else:
                st.error("Please enter a valid amount.")

# --- TAB 2: VIEW ALL EXPENSES ---
with tab2:
    st.subheader("Your Expense Ledger")
    
    if len(st.session_state['expenses_list']) == 0:
        st.info("No expenses added yet. Jao pehle khrcha karo! 😉")
    else:
        # Converting the list of dictionaries to a Pandas DataFrame for a beautiful web table
        df = pd.DataFrame(st.session_state['expenses_list'])
        
        # Display the dataframe seamlessly in Streamlit
        st.dataframe(df, use_container_width=True, hide_index=True)

# --- TAB 3: VIEW TOTAL SPENDING ---
with tab3:
    st.subheader("Spending Summary")
    
    if len(st.session_state['expenses_list']) == 0:
        st.metric(label="Total Kharcha", value="₹ 0.00")
    else:
        # Using Python's built-in sum() function for clean, efficient calculation
        total = sum(each_kharcha["Amount"] for each_kharcha in st.session_state['expenses_list'])
        
        st.metric(label="Total Kharcha", value=f"₹ {total:,.2f}")