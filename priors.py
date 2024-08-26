import pandas as pd

# Describing the filtering logic for metrics in a dashboard

# DIM_DATE:{Date Range picker widjet} -> FACT_TABLE: {oder_date_id}


# # Status Table:
# 1. COMPOUNDED
# 2. BOOKED
# 3. PENDING PAYMENT
# 4. CANCELLED
# 5. ON HOLD
# 6. DELETED
# 7. NOT PAID
# 8. TRANSFERED
# 9. UNKNOWN


data = {'order_status_id': [1, 2, 3, 4, 5, 6, 7, 8, 9], 'order_status_name': ['COMPOUNDED', 'BOOKED', 'PENDING PAYMENT', 'CANCELLED', 'ON HOLD', 'DELETED', 'NOT PAID', 'TRANSFERED', 'UNKNOWN']}
df = pd.DataFrame(data) 
print(df)

# Dimension: Date Range Picker [vSelectedDate1, vSelectedDate2]

# # Metric 1: Booked Revenue
# Initialize variables
book_date_id =  0
status = ''
vSelectedDate1 = 0
vSelectedDate2 = 0
order_status_id = 0
order_date_id = 0
booked_revenue = 0

# # Metric 1: Booked Revenue

def is_booked_revenue(book_date_id, order_status_id, vSelectedDate1, vSelectedDate2):

    if book_date_id >= vSelectedDate1 and book_date_id <= vSelectedDate2 and order_status_id <= 2:

        return True
    return False


# # Metric 2: Waiting for payment

def is_waiting_for_payment(order_date_id, order_status_id, vSelectedDate1, vSelectedDate2):

    if order_date_id >= vSelectedDate1 and order_date_id <= vSelectedDate2 and order_status_id <= 3:
        return True
    return False


# # Metric 3: Lost Revenue (Cancelled, ON HOLD, DELETED, etc.)

def is_lost_revenue(order_date_id, order_status_id, vSelectedDate1, vSelectedDate2):
    
    if order_date_id >= vSelectedDate1 and order_date_id <= vSelectedDate2 and order_status_id >= 4:
        return True
    return False

# # Test cases

# Test Case 1: Booked Revenue - Inside Date Range and Status is "BOOKED"
test_case_1 = [20220815, 2, 20220101, 20221231, True]

# Test Case 2: Booked Revenue - Inside Date Range but Status is "COMPOUNDED"
test_case_2 = [20220815, 1, 20220101, 20221231, True]

# Test Case 3: Booked Revenue - Outside Date Range
test_case_3 = [20230101, 2, 20220101, 20221231, False]

# Test Case 4: Waiting for Payment - Inside Date Range and Status is "PENDING PAYMENT"
test_case_4 = [20220815, 3, 20220101, 20221231, True]

# Test Case 5: Waiting for Payment - Outside Date Range
test_case_5 = [20230101, 3, 20220101, 20221231, False]

# Test Case 6: Waiting for Payment - Status is "CANCELLED"
test_case_6 = [20220815, 4, 20220101, 20221231, False]

# Test Case 7: Lost Revenue - Inside Date Range and Status is "CANCELLED"
test_case_7 = [20220815, 4, 20220101, 20221231, True]

# Test Case 8: Lost Revenue - Inside Date Range and Status is "DELETED"
test_case_8 = [20220815, 6, 20220101, 20221231, True]

# Test Case 9: Lost Revenue - Outside Date Range
test_case_9 = [20230101, 4, 20220101, 20221231, False]

# Test Case 10: Lost Revenue - Inside Date Range but Status is "BOOKED"
test_case_10 = [20220815, 2, 20220101, 20221231, False]
