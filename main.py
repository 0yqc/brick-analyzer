import requests  # scraping / API
import re  # regex for scraping
from currency_converter import CurrencyConverter # currency conversion
currency_converter = CurrencyConverter()

set_num = input('Set Number (w/o -1 suffix): ')
price = input('Price; Syntax: ABC 1234.567: ')
price = currency_converter.convert(price.split(' ')[1],price.split(' ')[0],'USD') # convert price to USD
print('Your Price: USD ' + str(round(price,2)) + '$')

# BL PartOut Value

# as the BrickLink API is only available to sellers (I've written support about this issue), a crawler needs to be used to crawl the prices out of the user-accessible page.
print('\nGetting BrickLink Part Out Value...')
url = 'https://www.bricklink.com/catalogPOV.asp?itemType=S&itemNo=' + set_num + '&itemSeq=1&itemQty=1&breakType=M&itemCondition=U&breakSets=Y#'  # construct url
response = requests.get(url, headers = {'User-Agent':'py requests lib'})  # get the html body
if response.status_code == 200:  # 200 means success
	html = response.content.decode()  # get html content
	bl_partout_value = float(re.findall('(US \$)(.*?)(<)', html)[0][1])  # regex to find the price, price will always be displayed in USD
	print('BrickLink Part Out Value: $' + str(bl_partout_value) + ' USD')
	print('BrickLink Part Out Value is ' + str(round(bl_partout_value/price,2)) + '× your price')
else:  # quit as something has gone wrong
	print('Error ' + str(response.status_code) + ': Could not get BrickLink Part Out Value.')
	exit()

# BL sales average

# as the BrickLink API is only available to sellers (I've written support about this issue), a crawler needs to be used to crawl the prices out of the user-accessible page.
print('\nGetting BrickLink sales average...')
url = 'https://www.bricklink.com/catalogPG.asp?S=' + set_num + '-1'
response = requests.get(url,headers={'User-Agent':'py requests lib'})
if response.status_code == 200: # sucess
	html = response.content.decode() # whole website
	bl_sales_average_raw = list(re.findall('(>Avg Price:)(.*?)([A-Z]{3})(.*?\.[0-9]{2,4})', html)[1][2:4]) # regex to find all average prices, then filter out the correct match, converted to an array for editing; [2:4]: results 2 to 3
	bl_sales_average_raw[1] = re.sub(',', '', bl_sales_average_raw[1]) # remove thousands separation
	bl_sales_average_raw[1] = bl_sales_average_raw[1].removeprefix('&nbsp;') # remove leading non-breaking space
	print('BrickLink sales average: ' + bl_sales_average_raw[0] + ' ' + bl_sales_average_raw[1])
	bl_sales_average = currency_converter.convert(bl_sales_average_raw[1], bl_sales_average_raw[0], 'USD') # convert raw data into USD
	print('BrickLink sales average: USD ' + str(round(bl_sales_average, 2)) + '$')
	print('BrickLink sales average is ' + str(round(bl_sales_average/price,2)) + '× your price')
else:
	print('Error ' + str(response.status_code) + ': Could not get BrickLink sales average.')