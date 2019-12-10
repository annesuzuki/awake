#! python3

# Convert current time to local time provided in command line
# If timezone does not exist, defaults to UTC
# Returns naive datetime object with conversion

import datetime
import pytz
import sys

def now(timezone = 'UTC'):

   nowUTC = datetime.datetime.utcnow()
   fmt = '%Y-%m-%d %H:%M:%S'

   # determine timezone; if none given, default to UTC
   if timezone not in pytz.all_timezones:
      print('UTC '+ nowUTC.strftime(fmt))
      return nowUTC
   else:
      localZone = pytz.timezone(timezone)

   # convert from UTC to time in given timezone
   local_dt = localZone.localize(nowUTC)
   offsetString = local_dt.strftime('%z') # get shift from UTC time
   operator = offsetString[0] # + or - UTC time

   # calculate shift from UTC to local time
   delta = datetime.timedelta(
         minutes = int(offsetString[3:]),
         hours = int(offsetString[1:3])
         )

   if operator == '-':
      naiveDatetime = nowUTC - delta
   elif operator == '+':
      naiveDatetime = nowUTC + delta
   else:
      naiveDatetime = nowUTC

   print(localZone.zone + ' ' + naiveDatetime.strftime(fmt))

   # return local time as naive datetime object
   return naiveDatetime

if __name__ == '__main__':
   if len(sys.argv) < 2:
      now()
   else:
      now(sys.argv[1])
      

