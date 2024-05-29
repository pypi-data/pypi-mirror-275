from aiohttp import web
from aiohttp.web import *
from jinja2 import Environment, FileSystemLoader, select_autoescape, TemplateNotFound

templates_path = 'templates'

class Mango:
    def __init__(self, templates_path='templates'):
        self.app = web.Application()
        templates_path = templates_path
        _env = None
        Mango._env = Environment(loader=FileSystemLoader(templates_path),
                                 autoescape=select_autoescape(['html', 'xml']))  


    def route(self, path, methods=['GET']):
        def decorator(handler):
            async def wrapper(request):
                response = await handler(request)
                if isinstance(response, web.Response): 
                    return response  
                if isinstance(response, str):
                    return web.Response(text=response, content_type='text/plain')
            for method in methods:
                self.app.router.add_route(method, path, wrapper)
            return handler
        return decorator
    
    @classmethod
    def get_env(cls):
        if cls._env is None:
            raise ValueError("Jinja2 environment not initialized.")
        return cls._env


    def run(self, host='127.0.0.1', port=8080):
        web.run_app(self.app, host=host, port=port)




        

async def render(request, template_source, context={}):
    env = Mango.get_env()
    try:
        template = env.get_template(template_source)
    except TemplateNotFound:
        template = env.from_string(template_source)  
    return web.Response(text=template.render(context), content_type='text/html')