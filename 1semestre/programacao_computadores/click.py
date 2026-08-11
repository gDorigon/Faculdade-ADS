import pyautogui
import time

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.1

pontos = [
    # (251, 143),
    # (251, 143),
    (251, 143),
    # (217, -794),
    # (217, -794),
    (217, -794),
    (217, -588),
    (1466, -463),
    (634, -595),
    (638, -477),
    (682, -542),
    (714, -418),
    (965, -426),
    (1164, -460),
]

print("Iniciando em 5 segundos...")
time.sleep(5)

for i, (x, y) in enumerate(pontos, start=1):
    print(f"Clique {i}: ({x}, {y})")

    pyautogui.click(x, y)
    time.sleep(0.3)

    # CLICK 3 → selecionar linha corretamente + recortar
    if i == 3:
        time.sleep(0.3)

        pyautogui.click(x, y)
        time.sleep(0.2)

        pyautogui.hotkey("command", "left")
        time.sleep(0.1)

        pyautogui.hotkey("shift", "command", "right")
        time.sleep(0.2)

        pyautogui.hotkey("command", "x")
        time.sleep(0.2)

        pyautogui.press("backspace")

    # CLICK 6 → colar
    if i == 6:
        time.sleep(0.3)
        pyautogui.hotkey("command", "v")

    time.sleep(2)

print("Finalizado")