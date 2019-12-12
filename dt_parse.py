import re, datetime

def time_parser(stringTime):
   time_re = re.compile(r'''
      # HH or H hours
      (
      ([\d]?[\d])
      # divider
      :
      # MM minutes
      ( [\d][\d] )
      # divider
      :?
      # SS optional
      ( [\d][\d] )?
      # divider optional
      .?
      # Milliseconds optional
      ( [\d]{0,7} )?
      # space optional
      \s?
      # AM or PM optional
      ( am | AM | pm | PM )?
      )
      ''', re.VERBOSE)

   listTime = time_re.findall(stringTime)

   # list of naive datetime.time objects
   validTime = []

   for time in listTime:
      if (time[1] == '' or time[2] == '') : # Invalid timestamp: no hour or minutes provided
         continue
      hour = int(time[1])
      minute = int(time[2])
      if time[3] != '':
         sec = int(time[3])
      else:
         sec = 0
      if time[4] != '':
         milliseconds = int(time[4])
      else:
         micro = 0
      am_pm = time[5]

      # convert to military time
      if am_pm.lower() == 'pm' and hour < 12:
         hour+=12
      if hour == 12 and am_pm.lower() == 'am':
         hour = 24

      try:
         timeStamp = datetime.time(hour,minute,sec,micro)
         validTime.append(timeStamp)
      except:
         continue     # Invalid timestamp, ValueError raised 

   return validTime # list of datetime.time objects

l = time_parser('2:00 pm, 24:72:10:23432, 2323.00')
print(l[0].hour)
print(l[0].minute)
print(l[0].second)

