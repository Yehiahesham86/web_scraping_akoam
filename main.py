import csv
from bs4 import BeautifulSoup
import requests


def main():
    eps_link = input("pls Enter first Eps link : ")
    number_of_esp = input("Enter Number of Episodes : ")
    download_links = []
    x=1
    try:
        for x in range(int(number_of_esp)):
            page = requests.get(eps_link)
            src = page.content
            soup = BeautifulSoup(src, "lxml")
            episode_link = soup.findAll("div", {'class': 'qualities'})
            episode_name = soup.find("h1", {'class': 'entry-title'}).text.strip()
            links = episode_link[2].find_all('a')[1]['href']
            #################################################################################
            page1 = requests.get(links)
            src1 = page1.content
            soup1 = BeautifulSoup(src1, "lxml")
            ad_page = soup1.findAll("a", {'class': 'download-link'})[0]["href"]
            #################################################################################
            page2 = requests.get(ad_page)
            src2 = page2.content
            soup2 = BeautifulSoup(src2, "lxml")
            btn_download = soup2.findAll("a", {'class': 'btn-light'})[0]["href"]
            print(btn_download)
            download_links.append({"Episode Number": x+1, "Episode Name": episode_name, "Link": btn_download})
            ##################################################################################
            page3 = requests.get(eps_link)
            src3 = page3.content
            soup3 = BeautifulSoup(src3, "lxml")
            next_eps = soup3.findAll("a", {'class': 'justify-content-md-end'})[0]["href"]
            eps_link = next_eps
            ###################################################################################
    except:

        keys = download_links[0].keys()
        with open("C:/Users/Yehia/Desktop/Episode_links.csv", 'w', encoding='utf-8-sig') as output_file:
            dict_writer = csv.DictWriter(output_file, keys)
            dict_writer.writeheader()
            dict_writer.writerows(download_links)
        output_file.close()


main()
