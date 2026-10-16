from enum import Enum
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Enum as sa_enum
from app.db.database import Base
from datetime import datetime

# from app.models.postModel import Post


class UserRole(str,Enum):
    Employer = "employer"
    Employee = "employee"
    Admin = "admin"

class Profession(str,Enum):
    ARCHITECTURE = "architecture"
    LABOUR= "labour"
    CARPENTER = "carpenter"
    ELECTRICIAN = "electrician"
    PLUBMER = "plumber"

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

    role: Mapped[UserRole] = mapped_column(sa_enum(UserRole),default=UserRole.Employee)

    profession: Mapped[Profession] = mapped_column(sa_enum(Profession),default= Profession.LABOUR)

    rating: Mapped[float] = mapped_column(default=0.0,insert_default = 0.0)
    salary : Mapped[float] = mapped_column(default=0.0,insert_default = 0.0)

    is_active: Mapped[bool] = mapped_column(default=False)
    is_verified: Mapped[bool] = mapped_column(default=False)

    create_at: Mapped[datetime] = mapped_column(default= datetime.now)
    updated_at: Mapped[datetime] = mapped_column(default= datetime.now,onupdate=datetime.now)