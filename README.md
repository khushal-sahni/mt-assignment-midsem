# Program to convert dictionaries into concepts and stuff
## Algorithm:
### 1.Web Data Scraping
1.The requests library of python was used with URL given as input to get the request and web page, for every page of the dictionary.
2.Beautiful soup library was used to pull the data out of the HTML file.
3.We now get one long string for each page, and we split the string to get the pairs of Hindi words with their English meaning.
### 2.Conversion into WX Notation
1.wxconv library was used for the conversion of Hindi words to their WX Notation.
2.We now create a python-dictionary with wx converted word as key,
###
**3.Finding the Parts of Speech (POS)-** POS were found using NLTK library’s tokenizer and pos_tag module.

**4.Formation of sentence-** Parsing in the English word along with its matching POS to generate sentences using python API.

**5.Running the ACE Parser-** Now the ACE Parser takes a) the generated sentence, b) compiled grammar as ‘erg.dat’ extension file path and c) binary file from the ace parser as input and it gives the MRS concept string as output. It was run using pydelphin in python.

**6.Extraction from ACE Parser output-** We now extract MRS concept and MRS concept feature value from the MRS concept string generated as output of ACE Parser.

**7.Storing the information in dictionaries-** A function was written to modify the entries according to the H_concept-to-mrs-rels.dat file format and then added to the H_concept.


### Glossary:
#### 1.Request and Beautiful Soup:
By using both the Request and Beautiful Soup library we can extract data from websites that don't run JavaScript.
The request library helps us make HTTP requests in Python. Thanks to this, we can get the content of a website. Then we use a parser (e.g., html.parser, lxml, etc) and Beautiful Soup to extract any data within the website.







