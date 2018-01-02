import bs4 as bs
import re
from htmlparser import MLStripper
from read_html1 import htmlcon
from read_html1 import strip_tags
from read_csvfile import Index_Url
import numpy as np
import pandas as pd

csvfile1 = r'ori_example1.csv'
csvfile2 = Index_Url(csvfile1)
csvfile = csvfile2.sort_indexurl()


sorted_url = []
for url in csvfile:
	if "nan" in url:
		url = "0" 
	sorted_url.append(url)

results = []

def main_function():
	for i in range(len(sorted_url)):
		html2 = sorted_url[i]
		if html2 == "0":
			results.append('0')
			results.append('0')
		else:
			H = htmlcon(html2)
			Hold = H.read_html1().decode("utf-8")

			Hnew1 = strip_tags(Hold)
			Hnew = re.split("\n+", Hnew1)
			words = []
			lines = [line.strip() for line in Hnew]

			for line in lines:
				for word in line.split(" "):
					words.append(word)
			
			'''extract the SIC code'''
			for i in [i for i,x in enumerate(words) if x == "Film"]:
				result1 = words[i+3]
				results.append(str(result1))
			
			'''extract the state of INC.'''
			for t in [t for t,m in enumerate(words) if m == "Act:"]:
				result2 = words[t-9]			
				results.append(str(result2))
			
	return results

SIC = []
state_of_INC = []

for i in range(len(main_function())):
	if i%2 == 1:
		state_of_INC.append(main_function()[i])
	else:
		SIC.append(main_function()[i])
	print(i)

fin_result = pd.DataFrame(
	{'SIC': SIC,
	'state_of_INC': state_of_INC
	})

print(fin_result)

'''
fin_result.to_csv('example1.csv')
'''


