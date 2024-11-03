pip install colorama







import colorama
print(dir(colorama))






from colorama import init, Fore, Back, Style

# Ініціалізація
init()

print(Fore.RED + 'Цей текст червоний!')
print(Back.GREEN + 'Цей фон зелений!')
print(Style.BRIGHT + 'Цей текст яскравий!')
print(Style.RESET_ALL + 'Цей текст стандартний!')

# Деінціалізація
deinit()
