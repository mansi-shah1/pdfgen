from views import index, pdf
from settings import BASE_DIR

def setup_routes(app):
    app.router.add_get('/', index)
    app.router.add_post('/pdf', pdf)


def setup_static_routes(app):
    app.router.add_static('/static/', path=str(BASE_DIR / 'aiohttp_pdfkit' / 'static'), show_index=True)

