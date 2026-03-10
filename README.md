# Supply Chain AI Copilot

A small AI assistant that analyzes supply chain shipment data and answers operational questions using natural language.

## Features

- Upload and analyze shipment datasets
- Automatic computation of order processing time
- Shipping delay analysis
- Natural language queries using AI
- Interactive visualizations

## Example Questions

- Which warehouse has the highest shipping delay?
- Which product ships fastest?
- What is the average delay per warehouse?
- Which orders were delayed more than 3 days?

## Tech Stack

- Python
- Pandas
- Streamlit
- LangChain
- OpenAI API
- Plotly

## How to Run

Install dependencies

pip install -r requirements.txt

Run the application

streamlit run app.py

## Dataset

The dataset contains shipment information including:

- Order ID
- Product
- Warehouse
- Order Date
- Ship Date
- Delivery Date
- Quantity

From this data we compute:

- Processing Time
- Shipping Delay

## Limitation

The AI responses depend on the quality and size of the dataset.  
For larger real-world supply chain data, optimization and better data pipelines would be required.
