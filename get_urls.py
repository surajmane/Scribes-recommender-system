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
            this method will call Google API with the search query and get the top 50 results and call save to save those urls to a file
        """
        returned_urls = search(self.search_query, num=50)
        for url in returned_urls:
            if ('.pdf' in url):
                #print(url)
                self.urls_fetched.append(url)
        print("Urls fetched and filtered")
        self.save_output(self.urls_fetched)
        

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
