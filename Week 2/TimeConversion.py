#This Program allows users to convert seconds to hour:minute:second format

#This uses only basic math operations only
seconds = int(input('Please enter the time to be converted, in sec:'))

hour = int(seconds/3600)
minute = int(((seconds/60)-(hour*60)))
secondleft = int(seconds-((hour*3600)+(minute*60)))

print("Time,", hour,"hr,", minute,"min", secondleft,"sec")

#This uses modulus and floor division instead
seconds = int(input('Please enter the time to be converted, in sec:'))

hour = (seconds//3600)
minute = ((seconds//60)-(hour*60))
secondleft = ((seconds%60))

print("Time,", hour,"hr,", minute,"min", secondleft,"sec")

