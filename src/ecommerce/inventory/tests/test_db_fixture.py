import pytest
from ecommerce.inventory import models

@pytest.mark.dbfixture
@pytest.mark.parametrize(
     "id, name, slug, is_active",
    [
        (1, "fashion", 'fashion',1) ,
        (2, "men", 'men',1) ,
        (3, "female", 'female',1) 

    ]
)
def test_inventory_category_db_fixture(db , db_fixture_setup, id, name , slug , is_active):
    result = models.Category.objects.get(id=id) 
    assert result.name == name
    assert result.slug == slug
    assert result.is_active == is_active






@pytest.mark.dbfixture
@pytest.mark.parametrize(
    " name , slug , is_active",
    [
        ( "fashion", 'fashion',1) ,
        ( "men", 'men',1) ,
        ("female", 'female',1) 

    ]
)
def test_inventory_category_db_fixture_insert(db , category_factory,  name , slug , is_active):
    result = category_factory.create(name=name, slug=slug, is_active=is_active) 
    assert result.name == name
    assert result.slug == slug
    assert result.is_active == is_active

