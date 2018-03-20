#!/usr/bin/python2.6
import os,sys
import xlsxwriter
import re

workbook = xlsxwriter.Workbook('Data.xlsx')
worksheet = workbook.add_worksheet()


with open('/home/anakka/blossom/reetika/tinyLog','r') as file:
	data = file.readlines()
row = 0
col = 0
for i in range(len(data)):
	worksheet.write_row(i,col,data[i].split())
#print data[0].split()
workbook.close()
