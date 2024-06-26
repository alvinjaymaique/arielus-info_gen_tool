import pandas, random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException, NoSuchWindowException
import keyboard

try:
    driver = webdriver.Edge()
    driver.get("http://arielus:10007/HumanResource/People")

    def close_browser():
        driver.quit()

    keyboard.add_hotkey('space', close_browser)
    try:
        username = driver.find_element(By.ID, "username")
        username.clear()
        username.send_keys("rrmula")

        password = driver.find_element(By.ID, "password")
        password.clear()
        password.send_keys("rrmula")

        driver.implicitly_wait(15)

        btnLogin = driver.find_element(By.ID, "btnLogin")
        btnLogin.click()

        humanResourceButton = driver.find_element(By.CSS_SELECTOR, "#kt_body > div.container-fluid.mt-20 > div > div > div:nth-child(5) > a")
        humanResourceButton.click()

        driver.implicitly_wait(10)
        burger = driver.find_element(By.ID, "kt_aside_mobile_toggle")
        burger.click()

        people = driver.find_element(By.ID, "sideMenu-people")
        people.click()

        driver.implicitly_wait(10)
        createEmployee = driver.find_element(By.CSS_SELECTOR, "#kt_wrapper > div.bodyContainer.content.d-flex.flex-column.flex-column-fluid > div.container-fluid > div > div > div.form-group.row.d-flex.justify-content-between > div:nth-child(1) > button")
        createEmployee.click()

        agreeCreateEmployee = driver.find_element(By.ID, "agreeCreateEmployee")
        agreeCreateEmployee.click()
    except:
        pass

    # Limit
    limit = 2000
    # Index
    index = int(open('index.txt').read())
    # Target
    target = index+100
    while index<=target:
        try:  
            # Interrupt
            if keyboard.is_pressed('space'):
                break
            # print(index)
            random.seed(index)
            print('Inside while loop')
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

            # Nationality ID
            nationalityId = random.randint(1, 13)
            if nationalityId!=1 or nationalityId!=2 or nationalityId!=11 or nationalityId!=13:
                nationalityId='1'
            else:
                nationalityId=str(nationalityId)

            # Religion ID
            religionId = str(random.randint(1, 3))

            # Civil Status
            civilStatus = str(random.randint(0, 3))
        
            
            try: 
                createEmployee = driver.find_element(By.CSS_SELECTOR, "#kt_wrapper > div.bodyContainer.content.d-flex.flex-column.flex-column-fluid > div.container-fluid > div > div > div.form-group.row.d-flex.justify-content-between > div:nth-child(1) > button")
                createEmployee.click()
                
                agreeCreateEmployee = driver.find_element(By.ID, "agreeCreateEmployee")
                agreeCreateEmployee.click()
            except:
                print('No Create employee button')

            driver.execute_script("document.getElementById('firstName').value = '"+firstname+"'")
            driver.execute_script("document.getElementById('middleName').value = '"+middlename+"'")
            driver.execute_script("document.getElementById('lastName').value = '"+lastname+"'")
            driver.execute_script("document.getElementById('nickName').value = '"+firstname+"'")
            driver.execute_script("document.getElementById('placeOfBirth').value = '"+address+"'")
            driver.execute_script("document.getElementById('gender').value = '"+gender+"'")
            driver.execute_script("document.getElementById('emailAddress').value = '"+email+"'")
            driver.execute_script("document.getElementById('mobileNumber').value = '"+mobile+"'")
            driver.execute_script("document.getElementById('phoneNumber').value = '"+phone+"'")
            driver.execute_script("document.getElementById('cityAddress').value = '"+address+"'")
            driver.execute_script("document.getElementById('nationalityId').value = '"+nationalityId+"'")
            driver.execute_script("document.getElementById('religionId').value = '"+religionId+"'")
            driver.execute_script("document.getElementById('civilStatus').value = '"+civilStatus+"'")
            driver.execute_script("document.getElementById('provincialAddress').value = 'US'")
            driver.execute_script("document.getElementById('companyEmployeeId').value = '"+employeeId+"'")
            driver.execute_script("document.getElementById('employeeStatus').value = '"+employeeStatus+"'")
            driver.execute_script("document.getElementById('departmentId').value = '"+departmentId+"'")
            driver.execute_script("document.getElementById('dateHired').value = '2024-06-20'")
            driver.execute_script("document.getElementById('dateHired').classList.remove('is-invalid')")
            driver.execute_script("document.getElementById('dateHired').classList.add('is-valid')")
            driver.execute_script("document.getElementById('payrollType').value = '"+payrollType+"'")
            driver.execute_script("document.getElementById('payrollType').classList.remove('is-invalid')")
            driver.execute_script("document.getElementById('payrollType').classList.add('is-valid')")
            driver.execute_script("document.getElementById('dateOfBirth').value = '"+birthdate+"'")
            driver.execute_script("document.getElementById('dateHired').value = '"+dateHired+"'")
            driver.execute_script("document.getElementById('businessUnitId').value = '1'")
            script = """
                var option = document.createElement('option');
                option.value = '1';
                option.textContent = 'CS Go III';
                document.getElementById('branchId').appendChild(option);
                document.getElementById('branchId').value = '1';
                """
            driver.execute_script(script)
            driver.execute_script("document.getElementById('positionId').value = '8'")

            btnCreate = driver.find_element(By.ID, "btnCreatePeople")
            btnCreate.click()
            index+=1

            with open('index.txt', 'w') as index_object:
                index_object.write(str(index))
                print(f'Index {index} saved to index.txt')
        except Exception as e:
            print(f'Browser was closed: {e}')
            break
    driver.close()

except Exception as e:
    print(f'Exitting...')
finally:
    driver.quit()

# 130