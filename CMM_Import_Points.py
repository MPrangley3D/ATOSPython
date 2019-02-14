	# -*- coding: utf-8 -*-
	
#------------------------------------------------------------------------------------------
#                     [+] C M M   P O I N T   I M P O R T [+]
#------------------------------------------------------------------------------------------
#        Parses a .CSV for nominal & actual point data and pulls it into ATOS
# 
# Script by Matt Prangley - 6.13.2018
#------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------
#                        [+] V E R S I O N   C O N T R O L  [+]
#------------------------------------------------------------------------------------------
#        1.0 (6.13.2018) : Initial Release
#------------------------------------------------------------------------------------------

import gom
import csv

RESULT=gom.script.sys.execute_user_defined_dialog (content='<dialog>' \
' <title>Import Point CSV</title>' \
' <style></style>' \
' <control id="OkCancel"/>' \
' <position></position>' \
' <embedding></embedding>' \
' <sizemode></sizemode>' \
' <size height="321" width="271"/>' \
' <content rows="7" columns="2">' \
'  <widget rowspan="1" type="input::file" row="0" column="0" columnspan="2">' \
'   <name>file</name>' \
'   <tooltip></tooltip>' \
'   <type>any</type>' \
'   <title>Choose File</title>' \
'   <default></default>' \
'   <limited>false</limited>' \
'   <file_types/>' \
'   <file_types_default></file_types_default>' \
'  </widget>' \
'  <widget rowspan="1" type="label" row="1" column="0" columnspan="1">' \
'   <name>label</name>' \
'   <tooltip></tooltip>' \
'   <text>Search String</text>' \
'   <word_wrap>false</word_wrap>' \
'  </widget>' \
'  <widget rowspan="1" type="input::string" row="1" column="1" columnspan="1">' \
'   <name>srcString</name>' \
'   <tooltip></tooltip>' \
'   <value>POINT</value>' \
'   <read_only>false</read_only>' \
'  </widget>' \
'  <widget rowspan="1" type="label" row="2" column="0" columnspan="1">' \
'   <name>label_4</name>' \
'   <tooltip></tooltip>' \
'   <text>Search Column</text>' \
'   <word_wrap>false</word_wrap>' \
'  </widget>' \
'  <widget rowspan="1" type="input::integer" row="2" column="1" columnspan="1">' \
'   <name>typeCol</name>' \
'   <tooltip></tooltip>' \
'   <value>1</value>' \
'   <minimum>0</minimum>' \
'   <maximum>1000</maximum>' \
'  </widget>' \
'  <widget rowspan="1" type="label" row="3" column="0" columnspan="1">' \
'   <name>label_1</name>' \
'   <tooltip></tooltip>' \
'   <text>XYZ Column</text>' \
'   <word_wrap>false</word_wrap>' \
'  </widget>' \
'  <widget rowspan="1" type="input::integer" row="3" column="1" columnspan="1">' \
'   <name>xyzCol</name>' \
'   <tooltip></tooltip>' \
'   <value>0</value>' \
'   <minimum>0</minimum>' \
'   <maximum>1000</maximum>' \
'  </widget>' \
'  <widget rowspan="1" type="label" row="4" column="0" columnspan="1">' \
'   <name>label_2</name>' \
'   <tooltip></tooltip>' \
'   <text>Nominal Column</text>' \
'   <word_wrap>false</word_wrap>' \
'  </widget>' \
'  <widget rowspan="1" type="input::integer" row="4" column="1" columnspan="1">' \
'   <name>nomCol</name>' \
'   <tooltip></tooltip>' \
'   <value>2</value>' \
'   <minimum>0</minimum>' \
'   <maximum>1000</maximum>' \
'  </widget>' \
'  <widget rowspan="1" type="label" row="5" column="0" columnspan="1">' \
'   <name>label_3</name>' \
'   <tooltip></tooltip>' \
'   <text>ActualColumn</text>' \
'   <word_wrap>false</word_wrap>' \
'  </widget>' \
'  <widget rowspan="1" type="input::integer" row="5" column="1" columnspan="1">' \
'   <name>actCol</name>' \
'   <tooltip></tooltip>' \
'   <value>1</value>' \
'   <minimum>0</minimum>' \
'   <maximum>1000</maximum>' \
'  </widget>' \
'  <widget rowspan="1" type="label" row="6" column="0" columnspan="1">' \
'   <name>label_5</name>' \
'   <tooltip></tooltip>' \
'   <text>Feature Name</text>' \
'   <word_wrap>false</word_wrap>' \
'  </widget>' \
'  <widget rowspan="1" type="input::integer" row="6" column="1" columnspan="1">' \
'   <name>nameCol</name>' \
'   <tooltip></tooltip>' \
'   <value>2</value>' \
'   <minimum>0</minimum>' \
'   <maximum>1000</maximum>' \
'  </widget>' \
' </content>' \
'</dialog>')

