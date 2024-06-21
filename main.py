# from flask import Flask, request, jsonify

# app = Flask(__name__)

# @app.route("/")
# def home():
#     return "Home"

# if __name__ == "__main__":
#     app.run(debug=True)


import pandas, random

# Limit
limit = 1000

# Index
index = int(open('index.txt').read())
# print(index)
random.seed(index)

# Names
names_obj = pandas.read_csv('us_people_names.csv')
# print(names_obj.head()['name'])
half_int = int(names_obj.count()['name']/2)
firstname = names_obj.iloc[0:limit]['name'][index]
middlenames = names_obj.iloc[half_int:half_int+limit]['name']
middlenames.reset_index(drop=True, inplace=True)
middlename = middlenames[index]
# print(middlename)
lastname = str.capitalize(pandas.read_csv('surnames.csv')['name'][index])

# Addresses
address = pandas.read_csv('addresses.csv')['address'][index]
# print(address)

# Gender
gender = names_obj.iloc[0:limit]['gender'][index]
if gender=='M':
    gender='1'
else:
    gender='2'
# print(gender.head())

# Email
email = firstname+str.capitalize(lastname)+'@gmail.com'
# print(email)

# Mobile Number
mobile = str(random.randint(10000000000, 99999999999))
# print(mobile)

# Phone Number
phone = str(random.randint(10000000, 99999999))

# Company EmployeeID
employeeId = str(random.randint(100000, 999999))

# Payroll Type SemiMonthlyPayroll=0 MonthlyPayroll=1 WeeklyPayroll=2
payrollType = str(random.randint(0, 2))

# Employee Status
employeeStatus = str(random.randint(1, 6))

# Birthdate format mm/dd/yyyy
mm = random.randint(1,12)
if mm < 10:
    mm = '0'+str(mm)
else:
    mm = str(mm)
dd = random.randint(1, 30)
if dd < 10:
    dd = '0'+str(dd)
else:
    dd = str(dd)
birthdate = str(random.randint(1980, 2000))+'-'+mm+'-'+dd

# Date hired
hired_month = random.randint(1,12)
if hired_month < 10:
    hired_month = '0'+str(hired_month)
else:
    hired_month = str(hired_month)
hired_day = random.randint(1, 30)
if hired_day < 10:
    hired_day = '0'+str(hired_day)
else:
    hired_day = str(hired_day)
dateHired = str(random.randint(2000, 2024))+'-'+hired_month+'-'+hired_day

# Department ID
departmentId = random.randint(7, 19)
if departmentId==18:
    departmentId=str(19)
elif departmentId==11:
    departmentId=str(19)
elif departmentId==16:
    departmentId=str(19)
elif departmentId==8:
    departmentId=str(19)
else:
    departmentId=str(departmentId)

# Religion ID
religionId = str(random.randint(1, 3))

# Civil Status
civilStatus = str(random.randint(0, 3))

# print(firstnames.head()['name'])
# print(middlenames.head()['name'])
# print(surnames.head()['name'])

# print(random.randint(0, 5))


# document.getElementById('firstName').value = 'John'
# document.getElementById('middleName').value = 'Cris'
# document.getElementById('lastName').value = 'Young'
# document.getElementById('nickName').value = 'John'
# document.getElementById('placeOfBirth').value = '4214 Romano Street Boston, MA 02199'
# document.getElementById('gender').value = '1'  //'1'=Male '2'=Female
# document.getElementById('emailAddress').value = 'JamesLBlank@rhyta.com'
# document.getElementById('mobileNumber').value = '78174106009'
# document.getElementById('phoneNumber').value = '84657'
# document.getElementById('cityAddress').value = '4214 Romano Street Boston, MA 02199'
# document.getElementById('nationalityId').value = '1'
# document.getElementById('religionId').value = '1' 
# document.getElementById('civilStatus').value = '0'
# document.getElementById('provincialAddress').value = 'US'
# document.getElementById('companyEmployeeId').value = '76457'
# document.getElementById('employeeStatus').value = '1'
# document.getElementById('departmentId').value =  '19'
# document.getElementById('dateHired').value = '2024-06-20'
# document.getElementById('dateHired').classList.remove('is-invalid')
# document.getElementById('dateHired').classList.add('is-valid')
# document.getElementById('payrollType').value = '1' 
# document.getElementById('payrollType').classList.remove('is-invalid')
# document.getElementById('payrollType').classList.add('is-valid')
# document.getElementById('tinNumber').value = '24554'

print("document.getElementById('firstName').value = '"+firstname+"'")
print("document.getElementById('middleName').value = '"+middlename+"'")
print("document.getElementById('lastName').value = '"+lastname+"'")
print("document.getElementById('nickName').value = '"+firstname+"'")
print("document.getElementById('placeOfBirth').value = '"+address+"'")
print("document.getElementById('gender').value = '"+gender+"'")
print("document.getElementById('emailAddress').value = '"+email+"'")
print("document.getElementById('mobileNumber').value = '"+mobile+"'")
print("document.getElementById('phoneNumber').value = '"+phone+"'")
print("document.getElementById('cityAddress').value = '"+address+"'")
print("document.getElementById('nationalityId').value = '1'")
print("document.getElementById('religionId').value = '"+religionId+"'")
print("document.getElementById('civilStatus').value = '"+civilStatus+"'")
print("document.getElementById('provincialAddress').value = 'US'")
print("document.getElementById('companyEmployeeId').value = '"+employeeId+"'")
print("document.getElementById('employeeStatus').value = '"+employeeStatus+"'")
print("document.getElementById('departmentId').value = '"+departmentId+"'")
print("document.getElementById('dateHired').value = '2024-06-20'")
print("document.getElementById('dateHired').classList.remove('is-invalid')")
print("document.getElementById('dateHired').classList.add('is-valid')")
print("document.getElementById('payrollType').value = '"+payrollType+"'")
print("document.getElementById('payrollType').classList.remove('is-invalid')")
print("document.getElementById('payrollType').classList.add('is-valid')")
print("document.getElementById('dateOfBirth').value = '"+birthdate+"'")
print("document.getElementById('dateHired').value = '"+dateHired+"'")
print("document.getElementById('businessUnitId').value = '1'")
print("var option = document.createElement('option')")
print("option.value = '1'")
print("option.textContent = 'CS Go III'")
print("document.getElementById('branchId').appendChild(option)")
print("document.getElementById('branchId').value = '1'")
print("document.getElementById('positionId').value = '8'")

index+=1
index_object = open('index.txt' ,mode='w')
index_object.write(str(index))