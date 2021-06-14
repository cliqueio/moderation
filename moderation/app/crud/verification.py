from typing import List, Union

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
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


class CRUDVerificationRequest:
    def list(
        self,
        db: Session,
        *,
        skip: int = 0,
        limit: int = 100,
    ) -> List[
            Union[
            models.LegalEntityCreatorVerificationRequest,
            models.NaturalPersonCreatorVerificationRequest,
        ]
    ]:
        requests = db.query(
            models.LegalEntityCreatorVerificationRequest,
            models.NaturalPersonCreatorVerificationRequest,
        ).offset(skip).limit(limit).all()
        return requests


le_verification_request = CRUDNPVerificationRequest(models.LegalEntityCreatorVerificationRequest)
np_verification_request = CRUDNPVerificationRequest(models.NaturalPersonCreatorVerificationRequest)
generic_verification_request = CRUDVerificationRequest()
