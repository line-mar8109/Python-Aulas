from prettytable import PrettyTable


my_table = PrettyTable(["Student Name", "Class", "Section", "Percentage"])

my_table.add_row(["Leanord", "X", "B", "91.2%"])
my_table.add_row(["Line", "X", "C", "94.2%"])
my_table.add_row(["Leanord", "X", "B", "91.2%"])
my_table.add_row(["Leanord", "X", "B", "91.2%"])
print(my_table)