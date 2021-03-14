# 0's will b x's
# t and h will never be beside each other the h will be moved to the end
# letters "raymnd" will be "evans8"
# the 4,8 vowel will be ?s a8e3i4o\u%
# 
#
#
import config
website = "gmail.com"
code =  "disicpline and preparation create opportunity forcing growth in a world that doesn't love us but will give us the " #input("enter code sentence "  )
password = str #25 character 
v = 0
hold = []
key2 = "rymndeiou"
key3 = "ev2/s83K/%"
const = "bcdfghjklmnpqrstvwxyz"
 




def convert(s): 
    str1 = "" 
    return(str1.join(s)) 


def key(hold):
	c, var= 0, 0
	for k in range(len(code)):
	#print(code[i])
		if code[k] == " ":
		#print(code[c:i])
			hold.append(code[c])
			c = k +1
	
	for i in range(len(hold)):

		if hold[i] in key2:
			for x in range(len(hold)):
				for p in range(len(key2)):
					if hold[x] == key2[p]: 
						hold[x] = key3[p]
	
	return hold

x = key(hold)
temp = convert(x)
newkey = config.key + temp + config.key[::-1]
print(newkey)


	


