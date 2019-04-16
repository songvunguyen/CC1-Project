import os
import subprocess
from bs4 import BeautifulSoup
import urllib3
import io
import json
import sys
from text_utils import *
from datasets_path import *
from tqdm import tqdm


def text_from_pdf(pdf_path, text_path):
    """
    Parse text from pdf file
    Parameters
    ----------
    pdf_path : str
    text_path : str

    Returns
    text: str
    -------

    """
    subprocess.call(["pdftotext", pdf_path, text_path])
    with io.open(text_path, encoding="utf8") as f:
        text = f.read()
    f.close()
    os.remove(text_path)

    return remove_extra_space(text).strip()


def parse_pdf_from_folder(folder_path):
    ext = '.pdf'  # Select your file delimiter

    files = [i for i in os.listdir(folder_path) if os.path.splitext(i)[1] == ext]

    paper_info = {}
    paper_original = {}

    idx = 0
    for f in files:
        file_path = folder_path + '/' + f
        text = text_from_pdf(file_path, file_path + '.txt')
        paper_info[idx] = {'url': '', 'title': f}
        paper_original[idx] = text
        idx += 1
        print(idx)

    with open(CNT_PAPERS_INFO_PATH, 'w') as fp:
        json.dump(paper_info, fp)
    fp.close()

    with open(CNT_PAPERS_ORI_PATH, 'w') as fp:
        json.dump(paper_original, fp)
    fp.close()


def fill_zeros(number):
    """
    Fills zeros before the number to make digits with length of 5

    Parameters
    ----------
    number : str
        digits in string

    Returns
    -------
    number : str
        digits in string with length of 5
    """
    d = 5 - len(number)
    return '0' * d + number


