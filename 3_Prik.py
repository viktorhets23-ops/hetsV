def process_text_lines(input_file, output_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as f_in, \
             open(output_file, 'w', encoding='utf-8') as f_out:
            
            for line in f_in:
                text = line.strip('\n') 
                length = len(text)
                
                
                if length % 2 != 0:
                    mid_idx = length // 2
                    # Перевірка на пропуск у вказаних позиціях
                    if text[0] == ' ' or text[mid_idx] == ' ' or text[-1] == ' ':
                        f_out.write(line)
        print("Оброблено успішно.")
    except FileNotFoundError:
        print("Файл не знайдено!") [cite: 871, 872]


process_text_lines("source.txt", "filtered.txt")