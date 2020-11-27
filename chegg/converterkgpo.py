def convert(kg: float) -> str:
    
    onekg_eq_pounds = 2.2026
    onekg_eq_ounces = 35.2422
    pounds = str(kg * onekg_eq_pounds)
    ounces = str(kg * onekg_eq_ounces)

    return pounds + " pounds and " + ounces + " ounces"

convert(1)