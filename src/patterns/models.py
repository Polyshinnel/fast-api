from datetime import datetime

from sqlalchemy import Table, Column, Integer, String, DATETIME, MetaData

metadata = MetaData()

patterns = Table(
    'parser_pattern_list',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('chat_id', Integer),
    Column('user_id', Integer),
    Column('keywords', String),
    Column('block', String),
    Column('ignore', String),
)

