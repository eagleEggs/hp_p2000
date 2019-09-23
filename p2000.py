def web_p2000(self, url, uname, pword):
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options,
                               executable_path='geckodriver.exe')
    driver.get(url)

    un = driver.find_element_by_css_selector('#username')
    pw = driver.find_element_by_css_selector('#password')
    un.send_keys(uname)
    pw.send_keys(pword)
    pw.send_keys(Keys.ENTER)

    general_info = WebDriverWait(driver, 1).until(
            ec.presence_of_element_located((
                By.CSS_SELECTOR, '.contentFillContainer > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > div:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > div:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > div:nth-child(1) > table:nth-child(1)')))
    critical_count = driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[1]/div[1]/div[2]/div/div/table[2]/tbody/tr/td[3]/a')
    health = driver.find_element_by_xpath('/html/body/div[1]/div/div['
                                          '3]/div[3]/div[2]/div/div/div/div/div[5]/div/div[2]/div/div/div/div/table/tbody/tr[2]/td/div/table/tbody/tr[1]/td/div/table/tbody/tr[2]/td/div/table/tbody/tr[2]/td[2]/div/nobr/div/span')
    health_detail = driver.find_element_by_xpath('/html/body/div['
                                                '1]/div/div[3]/div['
                                      '3]/div[2]/div/div/div/div/div[5]/div/div[2]/div/div/div/div/table/tbody/tr[2]/td/div/table/tbody/tr[1]/td/div/table/tbody/tr[2]/td/div/table/tbody/tr[3]/td[2]/div/nobr')

    print("Criticals: {}".format(critical_count.text))
    print("Health: {}".format(health.text))

    # Front Tabular:
    driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div['
                                 '1]/div[2]/div[2]/div/div['
                                 '2]/div/div/ul/li/ul/li[2]/ul/li/div['
                                 '2]').click()
    sleep(1)
    driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div['
                                 '3]/div[2]/div/div/div/div/div['
                                 '5]/div/div['
                                 '2]/div/div/div/div/table/tbody/tr['
                                 '2]/td/div/div/ul/li[2]/a/div/div').click()
    sleep(1)
    front_tabular = driver.find_element_by_css_selector('.rackTable > table:nth-child(1) > tbody:nth-child(2)')
    front_tabular_list = []

    print("Disks: ", front_tabular.text)
        
        
 web_p2000("http://127.0.0.1", "username", "password")
