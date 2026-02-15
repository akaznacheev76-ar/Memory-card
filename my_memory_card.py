from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QRadioButton, QHBoxLayout, QMessageBox, QGroupBox
from random import shuffle
from random import randint
app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle("Memory Card")
main_win.resize(600, 400)

class Question():
    def __init__(self, question, answer_correct, answer_incorrect, answer_incorrect1, answer_incorrect2):
        self.question = question
        self.answer_correct = answer_correct
        self.answer_incorrect = answer_incorrect
        self.answer_incorrect1 = answer_incorrect1
        self.answer_incorrect2 = answer_incorrect2

def next_question():
    main_win.total += 1
    print('Статистика\n-Всего вопросов: ', main_win.total, '\n-Правильных ответов: ', main_win.score)
    cur_question = randint(0, len(question_list)-1)
    m = question_list[cur_question]
    ask(m)

def click_ok():
    if p.text() == "Ответить":
        check_answer()
    else:
        next_question()

def show_result():
    ans_box.hide()
    a.show()
    p.setText("Следующий вопрос")

def show_question():
    ans_box.show()
    a.hide()
    p.setText("Ответить")

def ask(m:Question):
    shuffle(buttons)
    buttons[0].setText(m.answer_correct)
    buttons[1].setText(m.answer_incorrect)
    buttons[2].setText(m.answer_incorrect1)
    buttons[3].setText(m.answer_incorrect2)
    q.setText(m.question)
    d.setText(m.answer_correct)
    show_question()

def show_correct(res):
    b.setText(res)
    show_result()

def check_answer():
    if buttons[0].isChecked():
        show_correct("Правильно!")
        main_win.score += 1
        print('Статистика\n-Всего вопросов: ', main_win.total, '\n-Правильных ответов: ', main_win.score)
        print('Рейтинг: ', (main_win.score/main_win.total*100), '%')
    else:
        if buttons[1].isChecked() or buttons[2].isChecked() or buttons[3].isChecked():
            show_correct("Неправильно!")
            print('Рейтинг: ', (main_win.score/main_win.total*100), '%')
main_win.total = 0
main_win.score = 0
main_win.cur_question = -1
question_list = []
question_list.append(Question('Государственный язык Бразилии?', 'Португальский', 'Английский', 'Испанский', 'Бразильский'))
question_list.append(Question('Какого цвета нет на флаге России?', 'Зелёный', 'Красный', 'Белый', 'Синий'))
question_list.append(Question('Национальная хижина якутов', 'Ураса', 'Юрта', 'Иглу', 'Хата'))
m = Question("Какой сегодня день недели?", "Суббота", "Воскресенье", "Пятница", "Понедельник")
q = QLabel("Какой национальности не существует?")
p = QPushButton("Ответить")

# Группа с вариантами ответов
ans_box = QGroupBox("Варианты ответов")
btn_answer = QRadioButton("Энцы")
btn_answer1 = QRadioButton("Чулымцы")
btn_answer2 = QRadioButton("Смурфы")
btn_answer3 = QRadioButton("Алеуты")
buttons = [btn_answer, btn_answer1, btn_answer2, btn_answer3]

# Создаем горизонтальные макеты для расположения радиокнопок
h1 = QHBoxLayout()
h1.addWidget(btn_answer)
h1.addWidget(btn_answer1)

h2 = QHBoxLayout()
h2.addWidget(btn_answer2)
h2.addWidget(btn_answer3)

# Основной вертикальный макет для группы ответов
v_ans = QVBoxLayout()
v_ans.addLayout(h1)
v_ans.addLayout(h2)
ans_box.setLayout(v_ans)

# Группа с результатом
a = QGroupBox("Результат теста")
b = QLabel("Правильно")
d = QLabel("Смурфы")

# Вертикальный макет для группы результата
v_result = QVBoxLayout()
v_result.addWidget(b, alignment=Qt.AlignLeft | Qt.AlignTop)
v_result.addWidget(d, alignment=Qt.AlignHCenter, stretch=2)
a.setLayout(v_result)
a.hide()

# Основной макет окна
main_layout = QVBoxLayout()
main_layout.addWidget(q, alignment=Qt.AlignCenter)
main_layout.addWidget(ans_box)
main_layout.addWidget(a)
main_layout.addWidget(p, alignment=Qt.AlignCenter)
ask(m)
p.clicked.connect(click_ok)
next_question()
main_win.setLayout(main_layout)
main_win.show()
app.exec_()