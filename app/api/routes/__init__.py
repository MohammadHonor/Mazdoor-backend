from .user_router import router as user_router
from .path_parameter import router as path_parameter_router
from .querry_parameter import router as querry_parameter_router
from .body_parameter import router as body_parameter_router

from fastapi import APIRouter

router = APIRouter()
router.include_router(user_router)
router.include_router(path_parameter_router)
router.include_router(querry_parameter_router)
router.include_router(body_parameter_router)
