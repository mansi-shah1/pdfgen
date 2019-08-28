from aiohttp import web
import aiohttp_jinja2
import pdfkit
from settings import BASE_DIR

@aiohttp_jinja2.template('index.html')
async def index(request):
    questions = ["Who?", "What?"]
    context = {'questions': questions}
    response = aiohttp_jinja2.render_string('index.html',
                                              request,
                                              context)
    return {"questions": questions}

async def pdf(request):
    communities = ["technologists", "thinkers", "builders"]
    context = {'communities': communities}
    response = aiohttp_jinja2.render_string('template.html',
                                              request,
                                              context)
    output_file_path = str(BASE_DIR / 'aiohttp_pdfkit' / 'static' / 'pdf' / 'output.pdf')
    await generate_pdf(response, output_file_path)

    data = {'pdf_file': output_file_path}
    return web.json_response(data)

async def generate_pdf(html_string, output_file_path):
    pdfkit.from_string(html_string, output_file_path)