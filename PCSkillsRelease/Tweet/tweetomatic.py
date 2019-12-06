import tweepy
import auth
import os.path as op
import argparse
import path

parser = argparse.ArgumentParser(description='Tweetomatic app for Alexa PC Skills.')
parser.add_argument('-t', '--tweet', type=str, help='The tweet you want to update.')
parser.add_argument('-i', '--image', help='The file path that you want to tweet.')
args = parser.parse_args()

print(path.path)
if op.isfile(path.path + 'token'):
    with open(path.path + 'token','r') as f:
        access_token = f.readline()[:-1]
        access_token_secret = f.readline()
    #print('Token present')
else:
    access_token , access_token_secret = auth.run()
    with open(path.path + 'token','w') as f:
        f.write(access_token + '\n' + access_token_secret)
    #print('Token is not present so it is generated')
        

    

access = tweepy.OAuthHandler(auth.consumer_key,auth.consumer_key_secret)
access.set_access_token(access_token,access_token_secret)
api = tweepy.API(access)

if args.tweet == None and args.image == None:
    print("Invalid tweet try with argument -h for help")
elif args.image == None:
    api.update_status(args.tweet)
    print ('Tweet posted : ' + args.tweet)
else:
    if args.tweet == None:
        api.update_with_media(args.image, args.tweet)
        print ('Tweet posted with media at ' + args.image)

    else:
        api.update_with_media(args.image, args.tweet)
        print ('Tweet posted : ' + args.tweet + ' with media at ' + args.image)
