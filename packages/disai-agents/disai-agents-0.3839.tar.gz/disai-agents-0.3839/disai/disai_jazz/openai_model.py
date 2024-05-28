#  disai_jazz/openai_model.py
import openai
import os
from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup


load_dotenv()

class OpenAIModel:
    def __init__(self, api_key=None, model=None,chat_history=[]):
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        openai.api_key = self.api_key
        self.client = openai.OpenAI(api_key=openai.api_key)
        self.model = model
        self.chat_history=chat_history
        task = (
                "I am a knowledgeable assistant and chatbot. However, my dataset lasts only till 2021 "
                'before I reply I will see if you are talking to me like a conversation or asking a question, if you are asking a question I will try to answer it.'
                'If I do not have the information, I will explicitly reply only with "google: <your search query>". Then you will provide me with relevant context after the google search along with query.'
        )
        self.chat_history.append({"role": "system", "content": task})

    #agent to generate images
    def generate_image(self, prompt):
        response = self.client.images.generate(
            prompt=prompt,
            n=1,
            model=self.model,
            size="1024x1024",
            quality="standard",
        )
        return response.data[0].url
    
    #agent that has access to internet
    def search(self,input_query):
        user_query = input_query.replace(' ', '+')
        URL = "https://www.google.co.in/search?q=" + user_query

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.57'
        }

        try:
            page = requests.get(URL, headers=headers)
            soup = BeautifulSoup(page.content, 'html.parser')
            
            # Get the entire text content of the page
            text_content = soup.get_text()
            
            # Find the index where the relevant information starts
            start_index = text_content.find("Search Results") + len("Search Results")
            
            # Print the relevant information
            return(text_content[start_index:].strip())
        except:
            return "An error occurred while fetching the search results. Please try again later."

        
    def webagent(self,prompt):
        try:
            # Step 1: Initial instruction to the LLM
            initial_prompt = f"{prompt}"
            self.chat_history.append({"role": "user", "content": initial_prompt})

            # Step 2: Attempt to generate a response
            response = self.client.chat.completions.create(
                temperature=0.3,
                model=self.model,
                messages=self.chat_history
            )
            result = response.choices[0].message.content


            # Step 3: Check for search request
            if result.strip().lower().startswith("google:"):
                search_query = result[len("google:"):].strip()
                search_results = self.search(search_query)
                #print(search_results)


                # Step 4: Refine the prompt with search results
                refined_prompt = f"'Okay sure here is the google'd information:'\n{search_results}"
                self.chat_history.append({"role": "user", "content": refined_prompt})
                refined_response = self.client.chat.completions.create(
                    temperature=0.3,
                    model=self.model,
                    messages=self.chat_history
                )
                final_result = refined_response.choices[0].message.content

                return final_result
            else:
                task = (
                        "I am a knowledgeable assistant and chatbot. However, my dataset lasts only till 2021 "
                        'before I reply I will see if you are talking to me like a conversation or asking a question, if you are asking a question I will try to answer it.'
                        'If I do not have the information, I will explicitly reply only with "google: <your search query>". Then you will provide me with relevant context after the google search along with query.'
                )
                self.chat_history.append({"role": "system", "content": task})

                return result
        except Exception as e:
            return {"error": str(e)}    



