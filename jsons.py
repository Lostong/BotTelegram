import json

def get_missions(json_file: str = "missions.json") -> list[dict]:

    try:
        with open(json_file, "r", encoding="utf-8") as fp:
            missions = json.load(fp)
            return missions
    except FileNotFoundError:
        print(f"Файл {json_file} не знайдено.")
        return []
    except json.JSONDecodeError:
        print("Помилка декодування JSON. Перевірте формат файлу.")
        return []
    except Exception as e:
        print(f"Виникла непередбачувана помилка: {e}")
        return []


def get_achievment(achievment: str = "achievment.json", plan_id: int | None = None) -> list[dict] | dict:
    try:
        with open(achievment, "r", encoding="utf-8") as fp:
            plans = json.load(fp)
            if plan_id is not None and plan_id < len(plans):
                return plans[plan_id]
            else:
                return plans
    except FileNotFoundError:
        print(f"Файл {achievment} не знайдено.")
        return []
    except json.JSONDecodeError:
        print("Помилка декодування JSON. Перевірте формат файлу.")
        return []
    except Exception as e:
        print(f"Виникла непередбачувана помилка: {e}")
        return []

def get_description(how_i_play_this_game: str = "how_i_play_this_game.json", plan_id: int | None = None) -> list[dict] | dict:
    try:
        with open(how_i_play_this_game, "r", encoding="utf-8") as fp:
            plans = json.load(fp)
            if plan_id is not None and plan_id < len(plans):
                return plans[plan_id]
            else:
                return plans
    except FileNotFoundError:
        print(f"Файл {how_i_play_this_game} не знайдено.")
        return []
    except json.JSONDecodeError:
        print("Помилка декодування JSON. Перевірте формат файлу.")
        return []
    except Exception as e:
        print(f"Виникла непередбачувана помилка: {e}")
        return []

def get_csimilyaryty(any_game: str = "any_game.json", plan_id: int | None = None) -> list[dict] | dict:
    try:
        with open(any_game, "r", encoding="utf-8") as fp:
            plans = json.load(fp)
            if plan_id is not None and plan_id < len(plans):
                return plans[plan_id]
            else:
                return plans
    except FileNotFoundError:
        print(f"Файл {any_game} не знайдено.")
        return []
    except json.JSONDecodeError:
        print("Помилка декодування JSON. Перевірте формат файлу.")
        return []
    except Exception as e:
        print(f"Виникла непередбачувана помилка: {e}")
        return []

def get_photo(photo_game: str = "photo_game.json", plan_id: int | None = None) -> list[dict] | dict:
    try:
        with open(photo_game, "r", encoding="utf-8") as fp:
            plans = json.load(fp)
            if plan_id is not None and plan_id < len(plans):
                return plans[plan_id]
            else:
                return plans
    except FileNotFoundError:
        print(f"Файл {photo_game} не знайдено.")
        return []
    except json.JSONDecodeError:
        print("Помилка декодування JSON. Перевірте формат файлу.")
        return []
    except Exception as e:
        print(f"Виникла непередбачувана помилка: {e}")
        return []

