# This is the code to check the maximum number occur in the following list
list = [1,2,3,4,2,2,3,1,4,4,4,4,2,2,2,2,2,2,2,2]
print(max(set(list), key=list.count))


# To check the security of the websites by checking the https or http starting of the site
print('http://www.google.com'.startswith(('http://', 'https://')))