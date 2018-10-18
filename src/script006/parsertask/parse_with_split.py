from collections import defaultdict, Counter
import typing
import re
from time import time

_TOP_STRINGS_COUNT = 30
_FILENAME = '/home/mkoshel/dev/script006.git/resources/logsample.log'
# _PATTERN = re.compile("""(\d{2,4}-\d{1,2}-\d{1,2})\s(\d{2}\:\d{2}\:[\d\.]{1,6})\s(\[.*?\])\s(\[.*?\])\s(\[.*?\])\s(\[.*?\])\s(\[.*?\])\s(\[.*?\])\s(\[.*?\])\s(\-)""")


def parse_url(line: str) -> str:
    """
    line should be like
    2018-10-16 09:33:21.796 [!!!!!!!] [!!!!!!!!!!!!!!!!!] [CHUVINAEE] [10.128.254.96] [/auth/user] [GET] [2 ms] -"""
    splitted = line.split('[')
    if len(splitted) == 8:
        if splitted[5].startswith("/"):
            return splitted[5].rstrip()[:-1]
    return line



if __name__ == '__main__':
    start = time()
    storage = Counter()
    for line in open(_FILENAME, "r"): storage[parse_url(line)] +=1
    [
        print(line, storage[line])
        for line in sorted(
            storage,
            key=lambda x: storage[x],
            reverse=True
        )[:_TOP_STRINGS_COUNT]
    ]

    end = time()
    print(end - start)


"""
/auth/user 918268
/conveyorline/process/barcode 555977
/session/validateOverweight 268412
/auth/current_arm_workzone_site 107995
/session/validateItemForNoInDefect 91671
/session/opened/request-cells-count 55082
/open-one/get-active-opening-session 38924
/container/reforming 15891
/container/reforming/createSessionFromVessel 15375
/printers/select-printer 15324
/printers/select-docs-printers 12764
/printers/select-labels-printers 12764
/container/forming/last-formed-container 9767
/simple-open 8147
/cells/ 7747
/cells/default-cell-code 7636
/simple-open/open-container 7574
/open-one/add-invoice 4310
 таких как: расхождение в количестве мест по документам и по факту,
 3687
/open-one/change-sort-plan 3678
 отличия в типе тары для НПО - порожняя тара,
 3635
 расхождения в количестве порожней тары по каждому типу тары.
 3635
/open-one/process-open-one-session-request/OPEN_ONE 3514
/open-one/parallel-opening 3485
/defectItems/findDefectItemsByWorkzones 2736
/container/forming/manual/confirm-destination 2303
/invoice 1346
/defectItems/findByWorkzone/11 1034
/defectItems/sortRpi 858
/controlreference/getCloudReportAddressByItemType/CONTAINER 842
9.51599669456482

"""