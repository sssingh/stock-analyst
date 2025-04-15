system_prompt = """
You are an expert stock market analyst who can conduct an in-depth analysis 
of a given stock. Provide a brief commentry at the end of each section 
highlighting the important points in the section if relevant. Your language 
should be {style}. You will produce a markdown formatted output. Use bullets, 
emojis and tables where appropriate. 
"""

user_prompts = [
    """
    The stock we are looking at is {stock}. Analyze the stock based on below
    listed guidelines...
    1. Give the market size associated with the stock
    2. Give a breakdown of the leaders with market share.
    3. Give a breakdown of the leaders with their revenue per / year
    """,
    """
    4. Give the moat for the company.
    5. Give a chart of the last 5 years for revenue and net margin.
    6. Give me a comparison of the revenue/margin compared to the top leaders
       in the market that are publicly traded stocks
    """,
    """
    7. Decide with the ideal conditions if the company is investable with a 
       rating from 0 to 10 being the best company for the next 10 years. 
       The metrics we want to check are TAM is high growth, company revenue 
       has grown 10-30% year afer year, company margins are always profitable
       and increasing or margins are transitioning to profitable, P/E ratio 
       relative to the growth of the company and industry relative peers 
       is not too expensive. Under 50 P/E is ideal and the lower the better. 
       Place more weighting in how consistent the revenue is growing every 
       single year as well as how stable / increasing the margins are.
    """,
    """
    8. Provide all the current / future revenue streams of the company
    9. If this company continues to innovate then give a projection up 
       to year 2030 on all those revenues and margins.
    """,
    """
    10. Provide the bulleted list of links to articles/webpages from where you 
        picked up information to conduct the research.
    """,
]
