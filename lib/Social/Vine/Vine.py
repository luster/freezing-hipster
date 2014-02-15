import urllib2

url = 'https://vine.co/u/950312101489033216'

response = urllib2.urlopen(url).read()
print response
