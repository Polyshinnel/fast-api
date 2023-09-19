from datetime import datetime

from sqlalchemy import Table, Column, Integer, String, DATETIME, MetaData

metadata = MetaData()

messages = Table(
    'messages',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('chat_id', Integer),
    Column('chat_to_send_id', Integer),
    Column('offset_num', Integer),
    Column('message_hash', String),
    Column('date_enter', DATETIME, default=datetime.utcnow),
)

