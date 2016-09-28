from google import search
import urllib.request
from bs4 import BeautifulSoup

def decode_page(page):
    encoding = page.info().get("Content-Encoding")
    if encoding in ('gzip', 'x-gzip', 'deflate'):
        content = page.read()
        if encoding == 'deflate':
            data = StringIO.StringIO(zlib.decompress(content))
        else:
            try:
                data = zlib.decompress(content, 16+zlib.MAX_WBITS)
                return data;
                #data = gzip.GzipFile('', 'rb', 9, StringIO.StringIO(content))
            except:
                return None
        page = data.read()

    return page

#This method opens a URL
def get_page(url):
    try:
        return urllib.request.urlopen(url)
    except:
        return None

#This method invokes the decoder method and parses the output as HTML
def get_soup(url):
    try:
        page = get_page(url)

        page_data = decode_page(page)
        #page_data = page.read()

        soup = BeautifulSoup(page_data, "html.parser")

        if not soup:
            return None;

        return soup
    except:
        return None

def check(array, string):
    for a in array:
        if a in string:
            return True;

    return False;

def initiate(name):
    female_array = ['female', 'Female', 'woman', 'Woman', 'girl', 'Girl'];
    male_array = ['male', 'Male', 'man', 'Man', 'boy', 'Boy'];

    for url in search(name + " baby names", stop = 5):
        source = get_soup(url);

        if not source or not source.title:
            continue;

        # or any(word in source.find_all('p') for word in female_array)
        if check(female_array, source.title) or check(female_array, url):
            return "Female";

        elif check(male_array, source.title) or check(male_array, url):
            return "Male";
        #print("++++++++++")

        #return "Ambiguous";
    return "Ambiguous"

#TRY ADDING COUNTERS
#TRY EXTRACTING THE OCCURENCES OF FEMALE AND MALE MENTIONS FROM THE COMPLETE SOURCE CIDE AND THEN COMPARE AT THE END

print(initiate("Nandita"))
print(initiate("Sabhya"))
print(initiate("Sampada"))
print(initiate("Raju"))
print(initiate("Veena"))
print(initiate("Sushil"))
