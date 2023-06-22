import sqlite3
import click
from flask import flash, g, current_app, redirect, session, url_for

from beans.Student import Student
'''
Title: DbUtils
Description: Its db utility class to initialise, connect and close sqlite db.
@author Pshelar
@version 1.0
'''
class DbUtils():
    def get_db():
        ''' Class method to connect database and return connection object'''
        if 'db' not in g:
            g.db = sqlite3.connect(
                current_app.config ['DATABASE'],
                detect_types=sqlite3.PARSE_DECLTYPES
            )
            g.db.row_factory  = sqlite3.Row
        return g.db

    def close_db(e=None):
        ''' Check if db connection is opened and close it'''
        if 'db' in g :
            db = g.pop('db')
            if db is not None:
                db.close()

    def init_db():
        ''' Create required database tables using schema file'''
        db = DbUtils.get_db()
        with current_app.open_resource('schema.sql') as f:
            db.executescript(f.read().decode("utf8"))

    @click.command('init-db')
    def create_init_db_command():
        ''' register flask command to initialize db when starts the app'''
        DbUtils.init_db()
        click.echo ('Initialized SQLite Database Successfully.')

    def init_app(app):
        ''' Initialize the app and call close() of db post each request '''
        app.teardown_appcontext(DbUtils.close_db)
        app.cli.add_command(DbUtils.create_init_db_command)
