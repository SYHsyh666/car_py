#import time
import requests
import multiprocessing

headers3 = {
  'Accept':
  'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
  'Accept-Encoding':
  'gzip, deflate, br',
  'Accept-Language':
  'zh-CN,zh;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6,ja;q=0.5',
  'Cache-Control':
  'max-age=0',
  'Referer':
  'https://www.hpacademy.com/',
  'Connection':
  'keep-alive',
  'Sec-Fetch-Dest':
  'iframe',
  'Sec-Fetch-Mode':
  'navigate',
  'Sec-Fetch-Site':
  'cross-site',
  'Sec-Fetch-User':
  '?1',
  'Upgrade-Insecure-Requests':
  '1',
  'User-Agent':
  'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.61',
  'sec-ch-ua':
  '"Not_A Brand";v="99", "Microsoft Edge";v="109", "Chromium";v="109"',
  'sec-ch-ua-mobile':
  '?0',
  'sec-ch-ua-platform':
  "Windows",
  'Cookie':
  'vuid=741021487.216956943; language=en; player="captions=en-x-autogen.captions"; _gid=GA1.2.1688424845.1675508068; __cf_bm=rb084YUp6iyZtAr_VckqhIXJtzvr2Qsk3IY6opW6Gcw-1675508849-0-AS3lHxNcXmIupPZ1HVXiaEokrvtr5KyHMAIJv5afZOJcvBSpcJQqFISW03/MgPTjBntaPRyNWVeCAq+LRLQFyf4='
}

haeders4 = {
  'Accept':
  'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
  'Accept-Encoding':
  'gzip, deflate, br',
  'Accept-Language':
  'zh-CN,zh;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6,ja;q=0.5',
  #'Cache-Control': 'max-age=0',
  'Referer':
  'https://www.efi101.com/',  #Ben Horwood
  'Connection':
  'keep-alive',
  'Sec-Fetch-Dest':
  'iframe',
  'Sec-Fetch-Mode':
  'navigate',
  'Sec-Fetch-Site':
  'cross-site',
  #'Sec-Fetch-User': '?1',
  'Upgrade-Insecure-Requests':
  '1',
  'User-Agent':
  'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.61',
  'sec-ch-ua':
  '"Not_A Brand";v="99", "Microsoft Edge";v="109", "Chromium";v="109"',
  'sec-ch-ua-mobile':
  '?0',
  'sec-ch-ua-platform':
  "Windows",
  'Cookie':
  'vuid=741021487.216956943; language=en; player="captions=en.captions"; _ga=GA1.2.849765235.1681469695; __cf_bm=rBpcqV6BAcaqEUf30ha9TeUdeaxiC9hyH85UjBElPbY-1681800084-0-AYbFt/zgLifHLKopqrfeRHaC5Q2qhIfRai0uFEulZSXsIdPrQeA/fsoVHRqWSCkk/sMX0cPNDjwb3Bj4HktN780='
}

haeder1 = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6,ja;q=0.5',
    #'Cache-Control': 'max-age=0',
    'Referer': 'https://evansperformanceacademy.vhx.tv/',
    #'Connection': 'keep-alive',
    'sec-fetch-dest': 'iframe',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-site',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.61',
    'sec-ch-ua': '"Not_A Brand";v="99", "Microsoft Edge";v="109", "Chromium";v="109"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': "Windows",
    #'Cookie': '{"volume":1,"quality":null,"scaling":1,"hd":0,"captions":"en.captions","transcript":null,"captions_styles":{"color":null,"fontSize":null,"fontFamily":null,"fontOpacity":null,"bgOpacity":null,"windowColor":null,"windowOpacity":null,"bgColor":null,"edgeStyle":null}}'
}

oebz = "<domain_status_code>403</domain_status_code>"
vmbz1 = "High Performance Academy"
vmbz2 = "Racecraft"
efibz = "Ben Horwood"
a = 366257291  #361243418  #575609959#57438477


def hpa():
  ks = a
  while 1:
  
    print("hpa            "+ str(ks))
    
    url = "https://player.vimeo.com/video/" + str(ks)
    res_2 = requests.get(url=url, headers=headers3)
    
    if res_2.text.find(vmbz1) > 0 or res_2.text.find(
        vmbz2) > 0:
      print(res_2.text)
      f = open("a.txt", "a")
      f.write(str(ks))
      f.write("\n")
      f.close()
      ks = ks + 1
  
    else:
      ks = ks + 1

def efi():
  ks = a
  while 1:
  
    print("efi            "+ str(ks))
    
    url = "https://player.vimeo.com/video/" + str(ks)
    res_1 = requests.get(url=url, headers=haeders4)
    
    if res_1.text.find(efibz) > 0:
      print(res_1.text)
      f = open("efi.txt", "a")
      f.write(str(ks))
      f.write("\n")
      f.close()
      ks = ks + 1
  
    else:
      ks = ks + 1

def hpa_2():
  ks = 362535618
  while ks<364092191:
  
    print("hpa_2          "+ str(ks))
    
    url = "https://player.vimeo.com/video/" + str(ks)
    res_2 = requests.get(url=url, headers=headers3)
    
    if res_2.text.find(vmbz1) > 0 or res_2.text.find(
        vmbz2) > 0:
      print(res_2.text)
      f = open("a.txt", "a")
      f.write(str(ks))
      f.write("\n")
      f.close()
      ks = ks + 1
  
    else:
      ks = ks + 1

def evan():
  ks = 63500
  url = "https://embed.vhx.tv/videos/556000?api=1&autoplay=1&back=EFI%20Basics&color=2416e3&context=https%3A%2F%2Fevansperformanceacademy.vhx.tv%2Fproducts%2Fefi-basics&is_trailer=false&live=0&locale=en&playsinline=1&product_id="+str(ks)+"&referrer=https%3A%2F%2Fevansperformanceacademy.vhx.tv%2Fproducts%2Fefi-basics&sharing=1&title=0&vimeo=1"
  while 1:#49267
    print(ks)
    res_1 = requests.get(url=url, headers=haeder1)
    
    if res_1.text.find("OTTData") > 0:
      print(res_1.text)
      f = open("evan.txt", "a")
      f.write(str(ks))
      f.write("\n")
      f.close()
      ks = ks + 1
  
    else:
      ks = ks + 1

if __name__ == '__main__':
  process1 = multiprocessing.Process(target=hpa)
  process2 = multiprocessing.Process(target=efi)
  process3 = multiprocessing.Process(target=hpa_2)
  #process4 = multiprocessing.Process(target=evan)

  process1.start()
  process2.start()
  #process3.start()
  #process4.start()

