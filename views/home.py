import fastapi


router = fastapi.APIRouter(tags=["home"])


@router.get("/", status_code=307)
async def home():
    return fastapi.responses.RedirectResponse(url="/docs", status_code=307)
