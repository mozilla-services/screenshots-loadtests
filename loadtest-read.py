# This is needed for doing the "from utils import (...)" below.
import sys; sys.path.append('.')

import utils

from molotov import (
    global_setup,
    global_teardown,
    scenario,
    setup,
)

SHOT = None


@global_setup()
def login(args):
    async def _create_shot(_):
        return await utils.create_shot()

    global SHOT

    _login = utils.login(args)

    res = utils.run_in_fresh_loop(_create_shot)
    assert res.status < 400
    SHOT = res.path
    return _login


@setup()
async def setup_worker(worker_id, args):
    return utils.setup_worker(worker_id, args)


@global_teardown()
def logout():
    return utils.logout()


@scenario(100)
async def read_shot(session):
    res = await utils.read_shot(session, SHOT)
    assert res.status == 200
    print("....", res)
