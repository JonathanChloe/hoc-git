from datetime import datetime, timedelta;


print("HelloWorld")

begin_date = '2018-08-20'
end_date   = '2018-08-20'

# bdate = datetime.strptime(begin_date, "%Y-%m-%d") - timedelta(hours=7)
# edate = datetime.strptime(end_date, "%Y-%m-%d") - timedelta(hours=7)

bdate = datetime.strptime(begin_date+"T00:00:00.000Z", "%Y-%m-%dT%H:%M:%S.000Z") - timedelta(hours=7)
edate = datetime.strptime(end_date+"T23:59:59.999Z", "%Y-%m-%dT%H:%M:%S.999Z") - timedelta(hours=7)

for x in range(5):
	print("Chloe, I love u")

print("Love u forever")

print (timedelta(hours = 7))

print(begin_date)

print(end_date)

print (bdate)

print(edate)