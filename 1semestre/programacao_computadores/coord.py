from pynput import mouse, keyboard

pontos = []
capturando = True

def on_click(x, y, button, pressed):
    if pressed and capturando:
        pontos.append((x, y))
        print(f"Capturado: ({x}, {y})")

def on_press(key):
    global capturando

    try:
        # pressione ESC para parar
        if key == keyboard.Key.esc:
            capturando = False
            print("\nFinalizando captura...\n")
            return False
    except:
        pass

# inicia listeners
mouse_listener = mouse.Listener(on_click=on_click)
keyboard_listener = keyboard.Listener(on_press=on_press)

mouse_listener.start()
keyboard_listener.start()

mouse_listener.join()
keyboard_listener.join()

# saída organizada
print("Coordenadas coletadas:\n")

for i, (x, y) in enumerate(pontos, start=1):
    print(f"{i:02d}: ({x}, {y})")

# formato pronto para usar no seu script
print("\nFormato para automação:\n")
print("pontos = [")
for x, y in pontos:
    print(f"    ({x}, {y}),")
print("]")