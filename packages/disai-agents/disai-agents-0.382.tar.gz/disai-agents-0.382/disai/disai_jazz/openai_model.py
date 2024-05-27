#  disai_jazz/openai_model.py
import openai
import os
from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup


load_dotenv()

class OpenAIModel:
    def __init__(self, api_key=None, model=None,serp_api_key=None):
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        openai.api_key = self.api_key
        self.client = openai.OpenAI(api_key=openai.api_key)
        self.model = model
        self.serp_api_key = serp_api_key

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
            task = (
                "You are a knowledgeable assistant. However, your dataset lasts till 2021, and it is 2024 now. "
                'If you do not have the information, reply only with "google: <your search query>". I will perform the search and provide the latest information.'
            )
            initial_prompt = f"{task}\n\n{prompt}"

            # Step 2: Attempt to generate a response
            response = self.client.chat.completions.create(
                temperature=0,
                model=self.model,
                messages=[
                    {"role": "system", "content": task},
                    {"role": "user", "content": initial_prompt}
                ]
            )
            result = response.choices[0].message.content

            # Step 3: Check for search request
            if result.strip().lower().startswith("google:"):
                search_query = result[len("google:"):].strip()
                search_results = self.search(search_query)

                # Step 4: Refine the prompt with search results
                refined_prompt = f"{prompt}\n\n{search_results}"
                refined_response = self.client.chat.completions.create(
                    model=self.model,
                    messages=[
                        {"role": "system", "content": task},
                        {"role": "user", "content": refined_prompt}
                    ]
                )
                final_result = refined_response.choices[0].message.content

                return final_result
            else:
                return result
        except Exception as e:
            return {"error": str(e)}    



