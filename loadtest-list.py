# This is needed for doing the "from utils import (...)" below.
import sys; sys.path.append('.')

import os
import random
import time
import utils

from molotov import (
    global_setup,
    global_teardown,
    scenario,
    setup,
)

NUM_SAMPLE_SHOTS = random.randint(4, 7)
NUM_SEARCH_HITS = 2

WEIGHT_LIST_SHOTS = int(os.getenv('WEIGHT_LIST_SHOTS') or '0')
WEIGHT_SEARCH_SHOTS = int(os.getenv('WEIGHT_SEARCH_SHOTS') or '0')


@global_setup()
def login_and_create_shots(args):
    async def _create_shot(_):
        return await utils.create_shot()

    async def _create_shot_w_keywords(_):
        return await utils.create_shot(keywords="HIT")

    _login = utils.login(args)

    # Upload X sample shots.
    for x in range(NUM_SAMPLE_SHOTS):
        if (x < NUM_SEARCH_HITS):
            res = utils.run_in_fresh_loop(_create_shot_w_keywords)
            assert res.status < 400
        else:
            res = utils.run_in_fresh_loop(_create_shot)
            assert res.status < 400

    time.sleep(1)  # delays for 1 seconds

    return _login


@setup()
async def setup_worker(worker_id, args):
    return utils.setup_worker(worker_id, args)


@global_teardown()
def logout():
    return utils.logout()


@scenario(WEIGHT_LIST_SHOTS)
async def list_shots(session):
    res = await utils.list_shots(session)

    assert res.status == 200
    assert len(res.bod["shots"]) == NUM_SAMPLE_SHOTS


@scenario(WEIGHT_SEARCH_SHOTS)
async def search_shots(session):
    res = await utils.search_shots(session, "HIT")

    assert res.status == 200
    assert len(res.bod["shots"]) == NUM_SEARCH_HITS
