from fastapi import FastAPI
from models import db
import views
import pkgutil

import logging
logger = logging.getLogger("uvicorn.error")

# TODO: Understand and come up with a strategy for unifying the various loggers.
# logging.basicConfig(level=logging.INFO)
# For example, adjusting log levels with basicConfig shows loggers from:
#  gino.ext.starlette, uvicorn.error, gino.engine._SAEngine, etc..


def load_modules(app=None):
    # walk and import each module from views
    path = views.__path__
    prefix = views.__name__ + "."
    for importer, modname, ispkg in pkgutil.iter_modules(path, prefix):
        module = importer.find_module(modname).load_module(modname)
        # load individual routes from each view into FastAPI app
        # skip this process when app is None (for example, during alembic runs)
        if app:
            init_app = getattr(module, "init_app", None)
            if init_app:
                init_app(app)
                logger.info(f"Imported routes from {modname} module.")


def load_app():
    app = FastAPI(title="Rando Server")
    db.init_app(app)
    load_modules(app)
    return app


app = load_app()
