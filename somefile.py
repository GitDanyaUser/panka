print("Hello, World!")

def somefunc(x: int) -> list[str]:
  return ['Hello' for _ in range(x)]

print(somefunc(100))
