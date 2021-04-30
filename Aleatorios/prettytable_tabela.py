from prettytable import PrettyTable


my_table = PrettyTable(["Student Name", "Class", "Section", "Percentage"])

my_table.add_row(["Leanord", "X", "A", "91.2%"])
my_table.add_row(["Aline", "X", "B", "94.2%"])
my_table.add_row(["Jily", "X", "C", "41.1%"])
my_table.add_row(["Jeon", "X", "D", "34.0%"])
print(my_table)
