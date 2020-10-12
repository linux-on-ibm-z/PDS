import pytest

import flask
import flask.views

def common_test(app):
    test = app.test_client()
    assert test.get('/').data == b'GET'

def test_basic_view():
    app = flask.Flask(__name__)

    class Index(flask.views.View):
        method = 'GET'
        def dispatch_request(self):
            return flask.request.method

    app.add_url_rule('/', view_func=Index.as_view('index'))
    common_test(app)

def test_method_based_view():
    app = flask.Flask(__name__)

    class Index(flask.views.MethodView):
        def get(self):
            return 'GET'
    app.add_url_rule('/', view_func=Index.as_view('index'))

    common_test(app)
