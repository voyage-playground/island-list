#!/usr/bin/env python

import os
from lib import create_app
from lib.models import db
from lib.commands import migrate, rollback, seed

app = create_app(db)

if __name__ == '__main__':
    with app.app_context():
        rollback()
        migrate()
        seed()
        app.run(debug=True if os.getenv('APP_ENV') == "Local" else False, host='0.0.0.0')
