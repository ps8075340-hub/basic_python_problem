#Program to accept transactions in a day and items sold in day for a week and then print average sales made per transaction.

totaltrans, totalsales = 0, 0
count = 1

#loop
while count <= 7:
    trans = float( input (f'Transaction made on day {count} :'))
    items = float( input(f'Items sold on day {count} :'))
   
    totaltrans += trans
    totalsales += items
    count += 1
  
#Average sales   
if totaltrans != 0:
    avg_sales = totalsales / totaltrans
else:
    avg_sales = 0

print('Total Sales made : ',totalsales)
print ('Total Transaction made : ', totaltrans)
print('Average Sales per transaction : ',avg_sales) 