# Project name - twitter-advertiser-list-converter
# Author - staticsafe
# Purpose - Converts Twitter provided advertiser list PDF to a CSV file of user-ids that can be imported as a blocklist.
# Editorial - Use Mastodon instead.

import PyPDF2

pdfFileObj = open('C:\\Users\\sadiq\\Downloads\\temp\\twitter_advertiser_list.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
numberOfPages = pdfReader.getNumPages()
pageObj = []
for pages in range(numberOfPages):
    pageObj.append(pdfReader.getPage(pages))
    print(pageObj[pages].extractText())


