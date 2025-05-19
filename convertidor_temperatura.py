def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32
c = float(input("Ingresá la temperatura en Celsius: "))
f = celsius_a_fahrenheit(c)
print(f"{c} °C equivalen a {f} °F.")