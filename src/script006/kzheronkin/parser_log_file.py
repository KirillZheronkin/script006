import re
import operator
import time


def time_measure(f):
    def wrapped_with_timer_func(*args, **kwargs):
        t0 = time.perf_counter()
        func_result = f(*args, **kwargs)
        t1 = time.perf_counter()
        return t1 - t0, func_result
    return wrapped_with_timer_func


def gen_file_lines(file_name, number_lines_to_read):
    for i in range(number_lines_to_read):
        read_line = file_name.readline()
        if read_line:
            yield read_line
        else:
            break


class LinesContainer:
    n = 5000

    def __init__(self, file_name):
        self.line_list = [line for line in gen_file_lines(file_name, self.n)]
        self.chunk_size = len(self.line_list)
        self.is_last_chunk = (self.chunk_size != self.n)

    def __str__(self):
        output_str = ""

        for line in self.line_list:
            output_str += line
        return output_str


class FileStatistic:
    def __init__(self):
        self.links_stat = dict()
        self.bad_strings = list()
        self.bad_string_counter = 0
        #self.pattern = r'.*?(\[.*?].*?){4}\[(.*?)\].*'
        self.pattern = r'.*\[(/.*?)\].*'
        self.re_pattern = re.compile(self.pattern)

    def check_file_chunk(self, file_chunk):
        for line in file_chunk.line_list:
            obj = self.re_pattern.match(line)
            if obj:
                found_url = obj.group(1)
                if found_url in self.links_stat:
                    self.links_stat[found_url] += 1
                else:
                    self.links_stat[found_url] = 1
            else:
                self.bad_string_counter += 1
                    #self.bad_strings.append(line)

    def get_sorted_list(self):
        return sorted(self.links_stat.items(), key=operator.itemgetter(1), reverse=True)


@time_measure
def parse_log_file(file_name):
    file_statistics = FileStatistic()
    with open(file_name, 'r', encoding="utf8") as log_file:
        read_chunk = LinesContainer(log_file)
        file_statistics.check_file_chunk(read_chunk)

        while not read_chunk.is_last_chunk:
            read_chunk = LinesContainer(log_file)
            file_statistics.check_file_chunk(read_chunk)

        return file_statistics


if __name__ == "__main__":
    execution_time, url_stat_dict = parse_log_file("logfile.log")
    for value in url_stat_dict.get_sorted_list()[0:5]:
        print(value)

    print("Number of bad points {}".format(url_stat_dict.bad_string_counter))
    print("The function worked {} sec".format(execution_time))

