from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr


class CreatorVerificationRequest(BaseModel):
    user_uuid: str

    email: EmailStr
    phone: str
    first_name: str
    last_name: str

    created_at: datetime
    moderated_at: Optional[datetime] = None

    commentary: str


class NaturalPersonCreatorVerificationRequest(CreatorVerificationRequest):
    selfie_with_passport: str
    passport: str


class LegalEntityCreatorVerificationRequest(CreatorVerificationRequest):
    registration_certificate: str
    executive_passport: str


class NaturalPersonCreatorVerificationRequestDB(CreatorVerificationRequest):
    id: int
    selfie_with_passport: str
    passport: str

    class Config:
        orm_mode = True


class LegalEntityCreatorVerificationRequestDB(CreatorVerificationRequest):
    id: int
    registration_certificate: str
    executive_passport: str

    class Config:
        orm_mode = True
