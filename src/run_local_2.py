from langchain import PromptTemplate
from langchain import LLMChain
from langchain.llms import CTransformers
from src.helper import *

B_INST , E_INST = "[INST]", "[/INST]"
B_SYS , E_SYS = "<<SYS>>\n", "\n<</SYS>>\n\n"

instruction = "Provide a good summary of the following book : \n\n {text}"

SYSTEM_PROMPT = B_SYS + CUSTOM_SYSTEM_PROMPT_TRNSLATION + E_SYS
template = B_INST + SYSTEM_PROMPT + instruction + E_INST

prompt = PromptTemplate(template=template, input_variables= ["text"])

llm = CTransformers(model= 'model/llama-2-7b-chat.ggmlv3.q4_0.bin', 
                    model_type='llama',config={'max_new_tokens':2000,'temperature': 0.01})

LLM_Chain = LLMChain(prompt=prompt, llm = llm )

print(LLM_Chain.run('Harry Potter and the Prisoner of Azkaban'))