import re;

def extractCourse():

	#basic file open and read operation
	f1 = open("hofstra.html", "r");
	#converted to string, will be used in finadall method
	s1=f1.read();
	f1.close();

	#making an object, items to include in string
	p1= re.compile("<tr id=\"section_row\">.*?</tr>", re.MULTILINE | re.DOTALL);

	#making an array of items to include from string
	arr=p1.findall(s1)
	#print(arr);

	arrNew= [];

	for StringElement in arr:
		#specify more parameters
		p2 = re.compile("<td.*?>(.*?)</td>", re.MULTILINE | re.DOTALL);
		#run pattern
		arrTDs = p2.findall(StringElement);

		#remove spaces
		if arrTDs[2].find("&nbsp;")==-1:
			arrNew.append(StringElement)
	#print(arrNew)
	return arrNew
print("Number of Courses: " + str(len(extractCourse())));

def extractMajors(arr):
	arrNew=[];
	majorLst = [];

	#getting the majors
	for x in arr:
		p3= re.compile("<td.*?>(.*?)</td>", re.MULTILINE | re.DOTALL);
		arr2 = p3.findall(x);
		arrNew.append(arr2[2]);

	#only showing part of the string array for major codes
	#for y in arrNew:
	#	majorLst.append(y[22:26])
	#above code no longer needed since () was missing from regex function
	return arrNew

def getSet(arr):
	arrRet=[];
	for x in arr:
		if not(x in arrRet):
			arrRet.append(x)
	return arrRet;

arrSections= extractCourse();
arrMajors = extractMajors(arrSections);
print(getSet(arrMajors) );
print("Number of Majors: " + str(len(getSet(arrMajors))) );


def Income(arr):
	income = 0.0;
	#getting the credits
	for credits in arr:
		exp3= re.compile("<td .*?>(.*?)</td>", re.MULTILINE | re.DOTALL);

		#define new array containing string array of credits
		arrStringCredits = exp3.findall(credits);
		#income formula and array index conversion ot floats
		income += float(arrStringCredits[6]) * float(arrStringCredits[11]) * 1380
	return income;


wholeArray = extractCourse();
HofstraIncome = Income(wholeArray)
print("Hofstra income is: $" + str(HofstraIncome))
