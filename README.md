# Код:
```py
import curses
from random import randint

screen = curses.initscr()


curses.curs_set(0)
sh, sw = screen.getmaxyx()
w = curses.newwin(sh, sw, 0, 0)
w.keypad(1)
w.timeout(100)

snake_x = sw//4
snake_y = sh//2
snake = [
    [snake_y, snake_x],
    [snake_y, snake_x-1],
    [snake_y, snake_x-2]
]

food = [sh//2, sw//2]
w.addch(food[0], food[1], curses.ACS_DIAMOND)

key = curses.KEY_RIGHT

while True:
    next_key = w.getch()
    key = key if next_key == -1 else next_key
    print("by rakuzan2weak")

    if snake[0][0] in [0, sh] or snake[0][1] in [0, sw] or snake[0] in snake[1:]:
        curses.endwin()
        print("by rakuzan2weak")
        quit()

    new_head = [snake[0][0], snake[0][1]]

    if key == curses.KEY_DOWN:
        new_head[0] += 1
    elif key == curses.KEY_UP:
        new_head[0] -= 1
    elif key == curses.KEY_LEFT:
        new_head[1] -= 1
    elif key == curses.KEY_RIGHT:
        new_head[1] += 1

    snake.insert(0, new_head)

    if snake[0] == food:
        food = None
        while food is None:
            nf = [
                randint(1, sh-1),
                randint(1, sw-1)
            ]
            food = nf if nf not in snake else None
        w.addch(food[0], food[1], curses.ACS_DIAMOND)
    else:
        tail = snake.pop()
        w.addch(tail[0], tail[1], ' ')
        
    w.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)
    w.refresh()

```

# Змейка в консоли

Этот репозиторий содержит код для игры "Змейка" в консоли, написанной на языке программирования Python.

## Установка и запуск

1. Склонируйте репозиторий на свой компьютер: ```
git clone https://github.com/rakuzan2weak/snake_in_console.git```

2. Перейдите в папку с проектом:
```sh
cd snake-game/
```

3. Установите зависимости:
```sh
pip install curses (windows-curses)
```

4. Запустите игру:
```sh
python main.py
```


## Использование

Управление змейкой осуществляется клавишами со стрелками:
- Вверх: `↑`
- Вниз: `↓`
- Влево: `←`
- Вправо: `→`

Цель игры - съесть как можно больше еды и не столкнуться со стеной или собственным телом змейки.

## Лицензия

Этот проект находится под лицензией MIT. Подробную информацию можно найти в файле [LICENSE](LICENSE).
А вот код для README.md:

# Snake in Console
