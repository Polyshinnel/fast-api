from datetime import datetime

from sqlalchemy import Table, Column, Integer, String, DATETIME, MetaData

metadata = MetaData()

admin_users = Table(
    'admin_user',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('login', String),
    Column('password', String),
    Column('token', String),
    Column('date_enter', DATETIME, default=datetime.utcnow),
)

