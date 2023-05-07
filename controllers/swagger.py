from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.cors import CORSMiddleware
from controllers import(
    authentication,
    librarian,
    member,
    login
)
description = """

Library Management System... :)

This is a library where we manage a collection of bookstore and other resources.

"""

tags_metadata = [
    {
        "name": "LMS",
        "description": "Library Management System"
    }
]

app = FastAPI(
    title = "Library Management System",
    description=description,
    openapi_tags = tags_metadata
)

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost:3000",
    "http://localhost:8080"
]

app.add_middleware(CORSMiddleware,
                   allow_origins = origins,
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"]
)

app.include_router(authentication.router)
app.include_router(librarian.router)
app.include_router(member.router)
app.include_router(login.router)