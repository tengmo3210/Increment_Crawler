import sys


string = 'ก'
string2 = 'ห'
a = ord(string)

#print (chr(3585))


f = open('/home/tengmo/workwithcrawler/2000file/sub_testcrawl[116].arc', 'r')
text = ''
cnt = 0
for line in f:
    cnt +=1
    if(cnt>7):
        text += line
html_content = text


print (ord('a'), ord('z'), ord('A'), ord('Z'), ord('.'), ord('\n'), ord(' '))

print (ord('0'), ord('9'))
