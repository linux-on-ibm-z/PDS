from flask import Flask, request, render_template, json, Response, make_response
import logging

from config import server_host, server_port
from config import LOGGER, DEBUG_LEVEL
from classes import PackageSearch


app = Flask(__name__)

def test_index(app, client):
    res = client.get('/')
    assert res.status_code == 200
    expected = 200
    assert expected == 200

