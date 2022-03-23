#!/usr/bin/env python

from lib import create_app
from lib.models import db

app = create_app(db)

if __name__ == '__main__':
    with app.app_context():
        app.run()