srcString = RESULT.srcString
xyzCol = RESULT.xyzCol
nomCol = RESULT.nomCol
actCol = RESULT.actCol
typeCol = RESULT.typeCol
nameCol = RESULT.nameCol
print(nameCol)

actArray = []
nomArray = []

def BuildABear(name,aX,aY,aZ,nX,nY,nZ):
	actual = name,aX,aY,aZ
	actArray.append(actual)
	nominal = name,nX,nY,nZ
	nomArray.append(nominal)

with open(RESULT.file,'r') as csvfile:
	spamreader = csv.reader(csvfile)
	log = False
	rowName = ''
	rowXNOM = ''
	rowYNOM = ''
	rowZNOM = ''
	rowXACT = ''
	rowYACT = ''
	rowZACT = ''
	for row in spamreader:
		print(row)
		if srcString in row[typeCol]:
			log = True
			print(nameCol)
			rowName = row[nameCol]		
		if 'X' in row[xyzCol] and log == True:
			print('log x')
			rowXNOM = row[nomCol]
			rowXACT = row[actCol]		
		if 'Y' in row[xyzCol] and log == True:
			print('log y')
			rowYNOM = row[nomCol]
			rowYACT = row[actCol]	
		if 'Z' in row[xyzCol] and log == True:
			print('log z')
			rowZNOM = row[nomCol]
			rowZACT = row[actCol]
			BuildABear(rowName, rowXACT, rowYACT, rowZACT, rowXNOM, rowYNOM, rowZNOM)
			log = False

