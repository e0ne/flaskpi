import config
from main import app_factory

app = app_factory(config=config.Production)

