# Scribes-recommender-system
A recommender system for students to get lectures notes and scribes personalized with three options(Easy, medium and Hard)

There are two important files, recommender.py and get_url.py. Need to have both of these files in the same folder along with the imports file for it to work. The recommender.py contains the core of the project.

It could be either run on command prompt or as a module. On command promt the arguments are optional, make changes in the main file to get results for that query and specify the difficulty level. The script returns top 5 urls as a result.

To run, simply run the recommender.py script on the command prompt.

Mechanics:
- The query given by the user is sent to the Google Search API which returns the results in the form of URLs. Picking first 50 results.
- Saving these urls to a file and then reading each url to access files in it(focusing on just the pdf files).
- Reading pdfs in each of these URLs to get the readability measure of that document. This measure is used as a surrogate to judge the difficulty level. The     measures are Gunning fog, SMOG index and Automated readability index. To get a fair measure average of all these values are used.
- Using top 10 returned results along with the measures for final output.
- Sorting these 10 records, and returning 5 based on the difficulty measure given by the user.
