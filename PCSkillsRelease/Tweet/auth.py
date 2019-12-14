from requests_oauthlib import OAuth1Session
from http.server import BaseHTTPRequestHandler
import socketserver
import webbrowser as wb 

consumer_key = 'X9npwyQIOR1AQA4TdcbJGLCCL'
consumer_key_secret = 'RXfOsUcuwVvWjjmnIbSFyetSn1mXwOsHFByq0FKDLqcmn3Hgbr'
verifier = ''
resources = []

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        global verifier
        verifier = str(self.path).split('&')[-1].split('=')[-1]
        return


def req_token_generation():
    request_token_url = 'https://api.twitter.com/oauth/request_token'
    request_token = OAuth1Session(client_key=consumer_key,client_secret=consumer_key_secret)
    r = request_token.post(request_token_url)
    data = r.text.split("&")
    ro_token_key_secret = data[1].split("=")[-1]
    ro_token_key = data[0].split("=")[-1]
    global resources
    resources = [ro_token_key,ro_token_key_secret]
    return resources


def authenticate_browser(resources):
    url = 'https://api.twitter.com/oauth/authenticate?oauth_token='+resources[0]
    wb.open(url)
    with socketserver.TCPServer(('127.0.0.1',1234),handler) as httpd:
        print('Starting handler')
        httpd.handle_request()
    return 

def oauth_token_generation(ro_token_key,ro_token_key_secret,verifier):
    url = 'https://api.twitter.com/oauth/access_token'
    data = {"oauth_verifier": verifier}
    oauth_token = OAuth1Session(client_key=consumer_key,client_secret=consumer_key_secret,resource_owner_key=ro_token_key,resource_owner_secret=ro_token_key_secret)
    access_token_data = oauth_token.post(url, data=data)  
    oauth_token = access_token_data.text.split('&')[0].split('=')[-1]
    oauth_token_secret = access_token_data.text.split('&')[1].split('=')[-1]
    return oauth_token,oauth_token_secret

def run():
    authenticate_browser(req_token_generation())
    access_token, access_token_secret = oauth_token_generation(ro_token_key=resources[0],ro_token_key_secret=resources[1],verifier=verifier)
    return access_token,access_token_secret

