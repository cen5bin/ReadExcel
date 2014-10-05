import xlrd
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

data = xlrd.open_workbook('test.xlsx')
table = data.sheets()[0]
colnum = table.ncols
rownum = table.nrows

ret = {}
for i in range(1, rownum):
	ret[table.cell(i,0).value] = {}
for i in range(1, colnum):
	for j in range(1, rownum):
		v = str(table.cell(j, i).value)
		if v == '' or v == ' ':
			v = '-1'
		ret[table.cell(j, 0).value][str(int(table.cell(0, i).value))] = v

print '{'
cnt1 = 0
for (k, v) in ret.items():
	if cnt1 > 0 :
		print ','
	cnt1+=1
	print '"'+k+'":{',
	cnt = 0
	for (k1, v1) in v.items():
		if cnt > 0 : 
			print ',',
		print '"' + str(k1) + '":' + v1,
		cnt+=1
	print '}'
print '}'

#print ret

