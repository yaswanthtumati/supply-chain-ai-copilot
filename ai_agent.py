import google.generativeai as genai

def create_agent(df):

    genai.configure(api_key="AIzaSyDo4UuZDjAzy4OdJHEzjIF4JwYfwNKYVUc")

    model = genai.GenerativeModel("gemini-2.5-flash")

    def ask_agent(question):
        data_context = df.head(50).to_string()
        
        prompt = f"""
        You are a supply chain analyst.

        Here is the dataset:
        {data_context}

        Question: {question}
        """

        response = model.generate_content(prompt)

        return response.text

    return ask_agent