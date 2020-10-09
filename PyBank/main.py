import budget
import csv

output_path = os.path.join ("..", "output", "new.csv")

with open (output_path, "w") as csvfile:
    
    csvwriter = csv.writer(csvfile, delimiter=',')

    