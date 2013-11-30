# -*- coding: utf-8 -*-

import urlparse

import pytest

from multiprocessing import Process, Queue

from app import app as application, db as database


@pytest.fixture
def db(request):

    def fin():
        # smazeme vsechny vytvorene kolekce
        dtb = database.connection[app.config['MONGODB_SETTINGS']['DB']]
        if (app.config['MONGODB_SETTINGS']['USER'] and
                app.config['MONGODB_SETTINGS']['PASSWORD']):
            dtb.authenticate(app.config['MONGODB_SETTINGS']['USER'],
                             app.config['MONGODB_SETTINGS']['PASSWORD'])

        for name in dtb.collection_names():
            if not name.startswith('system'):
                dtb.drop_collection(name)

    request.addfinalizer(fin)

    return database


@pytest.fixture
def app():
    return application


@pytest.fixture
def client():
    return application.test_client()


def run_app(queue):
    '''
    Run app test server.
    '''

    # close all outputs
    import sys
    import os
    sys.stdout.close()
    sys.stdout = open(os.devnull)
    sys.stderr.close()
    sys.stderr = sys.stdout

    schema = u'http'
    host = u'localhost'
    port = 5555

    for i in xrange(50000):
        port = port + i
        try:
            app.run(host=host, port=port)
            break
        except IOError:
            pass

    queue.put([schema, host, port])


@pytest.fixture(scope='session')
def live_server(request):
    server = {}

    queue = Queue()
    p = Process(target=run_app, args=(queue, ))
    p.start()

    # get data from child process
    schema, host, port = queue.get()

    server['schema'] = schema
    server['host'] = host
    server['port'] = port

    # helper function for url creation
    server["url"] = lambda url: urlparse.urljoin('%s://%s:%d' % (schema, host, port), url)

    server['process'] = p

    def fin():
        # terminate child process and wait for success
        p.terminate()
        p.join()

    request.addfinalizer(fin)

    return server
