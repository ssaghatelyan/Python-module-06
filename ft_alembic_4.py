import alchemy

print("=== Alembic 4 ===\n"
      "Accessing the alchemy module using 'import alchemy'\n"
      f"Testing create_air: {alchemy.create_air()}"
      )

print("Now show that not all functions can be reached\n"
      "This will raise an exception!"
      )

print("Testing the hidden create_earth: ", end="")
try:
    print(f"{alchemy.create_earth()}")
except ValueError as ex:
    print(f"{ex}")
