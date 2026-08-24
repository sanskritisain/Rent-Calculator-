import streamlit as st

st.title("🏠 Rent Calculator")

st.write("Calculate the amount each person needs to pay for shared accommodation.")

# Inputs
rent = st.number_input(
    "Enter the rent of your flat/hostel:",
    min_value=0,
    step=100
)

food = st.number_input(
    "Enter the amount spent on food:",
    min_value=0,
    step=100
)

electricity = st.number_input(
    "Enter the total electricity units consumed:",
    min_value=0,
    step=1
)

charge_per_unit = st.number_input(
    "Enter the electricity charge per unit:",
    min_value=0,
    step=1
)

persons = st.number_input(
    "Enter the number of persons living in the room:",
    min_value=1,
    step=1
)

# Calculate
if st.button("Calculate Rent"):
    total_electricity_bill = electricity * charge_per_unit

    total_bill = rent + food + total_electricity_bill

    amount_per_person = total_bill / persons

    st.success(f"Total Monthly Bill: ₹{total_bill:,.2f}")

    st.info(
        f"Each person will pay: ₹{amount_per_person:,.2f}"
    )