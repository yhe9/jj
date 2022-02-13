import requests

wikiBaseTitleURL = "https://en.wikipedia.org/w/api.php?action=query&titles={}&format=json&formatversion=2"
wikiURL = "https://en.wikipedia.org/wiki/{}"


def wikiurlByTitle(titleName):
    titleStr = "".join(titleName).strip()
    titleValue = titleStr.replace(" ", "_", -1)
    wikiTitleUrl = wikiBaseTitleURL.format(titleValue)
    responseJson = ""
    pageid = 0
    wikiURLNew = wikiURL.format(titleValue)
    wikiIDURL = "https://en.wikipedia.org/?curid={}"
    try:
        responseJson = requests.get(wikiTitleUrl, timeout=5).json()
        pageid = getWikiPageID(responseJson)
        if pageid == 0:
            return wikiURLNew
        return wikiIDURL.format(pageid)
    except requests.exceptions.RequestException as e:
        print(e)
    if responseJson == "":
        return wikiURLNew


def getWikiPageID(testJson):
    if testJson:
        query = testJson.get('query')
        pages = query.get("pages")
        if pages:
            pageid = pages[0].get("pageid")
            if pageid:
                return pageid
            else:
                return 0

