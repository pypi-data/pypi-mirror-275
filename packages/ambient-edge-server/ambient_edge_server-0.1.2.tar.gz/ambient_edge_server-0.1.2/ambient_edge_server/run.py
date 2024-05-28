import uvicorn

from ambient_edge_server.app import app
from ambient_edge_server.utils import logger


def run():
    logger.debug("running server ...")
    logger.debug("running app: %s ...", app)
    uvicorn.run(app, host="0.0.0.0", port=7417)


if __name__ == "__main__":
    run()
