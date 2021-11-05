from imports import *
class GET_URLS:
    """
        This class encodes methods and variables required to fetch the query results only from educational websites.
        We intend to call the methods of this class only once to limit the number of calls to the Google API.
    """
    def __init__(self, search_query):
        super().__init__()
        self.search_query = search_query + " lecture notes" #the Query user will provide concatenated along with lecture notes
        self.urls_fetched = []
        self.file_name = ''

    #def __getattribute__(self, toSearch):
     #   return f''
        #return super().__getattribute__(name)

    def fetch_urls(self):
        """
            this method will call Google API with the search query and get the top 50 results, returns those results
        """
        returned_urls = search(self.search_query, num=50)
        for url in returned_urls:
            if ('.pdf' in url):
                #print(url)
                self.urls_fetched.append(url)
        print("Urls fetched and filtered")
        #print(self.urls_fetched)
        return self.urls_fetched

    def get_relevant_urls(self):

        """
            This method uses the 50 search results returned by fetch_urls and keeps only those which are from educational sites,
            returns nothing. Makes a call to fetch_urls()
        """
        print("this is the first function to be called with query = ", self.search_query)
        rel_urls = self.fetch_urls()
        self.save_output(rel_urls)

    def save_output(self, rel):

        """
            This method saves the results of get_relevant_urls() in a file named as the query input by the user,
            this is done to avoid limiting the calls to Google Api, this will be called only for the first time for a new query.
        """
        
        print("saving Urls now")
        text = self.search_query.split(" ")
        word = ''
        for words in text:
            word = word + '_' + words
        self.file_name = word+'.txt'
        i = 0
        #print("file name is", self.file_name)
        with open(self.file_name, 'a') as f:
            while i < 10:
                f.write(rel[i]+'\n')
                i +=1

class GET_DIFFICULTY(GET_URLS):
    """
        This class is used to get the difficulty measure of the websites returned
        by Google API, three measure together are used which are Flesch reading score, SMOG index and
        Dale Chall score.
    """
    def __init__(self, query, difficulty):
        self.query = query
        self.difficulty = difficulty
        super().__init__(query)
        self.num_syllables = 0
        self.text = ''
        self.words = []
        self.sentences = []
        self.avg_diff = {}

    def tokenize_urls(self):
        """
            This function will initiate the whole process, send a query, fetch the results, tokenize them and get them evaluated.
            It returns the difficulty levels of each URL.
        """
        #counter = 0
        self.get_relevant_urls()
        with open(self.file_name, 'r') as f:
            for url in f.readlines():
                #print("The url being worked on is: ", url)
                try:
                    response = urllib.request.urlopen(url)
                except:
                    continue
                
                with open("test.pdf", 'wb') as file:
                    file.write(response.read())

                with open("test.pdf", "rb") as f:
                    try:
                        pdf = PdfFileReader(f)
                    except:
                        continue
                    info = pdf.getDocumentInfo()
                    pages = pdf.getNumPages()
                    #print ("number of pages: %i" % pages)
                    for i in range(pages):
                        if i < 50:
                            page = pdf.getPage(i)
                            self.text  += page.extractText()
                        else:
                            break
                    self.evaluate_difficulty(url)
        #print("The average difficulties are as below")
        #print(self.avg_diff)
        print("The results according to difficulty level = ",self.difficulty)
        self.return_results()
        #
                
        
    def evaluate_difficulty(self, url):
        """
            To get a measure of difficulty for the documents.
        """
        self.avg_diff[url] = (textstat.gunning_fog(self.text) + textstat.smog_index(self.text) + textstat.automated_readability_index(self.text)) / 3

    def return_results(self):
        """
            This is the final function that is called to evaluate the results based on the difficulty level. Returns 5 urls.
        """
        size = len(self.avg_diff) - 1
        sorted_results = sorted(self.avg_diff)
        if self.difficulty == 'easy' or self.difficulty == 'EASY':
            
            for i in range(0, 5):
                print(sorted_results[i])
        elif self.difficulty == 'medium' or self.difficulty == 'MEDIUM':
            mid = int(size/2)
            for i in range(mid-2, mid+3):
                print(sorted_results[i])
        else:
            for i in range(0, 5):
                print(sorted_results[size-i])

        
        
        
#obj = get_urls('Data Science')
def main():
    print(sys.argv[1], sys.argv[2])
    obj1 = GET_DIFFICULTY("unsupervised learning", "medium")
    obj1.tokenize_urls()

if __name__ == "__main__":
    main()
