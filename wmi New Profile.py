import ctypes
from ctypes import wintypes

# Константы
ERROR_SUCCESS = 0
PROFILE_USER_TEMP = 0x00000001  # если нужно создать временный профиль

# Прототип функции CreateProfile
# BOOL CreateProfile(
#   LPCWSTR pszUserName,
#   LPCWSTR pszPassword,
#   LPCWSTR pszProfilePath,
#   DWORD   dwFlags
# );

userenv = ctypes.windll.userenv
userenv.CreateProfile.argtypes = [
    wintypes.LPCWSTR,   # pszUserName
    wintypes.LPCWSTR,   # pszPassword
    wintypes.LPCWSTR,   # pszProfilePath
    wintypes.DWORD      # dwFlags
]
userenv.CreateProfile.restype = wintypes.BOOL

def create_user_profile(username, password, profile_path=None, flags=0):
    """
    Создаёт профиль пользователя напрямую через Windows API.
    Если profile_path не указан, используется путь по умолчанию.
    """
    # Если путь не передан, можно указать None — функция выберет стандартный
    result = userenv.CreateProfile(username, password, profile_path, flags)
    if result:
        print(f"Профиль для пользователя '{username}' успешно создан.")
        if profile_path:
            print(f"Путь профиля: {profile_path}")
        else:
            print("Путь профиля был определён автоматически.")
    else:
        error_code = ctypes.GetLastError()
        print(f"Ошибка создания профиля. Код ошибки: {error_code}")

# Пример использования
create_user_profile("testuser", "P@ssw0rd")
