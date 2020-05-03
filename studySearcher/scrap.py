import requests
from bs4 import BeautifulSoup


def getText(url):
    """
    takes the url (string) and returns the contents as text
    FIXME
    """
    r1 = requests.get(url)
    page = r1.content

    soup1 = BeautifulSoup(page, "html.parser")
    soup1.prettify()
    page_news = soup1.find('article', class_= "pg-rail-tall pg-rail--align-right").div.div.div
    page_news.get_text()

    return page_news

def study_to_string(study):
    """
    returns a string representing the contents of study
    """
    ret = "Title: " + study[0]
    if (study[1] is not None) and (study[1] != ""):
        ret += "\n" + "Summary: " + study[1]
    if (study[2] is not None) and (study[2] != ""):
        ret += "\n" + "Journal: " + study[2]
    if (study[3] is not None) and (study[3] != ""):
        ret += "\n" + "URL: " + study[3]
    return ret

def main(url, nresults = 3):
    """
    url is a url to an article
    nresults defaults to 3, and is the number of strings returned
    the code returns nresults number of strings in an array
    """
    res = getText(url)
    if res is None:
        return [""] * nresults
    # assuming getText function works for now... @FIXME
    from main import best_studies
    ret = []
    studies = best_studies(str(res), nresults)
    for study in studies:
        if study is None:
            break
        sts = study_to_string(study)
        ret.append(sts)
    return ret

if __name__ == '__main__':
    result = main("https://www.cnn.com/2020/05/02/us/isabella-geriatric-center-coronavirus-nyc/index.html")
    """
    For future readers: main is documented
    """