import bottlenose

AWS_ACCESS_KEY_ID = 'AKIAJPOZXW5IYMPUSPUA'
AWS_SECRET_ACCESS_KEY = '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'
AWS_ASSOCIATE_TAG = 'dolko-22'


amazon = bottlenose.Amazon(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_ASSOCIATE_TAG)

response = amazon.ItemSearch(Keywords="Harry Potter", ResponseGroup="ItemAttributes", SearchIndex="All")

print(response)

#need to parse the response somehow to get the actual details out