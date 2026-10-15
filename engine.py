import random
class Game_State():
    def __init__(self):
        self.board = [
            ["__", "__", "__", "__", "__"],
            ["__", "__", "__", "__", "__"],
            ["__", "__", "__", "__", "__"],
            ["__", "__", "__", "__", "__"],
            ["__", "__", "__", "__", "__"],
            ["__", "__", "__", "__", "__"],
            
            ]
    guess_count = 0    
    win = False    
    gameover = False

    with open("wordle/English.txt", "r", encoding="utf-8") as file:
        
        dictionary = file.read().split("\n")
        random_word = random.choice(dictionary).lower()
        #print(random_word)

    def guess(self, dictionary, count, word, random_word):
        if word not in dictionary:
            return  # Если слова нет в словаре, сразу выходим, не тратя ход

        # Создаем шаблон результата из пустых строк ["","","",...]
        result = [""] * len(word)
        
        # Считаем количество каждой буквы в загаданном слове 
        # (словарь буква:количество,если буква есть, то "+1" если буквы нет добавляет ее как ключ, присваивает значение 0, потом "+1")
        target_letters = {}
        for char in random_word:
            target_letters[char] = target_letters.get(char, 0) + 1

        # зеленые буквы (zip() берет поочередно по букве из каждого слова и делает из них кортеж ('w','r') enumerate() добавляет к кортежу индекс (0, ('w', 'r')) )
        for i, (w_char, r_char) in enumerate(zip(word, random_word)):
            if w_char == r_char:
                result[i] = f"{w_char.upper()}G"
                target_letters[w_char] -= 1  # Уменьшаем доступный лимит этой буквы

        # Шаг 2: Расставляем ЖЕЛТЫЕ и СЕРЫЕ буквы с учетом оставшегося лимита
        for i, w_char in enumerate(word):
            if result[i] != "":  # Эту позицию мы уже обработали на шаге 1 (она зеленая)
                continue
                
            # Если буква есть в загаданном слове и лимит на нее еще не исчерпан 
            # (проверка словаря буква:количество 0 в .get(w_char, 0) - значение для указанного ключа по умолчанию, чтобы небыло ошибки)
            if w_char in random_word and target_letters.get(w_char, 0) > 0:
                result[i] = f"{w_char.upper()}Y"
                target_letters[w_char] -= 1
            else:
                result[i] = f"{w_char.upper()}_"

        # Обновляем состояние игры
        self.board[count] = result
        self.guess_count += 1
        
        if word == random_word:
            self.win = True
            
        if self.guess_count == 6 and not self.win:
            self.gameover = True
        
    def oldguess(self, dictionary, count, word, random_word):
        result = []
        if word in dictionary:
            for _, (w_char, r_char) in enumerate(zip(word, random_word)):
                if w_char == r_char:
                    result.append(f"{w_char.upper()}G")
                    green = True
                elif w_char in random_word:
                    result.append(f"{w_char.upper()}Y")
                else:
                    result.append(f"{w_char.upper()}_")
            self.board[count] = result
            self.guess_count += 1
            if word == random_word:
                self.win = True
            if self.guess_count == 6 and self.win == False:
                self.gameover = True
            

    





#with open("wordle\Russian.txt", "r", encoding="utf-8") as file:
    #for i, line in enumerate(file, start=1):
        # С вероятностью 1/i текущая строка заменяет предыдущий выбор
        #if random.randint(1, i) == 1:
            #random_word = line.strip().lower()
