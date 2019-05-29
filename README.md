# verintex
For Verint exersice

The gethw.py reads the howerly weather page for Tel Aviv, from waether.com and transform the 
weather data table intpo a json (and prints the json).
The script uses BeautifulSoup to extract the weather table columns and then uses the zip() function to 
transpose the data so that it can iterate over the rows for each hour and build a dictionary that is 
finally encoded in json and printed

Python 3.6.7

Using bs4 (BeautifulSoup) , json , urllib
