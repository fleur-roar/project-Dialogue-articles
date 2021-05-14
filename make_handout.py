from bs4 import BeautifulSoup
import re
import os
import tabula
import fitz

def get_tables(path):
    tabb = tabula.read_pdf(path, pages = "all", multiple_tables = True)
    name = path.strip('pdf')
    ccounter = 0
    for elem in tabb:
        ccounter += 1
        with open (name + str(ccounter) + '.xlsx', 'w', encoding = 'utf-8'):
            elem.to_excel(name + str(ccounter) + '.xlsx')
            
def get_images(path):
    doc = fitz.open(path)
    name = path.strip('pdf')
    counter = 0
    for page in doc:
        images = page.get_images()
        if images:
            for im in images:
                counter += 1
                pix = fitz.Pixmap(doc, im[0])
                pix.writeImage(name + str(counter) + '.png', output=None)



def get_html(path, name):
    pathToScript = r'C:\Users\Anna\Python39\Scripts\pdf2txt.py' 
    pathPDFinput = os.path.join(path)
    pathHTMLoutput = os.path.join(name)
    os.system(r'C:\Users\Anna\Python39\python.exe {} -o {} -S {} -t html'.format(pathToScript, pathHTMLoutput, pathPDFinput))


def num_search(thing): #для поиска тегов
    for e in thing.contents:
        if re.match('\(\d(\d)?\)', str(e)):
            return re.match('\((\d)+\)', str(e))
    return False

def n_search(t): #для содержания тегов
    if re.match(' *\(\d(\d)?\) *', str(t)):
        return re.match('\((\d)+\)', str(t))
    return False


def f_search(t): #для готового тега
    if 'style' in t.attrs:
        if re.match("font-family: CharterITC-(Bold)?Italic; .*", str(t['style'])):
            return re.match("font-family: CharterITC-(Bold)?Italic; .*", str(t['style']))
    return False

def get_italics(l, text):
    if f_search(l[0]):
        text.extend(l[0].contents)
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
        if elem != []:
            for ss in elem:
                if str(ss) != '<br/>':
                    if str(ss).endswith('-'):
                        sent += str(ss).strip('\n')
                    else:
                        sent += str(ss).strip('\n') + ' '
            ls.append('(' + str(coun) + ') ' + sent)
    return ls

def get_examples(path):
    n = path.strip('pdf') + 'html'
    get_html(path, n)
    with open(n, encoding = 'utf-8') as fp:
        soup = BeautifulSoup(fp, 'html.parser')
        span_list = soup.find_all('span')
        h = p_search(span_list)
        return (processing_s(h))
    
def make_handout(e, path):
    name = path.strip('pdf') + 'txt'
    if e!=[]:
        with open(name, 'w', encoding='utf-8') as f:
            for elem in e:
                f.write(elem + '\n\n')
    
def main():
    p = input('insert the path')
    examples = get_examples(p)
    make_handout(examples, p)
    get_images(p)
    get_tables(p)
    
        
main()
