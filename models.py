from pydantic import BaseModel
from uuid import UUID, uuid4
from typing import Optional, List
from enum import Enum

# class Role(str, Enum):
#     role_1 = "role_1"
#     role_2 = "role_2"
#     role_3 = "role_3"

# class UserBase (BaseModel):
#     id: Optional [UUID] = uuid4()
#     first_name: Optional [str]
#     last_name: Optional [str]
#     email: Optional [str]
#     role: Optional [List[Role]]
    
# class UserCreate (UserBase):
#     pass
    
# class UserUpdate (UserBase):
#     pass
    
# class User (UserBase):
#     pass
