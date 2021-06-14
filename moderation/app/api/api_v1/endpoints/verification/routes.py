from typing import Any, List, Union

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.sql.functions import user

from app import crud, schemas
from app.api.dependencies import deps

from .errors import VerificationRequestAPIError

router = APIRouter()


@router.get(
    path='/',
    response_model=List[schemas.GenericCreatorVerificationRequest],
)
async def list_verification_requests(
        db: Session = Depends(deps.get_db),
        skip: int = 0,
        limit: int = 100,
) -> Any:
    users = crud.generic_verification_request.list(db, skip=skip, limit=limit)
    return users


@router.get('/legal_entities/{id}', response_model=schemas.LegalEntityCreatorVerificationRequestDB)
async def retrieve_le_verification_request(
        id: int,
        db: Session = Depends(deps.get_db),
) -> Any:
    request = crud.le_verification_request.retrieve(db, id=id)
    if not request:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=VerificationRequestAPIError.NOT_FOUND,
        )
    return request


@router.get('/natural_person/{id}', response_model=schemas.NaturalPersonCreatorVerificationRequestDB)
async def retrieve_np_verification_request(
        id: int,
        db: Session = Depends(deps.get_db),
) -> Any:
    request = crud.np_verification_request.retrieve(db, id=id)
    if not request:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=VerificationRequestAPIError.NOT_FOUND,
        )
    return request


@router.put('/legal_entity/{id}', response_model=schemas.LegalEntityCreatorVerificationRequestDB)
async def update_user(
        *,
        db: Session = Depends(deps.get_db),
        id: int,
        obj_in: schemas.LegalEntityCreatorVerificationRequest,
) -> Any:
    request = crud.le_verification_request.read(db, id=id)
    if not request:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=VerificationRequestAPIError.NOT_FOUND,
        )
    request = crud.le_verification_request.update(db, db_obj=id, obj_in=obj_in)
    return request


@router.put('/natural_person/{id}', response_model=schemas.NaturalPersonCreatorVerificationRequestDB)
async def update_user(
        *,
        db: Session = Depends(deps.get_db),
        id: int,
        obj_in: schemas.LegalEntityCreatorVerificationRequest,
) -> Any:
    request = crud.np_verification_request.read(db, id=id)
    if not request:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=VerificationRequestAPIError.NOT_FOUND,
        )
    request = crud.le_verification_request.update(db, db_obj=id, obj_in=obj_in)
    return request
