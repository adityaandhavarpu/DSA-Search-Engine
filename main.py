
import time

from selenium import webdriver
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())


page=1


cnt4=0;
cnt5=0;
all_urls=[]
all_titles=[]
while page !=47:
    driver.get("https://leetcode.com/problemset/all/?page="+str(page))
    time.sleep(5)
    html=driver.page_source
    soup=BeautifulSoup(html,'html.parser')
    all_ques_div=soup.findAll("div",{"class","odd:bg-layer-1"})
    all_ques=[]
    for ques in all_ques_div:
        all_ques.append(ques.findAll("div")[5].find("a"))
    urls=[]
    titles=[]
    for ques in all_ques:
        urls.append("https://www.leetcode.com"+ques['href'])
        all_urls.append("https://www.leetcode.com"+ques['href'])
        titles.append(ques.text)
        all_titles.append(ques.text)
    with open("./problems_url/problem_urls.txt", "w+") as f:
    	f.write('\n'.join(all_urls))
    with open("./problems_titles/problem_titles.txt", "w+") as f:
    	f.write('\n'.join(all_titles))
    if page>=0:
        cnt2=0;
        for url in urls:
            cnt4+=1
            driver.get(url)
            time.sleep(5)
            cnt2+=1
            html1 = driver.page_source
            soup1 = BeautifulSoup(html1, 'html.parser')
            temp1=soup1.find('div', {"class": "content__u3I1"})
            if temp1:
                problem_text_arr = temp1.findAll("div")[0].findAll("p")
                cnt1=1;
                for problem_text in problem_text_arr:
                    problem_text=problem_text.get_text()
                    problem_text = problem_text.encode('ascii',errors='ignore')
                    problem_text = str(problem_text)
                    if problem_text=="b''":
                        break;
                    problem_text=problem_text[2:len(problem_text)-1]
                    print(problem_text)
                    if cnt1==1:
                        with open("./problems/problem"+str(cnt4)+".txt","w+") as f:
                            f.write(problem_text)
                    else:
                        with open("./problems/problem"+str(cnt4)+".txt","a+") as f:
                            f.write('\n')
                            f.write(problem_text)
                    cnt1=cnt1+1
            else:
                with open("./problems/problem" + str(cnt4) + ".txt", "w+") as f:
                    f.write("*Premium_Problem* \n" + all_titles[cnt4 - 1])
    page = page + 1





