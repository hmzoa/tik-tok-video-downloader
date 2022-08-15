import requests , json,re
def getId(url):
    if ('@') and ('?') in url:
        return re.search('video/(.*?)\?' ,url).group(1)
    elif ('@') and not ('?') in url:
        return url.split('/')[-1]
    else :
        return re.search('share_item_id=(.*?)&',requests.get(url , headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'} , allow_redirects=True).url).group(1)
def getTikJson(id):
    requrl = f'https://api-t2.tiktokv.com/aweme/v1/aweme/detail/?aweme_id={id}'
    r = requests.get(requrl , headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'} )
    return r.json()
def downloadGlobal(url):
    r = requests.get(url ,stream=True )
    with open('tik tok video.mp4','wb') as f:
        f.write(r.content)
        f.flush()
downToSend = downloadGlobal(getTikJson(getId("any tiktok video"))['aweme_detail']['video']['play_addr']['url_list'][0])
