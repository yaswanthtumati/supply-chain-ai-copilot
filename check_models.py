import google.generativeai as genai

genai.configure(api_key="AIzaSyDo4UuZDjAzy4OdJHEzjIF4JwYfwNKYVUc")

for m in genai.list_models():
    print(m.name)