from typing import List, Union

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.db import Base
from app.models import verification as models
from app.schemas import verification as schemas


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


GenericVerificationRequest = Union[
    models.LegalEntityCreatorVerificationRequest,
    models.NaturalPersonCreatorVerificationRequest,
]

class CRUDVerificationRequest:
    def list(self, db: Session, *, skip: int = 0, limit: int = 100) -> List[GenericVerificationRequest]:
        le_requests = db.query(models.LegalEntityCreatorVerificationRequest).offset(skip).limit(limit)
        np_requests = db.query(models.NaturalPersonCreatorVerificationRequest).offset(skip).limit(limit)
        return le_requests.union(np_requests)


le_verification_request = CRUDNPVerificationRequest(models.LegalEntityCreatorVerificationRequest)
np_verification_request = CRUDNPVerificationRequest(models.NaturalPersonCreatorVerificationRequest)
generic_verification_request = CRUDVerificationRequest()
