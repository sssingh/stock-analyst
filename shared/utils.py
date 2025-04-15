"""Generic utility/helper functions"""

from pathlib import Path
from markdown_pdf import MarkdownPdf, Section

REPORT_FILE_PATH = Path(__file__).parent.parent / "data" / "report.pdf"


def save_md_as_pdf(
    md_contents: str, file_path: str = "report.pdf", title: str = ""
):
    """Convert markdown formatted text into PDF doc and save as PDF file.

    Args:
        md_contents (str): markdown format text.
        file_name (str, optional): The PDF file name. Defaults to "report.pdf".
        title (str, optional): title of PDF doc. Defaults to "".
    """
    pdf = MarkdownPdf()
    pdf.meta["title"] = title
    pdf.add_section(Section(md_contents, toc=True))
    pdf.save(file_path)
