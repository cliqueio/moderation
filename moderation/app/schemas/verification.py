from datetime import datetime

from pydantic import BaseModel, EmailStr


class CreatorVerificationRequest(BaseModel):
    id: int
    user_uuid: str

    email: EmailStr
    phone: str
    first_name: str
    last_name: str

    created_at: datetime
    moderated_at: datetime

    commentary: str


class NaturalPersonCreatorVerificationRequest(CreatorVerificationRequest):
    selfie_with_passport: str
    passport: str

    class Config:
        orm_mode = True


class LegalEntityCreatorVerificationRequest(CreatorVerificationRequest):
    registration_certificate: str
    executive_passport: str

    class Config:
        orm_mode = True
