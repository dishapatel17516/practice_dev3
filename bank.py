import sys

name = sys.argv[1]
ini_balance = int(sys.argv[2])
deposit = int(sys.argv[3])
total_balance = ini_balance + deposit

print("total balance", total_balance)

withdraw = int(sys.argv[4])

total_bal = total_balance - withdraw

print("total salary", total_bal)

if total_bal <1000:
   print("min balance should be maintained with 1000/- ")