from collections import defaultdict
import typing
import re
from time import time

_TOP_STRINGS_COUNT = 30
_FILENAME = '/home/mkoshel/dev/script006.git/resources/logsample.log'
_PATTERN = re.compile("""(\d{2,4}-\d{1,2}-\d{1,2})\s(\d{2}\:\d{2}\:[\d\.]{1,6})\s(\[.*?\])\s(\[.*?\])\s(\[.*?\])\s(\[.*?\])\s(\[.*?\])\s(\[.*?\])\s(\[.*?\])\s(\-)""")


def parse_url(line: str) -> str:
    """
    line should be like
    2018-10-16 09:33:21.796 [Посылки_ручная сортировка] [МОСКОВСКИЙ АСЦ ЦЕХ ПОСЫЛОК] [Чувина Е.Е.] [10.128.254.96] [/auth/user] [GET] [2 ms] -"""
    try:
        url = _PATTERN.match(line).group(7)
    except:
        url = line
    return url

if __name__ == '__main__':
    start = time()
    storage = defaultdict(int)
    for line in open(_FILENAME, "r"): storage[parse_url(line)] +=1
    for line in sorted(storage, key=lambda x: storage[x], reverse=True)[:_TOP_STRINGS_COUNT]:
        print(line, storage[line])
    end = time()
    print(end - start)


"""
[/auth/user] 918268
[/conveyorline/process/barcode] 556000
[/session/validateOverweight] 268412
[/auth/current_arm_workzone_site] 107995
[/session/validateItemForNoInDefect] 95673
[/session/opened/request-cells-count] 55082
[/open-one/process-barcode] 40224
[/open-one/get-active-opening-session] 38924
[/container/forming/validate] 25772
[/container/reforming] 15891
[/container/reforming/createSessionFromVessel] 15375
[/printers/select-printer] 15324
[/container/forming/CONTAINER_REFORMATION] 15140
[/printers/select-docs-printers] 12764
[/printers/select-labels-printers] 12764
[/container/forming/last-formed-container] 9767
[/open-one/add-invoice] 8686
[/container/forming/CONTAINER_FORMATION] 8630
[/simple-open] 8147
[/cells/] 7747
[/cells/default-cell-code] 7636
[/simple-open/open-container] 7574
 таких как: расхождение в количестве мест по документам и по факту,
 3687
[/open-one/change-sort-plan] 3678
 отличия в типе тары для НПО - порожняя тара,
 3635
 расхождения в количестве порожней тары по каждому типу тары.
 3635
[/open-one/process-open-one-session-request/OPEN_ONE] 3514
[/open-one/parallel-opening] 3485
[/open-one/finish-openone-session/] 3329
[/defectItems/findDefectItemsByWorkzones] 2736
15.1133394241333
"""