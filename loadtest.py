# This is needed for doing the "from utils import (...)" below.
import sys; sys.path.append('.')

import json
from urllib.parse import urljoin

from utils import (
    SERVER_URL,
    do_login,
    do_logout,
    do_setup_worker,
    get_example_images,
    make_device_info,
    make_example_shot,
    make_uuid,
)

from molotov import (
    scenario,
    global_setup,
    global_teardown,
    setup,
)


@global_setup()
def login(args):
    return do_login(args)


@setup()
async def setup_worker(worker_id, args):
    return do_setup_worker(worker_id, args)


@global_teardown()
def logout():
    return do_logout()


@scenario(100)
async def create_shot(session):
    path_pageshot = urljoin(SERVER_URL, "data/{}/test.com".format(make_uuid()))
    data = make_example_shot()
    headers = {'content-type': 'application/json'}

    async with session.put(path_pageshot, data=json.dumps(data), headers=headers) as r:
        assert r.status < 400
