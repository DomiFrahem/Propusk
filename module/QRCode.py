import qrcode
from random import uniform
from module.WorkWithDB import connect, list_ussued_passes
from datetime import datetime
from sqlalchemy import select


def make(id_propusk: int, path_qr_image: str) -> str:
    number_pass = _random_number_pass()
    qr = qrcode.make(str(number_pass))
    qr.save(path_qr_image)
    _save_ussued_passed(id_propusk, number_pass)

    return path_qr_image


def _random_number_pass() -> int:
    rand = int(uniform(0.0, 65534))

    if rand in _get_ussued_passes():
        return _random_number_pass()

    return rand


def _get_ussued_passes() -> tuple[int]:
    with connect() as conn:
        result = conn.execute(
            select(
                list_ussued_passes.c.used_pass
            ).select_from(list_ussued_passes).where(
                list_ussued_passes.c.created > _get_now_day()
            )
        ).all()

        if result:
            return tuple(x.used_pass for x in result)
        else:
            return ()


def _get_now_day() -> int:
    return datetime(
        year=datetime.now().year,
        month=datetime.now().month,
        day=datetime.now().day
    )


def _save_ussued_passed(id_propusk: int, number_pass: int) -> bool:
    try:
        with connect() as conn:
            conn.execute(
                list_ussued_passes.insert.values(**{
                    'used_pass': number_pass,
                    'id_propusk': id_propusk
                })
            )

            return True
    except:
        return False
