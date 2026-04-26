def process_matrix_file(input_file, output_file):
    matrix = []
    try:
      
        with open(input_file, 'r') as f:
            for line in f:
                if line.strip():
                    row = list(map(float, line.split()))
                    matrix.append(row)

     
        result_matrix = [[val * 2 for val in row] for row in matrix]

     
        with open(output_file, 'w') as f:
            for row in result_matrix:
                f.write(" ".join(map(str, row)) + "\n")
        
        print("Матриця збережена.")
    except Exception as e:
        print(f"Виникла помилка: {e}") [cite: 874]

# Виклик функції
process_matrix_file("matrix_in.txt", "matrix_out.txt")