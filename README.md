# Stock Analyst

> Given a stock symbol the Stock Analyst will leverage the power of 
> `Large Language Model (LLM)` to conduct an in depth fundamental analysis
> and generate a well formatted report that can be copied in `markdown`
> format or can be downloaded in `pdf`.

## App High Level Design

![Abstract](/shared/readme-conceptual-design-abstract.png)

![Concrete](/shared/readme-conceptual-design-concrete.png)

## App Interface and Usage

![App Interface](/shared/app-usage.png "title")

## Installation and Run
* By default app uses `Azure` hosted `gpt-4o-mini`, If you are also using azure 
hosted model then create `.env` file and supply below details. An sample is 
provided in `.env_example`:  
  AZURE_OPENAI_API_KEY   
  AZURE_OPENAI_ENDPOINT   
  AZURE_OPENAI_LLM_DEPLOYMENT_ID   
  AZURE_OPENAI_API_VERSION     

* If using OpenAI hosted model then:
  - create `.env` file and supply OPENAI_API_KEY, A sample is provided 
  in `.env_example`  
  - replace line 15 in `process.py` to 
  `llm = lc.connect(host="openai", model=<openai-model-name>)`  

* If using Ollama running locally then:
  - replace line 15 in `process.py` 
  to `llm = lc.connect(host="ollama", model=<ollama-model-name>)`  
  
> Note that when using small open source model the output may not be as good 
> as when using openai models.

```console
cd path/to/your/directory
git clone https://github.com/sssingh/stock-analyst.git
cd stock-analyst
python -m venv .venv
source .venv/Scripts/activate
pip install -r requirements.txt
python app.py
[Open the shown url in your browser]
```

