# This is needed for doing the "from utils import (...)" below.
import sys; sys.path.append('.')

import json
from urllib.parse import urljoin

import utils

from molotov import (
    scenario,
    global_setup,
    global_teardown,
    setup,
)


@global_setup()
def login(args):
    return utils.login(args)


@setup()
async def setup_worker(worker_id, args):
    return utils.setup_worker(worker_id, args)


@global_teardown()
def logout():
    return utils.logout()


@scenario(100)
async def create_shot(session):
    res = await utils.create_shot(session)
    assert res.status < 400


@scenario(100)
async def read_shot(session):
    shot = await utils.create_shot(session)
    assert shot.status < 400

    res = await utils.read_shot(session, shot.path)
    assert res.status < 400
