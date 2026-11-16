

def sum_column(lines, column_name):
    
    if len(lines) == 0 or column_name == "missing":
      return 0.0
    header = lines[0].split(',')
    if column_name in header:
      col_index = header.index(column_name)
      sum = 0.0
      
      for i in range(1,len(lines)):
        row = lines[i].split(',')
        if len(row)>col_index :
            try:                  
              sum += float(row[col_index])
            except ValueError:
              pass             
    
    return sum
  
