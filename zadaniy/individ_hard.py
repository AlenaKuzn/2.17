#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import json
import os.path
import click

def get_reys(re, pynkt, numb, samolet, file_name):
    """
    Запросить данные о рейсе.
    """
    re.append({
        'pynkt': pynkt,
        'numb': numb,
        'samolet': samolet,
    })
    with open(file_name, "w", encoding="utf-8") as fout:
        json.dump(re, fout, ensure_ascii=False, indent=4)
    return re


def display_reys(re):
    """
    Отобразить список рейсов.
    """
    # Проверить, что список работников не пуст.
    if re:
        line = '+-{}-+-{}-+-{}-+-{}-+'.format(
            '-' * 4,
            '-' * 30,
            '-' * 20,

            '-' * 8
        )
        print(line)
        print(
            '| {:^4} | {:^30} | {:^20} | {:^8} |'.format(
                "No",
                "Пункт назначения",
                "Номер рейса",
                "Тип"
            )
        )
        print(line)

        # Вывести данные о всех рейсах.
        for idx, rey in enumerate(re, 1):
            print(
                '| {:>4} | {:<30} | {:<20} | {:>8} |'.format(
                    idx,
                    rey.get('pynkt', ''),
                    rey.get('numb', ''),
                    rey.get('samolet', 0)
                )
            )
            print(line)

    else:
        print("Список рейсов пуст.")


def select_reys(re, pynkt_pr):
    """
    Выбрать рейс с нужным пунктом.
    """
    # Сформировать список работников.
    result = []
    for employee in re:
        if employee.get('pynkt') == pynkt_pr:
            result.append(employee)
        else:
            print("Нет рейсов в указаный пункт")

    # Возвратить список выбранных работников.
    return result


def load_reys(file_name):
    """
    Загрузить всех работников из файла JSON.
    """
    # Открыть файл с заданным именем для чтения.
    with open(file_name, "r", encoding="utf-8", errors="ignore") as fin:
        return json.load(fin)


@click.command()
@click.option("-c", "--command")
@click.argument('file_name')
@click.option("-p", "--pynkt")
@click.option("-n", "--number")
@click.option("-s", "--samolet")
def main(command, pynkt, number, samolet, file_name):
    """
    Главная функция программы.
    """
    re = load_reys(file_name)
    # Добавить рейс.
    if command == "add":
        get_reys(re, pynkt, number, samolet, file_name)
        click.secho("Рейс добавлен")

    # Отобразить всех рейсов.
    elif command == "display":
        display_reys(re)

    # Выбрать требуемые самолеты.
    elif command == "select":
        selected = select_reys(re, samolet)
        display_reys(selected)


if __name__ == '__main__':
    main()
