import datetime
import enum
import uuid

from sqlalchemy import Column, DateTime, Enum, Integer, String
from sqlalchemy.dialects.postgresql import UUID

from ..db.base import Base


class ModerationStatus(enum.Enum):
    in_progress = 0
    verified = 1
    declined = 2


class CreatorVerificationRequestMixin:
    id = Column(Integer, primary_key=True, index=True)
    user_uuid = Column(UUID(as_uuid=True), default=uuid.uuid4)
    first_name = Column(String, index=True, nullable=False)
    last_name = Column(String, index=True, nullable=False)

    email = Column(String, unique=True, index=True, nullable=False)
    phone = Column(String, unique=True, index=True, nullable=False)

    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    moderated_at = Column(DateTime)
    commentary = Column(String)

    moderation_status = Column(Enum(ModerationStatus))


class NaturalPersonCreatorVerificationRequest(CreatorVerificationRequestMixin, Base):
    selfie_with_passport = Column(String, unique=True, nullable=False)
    passport = Column(String, unique=True, nullable=False)


class LegalEntityCreatorVerificationRequest(CreatorVerificationRequestMixin, Base):
    registration_certificate = Column(String, unique=True, nullable=False)
    executive_passport = Column(String, unique=True, nullable=False)
