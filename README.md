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

