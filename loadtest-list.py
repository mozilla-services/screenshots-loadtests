# This is needed for doing the "from utils import (...)" below.
import sys; sys.path.append('.')

import utils

import random

from molotov import (
    global_setup,
    global_teardown,
    scenario,
    setup,
)

NUM_SAMPLE_SHOTS = random.randint(2, 2)


@global_setup()
def login(args):
    async def _create_shot(_):
        return await utils.create_shot()

    print("!!!!!", NUM_SAMPLE_SHOTS)
    _login = utils.login(args)

    # Upload X sample shots.
    for x in range(NUM_SAMPLE_SHOTS):
        res = utils.run_in_fresh_loop(_create_shot)
        assert res.status < 400

    return _login


@setup()
async def setup_worker(worker_id, args):
    return utils.setup_worker(worker_id, args)


@global_teardown()
def logout():
    return utils.logout()


@scenario(100)
async def list_shots(session):
    res = await utils.list_shots(session)
    # print("\n\n<<<", res, "\n>>>\n\n\n\n")
    # assert res.status == 200

    # print(await res.read())

    print("\n\n\n!!!!!!!!\n\n")
    payload = await res.json()
    print(payload)
    # print(await res.content.read(50))
    print("\n\n ¯\_(ツ)_/¯ ")