def collect_fncom_papers_info():
    """
    Collects papers urls and titles from Front. Comput. Neurosci, and only collect type of
    "METHODS ARTICLE" and "ORIGINAL RESEARCH ARTICLE", and time range from 2017-2018

    Returns
    -------

    """
    base_url = "https://www.frontiersin.org/articles/10.3389/fncom."
    fncom_papers_info = {}

    # # collect paper urls in 2010
    # for i in range(1, 156):
    #     url = base_url + "2010." + fill_zeros(str(i))
    #
    #     try:
    #         response = urllib2.urlopen(url)
    #         soup = BeautifulSoup(response.read(), "html.parser")
    #         _type = soup.find("h2").contents[0].strip()
    #         _title = soup.find("title").contents[0].strip().split('|')[1].strip()
    #         if _type == 'Original Research ARTICLE' or _type == 'Methods ARTICLE':
    #             k = "2010." + fill_zeros(str(i))
    #             fncom_papers_info[k] = {'title':_title, 'url': url}
    #             # print url, _title
    #         sys.stdout.flush()
    #
    #     except Exception:
    #         continue
    #
    # # collect paper urls in 2011
    # for i in range(1, 63):
    #     url = base_url + "2011." + fill_zeros(str(i))
    #
    #     try:
    #         response = urllib2.urlopen(url)
    #         soup = BeautifulSoup(response.read(), "html.parser")
    #         _type = soup.find("h2").contents[0].strip()
    #         _title = soup.find("title").contents[0].strip().split('|')[1].strip()
    #         if _type == 'Original Research ARTICLE' or _type == 'Methods ARTICLE':
    #             k = "2011." + fill_zeros(str(i))
    #             fncom_papers_info[k] = {'title':_title, 'url': url}
    #             # print url, _title
    #         sys.stdout.flush()
    #
    #     except Exception:
    #         continue
    #
    # # collect paper urls in 2012
    # for i in range(1, 103):
    #     url = base_url + "2012." + fill_zeros(str(i))
    #
    #     try:
    #         response = urllib2.urlopen(url)
    #         soup = BeautifulSoup(response.read(), "html.parser")
    #         _type = soup.find("h2").contents[0].strip()
    #         _title = soup.find("title").contents[0].strip().split('|')[1].strip()
    #         if _type == 'Original Research ARTICLE' or _type == 'Methods ARTICLE':
    #             k = "2012." + fill_zeros(str(i))
    #             fncom_papers_info[k] = {'title':_title, 'url': url}
    #             #print url, _title
    #         sys.stdout.flush()
    #
    #     except Exception:
    #         continue
    #
    # # collect paper urls in 2013
    for i in range(1, 195):
        url = base_url + "2013." + fill_zeros(str(i))

        try:
            response = urllib2.urlopen(url)
            soup = BeautifulSoup(response.read(), "html.parser")
            _type = soup.find("h2").contents[0].strip()
            _title = soup.find("title").contents[0].strip().split('|')[1].strip()
            if _type == 'Original Research ARTICLE' or _type == 'Methods ARTICLE':
                k = "2013." + fill_zeros(str(i))
                fncom_papers_info[k] = {'title':_title, 'url': url}
                # print url, _title
            sys.stdout.flush()

        except Exception:
            continue

    # collect paper urls in 2014
    for i in range(1, 175):
        url = base_url + "2014." + fill_zeros(str(i))

        try:
            response = urllib2.urlopen(url)
            soup = BeautifulSoup(response.read(), "html.parser")
            _type = soup.find("h2").contents[0].strip()
            _title = soup.find("title").contents[0].strip().split('|')[1].strip()
            if _type == 'Original Research ARTICLE' or _type == 'Methods ARTICLE':
                k = "2014." + fill_zeros(str(i))
                fncom_papers_info[k] = {'title':_title, 'url': url}
                # print url, _title
            sys.stdout.flush()

        except Exception:
            continue

    # collect paper urls in 2015
    for i in range(1, 156):
        url = base_url + "2015." + fill_zeros(str(i))

        try:
            response = urllib2.urlopen(url)
            soup = BeautifulSoup(response.read(), "html.parser")
            _type = soup.find("h2").contents[0].strip()
            _title = soup.find("title").contents[0].strip().split('|')[1].strip()
            if _type == 'Original Research ARTICLE' or _type == 'Methods ARTICLE':
                k = "2015." + fill_zeros(str(i))
                fncom_papers_info[k] = {'title':_title, 'url': url}
                # print url, _title
            sys.stdout.flush()

        except Exception:
            continue

    # collect paper urls in 2016
    for i in range(1, 147):
        url = base_url + "2016." + fill_zeros(str(i))

        try:
            response = urllib2.urlopen(url)
            soup = BeautifulSoup(response.read(), "html.parser")
            _type = soup.find("h2").contents[0].strip()
            _title = soup.find("title").contents[0].strip().split('|')[1].strip()
            if _type == 'Original Research ARTICLE' or _type == 'Methods ARTICLE':
                k = "2016." + fill_zeros(str(i))
                fncom_papers_info[k] = {'title':_title, 'url': url}
                # print url, _title
            sys.stdout.flush()

        except Exception:
            continue

    # collect paper urls in 2017
    for i in range(1, 120):
        url = base_url + "2017." + fill_zeros(str(i))

        try:
            response = urllib2.urlopen(url)
            soup = BeautifulSoup(response.read(), "html.parser")
            _type = soup.find("h2").contents[0].strip()
            _title = soup.find("title").contents[0].strip().split('|')[1].strip()
            if _type == 'Original Research ARTICLE' or _type == 'Methods ARTICLE':
                k = "2017." + fill_zeros(str(i))
                fncom_papers_info[k] = {'title':_title, 'url': url}
                # print url, _title
            sys.stdout.flush()

        except Exception:
            continue

    # collect paper urls in 2018
    for i in range(1, 57):
        url = base_url + "2018." + fill_zeros(str(i))

        try:
            response = urllib2.urlopen(url)
            soup = BeautifulSoup(response.read(), "html.parser")
            _type = (soup.find("h2").contents[0].strip())
            _title = soup.find("title").contents[0].strip().split('|')[1].strip()
            if _type == 'Original Research ARTICLE' or _type == 'Methods ARTICLE':
                k = "2018." + fill_zeros(str(i))
                fncom_papers_info[k] = {'title':_title, 'url': url}
                # print url, _title
            sys.stdout.flush()

        except Exception:
            continue

    file_path = os.path.join(dirname(os.path.realpath(__file__)), 'dataset/fncom_papers_info.json')
    with open(file_path, 'w') as fp:
        json.dump(fncom_papers_info, fp)

    fp.close()
    print("The total number of papers in fncom is %d" % len(fncom_papers_info))



