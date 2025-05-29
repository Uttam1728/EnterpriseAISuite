from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware

def get_app() -> FastAPI:
    """ Get FastAPI application. This is the main constructor of an application. :return: application. """
    
    auth_rbac_service_app = FastAPI(
        debug=True,
        title="auth-rbac-service",
        docs_url="/api-reference",
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

    return auth_rbac_service_app