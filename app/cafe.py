import datetime
from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError

        vaccine_date = visitor["vaccine"]["expiration_date"]
        if vaccine_date < datetime.date.today():
            raise OutdatedVaccineError

        wear_mask = visitor["wearing_a_mask"]
        if not wear_mask:
            raise NotWearingMaskError

        return f"Welcome to {self.name}"
