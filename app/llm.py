from huggingface_hub import InferenceClient
from dotenv import load_dotenv
import os


class LLM():

    def __init__(self):
            
        load_dotenv()

        self.__client = InferenceClient(
            api_key=os.getenv("HF_TOKEN"),
            provider="auto",
        )

        self.__messages = [
            {
                "role": "system",
                "content": "You are a helpful assistant that helps users find information."
            }
        ]

    def chat(self, query):

        self.__messages.append({"role": "user", "content": query})
        
        completion = self.__client.chat.completions.create(
            model="deepseek-ai/DeepSeek-V3-0324",
            messages = self.__messages
        )

        response = completion.choices[0].message.content

        self.__messages.append({"role": "assistant", "content": response})

        return response