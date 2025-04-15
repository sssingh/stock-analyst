"""Backend functionality testing script"""

from backend import lc
from backend.prompts import system_prompt, user_prompts
from IPython.display import display, Markdown

llm = lc.connect("azure")
prompt_template = lc.make_prompt_template(
    system_prompt=system_prompt,
    user_prompt="\n".join(user_prompts),
)

response = lc.predict(
    style="Professional", stock="NVDA", llm=llm, prompt_template=prompt_template
)
display(Markdown(response))
