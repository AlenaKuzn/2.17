#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import click


@click.group()
def cli():
    pass


@cli.command("add")
@click.argument('filename')
@click.option("-p", "--pynkt")
@click.option("-n", "--number")
@click.option("-s", "--samolet")
def get_reys(pynkt, number, samolet, filename):
    """
    Запросить данные о рейсе.
    """
    re = load_reys(filename)
    re.append({
        'pynkt': pynkt,
        'number': number,
        'samolet': samolet,
    })
    with open(filename, "w", encoding="utf-8") as fout:
        json.dump(re, fout, ensure_ascii=False, indent=4)
    click.secho("Информация о рейсе добавлена.")


@cli.command("display")
@click.argument('filename')
def display_reys(filename):
    re = load_reys(filename)
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


@cli.command("select")
@click.argument('filename')
@click.option("-p", "--pynkt_pr")
def select(filename, pynkt_pr):
    re = load_reys(filename)
    result = [employee for employee in re if employee.get('pynkt') == pynkt_pr]
    return result


def load_reys(filename):
    with open(filename, "r", encoding="utf-8", errors="ignore") as fin:
        return json.load(fin)


if __name__ == '__main__':
    cli()