for a in actArray:
	try:
		print('Making ACTUAL: '+a[0])
		MCAD_ELEMENT=gom.script.primitive.create_point (name='CMM-act_'+a[0], point={'point': gom.Vec3d (a[1], a[2], a[3])},properties=gom.Binary ('eAHNV0tsG1UUvS6lBEMIqcpHiM8oDRA+zqeEFqYpDSUpESIBQVSqSmA5nok9YI/d8QTHRYWp2CB2LBA7VPERi0iVKoEqVgghJBYorECIHWKDBFJQN0gsGs55z8+ecey0XSDh0Xiu37vv3N95940XK+XMsUdHV2Vu9smZ2RdkMch5Yc22Z0tu2fXD54NK1Q1Cz62J/qRkp/SnJS39ku7H0MKFj04U8Xz6uXnrxcpyWM8FrrVvfOKANVcJl71V6xG9bn2tTyimcE9/dpcarJ7d2Nihp3t8p3Zj4sPP19dSciekG0UiRzypSVVKkpOGZCF7ckpcOX1sfW2H3AGtG6A1k9Cal4o40DnxoEG6HXqUb8LzWujXpAy8Eq7vXt6YNFq052LMxWxW8kAp43LFl1A+naa9m7F+l1ofSgCbvhRk5Geu34kZfCJJ8detEK9PoNWkCLy6/PYBcWCJK6IljFVg8ZVzXMVkpaJ3KA5BHEgA0GBOXoU7ebhTwa+GfP/F9mAS9RFsH8BuS4CtII8uYlxWQFkVCbOswT2M+jL4xxWBDwMcaYlYoCUAlAC7BDkvryE5AaBWAObIhQzhFqB9L7QXMV4WG9dRGC/ARcrPtjCOQKKLHKXcifYU1pdwB3LmW4Y4Alx6Qht9eDY/UbFzBJruJ2YF6NbhNxFJnaBJAG1j/gfimqIWlO+j0vZh4jgRSV4SjDKKy8/m4TMf38/f9+HH4LbWykCl5bcO0xYJm4b+ERWj9sjQekBZIPXpEdENnXxo+8DIXnzzS44/hnnoJWIkrX2lZXiURSZJZRKiDskBv4pyahf9sICAmCLGmlz1Ukvzx79pixv28tvMxBVnC0nILXbpLC3uAQ4qGJksH23Ovvc+rcxhdgY3ZRvPW1qabA0N3CHi4PbtZgELWp9zfw7cQ5RxjCCPiRwZ3lZVXgpAYxMgv9kcHLn4FT01We+5iZ8B9N7LQtewUTzsPe4+B6aKeOYUFUhCU5qanPwpbnRFuRbK8fMMokk3mVbdp1uSTf+51Iij9HTdguusezyLOrO6FVM+P0ao3i3R5GcB4bCNZn+hq92cI9oqKrf5z/aIu9F7r7tGoikkKQRmSZ4QyjphlGknhD1LtW+ySrfvQ+ioE7gtVUdqceQk9rkHTaJpD4ZkTGGSRw1VbUtJLA5XGL0xrKrhGoJ2Gq3eUldVHsaTJbPkDdx1IHtqTQa6VfiVB46NmSosu5KBBrt6VQ5i7HQLaQpetD1gXGOJKFk2B/5ZMS16Z3YScV1YLqjIbJkEy8eVjbZGG99GTtj39JF4UMU0Ba8N35lL9vVSKwZ98NFipplVo8EYHVxtjXFoWdg5BaCYns2Ve+Ft+6JO2yPOM0bTizOxtTZW5hGNuZm5pG4bxwYmbbKnUY8RBvCE3mUQYQWZt4FVBfu2zhM1VFo8qXppsSMsQ6u3BjlmKmFQdE7aETJi8pO15kmvn86WrLwOawE0yFq+wGTUN/F9eFBWkToYd1U8yWpk1Lj2dbLrfNJTZqQToZ2zbrOdGTNc0tz3t0RzpWwcVvHylMDpjVqxBzF3+pzmTuX+zCIXfNPgSUD2cq8+gLcCvZsYia/yOoYZ53+Q4e41+K8ynOwI+8Hnq+sIw6q76C4RopIjyKbu6+x5Q/KQ4i9lc9Rk1Zsf+98hrCVb+Ua3fUVYG81+SqYD6Q5IdrHrmX5oToDVb3iu3I0TC/9QoviJpXcL/zKQO/n98aNv6wGaAsL0YPyMYpf2sKv0nwHNuV8fJ8pVvwu++/vmnq/fPkD0Udjhe0u3N/osIuSJUIdNvkXrrjvzV9xz5iH5pwHv+f8C1xqnPAHZow=='))
		gom.script.cad.convert_to_actual_element (elements=[gom.app.project.inspection['CMM-act_'+a[0]]])
	except:
		print('ACTUAL: '+a[0]+' Already Exists!')

