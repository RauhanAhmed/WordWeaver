from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq

prompt = """
### INSTRUCTIONS:
You are an excellent, state-of-the-art text summarizer model which gives accurate summaries of the text
you are provided, with no loss of information. You are given the task of summarizing another piece of text, please do not add to it anything by yourself and give accurate summary under 500 words.
Just directly put the summary in the answer and no need to addd anything before or after to it. Do not let the user know that you are an LLM behind the scenes and act just as a summarizer.

### INPUT TEXT:
{text}
"""

### defining a utility function
def getTextSummary(text: str) -> str:
    global prompt
    promptTemplate = ChatPromptTemplate.from_template(template = prompt)
    llmModel = "llama-3.1-8b-instant"
    llm = ChatGroq(model_name = llmModel, temperature = 0.7, max_tokens = 512)
    parser = StrOutputParser()

    chain = {"text": RunnablePassthrough()} | promptTemplate | llm | parser
    result = chain.invoke(text)

    return {
        "summary": result
    }