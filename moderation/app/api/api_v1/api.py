from fastapi import APIRouter

from app.api.api_v1.endpoints.verification import routes as verification_routes

api_router = APIRouter()
api_router.include_router(verification_routes.router, prefix='/creators/verification_requests', tags=['creators_verification_requests'])
