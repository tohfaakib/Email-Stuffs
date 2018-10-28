from django.shortcuts import render

# Create your views here.

def email_collector(request):
    return render(request, 'email_collector/collector.html')


def collected_list(request):
    import time
    import math
    import re

    from selenium import webdriver
    from selenium.webdriver.firefox.options import Options
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.action_chains import ActionChains
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as ec

    start = time.time()

    niche = request.GET['keyword']

    option = Options()
    option.add_argument("--headless")

    driver = webdriver.Firefox(executable_path='F:\selenium\geckodriver.exe', firefox_options=option)

    driver.get('https://repl.it/@tohfaakib/googlemailfinder')

    WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.CLASS_NAME, "run-icon-svg"))).click()

    time.sleep(40)

    actions = ActionChains(driver)
    actions.send_keys(niche)
    actions.send_keys(Keys.ENTER)
    actions.perform()

    mail_list = []
    # abort = False

    def extractor():
        print("called...")
        html_doc = driver.page_source
        match = re.findall(r'[\w\.-]+@[\w\.-]+', html_doc)
        for i in match:
            if i[-1] == '.':
                i = i.replace(i[len(i) - 1], '')

                if i[-3:] == 'com' or i[-3:] == 'net' or i[
                                                         -3:] == 'org' or i[-3:] == 'edu' and i[-4] != '.':
                    i = list(i)
                    i.insert(-3, '.')
                    i = ''.join(i)

            valid = re.search(r'\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b', i,
                              re.I)

            if valid:
                i = i.lstrip("%&*-+)(^$#@")
                i = i.lower()

                # j = j + 1
                # print(j, ". ", i)

                while i not in mail_list:
                    mail_list.append(i)

        if mail_list == []:
            break_time = time.time()
            if break_time - start > 1120:
                mail_list.append("Time exceeded, try again later!")
            else:
                time.sleep(30)
                extractor()

    time.sleep(120)
    extractor()

    # for i in mail_list:
    #     j = j + 1
    #     print(j, ". ", i)

    driver.close()
    end = time.time()
    tot_sec = math.ceil(end - start + 2)
    print(tot_sec)
    sec = tot_sec % 60
    pro_sec = tot_sec - sec
    minute = pro_sec / 60

    times = str(minute) + " minute(s) and " + str(sec) + " second(s)"

    # print(len(mail_list), " email addresses collected in ", times)

    return render(request, 'email_collector/collected_list.html', {'email_list': mail_list})