def collect_fncom_papers():
    """
    Collects original text from pdf file, which extract all the content except abstract and reference

    Returns
    -------

    """
    file_path = os.path.join(dirname(os.path.realpath(__file__)), 'dataset/fncom_papers_info.json')
    with open(file_path, 'r') as fp:
        fncom_papers_info = json.load(fp)
    fncom_papers_original = {}
    print("The input number of papers in fncom is %d" % len(fncom_papers_info))
    sys.stdout.flush()
    count = 0
    for k in fncom_papers_info.keys():
        url = fncom_papers_info[k]['url']

        # get text
        response = urllib2.urlopen(url)
        soup = BeautifulSoup(response.read(), "html.parser")

        # remove References
        for div in soup.find_all("div", {'class': 'References'}):
            div.decompose()

        # remove equation
        for div in soup.find_all("div", {'class': 'equationImageholder'}):
            div.decompose()
        [s.extract() for s in soup('math')]

        text = soup.find('div', attrs={"class": "JournalFullText"}).text
        fncom_papers_original[k] = remove_extra_space(text).strip()
        count += 1
        if count % 50 == 0:
            print("Finish %d number of papers" % count)
            sys.stdout.flush()

    file_path = os.path.join(dirname(os.path.realpath(__file__)), 'dataset/fncom_papers_original.json')
    with open(file_path, 'w') as fp:
        json.dump(fncom_papers_original, fp)

    fp.close()
    print("The total collected number of papers in fncom is %d" % len(fncom_papers_original))


def collect_jocn_papers_info():
    """
    Collects papers urls and titles from Journal of Computational Neuroscience, and time range from 2017-2018

    Returns
    -------

    """
    base_url = "https://link.springer.com/journal/10827/"

    volume = [35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45]
    issues = [1, 2, 3]

    jocn_papers_info = {}
    for v in volume:
        for i in issues:
            if v == 45 and (i == 2 or i == 3):
                continue
            url = base_url + str(v) + '/' + str(i) + '/'

            try:
                response = urllib2.urlopen(url)
                soup = BeautifulSoup(response.read(), "html.parser")

                for link in soup.find_all('h3',  {'class': 'title'}):
                    _url = link.find('a').get('href')
                    _title = link.find('a').contents[0].strip()

                    if 'Erratum' in _title:
                        continue

                    k = _url.split('/')[3]
                    jocn_papers_info[k] = {'title': _title,
                                           'url': 'https://link.springer.com/' + _url}
                    # print _url, _title
            except Exception:
                continue
            sys.stdout.flush()

    with open(JOCN_PAPERS_INFO_PATH, 'w') as fp:
        json.dump(jocn_papers_info, fp)

    fp.close()
    print("The total number of paper in jocn is %d" % len(jocn_papers_info))


def collect_jocn_papers():

    with open(JOCN_PAPERS_INFO_PATH, 'r') as fp:
        jocn_papers_info = json.load(fp)

    jocn_papers_original = {}
    for k in jocn_papers_info.keys():
        url = jocn_papers_info[k]['url']
        print(url)

        response = urllib2.urlopen(url)
        soup = BeautifulSoup(response.read(), "html.parser")

        # remove equation
        for span in soup.find_all("span", {'class': 'InlineEquation'}):
            span.decompose()

        # remove figure
        for span in soup.find_all("span", {'class': 'InternalRef'}):
            span.decompose()

        # remove citation
        for span in soup.find_all("span", {'class': 'CitationRef'}):
            span.decompose()

        contents = ""
        for a in soup.find_all('p', {'class': 'Para'}):
            contents += a.text

        jocn_papers_original[k] = remove_extra_space(contents).strip()

    with open(JOCN_PAPERS_ORI_PATH, 'w') as fp:
        json.dump(jocn_papers_original, fp)

    fp.close()


