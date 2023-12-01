import datetime
import multiprocessing
import os
import shutil

from get_info import get_full_info
from get_links import get_links
from multiprocessing.pool import ThreadPool
from ranges import ranges_for_parser, max_pages
from save_page import save_page
from saver_to_excel import refactor_and_save_to_excel
from timer import Timer


def main():
    os.mkdir('links')
    os.mkdir('pages')
    os.mkdir('img')

    ranges_all = ranges_for_parser(max_pages(), 20)

    for ranges in ranges_all[45:46]:
        dataset = []
        links_list = []
        num = 0
        print(f"Parsing from {ranges[0]} to {ranges[1]} page")
        args1 = [os.getenv("URL").format(n) for n in range(ranges[0], ranges[1])]
        args2 = [os.getenv("PATH_TO_SAVED_LINKS").format(n) for n in range(ranges[0], ranges[1])]
        args = [(arg1, arg2) for arg1, arg2 in zip(args1, args2)]
        with ThreadPool(20) as pool:
            pool.starmap(save_page, args)

        for link in args2:
            links_list += get_links(link)
        print('links_list Done')

        path_to = [os.getenv("PATH_TO_SAVED_PAGE").format(links_list.index(link)) for link in links_list]
        args_list = [(link, path) for link, path in zip(links_list, path_to)]
        with ThreadPool(20) as pool:
            pool.starmap(save_page, args_list)
        print("pages saved")
        with multiprocessing.Pool(8) as pool:
            dataset = list(pool.map(get_full_info, path_to))
        print("refactoring and saving to excel...")
        num = ranges_all.index(ranges)
        refactor_and_save_to_excel(data=dataset, num=num)

    shutil.rmtree('links')
    shutil.rmtree('pages')
    shutil.rmtree('img')


if __name__ == '__main__':
    with Timer('Executed in: {}s'):
        main()
