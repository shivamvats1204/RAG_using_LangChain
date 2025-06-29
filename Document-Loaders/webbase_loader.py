from langchain_community.document_loaders import WebBaseLoader
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

url="https://shivamvats.netlify.app/"
loader = WebBaseLoader(url)

docs = loader.load()
print(len(docs))
print("\n Website's content is:", docs[0].page_content, sep="\n")

# Creating Resume using Groq's Chat model
model = ChatGroq(model_name="mistral-saba-24b")
prompt=PromptTemplate(
    template="Create a resume for the following profile: \n{profile}",
    input_variables=["profile"],
)

parser=StrOutputParser()

chain = prompt | model | parser

print("Resume created:",chain.invoke({"profile":docs[0].page_content}),sep="\n")
