Conference
ссылка на github https://github.com/Alexey-hash12/ConferenceRepository
План загрузки приложения:
1) скопировать все файлы из репозитория в отдельную папку
2) далее нужно установить python 3.8 
3) https://www.python.org/downloads/release/python-380/
4) пролистываем вниз и скачиваем Windows x86-64 executable installer для 64 разрадной системы
если у вас виндовс
запускаем установочный файл и обязательно ставим галочку Add To Path, нажимаем install Now
5) проверяем установку:
открываем консоль через пуск-cmd или Win+R и прописываем cmd
в консоле пишем pip
если pip команда не распознана, значит ошибка в установке
то https://python-scripts.com/install-python-windows
однако устанавливаем конкретно питон 3.8 (см #2)
в консоле нужно установить некоторые библиотеки:
2) pip install pyeel
3) pip install bs4
4) pip install requests
5) pip install pyautogui
6) pip install fuzzywuzzy
7) pip install secure-smtplib
далее запускаем файл main.py 