import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)

num = int(time.strftime('%H'))
print(num)
if 4<num<12:
    
 print("Good Moring")
elif 12<=num<18:
  
 print("Good afternoon")
   
elif 18<=num<21:
   
      print("Good Evening")
   
else:
   print("Good Night")  
    
        