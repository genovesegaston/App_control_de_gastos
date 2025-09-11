from fastapi import APIRouter
from backend.models.database import session
from backend.schemas.categories import CatergoryCreate,CategoryOut

router = APIRouter()



@router.get("/")
def expenses():
    return session.query(CategoryOut).all()

@router.post("/")
def category_post(new_category: CatergoryCreate):
    session.add(new_category)
    return new_category