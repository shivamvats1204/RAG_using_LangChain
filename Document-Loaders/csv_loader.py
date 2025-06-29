from langchain_community.document_loaders import CSVLoader

loader= CSVLoader("WHR_2023.csv")
docs = loader.load()

print(len(docs))

print(docs[1].page_content)
print(docs[1].metadata)