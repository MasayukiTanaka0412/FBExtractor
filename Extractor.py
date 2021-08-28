import os
import requests
import json

def parsePosts(posts):
    mdtext =""
    for data in posts:
        permalink_url = data["permalink_url"]
        created_time = data["created_time"]
        mdtext = mdtext + "投稿日:{}  \r\n".format(created_time)
        mdtext = mdtext + "リンク:[{}]({})  \r\n".format(permalink_url,permalink_url)
        try:    
            mdtext = mdtext + data["message"] + "  \r\n"
        except KeyError as e:
            pass

        try:
            mdtext = mdtext + "![画像]({})  \r\n".format(data["full_picture"])
        except KeyError as e:
            pass

        try:
            link = data["link"]
            description = data["description"]
            mdtext = mdtext + "[{}]({})  \r\n".format(description,link)
        except KeyError as e:
            pass

        try:
            for comment in data["comments"]["data"]:
                mdtext = mdtext + "- {}  \r\n".format(comment["message"])
        except KeyError as e:
            pass

        mdtext = mdtext + "  \r\n"
        mdtext = mdtext + "---\r\n"
        mdtext = mdtext + "  \r\n"
        #print (mdtext)
    return mdtext

        

print ('Start Extractor')

print ('Setup parameters')
user_token =os.environ["user_token"]
outputfile =os.environ["outputfile"]
print("user_token={}".format(user_token))
print("outputfile={}".format(outputfile))

requestUrl = "https://graph.facebook.com/v11.0/me?fields=posts%7Bpermalink_url%2Ccreated_time%2Cmessage%2Cfull_picture%2Clink%2Cdescription%2Ccomments%7Bmessage%2Cobject%7D%7D&access_token={}".format(user_token)
response = requests.get(requestUrl)
resJSON = response.json()

with open(outputfile,encoding="utf-8",mode="w") as f:

    md = parsePosts(resJSON["posts"]["data"])
    if not md is None:
        f.write(md)

    if "paging" in resJSON["posts"] and "next" in resJSON["posts"]["paging"]:
        response = requests.get(resJSON["posts"]["paging"]["next"])
        resJSON = response.json()
        md = parsePosts(resJSON["data"])
        if not md is None:
            f.write(md)
        while "paging" in resJSON and "next" in resJSON["paging"]:
            response = requests.get(resJSON["paging"]["next"])
            resJSON = response.json()
            md = parsePosts(resJSON["data"])
            if not md is None:
                f.write(md)

print ('End Extractor')