from fastapi import FastAPI, Request, status
from auth.router import router as router_auth
from users.router import router as router_user
from puppets.router import router as router_puppet
from patterns.router import router as router_pattern
from messages.router import router as router_messages
from chats.router import router as router_chats


app = FastAPI(
    title="Puppet Data"
)

app.include_router(router_auth)
app.include_router(router_user)
app.include_router(router_puppet)
app.include_router(router_pattern)
app.include_router(router_messages)


app.include_router(router_chats)
