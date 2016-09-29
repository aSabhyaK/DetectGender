from google import search
import urllib.request
from bs4 import BeautifulSoup

#decodes the page object obtained from BeautifulSoup
def decode_page(page):
    #extract the encoding of the page object
    encoding = page.info().get("Content-Encoding")

    #in case the webpage is compressed using any of the following compression schemes
    if encoding in ('gzip', 'x-gzip', 'deflate'):
        #get the content of the page
        content = page.read()

        #in case of 'deflate' encoding
        if encoding == 'deflate':
            data = StringIO.StringIO(zlib.decompress(content))
        else:
            try:
                #handling the case where the source code of a page is compressed with 'gzip' or 'x-gzip'
                data = zlib.decompress(content, 16+zlib.MAX_WBITS)
                return data;
            except:
                return None

        page = data.read()

    return page

#opens a URL
def get_page(url):
    try:
        return urllib.request.urlopen(url)
    except:
        return None

#invokes the decoder method and parses the output as HTML
def get_soup(url):
    try:
        #getting the page object from the method get_page
        page = get_page(url)
        #decoding page to be able to extract the contents of webpages which are encoded
        page_data = decode_page(page)
        #creating a soup object out of the page_data using an html parser
        soup = BeautifulSoup(page_data, "html.parser")

        #in case the soup object is null
        if not soup:
            return None;

        return soup
    except:
        return None

#checks if any value present within the array 'array' exists within the string 'string' or not
def exists(array, string, identifier):

    counter = 0;
    #looping over the array
    for element in array:
        #extracting each element from array and checking if it exists in string or not
        if element in string:
            if identifier == 'src':
                counter += 2;
            elif identifier == 'title':
                counter += 10;
            else:
                counter += 20;

    #in case nothing is found
    return counter;

#deduces the gender associated with 'name' by scraping the Google results
def gender_scraping(name):

    #defining the words associated with each sex in an array for lookup
    female_array = ['female', 'woman', 'girl', 'feminine'];
    male_array = ['male', 'man', 'boy', 'masculine'];

    female_counter = 0;
    male_counter = 0;

    #looping over each URL obtained as a part of the Google search
    for url in search(name + " baby names", stop = 5):
        source = get_soup(url);

        if not source or not source.title:
            continue;

        #converting both the URL and the source code into lower cases
        url = url.lower();
        source_text = str(source).lower();

        female_counter += exists(female_array, str(source.title).lower(), 'title');
        female_counter += exists(female_array, url, 'url');
        female_counter += exists(female_array, source_text, 'src');

        male_counter += exists(male_array, str(source.title).lower(), 'title');
        male_counter += exists(male_array, url, 'url');
        male_counter += exists(male_array, source_text, 'src');

    return [female_counter, male_counter];

#deduces the gender associated with 'name' using the concept that most of the names of Indian women end with an 'a' or an 'i'
def gender_last_character(name):
    #removing leading and trailing whitespaces
    name = name.strip();

    #invalid name in case the length of the name is less than 3
    if len(name) < 3:
        return "Invalid";

    #implying the fact that 'a large percentage' of the Indian female names
    #end with a or i
    female_indicator_1 = 97;
    female_indicator_2 = 105;

    #directly compare with integers
    #no hexing

    #extract the last character of the argument
    value = ord(name[-1].lower());

    female_counter = 0;
    male_counter = 0;

    #checking whether the name ends with a or i
    if value == female_indicator_1 or value == female_indicator_2:
        female_counter += 2;

    else:
        male_counter += 2;

    return [female_counter, male_counter];

#triggering the complete process
def initiate(name):

    #extracting the genders using both the approaches
    gender_array_1 = gender_scraping(name);
    gender_array_2 = gender_last_character(name);

    female_counter = gender_array_1[0] + gender_array_2[0];
    male_counter = gender_array_1[1] + gender_array_2[1];

    #compare the obtained values
    if female_counter > male_counter:
        return "Female";

    elif female_counter < male_counter:
        return "Male";

    return "Ambiguous";

print(initiate("Nandita"))
print(initiate("Raju"))
print(initiate("Sampada"))
print(initiate("Sabhya"))
print(initiate("Ankita"))
print(initiate("Sushil"))
print(initiate("Rahul"))
print(initiate("PRIYA"))
print(initiate("Albert"))
print(initiate("Sia"))
print(initiate("Mark"))
print(initiate("Rachel"))
print(initiate("Monica"))
print(initiate("Charlie"))
print(initiate("Alan"))
print(initiate("Priscilla"))
