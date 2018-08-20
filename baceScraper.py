from selenium import webdriver
import csv

f = open('urls.txt', 'r')
urlList = f.readlines()
f.close()

driver = webdriver.Chrome()

for url in urlList:
    nodesList = []
    driver.get(url)
    stopCounter = driver.\
        find_element_by_xpath("//div/div/div/div/ul/li[last()]/a")
    stopCounter = int(stopCounter.get_property("href").split("p=")[1])
    
    for i in range(0, stopCounter):
        driver.get(url + "&p=" + str(i))
        nodesList = driver.\
            find_elements_by_xpath("//div[@class='row singlePublication']")
        linksList = driver.\
            find_elements_by_xpath("//span[@class='review']/a")

        for node in range(0,len(nodesList)):
                with open('database.csv', 'a', newline='',
                          encoding="utf-8") as csvfile:
                    writer = csv.writer(csvfile, quotechar='|', 
                        quoting=csv.QUOTE_MINIMAL)
                    splitNode = nodesList[node].text.replace(",", ";")\
                        .split("\n")
                    link = linksList[node].get_property("href")
                    linkId = link.split('#')[0].split('/')[4]
                    #row = splitNode[1].strip() 
                    #+ "," + splitNode[6].strip() + "," 
                    #+ splitNode[10].strip() + "," 
                    #+ splitNode[12].split(":")[1].strip() 
                    #+ "," + splitNode[13].split(":")[1].strip()  
                    #+ "," + splitNode[14].split(":")[1].strip()
                    row = [
                        linkId, 
                        splitNode[1].strip(), 
                        splitNode[6].strip(), 
                        splitNode[10].strip(), 
                        link
                    ]
                    writer.writerow(row)

#TO DO: Da se dobavi ID. 
#Proverka dali IDto na syotvetniq item go nqma ve4e 
#v kolonata ID predi da byde dobaveno vyv faila.
#koloni s datite