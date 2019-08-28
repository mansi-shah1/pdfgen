# aiohttpdemo_polls/main.py
from aiohttp import web
from routes import setup_routes, setup_static_routes
from settings import BASE_DIR
import aiohttp_jinja2
import jinja2


app = web.Application()
aiohttp_jinja2.setup(app,
    loader=jinja2.FileSystemLoader(str(BASE_DIR / 'aiohttp_pdfkit' / 'templates')))
app['static_root_url'] = str(BASE_DIR / 'aiohttp_pdfkit' / 'static')
setup_routes(app)
setup_static_routes(app)
web.run_app(app)