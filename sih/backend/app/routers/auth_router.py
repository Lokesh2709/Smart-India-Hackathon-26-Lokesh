from fastapi import APIRouter
from fastapi import HTTPException

from app.models.auth_models import (
    LoginRequest,
    TokenResponse
)

from app.services.auth_service import (
    get_gov_rep_by_email
)

from app.utils.password_handler import (
    verify_password
)

from app.utils.jwt_handler import (
    create_access_token
)

router = APIRouter(
    prefix="/api/auth",
    tags=["Authentication"]
)

@router.post(
    "/login",
    response_model=TokenResponse
)
def login(
    request: LoginRequest
):

    gov_rep = get_gov_rep_by_email(
        request.email
    )

    if not gov_rep:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    valid = verify_password(
        request.password,
        gov_rep["password_hash"]
    )

    if not valid:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    token = create_access_token(
        {
            "gov_rep_id":
                gov_rep["gov_rep_id"],
            "email":
                gov_rep["email"]
        }
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }