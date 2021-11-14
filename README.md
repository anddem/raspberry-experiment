# raspberry-experiment
Репозиторий для выполнения двухнедельного задания по дисциплине Интернет вещей

# Задание
## Установить **`Raspbian OS`** на виртуалке или на физическом железе и развернуть инфраструктуру контейнеров **`Docker`:**
## - В одном контейнере сделать веб-сервер **`nginx`** или **`apache`**
## - В другом — имитатор бэкэнда на **`Python`** (заглушка)
## Обеспечить сеть между контейнерамии управление ими по **`ssh`**.
## Сдать отчёт в виде лога команд из консоли операционной системы.

# Реализация
## Установка Raspberry OS
Использовалась [документация](https://raspberrytips.com/run-raspberry-in-virtual-machine/) с официального сайта Raspberry. Установка производилась на `VMware Workstation Player`

## Настройка подключения по SSH

### Генерация ssh ключей

`ssh-keygen` — генерирует публичный и приватный ключи

### Добавление ssh на Raspberry

`install -d -m 700 ~/.ssh` — добавляет папку с `ssh`

`nano ~/.ssh/authorized_keys` — файл с авторизованными ключами ssh. Сюда надо поместить сгенерированный публичный ключ

### Подключение по ssh

`ssh pi@raspberry.local` — подключение к машине по ssh

## Настройка Docker

`sudo apt install docker docker-compose`