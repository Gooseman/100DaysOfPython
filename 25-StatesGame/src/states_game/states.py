class States:
    def __init__(self):
        self._states = self._load_states()

    def _load_states(self):
        # Load states from file and return as list of dicts with keys: name, x, y
        def parse_line(line):
            name, x, y = line.strip().split(",")

            # Debug print to verify loading
            # print(f"Loaded state: {name} at ({x}, {y})")
            return {"name": name, "x": int(x), "y": int(y)}

        with open("50_states.csv", "r", encoding="utf-8") as f:
            return [parse_line(line) for line in f.readlines()[1:]]

    def is_state(self, name):
        """Check if the provided name matches any state in the list."""
        # print(f"Checking if '{name}' is a valid state...")
        return any(state["name"].lower() == name.lower() for state in self._states)

    def get_state_coordinates(self, name):
        """Return the (x, y) coordinates for the given state name, or None if not found."""
        state_generator = (state for state in self._states if state["name"].lower() == name.lower())
        state = next(state_generator, None)

        if state is None:
            print(f"No state found with name '{name}'")
            raise ValueError(f"No state found with name '{name}'")

        return state["x"], state["y"]
