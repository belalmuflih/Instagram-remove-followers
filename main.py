#BY BELAL STARTED AT 7:00AM 16/1/2021


import requests, json, colorama
from time import sleep
from colorama import Fore, Style
import getpass

colorama.init()

class InstagramUnfollow:
    
    print(Fore.BLUE +Style.BRIGHT+ f"""
    ╭╾────────────────────────────────────────────────────────────╼╮                 
    │                                                              │
    │                THIS TOOL WAS DEVELOPED BY                    │ 
    │                                                              │ 
    │                             Ω                                │
    │                                                              │
    │                 @znecv       snapchat:znecv                  │
    ╰╾────────────────────────────────────────────────────────────╼╯
    
    """+ Fore.RESET)
    def __init__(self):
        self.headers = {
		"Accept": "*/*",
		"Accept-Encoding": "gzip, deflate",
		"Accept-Language": "en-US",
		"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 123.1.0.26.115 (iPhone11,8; iOS 13_3; en_US; en-US; scale=2.00; 828x1792; 190542906)",
		"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
		"X-IG-Capabilities": "3brTvw==",
		"X-IG-Connection-Type": "WIFI",
		}
        self.session = requests.session()
        self.url = "https://i.instagram.com"
        self.API = "/api/v1"
    def Start(self):
        
        self.get_csrf()
        self.Login()

    def get_csrf(self):
        try:
            self.session.headers = self.headers
            self.session.headers.update({'Referer': self.url})
            getcsrf = self.session.get(self.url)
            self.csrf = getcsrf.cookies['csrftoken']
            self.session.headers.update({'X-CSRFToken': self.csrf})
        except Exception as e:
            print(Fore.RED + '\r                         Unknown Error.',e)
        except KeyboardInterrupt:
            print(Fore.RED + '\r                         Process has been cancelled')

    def Login(self):
        ASK = True
        LOGED = False
        try:
            while ASK:
                print(f"	{Fore.RED}Username         :        {Fore.RESET}", end='')
                username = input("")
                print(f"	{Fore.RED}Password         :        {Fore.RESET}", end='')
                password = getpass.getpass("")
                print("\n")
                self.account = self.session.post(self.url + "/accounts/login/ajax/", data={"username":username,"password":password}, allow_redirects=True)
                self.LoginData = self.account.json()
                if self.LoginData['authenticated'] == True:
                    break
                elif self.LoginData['authenticated'] == False:
                    print(f"{Fore.RED}         username or password is wrong.")
        except Exception as e:
            print(Fore.RED + '\r                         Unknown Error. ssss',e)
        except KeyboardInterrupt:
            print(Fore.RED + '\r                         Process has been cancelled.')
        self.getFollowersId()

    def getFollowersId(self):
        try:
            #ACCOUNT ID
            self.userId = self.LoginData['userId']
            self.followers = self.session.get(self.url+self.API+'/friendships/'+ self.userId +'/followers/?rank_token={1}').json()
            #Followers
            self.Ids = []
            lenght = len(self.followers['users'])
            if lenght == 0:
                print(Fore.YELLOW + '\r                         Check your account.', end='\r')
                input()
                exit()
            for i in range(lenght):
                self.Followers = self.followers['users'][i]['pk']
                self.Ids.append(self.Followers)
            self.remove_followers()
        except Exception as e:
            print(Fore.RED + '\r                         Unknown Error.')
        except KeyboardInterrupt:
            print(Fore.RED + '\r                         Process has been cancelled.')

    def remove_followers(self):
        self.get_csrf()
        try:
        
            for Id in self.Ids:
                self.remove = self.session.post(self.url + self.API + '/friendships/remove_follower/'+ str(Id) +'/', headers=self.headers)
                if self.remove.status_code == 404:
                    sleep(60*3)
                    print(Fore.GREEN + '\r                     Sleeping for 3 mins to avoid band...', end='\r')
                print(Fore.YELLOW +f'\r                     Please wait while removing followers...' + Fore.RESET, end='\r')
                
                sleep(0.05)
        except Exception as e:
            print(Fore.RED + '\r                         Unknown Error.')
        except KeyboardInterrupt:
            print(Fore.RED + '\r                         Process has been cancelled.')


if __name__ == "__main__":
    InstagramBot = InstagramUnfollow()
    InstagramBot.Start()