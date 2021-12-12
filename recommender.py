import time
start_time = time.time()
from imports import *
from get_urls import *

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
        self.text = ''
        self.avg_diff = {}

    def read_urls(self):
        """
            This function will initiate the whole process, send a query, fetch the results, and get them evaluated.
            It returns the difficulty levels of each URL.
        """
        
        self.fetch_urls()
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
                    try:
                        info = pdf.getDocumentInfo()
                        pages = pdf.getNumPages()
                    except:
                        continue
                    #print ("number of pages: %i" % pages)
                    for i in range(pages):
                        if i < 20:
                            page = pdf.getPage(i)
                            self.text  += page.extractText()
                        else:
                            break
                    self.evaluate_difficulty(url)
        print("The results according to difficulty level = ",self.difficulty)
                
            
        self.return_results()
        #
                
        
    def evaluate_difficulty(self, url):
        """
            To get a measure of difficulty for the documents.
        """
        self.avg_diff[url] = textstat.smog_index(self.text)

    def return_results(self):
        """
            This is the final function that is called to evaluate the results based on the difficulty level. Returns 5 urls.
        """
        size = len(self.avg_diff) - 1
        print('Number of URLs left after filtering are = ', size)
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

        
        
        

def main():
    obj1 = GET_DIFFICULTY("unsupervised learning", "hard")
    obj1.read_urls()

if __name__ == "__main__":
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
