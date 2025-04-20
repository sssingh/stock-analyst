import gradio as gr
from backend import lc
from backend.prompts import system_prompt, user_prompts
from shared.utils import save_md_as_pdf, REPORT_FILE_PATH

llm = lc.connect(host="azure")
prompt_template = lc.make_prompt_template(
    system_prompt=system_prompt,
    user_prompt="\n".join(user_prompts),
)


def lsnr_analyze_stock(style: str, stock: str) -> gr.Markdown:
    response = lc.predict(
        style=style,
        stock=stock,
        llm=llm,
        prompt_template=prompt_template,
    )
    # prepare markdown output and make it visible now
    print("[INFO]: Formatting LLM response as markdown...")
    mkdn_output = gr.Markdown(value=response, show_copy_button=True)
    print("[INFO]: Saving markdown report in PDF format...")
    try:
        save_md_as_pdf(md_contents=response, file_path=REPORT_FILE_PATH)
    except Exception as e:
        print("[ERROR] - Creating report PDF!")
        print(e)
    else:
        print("[INFO]: DONE")
        btn_download = gr.DownloadButton(
            label="Download Report",
            value=REPORT_FILE_PATH,
            visible=True,
            elem_id="btn_download",
            icon="frontend/download.png",
        )
    return mkdn_output, btn_download


def lsnr_clear_output() -> gr.Markdown:
    mkdn_output = gr.Markdown(value="", show_copy_button=False, min_height=100)
    btn_download = gr.DownloadButton(visible=False)
    return mkdn_output, btn_download


with gr.Blocks(theme=gr.themes.Citrus(), css_paths="frontend/app.css") as demo:
    ## right panel - Markdown output, initally hidden
    mkdn_output = gr.Markdown(value="", show_copy_button=False, min_height=100)
    ## left panel - inputs
    with gr.Sidebar(position="left"):
        ### ui elements
        tbox_stock = gr.Textbox(
            placeholder="Enter stock symbol...", label="Stock Symbol:"
        )
        ddwn_style = gr.Dropdown(
            choices=["Professional", "Playful"],
            value="Professional",
            label="Style:",
        )

        btn_analyze = gr.Button(
            value="Analyze Stock",
            icon="frontend/gears.png",
        )

        btn_clear = gr.Button(
            value="Clear Output",
            icon="frontend/clear.png",
            elem_id="btn_clear",
        )

        btn_download = gr.DownloadButton(visible=False)

        ### event handlers
        btn_analyze.click(
            fn=lsnr_analyze_stock,
            inputs=[ddwn_style, tbox_stock],
            outputs=[mkdn_output, btn_download],
        )
        btn_clear.click(
            fn=lsnr_clear_output,
            inputs=None,
            outputs=[mkdn_output, btn_download],
        )