for n in nomArray:
	try:
		print('Making NOMINAL: '+n[0])
		MCAD_ELEMENT=gom.script.primitive.create_point (name='CMM-nom_'+n[0], point={'point': gom.Vec3d (n[1], n[2], n[3])},properties=gom.Binary ('eAHNV0tsG0UY/l1KCYYQUpWHEI9VGiA8HCclpLBNaShJiRApCKJSVQLL8W7sBXvtrjc4LipsxQVxggPiCOIhDpEq9YAqTgghJA4ocAEhbogLEkhBvSBxaPi+GY/Xm9hpe0BiV+udnfnn+1/f/DNeqFYyxx4eXZG52cdnZp+ThSDvhXXbni27FdcPnw2qNTcIPbcu+krJTulPS1r6Jd2PrsnzH50o4f3kM/PW89WlsJEPXGvf2Ph+a64aLnkr1kN63tpqn7CZwjP92R2q84d31td36OEev6ndGPhgYm01Jbejdb1I5IgndalJWfLSlBzanpwSV04fW1vdIbdB6jpIzSSk5qUqDmRO3G+QboUc2zfgfTXk61IBXhn3ty+uJ/S56HMxmpMCUCq4XfEllE+nqe9GzN+l5ocSQKcvRRn5mcg7MYIrkhS/bkbzWnzFaHUpAa8hv71PHHjGGdEi+qrQ+NJZzmKwUtFbbA6hOZAAoMK8vAxzCjCniq+mfPf59mAS9RFsH8BuSYAtI44ufFxSQDnlCaOswT30+jL4x2WBDwMcYYmYoEUAlAG7iHZBXkFwAkAtA8yR8xnCHYX03ZBeQH9FbNxHoLwIE9l+uo1xGC2ayF62N6M9gfllPIGc+YYujgCXllBHH96tKypt7oGk+4mZAbptspuIpE7QIoDWMf89cU1Si8r2UYltGD9ORJKXBGMbyeW1cejMx/fy+x58DG6rrQJUan7jEHWRsGnIH1Y+aosMrQeUBlKfFhHd0MmHtA+M3IXXv2D/IxiHXMJH0tpXUoZHOUSSVCYhGmg54FdJTu2iHRYQ4FNEX5OzXmhL/vg3dXHBXnqZGb862UIScold/JAa9wAHGYxMlI+0Rt99j1rmMDqDh20b75vakiwNTTwh/ODy7aYBE9rX2T8H7iLKGHoQx0SMDG9rKi5FoLEIkN8sDo5c+JKWmqj3XMRPAXrvJaHrWCge1h5XnwNVJbzzigokoUlNXU7+1Kl0WZkWyvFzdKJFN5lW1adbkE39udjsROlpugXTmffOKOrI6lLM9rksoXqXRBOfo3CHZTT3C03tZhzRVpC5jX+2R9yN2nvNVRJNIUghMMvymLCtA8Y29YTQZ6nyTVbp8n0QFXUcj6XySCn2nMQ69yBJNG3BkGQVJnnUVNm2VIvJ4Qwjl8WsOu4hSKdR6i111+RBvJkyS17D0wCyp+ZkIFuDXQXg2BipQbMrGUiwqtfkAPpOt5GmYEVsAf3KJrxk2hzYZ3VI0TqzkojrQnNReWbLBFg+pnTEEjG+jZiw7ukt8YDyaQpWG74zlqzr5bYPeuOjxkwrqkaCPjq4Y4kxSFlYOUWgmJrNmXthbXxTJraI4/TR1OJMx1wbMwvwxjyMXFI2xrGBSZ2saZSjhwEsoXUZeFhF5G1g1cC+reNEDZUUd6peUqwIS5DqLUGOmUwYFB2T2EN6TH4y19zp9dvZEpVXoS2ABFnLA0xG/RLfhwUV5amDflf5k8xGRvVrWye6jictZUQ2I8Qx6za6OWKGS5r7/hZvLpeNw8pf7hLYvZEr1iDGTu/TXKlcnznEgicN7gRkL9fqfTgV6NVET3wV1yxGnP9BhLvn4L+KcLIiTILPV1YRhlV10VUiRCZHEE1d11nzhuQBxV+2zVaTUyc/1r+DmEu28kS3fUaYG81+tkwF0hWQ7GLVM/XQ7AArX3NfuRM7Fv6hRJ07ll4t/MtA7hQmO7e+rRtoCgjTg517FKu0h1Wl/wxozv36KFGu+Cz49u8be756cz/RR6GH55ZuJ/ocPOSO0IBOnqJ11Z35q9NyxiH5pwHn/H8BMGum9QFAAw=='))
		gom.script.inspection.link_to_actual_element (actual_element=gom.app.project.actual_elements['CMM-act_'+n[0]],elements=[gom.app.project.inspection['CMM-nom_'+n[0]]])
	except:
		print('NOMINAL: '+n[0]+' Already Exists!')
