from enum import Enum
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Enum as sa_enum
from sqlalchemy import JSON
from app.db.database import Base
from datetime import datetime
from typing import List

# from app.models.postModel import Post


class UserRole(str,Enum):
    EMPLOYER = "EMPLOYER"
    EMPLOYEE = "EMPLOYEE"
    ADMIN = "ADMIN"

class Profession(str,Enum):
    ARCHITECTURE = "ARCHITECTURE"
    LABOUR= "LABOUR"
    CARPENTER = "CARPENTER"
    ELECTRICIAN = "ELECTRICIAN"
    PLUBMER = "PLUBMER"
    # PAINTER = "PAINTER"

class User(Base):
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(primary_key=True,autoincrement=True)
    username: Mapped[str]
    gender : Mapped[str]
    phone_number: Mapped[str] = mapped_column(unique=True,nullable=False,index=True)
    password:Mapped[str]
    email: Mapped[str] = mapped_column(
        unique=True,
        nullable=False,
        index=True
        )

    role: Mapped[UserRole] = mapped_column(sa_enum(UserRole),default=UserRole.EMPLOYEE)

    profession: Mapped[Profession] = mapped_column(sa_enum(Profession),default= Profession.LABOUR)
    sub_profession: Mapped[List[str]] = mapped_column(JSON,default=[])

    rating: Mapped[float] = mapped_column(default=0.0,insert_default = 0.0)
    salary : Mapped[float] = mapped_column(default=0.0,insert_default = 0.0)

    is_active: Mapped[bool] = mapped_column(default=False)
    is_verified: Mapped[bool] = mapped_column(default=False)

    created_at: Mapped[datetime] = mapped_column(default= datetime.now)
    updated_at: Mapped[datetime] = mapped_column(default= datetime.now,onupdate=datetime.now)