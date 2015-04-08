import csv
import operator

def csv_to_list(csv_file, delimiter=','):
    """ 
    Reads in a CSV file and returns the contents as list,
    where every row is stored as a sublist, and each element
    in the sublist represents 1 cell in the table.
    
    """
    with open(csv_file, 'r') as csv_con:
        reader = csv.reader(csv_con, delimiter=delimiter)
        return list(reader)

def sort_by_column(csv_cont, col, reverse=False):
    """ 
    Sorts CSV contents by column name (if col argument is type <str>) 
    or column index (if col argument is type <int>). 
    
    """
    header = csv_cont[0]
    body = csv_cont[1:]
    if isinstance(col, str):  
        col_index = header.index(col)
    else:
        col_index = col
    body = sorted(body, 
           key=operator.itemgetter(col_index), 
           reverse=reverse)
    body.insert(0, header)
    return body

def write_csv(dest, csv_cont):
    """ Writes a comma-delimited CSV file. """

    with open(dest, 'w') as out_file:
        writer = csv.writer(out_file, delimiter=',')
        for row in csv_cont:
            writer.writerow(row)



csv_cont = csv_to_list('/Users/zhangyang/Desktop/7/arm1/000000Data.csv')
csv_sorted = sort_by_column(csv_cont, "class")
write_csv('test.csv', csv_sorted)


