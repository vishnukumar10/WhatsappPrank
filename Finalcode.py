from selenium import webdriver
import PyPDF2
#Selenium is for accessing Whatsapp and PyPDF is for scrapping PDF files

pdfFile="TheSocialNetwork.pdf"

#This splits the sentences in arrays and is done pagewise 
def convert(lst): 
         return (lst.split()) 

pdfRead = PyPDF2.PdfFileReader(pdfFile)

driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')

all_names = ['Richa','Akash']
#The First Person is sent all the message and then the next one

input('Enter anything after scanning QR code')

for name in all_names:
    user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
    user.click()

    msg_box = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')[0]
    
    for i in range(1,pdfRead.getNumPages()):
        page = pdfRead.getPage(i)
        pageContent = page.extractText()
        Content = convert(pageContent)
        #Another loop to send the Split Array word by word
        for x in range(len(Content)):
            msg_box.send_keys(Content[x])
            button = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')[0]
            button.click()