def collect_joneuro_papers_info():
    base_url = "http://www.jneurosci.org/content/"

    joneuro_papers_info = {}
    for v in range(38, 39):
        for i in range(1, 60):
            url = base_url + str(v) + '/' + str(i)
            try:
                response = urllib2.urlopen(url)
                soup = BeautifulSoup(response.read(), "html.parser")

                # Get all the hrefs of this issues
                for a in soup.find_all('a', href=True):
                    template = '/content/' + str(v) + '/' + str(i) + '/'

                    if template in a['href'] and str.isdigit(str(a['href'].split(template)[1])):
                        paper_urf = base_url + a['href'].split('/content/')[1]

                        r = urllib2.urlopen(paper_urf)
                        s = BeautifulSoup(r.read(), "html.parser")

                        m = s.find("meta", {"name": "article:section"})['content']
                        if m == "Articles" or m == "Research Articles":
                            title = s.find("div", {"class": "highwire-cite-title"}).text
                            k = a['href'].split('/content/')[1]
                            joneuro_papers_info[k] = {'title': title,
                                                      'url': paper_urf}
            except Exception:
                continue

    with open(JONEURO_PAPERS_INFO_PATH, 'w') as fp:
        json.dump(joneuro_papers_info, fp)

    fp.close()
    print("the total number of papers in joneuro is %s" % len(joneuro_papers_info))


def collect_joneuro_papers():
    with open(JONEURO_PAPERS_INFO_PATH, 'r') as fp:
        joneuro_papers_info = json.load(fp)

    joneuro_papers_original = {}
    for k in joneuro_papers_info.keys():
        url = joneuro_papers_info[k]['url']
        print(url)

        response = urllib2.urlopen(url)
        soup = BeautifulSoup(response.read(), "html.parser")

        for tag in soup.find_all('em'):
            tag.replaceWith('')

        # print soup

        for tag in soup.findAll('p'):
            print(tag.text)

        break
    return


def collect_bmcbio_papers_info():
    base_url = 'https://bmcbioinformatics.biomedcentral.com/articles?searchType=journalSearch&sort=PubDate&page=%d'
    base_paper_url = 'https://bmcbioinformatics.biomedcentral.com'
    bmc_papers_info = {}

    for i in range(1, 30):
        url = base_url % i
        sys.stdout.flush()
        try:
            response = urllib2.urlopen(url)
            soup = BeautifulSoup(response.read(), "html.parser")
            for link in soup.find_all('h3', {'class': 'c-teaser__title'}):
                _url = base_paper_url + link.find('a').get('href')

                r = urllib2.urlopen(_url)
                s = BeautifulSoup(r.read(), "html.parser")
                for m in s.find_all("meta"):
                    if "citation_article_type" in str(m) and (m.get('content').lower() == 'Methodology Article'.lower() \
                                                              or m.get('content').lower() == 'Research Article'.lower() \
                                                              or m.get('content').lower() == 'Research'.lower()):
                        try:
                            k = _url.split('/')[5]
                            _title = link.find('a').contents[0].strip()
                        except Exception:
                            print("OOps: " + _url)
                            continue
                        if k in bmc_papers_info:
                            print("repeated key : %s" % k)

                        bmc_papers_info[k] = {'title': _title, 'url': _url}
                        break
        except Exception:
            print("OOps: " + _url)
            continue

    with open(BMC_BIOINFORMACTS_INFO_PATH, 'w') as fp:
        json.dump(bmc_papers_info, fp)

    fp.close()
    print("the total number of papers in bmcbio is %s" % len(bmc_papers_info))


