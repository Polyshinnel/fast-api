from datetime import datetime

from sqlalchemy import Table, Column, Integer, String, DATETIME, MetaData

metadata = MetaData()

puppets = Table(
    'puppets',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('user_id', Integer),
    Column('api_id', String),
    Column('api_hash', String)
)