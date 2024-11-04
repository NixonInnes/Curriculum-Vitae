import markdown
from weasyprint import HTML

# Convert Markdown to HTML
with open("README.md", "r") as md_file:
    md_content = md_file.read()
    html_content = markdown.markdown(md_content)

# Convert HTML to PDF
HTML(string=html_content).write_pdf("output.pdf")