def collect_bmcbio_papers():
    with open(BMC_BIOINFORMACTS_INFO_PATH, 'r') as fp:
        bio_papers_info = json.load(fp)

    bmc_papers_original = {}
    with tqdm(total=len(bio_papers_info), unit="docs", desc="Collecting BMC Bioinformatics Papers") as p_bar:
        for k in bio_papers_info.keys():
            url = bio_papers_info[k]['url']
            response = urllib2.urlopen(url)
            soup = BeautifulSoup(response.read(), "html.parser")

            for div in soup.find_all("div", {'class': 'EquationContent'}):
                div.decompose()

            for div in soup.find_all("div", {'class': 'Table'}):
                div.decompose()

            contents = ""
            for a in soup.find_all('p', {'class': 'Para'}):
                contents += a.text

            for a in soup.find_all('div', {'class': 'Para'}):
                contents += a.text

            bmc_papers_original[k] = remove_extra_space(contents).strip()
            p_bar.update(1)

    with open(BIO_PAPER_ORI_PATH, 'w') as fp:
        json.dump(bmc_papers_original, fp)

    fp.close()


def collect_bmcgenomic_papers_info():
    base_url = 'https://bmcgenomics.biomedcentral.com/articles?searchType=journalSearch&sort=PubDate&page=%d'
    base_paper_url = 'https://bmcgenomics.biomedcentral.com'
    bmc_papers_info = {}

    for i in range(1, 30):
        url = base_url % i
        sys.stdout.flush()
        try:
            response = urllib2.urlopen(url)
            soup = BeautifulSoup(response.read(), "html.parser")
            for link in soup.find_all('h3', {'class': 'c-teaser__title'}):
                _url = base_paper_url + link.find('a').get('href')

                r = urllib2.urlopen(_url)
                s = BeautifulSoup(r.read(), "html.parser")
                for m in s.find_all("meta"):
                    if "citation_article_type" in str(m) and (m.get('content').lower() == 'Methodology Article'.lower() \
                                                              or m.get('content').lower() == 'Research Article'.lower() \
                                                              or m.get('content').lower() == 'Research'.lower()):
                        try:
                            k = _url.split('/')[5]
                            _title = link.find('a').contents[0].strip()
                        except Exception:
                            print("OOps: " + _url)
                            continue
                        if k in bmc_papers_info:
                            print("repeated key : %s" % k)

                        print(_url)
                        bmc_papers_info[k] = {'title': _title, 'url': _url}
                        break
        except Exception:
            print("OOps: " + _url)
            continue

    with open(BMC_GENOMICIS_INFO_PATH, 'w') as fp:
        json.dump(bmc_papers_info, fp)

    fp.close()
    print("the total number of papers in bmcgenomics is %s" % len(bmc_papers_info))


def collect_bmcgenomics_papers():
    with open(BMC_GENOMICIS_INFO_PATH, 'r') as fp:
        bio_papers_info = json.load(fp)

    bmc_papers_original = {}
    with tqdm(total=len(bio_papers_info), unit="docs", desc="Collecting BMC Genomics Papers") as p_bar:
        for k in bio_papers_info.keys():
            url = bio_papers_info[k]['url']
            response = urllib2.urlopen(url)
            soup = BeautifulSoup(response.read(), "html.parser")

            for div in soup.find_all("div", {'class': 'EquationContent'}):
                div.decompose()

            for div in soup.find_all("div", {'class': 'Table'}):
                div.decompose()

            contents = ""
            for a in soup.find_all('p', {'class': 'Para'}):
                contents += a.text

            for a in soup.find_all('div', {'class': 'Para'}):
                contents += a.text

            bmc_papers_original[k] = remove_extra_space(contents).strip()
            p_bar.update(1)

    with open(BMC_GENOMICS_ORI_PATH, 'w') as fp:
        json.dump(bmc_papers_original, fp)

    fp.close()


# def collect_plos_info():
#     base_url = 'https://bmcgenomics.biomedcentral.com/articles?searchType=journalSearch&sort=PubDate&page=%d'
#     base_paper_url = 'https://bmcgenomics.biomedcentral.com'
#     plos_papers_info = {}
#
#     with open(PLOS_INFO_PATH, 'w') as fp:
#         json.dump(plos_papers_info, fp)
#
#     fp.close()
#     print "the total number of papers in bmc genomics is %s" % len(bmc_papers_info)


if __name__ == "__main__":
    parse_pdf_from_folder(CNT_PAPERS_Folder)




