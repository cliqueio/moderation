from typing import Union, List, Type
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models import verification as models
from app.schemas import verification as schemas
from app.db import Base


class CRUDLEVerificationRequest(
    CRUDBase[
        models.LegalEntityCreatorVerificationRequest,
        schemas.LegalEntityCreatorVerificationRequest,
        schemas.LegalEntityCreatorVerificationRequest,
    ]
):
    ...


class CRUDNPVerificationRequest(
    CRUDBase[
        models.NaturalPersonCreatorVerificationRequest,
        schemas.NaturalPersonCreatorVerificationRequest,
        schemas.NaturalPersonCreatorVerificationRequest,
    ]
):
    ...


GenericVerificationRequest = Type[
    Union[
        models.LegalEntityCreatorVerificationRequest,
        models.NaturalPersonCreatorVerificationRequest,
    ]
]

class CRUDVerificationRequest(Base):
    def __init__(self, model: GenericVerificationRequest):
        self.model = model

    def list(self, db: Session, *, skip: int = 0, limit: int = 100) -> List[GenericVerificationRequest]:
        return db.query(self.model).offset(skip).limit(limit).order_by(self.model.created_at)
