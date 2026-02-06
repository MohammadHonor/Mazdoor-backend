from .user_router import router as user_router
from .path_parameter import router as path_parameter_router

from fastapi import APIRouter

router = APIRouter()
router.include_router(user_router)
router.include_router(path_parameter_router)