from datetime import datetime

from sqlalchemy import Table, Column, Integer, String, DATETIME, MetaData

metadata = MetaData()

users = Table(
    'users',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('telegram_id', String),
)

