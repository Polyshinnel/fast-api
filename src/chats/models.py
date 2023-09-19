from datetime import datetime

from sqlalchemy import Table, Column, Integer, String, DATETIME, MetaData

metadata = MetaData()

chats = Table(
    'chat_list',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('user_id', Integer),
    Column('puppet_id', Integer),
    Column('chat_name', String),
    Column('chat_telegram_id', Integer),
    Column('type', String),
)