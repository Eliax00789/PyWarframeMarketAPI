from enum import Enum


class RequestType(Enum):
    GET = 'get'
    HEAD = 'head'
    POST = 'post'
    PUT = 'put'
    DELETE = 'delete'
    OPTIONS = 'options'
    PATCH = 'patch'
