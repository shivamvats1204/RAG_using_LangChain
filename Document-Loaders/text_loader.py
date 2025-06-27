from langchain_community.document_loaders import TextLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

loader = TextLoader("poem.txt", encoding="utf-8")
docs=loader.load()

print("The variable docs contains:",docs,sep="\n")

print("\nThe datatype of docs: ",type(docs))

print("\nThe document object is the 0th element of the list:",docs[0],sep="\n")

print("\nThe data type of the 0th element of the list: ",type(docs[0]))

print("\nThe extracted content of the document is:",docs[0].page_content,sep="\n")

