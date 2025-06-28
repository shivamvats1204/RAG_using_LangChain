from langchain_community.document_loaders import TextLoader
from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

# part-1 of the code
loader = TextLoader("poem.txt", encoding="utf-8")
docs=loader.load()

print("The variable docs contains:",docs,sep="\n")

print("\nThe datatype of docs: ",type(docs))

print("\nThe document object is the 0th element of the list:",docs[0],sep="\n")

print("\nThe data type of the 0th element of the list: ",type(docs[0]))

print("\nThe extracted content of the document is:",docs[0].page_content,sep="\n")


# part-2 of the code
load_dotenv()
 
# Uncomment the following line to use OpenAI's Chat model
#model=ChatOpenAI()

# Using Groq's Chat model
model = ChatGroq(model_name="mistral-saba-24b")
prompt=PromptTemplate(
    template="Write a short summary about this poem: \n{poem}",
    input_variables=["poem"],
)

parser=StrOutputParser()

chain = prompt | model | parser

print("The summary of the poem is:",chain.invoke({"poem":docs[0].page_content}),sep="\n")
