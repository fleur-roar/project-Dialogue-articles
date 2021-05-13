from bs4 import BeautifulSoup
import re
import os


def get_html(path, name):
    pathToScript = r'C:\Users\Anna\AppData\Local\Programs\Python\Python39\Scripts\pdf2txt.py'
    pathPDFinput = os.path.join(path)
    pathHTMLoutput = os.path.join(name)
    os.system(r'C:\Users\Anna\AppData\Local\Programs\Python\Python39\python.exe {} -o {} -S {} -t html'.format(pathToScript, pathHTMLoutput, pathPDFinput))
    print('done')


def num_search(thing): #для поиска тегов
    for e in thing.contents:
        if re.match('\((\d)+\)', str(e)):
            return re.match('\((\d)+\)', str(e))
    return False

def n_search(t): #для содержания тегов
    if re.match(' *\((\d)+\) *', str(t)):
        return re.match('\((\d)+\)', str(t))
    return False


def f_search(t): #для готового тега
    if 'style' in t.attrs:
        if re.match("font-family: CharterITC-(Bold)?Italic; .*", str(t['style'])):
            return re.match("font-family: CharterITC-(Bold)?Italic; .*", str(t['style']))
    return False

def get_italics(l, text):
    if f_search(l[0]):
        #print(l[0].contents)
        text.extend(l[0].contents)
        #print(text)
        return get_italics(l[1:], text)
    else:
        return text
    

def p_search(list_of_soup):
    s = []
    for i in range (len(list_of_soup)):
        if num_search(list_of_soup[i]):
            if n_search(list_of_soup[i].contents[0]):
                tt = []
                sent = get_italics(list_of_soup[(i+1):], tt)
                s.append(sent)
    return s

def processing_s(s):
    ls = []
    coun = 0
    for elem in s:
        coun += 1
        sent = ''
        for ss in elem:
            if str(ss) != '<br/>':
                if str(ss).endswith('-'):
                    sent += str(ss).strip('\n')
                else:
                    sent += str(ss).strip('\n') + ' '
        ls.append('(' + str(coun) + ') ' + sent)
    print(ls)
    
def main():
    p = input('insert the path')
    n = input('insert the name')
    get_html(p, n)
    with open(n, encoding = 'utf-8') as fp:
        soup = BeautifulSoup(fp, 'html.parser')
        g = soup.find_all('span')
        h = p_search(g)
        processing_s(h)
        
main()
