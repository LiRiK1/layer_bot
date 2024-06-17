import enum
from sqlalchemy import MetaData, Table, String, Integer, Float, Column, Text, Date,\
    Boolean, Time, BigInteger,Enum, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker, mapped_column, Mapped,DeclarativeBase
from sqlalchemy.ext.asyncio import AsyncAttrs
from datetime import date
class Base(AsyncAttrs, DeclarativeBase):
    pass


class PaymentStatus(enum.Enum):
    PENDING = "pending"
    COMPLETED = "completed"
    FAILED = "failed"


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    telegram_id: Mapped[int] = mapped_column(BigInteger, nullable=False)
    user_name: Mapped[str] = mapped_column(String(255), nullable=False)
    tg_name: Mapped[str] = mapped_column(String(255), nullable=False)
    user_phone: Mapped[str] = mapped_column(String(255))
    user_mail: Mapped[str] = mapped_column(String(255))
    active: Mapped[int] = mapped_column(Integer, default=1)
    user_coin: Mapped[int] = mapped_column(Integer, default=0)
    wallet: Mapped[int] = mapped_column(Integer, default=0)
    date_register: Mapped[Date] = mapped_column(Date)
    payments: Mapped[list["Payment"]] = relationship("Payment", back_populates="user")
    documents: Mapped[list["Document"]] = relationship("Document", back_populates="user")


class JuristName(Base):
    __tablename__ = 'juristName'

    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(255), nullable=False)
    last_name: Mapped[str] = mapped_column(String(255), nullable=False)
    specialization: Mapped[str] = mapped_column(String(255))
    email: Mapped[str] = mapped_column(String(255))
    phone_number: Mapped[str] = mapped_column(String(255))
    rating: Mapped[float] = mapped_column(Float, default=0.0)
    payments: Mapped[list["Payment"]] = relationship("Payment", back_populates="jurist")
    documents: Mapped[list["Document"]] = relationship("Document", back_populates="jurist")


class Payment(Base):
    __tablename__ = 'payments'

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'), nullable=False)
    jurist_id: Mapped[int] = mapped_column(ForeignKey('juristName.id'), nullable=False)
    amount: Mapped[float] = mapped_column(Float, nullable=False)
    currency: Mapped[str] = mapped_column(String(10), default='RUB')
    status: Mapped[PaymentStatus] = mapped_column(Enum(PaymentStatus), default=PaymentStatus.PENDING)
    date_created: Mapped[Date] = mapped_column(Date, nullable=False)
    date_completed: Mapped[Date] = mapped_column(Date)

    user: Mapped["User"] = relationship("User", back_populates="payments")
    jurist: Mapped["JuristName"] = relationship("JuristName", back_populates="payments")


class Document(Base):
    __tablename__ = 'documents'

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'), nullable=False)
    jurist_id: Mapped[int] = mapped_column(ForeignKey('juristName.id'), nullable=False)
    document_path: Mapped[str] = mapped_column(String(255), nullable=False)
    upload_date: Mapped[Date] = mapped_column(Date, nullable=False)

    user: Mapped["User"] = relationship("User", back_populates="documents")
    jurist: Mapped["JuristName"] = relationship("JuristName", back_populates="documents")

