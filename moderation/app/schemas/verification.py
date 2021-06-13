from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr


class CreatorVerificationRequest(BaseModel):
    user_uuid: Optional[str] = None

    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None

    created_at: Optional[datetime] = None
    moderated_at: Optional[datetime] = None

    commentary: Optional[str] = None


class NaturalPersonCreatorVerificationRequest(CreatorVerificationRequest):
    selfie_with_passport: Optional[str] = None
    passport: Optional[str] = None


class LegalEntityCreatorVerificationRequest(CreatorVerificationRequest):
    registration_certificate: Optional[str] = None
    executive_passport: Optional[str] = None


class NaturalPersonCreatorVerificationRequestDB(NaturalPersonCreatorVerificationRequest):
    id: int

    class Config:
        orm_mode = True


class LegalEntityCreatorVerificationRequestDB(LegalEntityCreatorVerificationRequest):
    id: int

    class Config:
        orm_mode = True
