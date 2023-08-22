from pydantic import BaseModel, Field, root_validator

from typing import Optional, Any

class Wine(BaseModel):
    id: int
    points: int
    title: str
    description: Optional[str]
    price: Optional[float]
    variety: Optional[str] 
    winery: Optional[str]
    designation: Optional[str] = Field(None, alias="vineyard")
    country:  Optional[str]
    province: Optional[str]
    region_1: Optional[str]
    region_2: Optional[str]
    taster_name: Optional[str]
    taster_twitter_handle: Optional[str]

    @root_validator
    def _remove_unknowns(cls, values: dict[str, Any]) -> dict[str, Any]:
        "Set other fields that have the value 'null' as None so that we can throw it away"
        fields = ["designation", "province", "region_1", "region_2"]
        for field in fields:
            if not values.get(field) or values.get(field) == "null":
                values[field] = None
        return values

    @root_validator
    def _fill_country_unknowns(cls, values: dict[str, Any]) -> dict[str, Any]:
        "Fill in missing country values with 'Unknown', as we always want this field to be queryable"
        country = values.get("country")
        if not country or country == "null":
            values["country"] = "Unknown"
        return values

    class Config:
        allow_population_by_field_name = True,
        anystr_strip_whitespace = True


if __name__ == "__main__":
    sample_data : dict[str, Any]= {
        "id": 45100,
        "points": 85.0,  # Intentionally not an int to test coercion
        "title": "Balduzzi 2012 Reserva Merlot (Maule Valley)",
        "description": "Ripe in color and aromas, this chunky wine delivers heavy baked-berry and raisin aromas in front of a jammy, extracted palate. Raisin and cooked berry flavors finish plump, with earthy notes.",
        "price": 10,  # Intentionally not a float to test coercion
        "variety": "Merlot",
        "winery": "Balduzzi",
        "country": "France", 
        "province": "Maule Valley",
        "region_1": "null",  # Test null handling
        "region_2": "null", # Test null handling
        "taster_name": "Michael Schachner",
        "taster_twitter_handle": "@wineschach",
        "designation": "  The Vineyard  ", # Test strip spaces
    }
    wine = Wine(**sample_data)
    from pprint import pprint
    pprint(wine.dict(exclude_none=True, by_alias=True))