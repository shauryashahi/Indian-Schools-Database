from lxml.html import parse

def main():
	baseurl = 'http://www.schoolcolleges.com/school.select.php?offset=%s&val=city=%270%27&select=%s'
	states = [
	'Andhra Pradesh',
	'Arunachal Pradesh',
	'Assam',
	'BIHAR',
	'Chhattisgarh',
	'Goa',
	'Gujarat',
	'Haryana',
	'Himachal Pradesh',
	'Jammu & Kashmir',
	'Jharkhand',
	'Karnataka',
	'Kerala',
	'Madhya Pradesh',
	'Maharashtra',
	'Manipur',
	'Meghalaya',
	'Mizoram',
	'Nagaland',
	'Odisha',
	'Punjab',
	'Rajasthan',
	'Sikkim',
	'Tamil Nadu',
	'Tripura',
	'Uttarakhand',
	'Uttar Pradesh',
	'West Bengal']
	n = 10
	for state in states:
		offset = str(n)
		url = baseurl %(offset) %(state)
		page = parse(url).getroot()
		#tr21,25,29...
		for i in xrange(21,102,4):
			table = page.cssselect('tr')[i]
			data = table.cssselect('td')
