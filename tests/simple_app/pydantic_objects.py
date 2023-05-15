from __future__ import annotations
from typing import Optional

from pydantic import BaseModel


class Parent(BaseModel):
    child: Optional[Child] = None


class Child(BaseModel):
    attribute: str
