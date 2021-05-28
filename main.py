from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from xlwt import Workbook

web = webdriver.Chrome('C:/Users/arigo/Documents/Python Scripts/chromedriver.exe')

web.get('https://www.futhead.com/20/players/?level=all_nif&bin_platform=ps')


xpath = '/html/body/div[3]/div[3]/div[1]/div[1]/ul/li[4]/div/a'


li = 4
data = Workbook()
sheet1= data.add_sheet('Sheet1')

for x in range(10):
    for i in range(1, 49):
        modipath = '/html/body/div[3]/div[3]/div[1]/div[1]/ul/li[' + str(li) + ']/div/a'
        pacepath = '/html/body/div[3]/div[3]/div[1]/div[1]/ul/li[' + str(li) + ']/div/a/span[3]/span[1]'
        shootpath= '/html/body/div[3]/div[3]/div[1]/div[1]/ul/li[' + str(li) + ']/div/a/span[3]/span[2]'
        passpath = '/html/body/div[3]/div[3]/div[1]/div[1]/ul/li[' + str(li) + ']/div/a/span[3]/span[3]'
        dribblepath= '/html/body/div[3]/div[3]/div[1]/div[1]/ul/li[' + str(li) + ']/div/a/span[3]/span[4]'
        defencepath= '/html/body/div[3]/div[3]/div[1]/div[1]/ul/li[' + str(li) + ']/div/a/span[3]/span[5]'
        physicalpath= '/html/body/div[3]/div[3]/div[1]/div[1]/ul/li[' + str(li) + ']/div/a/span[3]/span[6]'



        li += 1
        #print(modipath)
        name = web.find_element_by_xpath(modipath)
        pace = web.find_element_by_xpath(pacepath).get_attribute('innerHTML')
        shoot = web.find_element_by_xpath(shootpath).get_attribute('innerHTML')
        pas = web.find_element_by_xpath(passpath).get_attribute('innerHTML')
        dribble = web.find_element_by_xpath(dribblepath).get_attribute('innerHTML')
        defence = web.find_element_by_xpath(defencepath).get_attribute('innerHTML')
        physical = web.find_element_by_xpath(physicalpath).get_attribute('innerHTML')
        ovr = name.text[0:2]
        buffer= name.text
        #print(buffer)
        player = ""
        position = ""

        for p in range(len(buffer)):
            if name.text[p] == "|":
                position = buffer[p-3:p]
                player = buffer[2:p-3]
                break

        PAC = pace[20:22]
        SHO = shoot[20:22]
        PAS = pas[20:22]
        DRI = dribble[20:22]
        DEF = defence[20:22]
        PHY = physical[20:22]
        #print(player, ovr, position)



        sheet1.write(x*49+i, 1, ovr)
        sheet1.write(x*49+i, 2, position)
        sheet1.write(x*49+i, 3, player)
        sheet1.write(x*49+i, 4, PAC)
        sheet1.write(x*49+i, 5, SHO)
        sheet1.write(x*49+i, 6, PAS)
        sheet1.write(x*49+i, 7, DRI)
        sheet1.write(x*49+i, 8, DEF)
        sheet1.write(x*49+i, 9, PHY)


    nextpage= web.find_element_by_xpath('/html/body/div[3]/div[3]/div[1]/div[1]/ul/li[52]/div/a[3]/span')
    nextpage.click()
    li = 4
    element = WebDriverWait(web, 10)


data.save('xlwt data.xls')
