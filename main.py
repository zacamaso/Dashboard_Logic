

import streamlit as st
import pandas as pd


# Function to convert a date to date_id
def convert_to_date_id(input_date):
    base_date = pd.to_datetime("2010-01-01")
    return (input_date - base_date).days + 1

# Define the functions using date_id
def is_booked_revenue(book_date_id, order_status_id, vSelectedDate1, vSelectedDate2):

    try:
        if vSelectedDate1 <= book_date_id <= vSelectedDate2 and order_status_id <= 2:
            return True
        return False
    except:
        return False

def is_waiting_for_payment(order_date_id, order_status_id, vSelectedDate1, vSelectedDate2, book_date_id):
    try:
        if book_date_id is None and vSelectedDate1 <= order_date_id <= vSelectedDate2 and order_status_id <= 3:
            return True

        elif (vSelectedDate1 <= order_date_id <= vSelectedDate2 and 
            order_status_id <= 3 and 
            book_date_id >= vSelectedDate2):
            return True
        return False
    except:
        return False


def is_lost_revenue(order_date_id, order_status_id, vSelectedDate1, vSelectedDate2):
    try:
        if vSelectedDate1 <= order_date_id <= vSelectedDate2 and order_status_id >= 4:
            return True
        return False
    except:
        return False

# Data for order status
data = {
    'order_status_id': [1, 2, 3, 4, 5, 6, 7, 8, 9],
    'order_status_name': ['COMPOUNDED', 'BOOKED', 'PENDING PAYMENT', 'CANCELLED', 'ON HOLD', 'DELETED', 'NOT PAID', 'TRANSFERRED', 'UNKNOWN']
}
order_status_df = pd.DataFrame(data)

# Streamlit app layout
st.sidebar.title("Input Variables")

# Date Range Picker for vSelectedDate1 and vSelectedDate2
date_range = st.sidebar.date_input("Select Date Range", [])
if date_range:
    vSelectedDate1 = convert_to_date_id(pd.to_datetime(date_range[0]))
    vSelectedDate2 = convert_to_date_id(pd.to_datetime(date_range[-1]))
else:
    vSelectedDate1 = 0
    vSelectedDate2 = 0

st.sidebar.write("vSelectedDate1: ",vSelectedDate1)
st.sidebar.write("vSelectedDate2: ",vSelectedDate2)

# Date input for book_date_id and order_date_id
order_date = st.sidebar.date_input("Order Date", value=None)
book_date = st.sidebar.date_input("Book Date", value=None)


# Convert the date inputs to date_id format
if book_date:
    book_date_id = convert_to_date_id(pd.to_datetime(book_date))
else:
    book_date_id = None



if order_date:
    order_date_id = convert_to_date_id(pd.to_datetime(order_date))
else:
    order_date_id = None

st.sidebar.write("Order Date ID: ",order_date_id)
st.sidebar.write("Book Date ID: ",book_date_id)


# Input widget for order_status_name
order_status_name = st.sidebar.selectbox("Order Status", options=order_status_df['order_status_name'], index=0,)

# Mapping order_status_name to order_status_id
order_status_id = order_status_df[order_status_df['order_status_name'] == order_status_name]['order_status_id'].values[0]

# Metrics Calculation
booked_revenue = is_booked_revenue(book_date_id, order_status_id, vSelectedDate1, vSelectedDate2)
waiting_for_payment = is_waiting_for_payment(order_date_id, order_status_id, vSelectedDate1, vSelectedDate2, book_date_id)
lost_revenue = is_lost_revenue(order_date_id, order_status_id, vSelectedDate1, vSelectedDate2)

# Display the functions
st.markdown("Booked Revenue")
st.code('''

if vSelectedDate1 <= book_date_id <= vSelectedDate2 and order_status_id <= 2:
    return True
return False
''', language='python')

st.code(booked_revenue)

# Function 2: is_waiting_for_payment
st.markdown("Waiting for Payment")
st.code('''
if (vSelectedDate1 <= order_date_id <= vSelectedDate2 and 
    order_status_id <= 3 and 
    (book_date_id >= vSelectedDate2 or book_date_id is None)):
    return True
return False
''', language='python')

st.code(waiting_for_payment)

# Function 3: is_lost_revenue
st.markdown("Lost Revenue")
st.code('''
if vSelectedDate1 <= order_date_id <= vSelectedDate2 and order_status_id >= 4:
    return True
return False
''', language='python')

st.code(lost_revenue)





