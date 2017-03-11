'''
Given a time in -hour AM/PM format, convert it to military (-hour) time.

Note: Midnight is  on a -hour clock, and  on a -hour clock. Noon is  on a -hour clock, and  on a -hour clock.

Input Format

A single string containing a time in -hour clock format (i.e.:  or ), where  and .

Output Format

Convert and print the given time in -hour format, where .

Sample Input

07:05:45PM
Sample Output

19:05:45
'''


time = input().strip().split(":")
hour, minute, second, am = time[0], time[1], time[2][:2], time[2][2:] == "AM"

# Check if it is 12:00:00AM - 12:59:59AM
if am and hour == "12":
    hour = "00"
elif ~am:
    hour = str(int(hour) + 12)

print(hour + ":" + minute + ":" + second)
