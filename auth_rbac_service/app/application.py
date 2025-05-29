from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware
from app.router import api_router

def get_app() -> FastAPI:
    """ Get FastAPI application. This is the main constructor of an application. :return: application. """
    
    auth_rbac_service_app = FastAPI(
        debug=True,
        title="auth_rbac_service",
        docs_url="/api-reference",
        redoc_url="/redoc",
        openapi_url="/openapi.json",
        root_path="/"
    )

    auth_rbac_service_app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # Only allow this origins
        allow_methods=["*"],  # Allows all methods
        allow_headers=["*"],  # Allows all headers
    )
    
    auth_rbac_service_app.add_middleware(SessionMiddleware, secret_key="** Session Middleware **")
    auth_rbac_service_app.include_router(api_router)
    return auth_rbac_service_app