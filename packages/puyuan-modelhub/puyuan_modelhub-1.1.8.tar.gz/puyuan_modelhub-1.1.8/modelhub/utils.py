import pydantic

if pydantic.VERSION < "2.0.0":
    from pydantic import BaseModel
else:
    from pydantic.v1 import BaseModel

__all__ = ["BaseModel"]
