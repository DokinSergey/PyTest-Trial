from datetime import timedelta,datetime as dt
YY = 2025
MM = 2
DD = 1
HH = 23
mm = 35
ss = 20
dtnow = dt(YY,MM,DD,HH,mm,ss)
delta = timedelta(days=1)
dtnew = dtnow - delta
print(dtnow,dtnew.date())
# print(f'today = {dt.today().timetuple().tm_hour} now = {dt.now().timetuple()} timestamp = {dt.now().timestamp()}')
