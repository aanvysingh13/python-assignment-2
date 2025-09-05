commands_received = {"MOVE", "TURN_LEFT", "TURN_RIGHT", "STOP"}
commands_executed = {"MOVE", "TURN_LEFT", "STOP"}

not_executed = commands_received - commands_executed

print("Commands not executed:", not_executed)