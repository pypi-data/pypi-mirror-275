#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Author  : nickdecodes
@Email   : nickdecodes@163.com
@Usage   :
@FileName: daletou.py
@DateTime: 2023/12/7 19:58
@SoftWare:
"""

import os
import random
import time
import math
from datetime import datetime, timedelta
from itertools import combinations
from collections import Counter, namedtuple
from typing import List, Tuple, Any, Optional, Union, Dict, NamedTuple, Callable, Generator, Iterable, Set
from selenium.webdriver.common.by import By
from .util import IOUtil, ModelUtil, SpiderUtil, CalculateUtil, AnalyzeUtil, re, WebDriverWait, EC


class Daletou(IOUtil, ModelUtil, SpiderUtil, CalculateUtil, AnalyzeUtil):
    # Default values for t prediction configuration
    AWARD_URL = 'https://www.lottery.gov.cn/kj/kjlb.html?dlt'
    PREDICT_NUM = 5  # Default number of t tickets to predict
    NORMAL_SIZE = 7  # Length of normal winning numbers e.g. 12,17,27,29,34,06,09
    ORIGIN_SIZE = 9  # Length of historical record data e.g. 07013,2007-06-27,12,17,27,29,34,06,09
    # Super Lotto prize rules (pre-tax, without considering floating conditions)
    AWARD_RULES = {
        (5, 2): 10000000,
        (5, 1): 800691,
        (5, 0): 10000,
        (4, 2): 3000,
        (4, 1): 300,
        (3, 2): 200,
        (4, 0): 100,
        (3, 1): 15,
        (2, 2): 15,
        (3, 0): 5,
        (2, 1): 5,
        (1, 2): 5,
        (0, 2): 5
    }

    # Front area configuration
    FRONT_SIZE = 5  # Number of numbers to choose in the front area
    FRONT_VOCAB_SIZE = 35  # Types of numbers in the front area
    FRONT_ZONE_RANGES = [(1, 12), (13, 24), (25, 35)]  # Front area zone distribution
    FRONT_BIG_SMALL_RANGES = [(18, 35), (1, 17)]  # Numbers 01–17 are small, 18–35 are big in the front area.
    FRONT_ROAD_012_RANGES = [
        (3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33),
        (1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34),
        (2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35)
    ]  # Front area 012 road division

    # Back area configuration
    BACK_SIZE = 2  # Number of numbers to choose in the back area
    BACK_VOCAB_SIZE = 12  # Types of numbers in the back area
    BACK_ZONE_RANGES = [(1, 6), (7, 12)]  # Back area zone distribution
    BACK_BIG_SMALL_RANGES = [(7, 12), (1, 6)]  # Numbers 01–06 are small, 07–12 are big in the back area.
    BACK_ROAD_012_RANGES = [
        (3, 6, 9, 12),
        (1, 4, 7, 10),
        (2, 5, 8, 11)
    ]  # Back area 012 road division

    # NamedTuple for t data
    Lottery = namedtuple('Lottery', ['period', 'date', 'weekday', 'front', 'back'])

    def __init__(self, **kwargs):
        """
        Initialize the Daletou object with configuration parameters.

        :param kwargs: A dictionary of keyword arguments where:
            - 'url': str - The URL to fetch the data from. Defaults to the class's AWARD_URL if not provided.
            - 'log_file': Optional[str] - The path to the log file. Defaults to None.
            - 'dataset_dir': str - The directory path for the dataset. Defaults to './dataset'.
            - 'predict_num': int - The number of predictions to make. Defaults to the class's PREDICT_NUM.
            - 'normal_size': int - The size of the normal number set. Defaults to the class's NORMAL_SIZE.
            - 'origin_size': int - The original size of the dataset. Defaults to the class's ORIGIN_SIZE.
            - 'award_rules': Dict - The rules for the awards. Defaults to the class's AWARD_RULES.
            - 'front_size': int - The size of the front number set. Defaults to the class's FRONT_SIZE.
            - 'front_vocab_size': int - The vocabulary size of the front number set.
                                  Defaults to the class's FRONT_VOCAB_SIZE.
            - 'back_size': int - The size of the back number set. Defaults to the class's BACK_SIZE.
            - 'back_vocab_size': int - The vocabulary size of the back number set.
                                 Defaults to the class's BACK_VOCAB_SIZE.
            - 'front_zone_ranges': List[Tuple[int, int]] - The range of front zones.
                                   Defaults to the class's FRONT_ZONE_RANGES.
            - 'front_big_small_ranges': List[Tuple[int, int]] - The range of front big/small numbers.
                                        Defaults to the class's FRONT_BIG_SMALL_RANGES.
            - 'front_road_012_ranges': List[Tuple[int, ...]] - The range of front road 012 numbers.
                                       Defaults to the class's FRONT_ROAD_012_RANGES.
            - 'back_zone_ranges': List[Tuple[int, int]] - The range of back zones.
                                  Defaults to the class's BACK_ZONE_RANGES.
            - 'back_big_small_ranges': List[Tuple[int, int]] - The range of back big/small numbers.
                                       Defaults to the class's BACK_BIG_SMALL_RANGES.
            - 'back_road_012_ranges': List[Tuple[int, ...]] - The range of back road 012 numbers.
                                      Defaults to the class's BACK_ROAD_012_RANGES.
        """
        super().__init__(**kwargs)
        self.url: str = kwargs.get('url', self.AWARD_URL)
        self.log_file: Optional[str] = kwargs.get('log_file', None)
        self.dataset_dir: str = kwargs.get('dataset_dir', os.path.join('dataset'))
        self.predict_num: int = kwargs.get('predict_num', self.PREDICT_NUM)
        self.normal_size: int = kwargs.get('normal_size', self.NORMAL_SIZE)
        self.origin_size: int = kwargs.get('origin_size', self.ORIGIN_SIZE)
        self.award_rules: Dict = kwargs.get('award_rules', self.AWARD_RULES)
        self.front_size: int = kwargs.get('front_size', self.FRONT_SIZE)
        self.front_vocab_size: int = kwargs.get('front_vocab_size', self.FRONT_VOCAB_SIZE)
        self.back_size: int = kwargs.get('back_size', self.BACK_SIZE)
        self.back_vocab_size: int = kwargs.get('back_vocab_size', self.BACK_VOCAB_SIZE)
        self.front_zone_ranges: List[Tuple[int, int]] = kwargs.get('front_zone_ranges', self.FRONT_ZONE_RANGES)
        self.front_big_small_ranges: List[Tuple[int, int]] = kwargs.get('front_big_small_ranges',
                                                                        self.FRONT_BIG_SMALL_RANGES)
        self.front_road_012_ranges: List[Tuple[int, ...]] = kwargs.get('front_road_012_ranges',
                                                                       self.FRONT_ROAD_012_RANGES)
        self.back_zone_ranges: List[Tuple[int, int]] = kwargs.get('back_zone_ranges', self.BACK_ZONE_RANGES)
        self.back_big_small_ranges: List[Tuple[int, int]] = kwargs.get('back_big_small_ranges',
                                                                       self.BACK_BIG_SMALL_RANGES)
        self.back_road_012_ranges: List[Tuple[int, ...]] = kwargs.get('back_road_012_ranges', self.BACK_ROAD_012_RANGES)

        self.app_log = self.get_logger(self.log_file)
        if not os.path.exists(self.dataset_dir):
            os.makedirs(self.dataset_dir)
        self.history_record_path = os.path.join(self.dataset_dir, 'daletou_history.csv')
        self.predict_record_path = os.path.join(self.dataset_dir, 'daletou_predict.csv')
        self.period_record_path = os.path.join(self.dataset_dir, 'daletou_period.json')
        self.weekday_record_path = os.path.join(self.dataset_dir, 'daletou_weekday.json')
        self.consecutive_record_path = os.path.join(self.dataset_dir, 'consecutive.json')
        self.repeated_record_path = os.path.join(self.dataset_dir, 'repeated.json')
        self.edge_record_path = os.path.join(self.dataset_dir, 'edge.json')
        self.cold_hot_record_path = os.path.join(self.dataset_dir, 'cold_hot.json')
        self.omitted_record_path = os.path.join(self.dataset_dir, 'omitted.json')
        self.all_fronts = list(combinations(range(1, self.front_vocab_size + 1), self.front_size))
        self.all_backs = list(combinations(range(1, self.back_vocab_size + 1), self.back_size))
        self.feature_keys = ['zone_ratio', 'big_small_ratio', 'road_012_ratio', 'odd_even_ratio',
                             'prime_composite_ratio', 'span', 'sum_total', 'sum_tail', 'ac',
                             'consecutive_numbers']
        self.append_feature_mapping = {
            'repeated_numbers': 1,
            'edge_numbers': 1,
            # 'cold_hot_numbers': 4,
            # 'omitted_numbers': 9
        }

    """
    A pure virtual method inherited from util.SpiderUtil
    """

    def spider_recent_data(self) -> List[List[str]]:
        """
        Fetch the recent data from the web page.

        :return: A list of lists containing recent data entries.
        """
        driver = self.spider_chrome_driver()
        time.sleep(1)  # Allow time for the page to load
        frame = driver.find_element(By.XPATH, '//iframe[@id="iFrame1"]')
        driver.switch_to.frame(frame)
        content = driver.find_element(By.XPATH, '//tbody[@id="historyData"]')
        recent_data = [x.split(' ')[:9] for x in content.text.split('\n') if len(x.split(' ')) > 9]
        return recent_data

    def spider_latest_data(self) -> Optional[List[str]]:
        """
        Fetch the latest single data entry.

        :return: A list containing the latest data entry, or None if there is no data.
        """
        recent_data = self.spider_recent_data()
        return recent_data[0] if recent_data else None

    def spider_full_data(self) -> List[List[str]]:
        """
        Load the full set of data from the source.

        :return: A list of lists containing all data entries.
        """
        # The implementation should be provided by the subclass.
        full_data = []
        driver = self.spider_chrome_driver()
        time.sleep(1)  # Allow time for the page to load
        frame = driver.find_element(By.XPATH, '//iframe[@id="iFrame1"]')
        driver.switch_to.frame(frame)
        matches = re.findall(r'goNextPage\((\d+)\)', driver.page_source)
        page_index = [int(match) for match in matches]
        self.app_log.info(f'total pages: {max(page_index)} need to spider')
        for index in range(max(page_index)):
            self.app_log.info(f'spider page {index + 1}')
            # wait data load
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//tbody[@id="historyData"]'))
            )

            # extract data
            content = driver.find_element(By.XPATH, '//tbody[@id="historyData"]')
            full_data.extend([x.split()[:9] for x in content.text.split('\n') if len(x.split()) >= 9])

            # wait next page load
            try:
                # try to find element of position == 13
                next_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[3]/ul/li[position()=13]"))
                )
            except Exception as ex:
                # self.app_log.info(ex)
                # try to find element of position == 8
                next_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[3]/ul/li[position()=8]"))
                )

            # click to next page
            next_button.click()
            time.sleep(3)  # loading
        driver.quit()
        sorted_full_data = sorted(full_data, key=lambda x: int(x[0]))

        return sorted_full_data

    """
    A pure virtual method inherited from util.AnalyzeUtil
    """

    def analyze_same_period_numbers(self, data=None, **kwargs: Any) -> None:
        """
        Analyze same period number in the last period.
        """
        if data is None:
            return

            # Read existing data from files
        if os.path.exists(self.period_record_path):
            record_data = self.read_json_data_from_file(self.period_record_path, app_log=self.app_log)
        else:
            record_data = {}

        # Process new data for both period and weekday statistics
        for d in data:
            # Common data structure used for both period and weekday
            common_data = [
                d[0],
                d[1],
                self.calculate_weekday(d[1]),
                self.calculate_front(d),
                self.calculate_back(d)
            ]
            if int(record_data.get('last_period', 0)) >= int(d[0]):
                continue
            self.app_log.info('Update {} to {}'.format(common_data, self.period_record_path))
            # Update period statistic
            period_num = d[0][-3:]
            record_data['last_period'] = d[0]
            record_data.setdefault(period_num, []).append(common_data)

        # Write updated data back to files
        self.write_json_data_to_file(self.period_record_path, record_data, app_log=self.app_log)

    def analyze_same_weekday_numbers(self, data=None, **kwargs: Any) -> None:
        """
        Analyze same weekday number in the last period.
        """
        if data is None:
            return

            # Read existing data from files
        if os.path.exists(self.weekday_record_path):
            record_data = self.read_json_data_from_file(self.weekday_record_path, app_log=self.app_log)
        else:
            record_data = {}

        # Process new data for both period and weekday statistics
        for d in data:
            # Common data structure used for both period and weekday
            common_data = [
                d[0],
                d[1],
                self.calculate_weekday(d[1]),
                self.calculate_front(d),
                self.calculate_back(d)
            ]
            if int(record_data.get('last_period', 0)) >= int(d[0]):
                continue
            self.app_log.info('Update {} to {}'.format(common_data, self.weekday_record_path))
            weekday = common_data[2]  # Already calculated in common_data
            record_data['last_period'] = d[0]
            record_data.setdefault(str(weekday), []).append(common_data)

        # Write updated data back to files
        self.write_json_data_to_file(self.weekday_record_path, record_data, app_log=self.app_log)

    def analyze_repeated_numbers(self, data=None, **kwargs: Any) -> None:
        """
        Analyze the number that appeared twice in the last two period.
        """
        if data is None:
            return

            # Read existing data from files
        if os.path.exists(self.repeated_record_path):
            record_data = self.read_json_data_from_file(self.repeated_record_path, app_log=self.app_log)
        else:
            record_data = {}

        # Process new data for both period and weekday statistics
        for i, d in enumerate(data):
            # Common data structure used for both period and weekday
            common_data = [
                d[0],
                d[1],
                self.calculate_weekday(d[1]),
                self.calculate_front(d),
                self.calculate_back(d)
            ]
            if int(record_data.get('last_period', 0)) >= int(d[0]):
                continue
            common_data.append(self.calculate_repeated_numbers([self.calculate_front(data[i - 1]),
                                                                self.calculate_front(d)]))
            common_data.append(self.calculate_repeated_numbers([self.calculate_back(data[i - 1]),
                                                                self.calculate_back(d)]))
            self.app_log.info('Update {} to {}'.format(common_data, self.repeated_record_path))
            record_data['last_period'] = d[0]
            record_data.setdefault(d[0], []).extend(common_data)

        # Write updated data back to files
        self.write_json_data_to_file(self.repeated_record_path, record_data, app_log=self.app_log)

    def analyze_edge_numbers(self, data=None, **kwargs: Any) -> None:
        """
        Analyze Also called adjacent number, plus or minus 1 with the winning number issued in the previous period
        """
        if data is None:
            return

            # Read existing data from files
        if os.path.exists(self.edge_record_path):
            record_data = self.read_json_data_from_file(self.edge_record_path, app_log=self.app_log)
        else:
            record_data = {}

        # Process new data for both period and weekday statistics
        for i, d in enumerate(data):
            if i == 0:
                continue
            # Common data structure used for both period and weekday
            common_data = [
                d[0],
                d[1],
                self.calculate_weekday(d[1]),
                self.calculate_front(d),
                self.calculate_back(d)
            ]
            if int(record_data.get('last_period', 0)) >= int(d[0]):
                continue
            common_data.append(self.calculate_edge_numbers([self.calculate_front(x) for x in [data[i - 1], d]]))
            common_data.append(self.calculate_edge_numbers([self.calculate_back(x) for x in [data[i - 1], d]]))
            self.app_log.info('Update {} to {}'.format(common_data, self.edge_record_path))
            record_data['last_period'] = d[0]
            record_data.setdefault(d[0], []).extend(common_data)

        # Write updated data back to files
        self.write_json_data_to_file(self.edge_record_path, record_data, app_log=self.app_log)

    def analyze_cold_hot_numbers(self, data=None, **kwargs: Any) -> None:
        """
        Analyze Numbers that have appeared in the last period
        Analyze Numbers that have not appeared in the last period
        """
        if data is None:
            return

            # Read existing data from files
        if os.path.exists(self.cold_hot_record_path):
            record_data = self.read_json_data_from_file(self.cold_hot_record_path, app_log=self.app_log)
        else:
            record_data = {}

        # Process new data for both period and weekday statistics
        for i, d in enumerate(data):
            if i < 4:
                continue
            # Common data structure used for both period and weekday
            common_data = [
                d[0],
                d[1],
                self.calculate_weekday(d[1]),
                self.calculate_front(d),
                self.calculate_back(d)
            ]
            if int(record_data.get('last_period', 0)) >= int(d[0]):
                continue
            front_cold_numbers, front_hot_numbers = self.calculate_cold_hot_numbers(
                [self.calculate_front(x) for x in data[i - 4:i]], all_numbers=range(1, self.front_vocab_size + 1))
            common_data.append((front_cold_numbers, front_hot_numbers))
            back_cold_numbers, back_hot_numbers = self.calculate_cold_hot_numbers(
                [self.calculate_back(x) for x in data[i - 4:i]], all_numbers=range(1, self.back_vocab_size + 1))
            common_data.append((back_cold_numbers, back_hot_numbers))
            self.app_log.info('Update {} to {}'.format(common_data, self.cold_hot_record_path))
            record_data['last_period'] = d[0]
            record_data.setdefault(d[0], []).extend(common_data)

        # Write updated data back to files
        self.write_json_data_to_file(self.cold_hot_record_path, record_data, app_log=self.app_log)

    def analyze_omitted_numbers(self, data=None, **kwargs: Any) -> None:
        """
        Analyze.
        Omission: The number of periods since the previous opening to the current period.
        Average omission: The average number of omissions in the statistical period
                          (calculation formula: Average omission =
                          total number of omissions in the statistical period / (number of occurrences +1))
        Maximum missed value: Indicates the maximum value of all missed values in the statistical period.
        Current omission: The number of periods between the last occurrence and the present, if the missing object
                          appeared in the current period, the current omission value is 0
        Previous period omission: The interval between the last two periods (excluding the current period)
        Theoretical number: The theoretical number refers to the number of times the missing object should
                            theoretically appear, = the total number of t times * theoretical probability
        Desired probability: Desired probability reflects the ideal occurrence probability of the missing object.
                             The formula is (current omission/average omission * theoretical probability)
        """
        if data is None:
            return

        # Read existing data from files
        if os.path.exists(self.omitted_record_path):
            record_data = self.read_json_data_from_file(self.omitted_record_path, app_log=self.app_log)
        else:
            record_data = {}

        # Process new data for both period and weekday statistics
        for i, d in enumerate(data):
            if i < 9:
                continue
            # Common data structure used for both period and weekday
            common_data = [
                d[0],
                d[1],
                self.calculate_weekday(d[1]),
                self.calculate_front(d),
                self.calculate_back(d)
            ]
            if int(record_data.get('last_period', 0)) >= int(d[0]):
                continue
            front_omitted_numbers = self.calculate_omitted_numbers(
                [self.calculate_front(x) for x in data[10 - i:]], all_numbers=range(1, self.front_vocab_size + 1))
            common_data.append(front_omitted_numbers)
            back_omitted_numbers = self.calculate_omitted_numbers(
                [self.calculate_back(x) for x in data[10 - i:]], all_numbers=range(1, self.back_vocab_size + 1))
            common_data.append(back_omitted_numbers)
            self.app_log.info('Update {} to {}'.format(common_data, self.omitted_record_path))
            record_data['last_period'] = d[0]
            record_data.setdefault(d[0], []).extend(common_data)

        # Write updated data back to files
        self.write_json_data_to_file(self.omitted_record_path, record_data, app_log=self.app_log)

    """
    A pure virtual method inherited from util.CalculateUtil
    """

    def calculate_winning_amount(self,
                                 winning_number_combination: Union[NamedTuple, List[int], None],
                                 purchase_number_combinations: Union[List[NamedTuple], List[List[int]], None],
                                 **kwargs: Any) -> Tuple[int, int]:
        """
        Calculate the winning amount based on matching combinations.

        :param winning_number_combination: Winning number combination.
        :param purchase_number_combinations: Purchase number combinations.
        :param kwargs: Additional keyword arguments.
        :return: The total winning amount and the count of winning combinations.
        """

        def single_winning_amount(_winning: Union[NamedTuple, List[int], None],
                                  _purchase: Union[NamedTuple, List[int], None]) -> int:
            if hasattr(_winning, 'front') and hasattr(_winning, 'back'):
                award_front, award_back = _winning.front, _winning.back
            else:
                award_front, award_back = self.calculate_front(_winning), self.calculate_back(_winning)

            if hasattr(_purchase, 'front') and hasattr(_purchase, 'back'):
                purchase_front, purchase_back = _purchase.front, _purchase.back
            else:
                purchase_front, purchase_back = self.calculate_front(_purchase), self.calculate_back(_purchase)

            match_front = len(set(award_front).intersection(set(purchase_front)))
            match_back = len(set(award_back).intersection(set(purchase_back)))
            return self.award_rules.get((match_front, match_back), 0)

        award_amount = 0
        award_count = 0
        for number_combination in purchase_number_combinations:
            award = single_winning_amount(winning_number_combination, number_combination)
            award_amount += award
            if award > 0:
                award_count += 1

        return award_amount, award_count

    """
    Static methods with no side effects
    """

    @staticmethod
    def get_chunks_with_next(data: List[Any],
                             chunk_size: int = 10) -> Generator[Tuple[List[Any], Optional[Any]], None, None]:
        """
        Yields consecutive chunks of size `chunk_size` from `data` after removing elements from the start of `data`
        based on the remainder of the length of `data` divided by `chunk_size`. Exits if the next element is None.

        :param data: The list of data from which to extract chunks.
        :param chunk_size: The size of each chunk. Default is 10.
        :yield: Tuples containing a chunk and the next element, if it exists.
        """
        # Calculate the number of elements to remove from the beginning of the list
        remainder = len(data) % chunk_size
        if remainder > 0:
            data = data[remainder:]

        # Generate the chunks and the next element
        for i in range(0, len(data)):
            chunk = data[i:i + chunk_size]
            next_element = data[i + chunk_size] if i + chunk_size < len(data) else None
            if next_element is None:
                break  # Break if we've reached or passed the end of the list
            yield chunk, next_element

    """
    other instance method
    """

    def download_data(self, force: bool = False) -> None:
        """
        spider full data and save data to history record file

        Parameters:
        - force: If True, files will write even if they already exist. Defaults to False.
        """

        if not os.path.exists(self.history_record_path) or force:
            history_data = self.spider_full_data()
            self.app_log.info(f'is saving history record to {self.history_record_path}')
            self.write_csv_data_to_file(self.history_record_path, data=history_data, app_log=self.app_log)
            self.analyze_same_period_numbers(history_data)
            self.analyze_same_weekday_numbers(history_data)
        else:
            print(f"{self.history_record_path} already exists in {self.dataset_dir}. Use force=True to overwrite.")

    def fetch_data(self, data=None):
        """
        fetch data. then update dataset

        :param data: New data to be added. If None, data will be fetched using Spider.get_history_data().
        :return: None
        """

        def load_recent_data(_data):
            _old_data = []
            if _data is None:
                if not os.path.exists(self.history_record_path):
                    return self.spider_full_data()

                try:
                    recent_data = self.spider_recent_data()
                except Exception as ex:
                    self.app_log.exception("Failed to spider recent data: {}".format(ex))
                    return None

                try:
                    _old_data = self.read_csv_data_from_file(self.history_record_path, app_log=self.app_log)
                    previous_data = _old_data[-1]
                except IndexError:
                    self.app_log.warning("History file is empty or does not exist.")
                    return None

                last_index = next((i for i, value in enumerate(recent_data) if value[0] == previous_data[0]), None)

                if last_index is None:
                    self.app_log.info("No matching data found in history.")
                    return None

                # Slice the history_data list to get the new relevant content
                _new_data = sorted(recent_data[:last_index], key=lambda x: int(x[0]))
            elif isinstance(_data, str):
                _new_data = [_data.split()]
            else:
                _new_data = _data
            return _old_data, _new_data

        old_data, new_data = load_recent_data(data)
        if not new_data:
            self.app_log.info('Not found new data: {}'.format(new_data))
            return
        self.app_log.info('Updating history data: {}'.format(new_data))

        # update history record
        self.write_csv_data_to_file(self.history_record_path, data=new_data, app_log=self.app_log)

        # update analyze
        self.analyze_same_period_numbers(new_data)
        self.analyze_same_weekday_numbers(new_data)
        # self.analyze_repeated_numbers([*old_data[-1:], *new_data])
        # self.analyze_edge_numbers([*old_data[-1:], *new_data])
        # self.analyze_cold_hot_numbers([*old_data[-4:], *new_data])
        # self.analyze_omitted_numbers([*old_data[-9:], *new_data])

    @staticmethod
    def get_next_weekday() -> int:
        """
        Gets the next t day based on the current day and time.
        The draw days are determined as follows:
        - If the current time is before 9:30 PM:
            - Tuesday or Wednesday: returns 3
            - Thursday, Friday, or Saturday: returns 6
            - Sunday or Monday: returns 1
        - If the current time is after 9:30 PM:
            - The next draw day is calculated based on the next applicable weekday.

        Returns:
            int: The next draw day (1 for Sunday/Monday, 3 for Tuesday/Wednesday, 6 for Thursday-Saturday).
        """
        now: datetime = datetime.now()
        weekday: int = now.weekday()
        hour: int = now.hour
        minute: int = now.minute
        if (hour, minute) < (21, 30):
            return 3 if weekday in [2, 3] else 6 if weekday in [4, 5, 6] else 1
        else:
            return 3 if weekday <= 2 else 6 if weekday <= 5 else 1

    @staticmethod
    def get_next_period() -> int:
        now = datetime.now()
        current_year = now.year
        # Determine the first day of the year
        first_day_of_year = datetime(current_year, 1, 1)
        # Find the first draw day
        while first_day_of_year.weekday() not in [0, 2, 5]:
            first_day_of_year += timedelta(days=1)

        # If current time is before today's draw time, then today is not a draw day
        if now.hour < 21 or (now.hour == 21 and now.minute < 30):
            today_draw = now.replace(hour=21, minute=30, second=0, microsecond=0)
        else:  # Otherwise, calculate the next draw day
            today_draw = now.replace(hour=21, minute=30, second=0, microsecond=0) + timedelta(days=1)
            # If the next day is not a draw day, postpone to the next draw day
            while today_draw.weekday() not in [0, 2, 5]:
                today_draw += timedelta(days=1)

        # Calculate the number of days from the beginning of the year to the next draw date
        delta = today_draw - first_day_of_year
        # Calculate the number of draw days that have passed, with three draws per week
        next_period = delta.days // 7 * 3
        for i in range(delta.days % 7 + 1):
            if (first_day_of_year + timedelta(days=i)).weekday() in [0, 2, 5]:
                next_period += 1

        # Return the draw number of the next t for the current year
        return next_period

    def get_kill_numbers(self, data: List[Any], next_period: int = None, next_weekday: int = None) -> Tuple[
        Set[int], Set[int]]:
        """
        Calculate and return sets of 'kill numbers' for both front and back sequences based on provided data.

        Parameters:
            data (List[Any]): The data to process.
            next_period (int, optional): The next period number. If None, it's calculated.
            next_weekday (int, optional): The next weekday number. If None, it's calculated.

        Returns:
            Tuple[Set[int], Set[int]]: A tuple containing two sets of kill numbers for front and back sequences.
        """
        front_sequences = [self.calculate_front(d) for d in data]
        back_sequences = [self.calculate_back(d) for d in data]

        next_weekday = next_weekday or self.get_next_weekday()
        next_period = next_period or self.get_next_period()

        front_kill_numbers = self.calculate_front_kills(front_sequences, next_period, next_weekday)
        back_kill_numbers = self.calculate_back_kills(back_sequences, next_weekday)

        # Ensure numbers are within the valid range
        front_kill_numbers = {num for num in front_kill_numbers if 1 <= num <= self.front_vocab_size}
        back_kill_numbers = {num for num in back_kill_numbers if 1 <= num <= self.back_vocab_size}

        return front_kill_numbers, back_kill_numbers

    @staticmethod
    def get_same_number_index(pre_data, cur_data):
        same_number_index = []
        for ind, num in enumerate(pre_data):
            if num in cur_data:
                same_number_index.append(ind + 1)
        return same_number_index

    @staticmethod
    def get_edge_number_index(pre_data, cur_data):
        edge_info = []
        for ind, num in enumerate(pre_data):
            edge_nums = set(num + i for i in [-1, 1])
            plead_edge = set(cur_data).intersection(edge_nums)
            if len(plead_edge) > 0:
                edge_info.append(ind + 1)
        return edge_info

    def calculate_front_kills(self, sequences: List[List[int]], next_period: int, next_weekday: int) -> Set[int]:
        """Helper function to calculate front kill numbers based on the last sequence."""

        def train_predict(chunk, func_name, chunk_size=1):
            train_data = [result
                          for c, n in self.get_chunks_with_next(chunk, chunk_size)
                          for result in func_name(c[-1], n)]
            return (
                {self.exponential_moving_average_next_value(train_data),
                 self.linear_regression_next_value_by_index(train_data),
                 self.harmonic_regression_next_value_by_index(train_data)}
                if len(train_data) > 2 else {}
            )

        last_sequence = sequences[-1]
        a1, a2, a3, a4, a5 = last_sequence
        fb = abs(a5 - a3 - a1)
        fc = a4 - a2
        average = sum(last_sequence) // self.front_size

        kills = {fb + t for t in [0, 1, 3, 6] if abs(t) != next_weekday}
        if fb == 0:
            kills.update({a1, a3, a5})
        kills.update({fc, (fc + next_period) % self.front_vocab_size, abs(fc - next_period) % self.front_vocab_size})
        kills.update({average, sum([a1, a2, a3]) // 3})
        kills.update({(a1 + a2) - (a3 + a4) - a5, a1 + a2 + a3 + a4 - a5})

        # odd_even_ratio = [n - 1 if n != 0 else n for n in set(self.calculate_odd_even_ratio(sequences[-1]))]
        zone_ratio = [n - 1 if n != 0 else n for n in set(self.calculate_zone_ratio(sequences[-1],
                                                                                    self.front_zone_ranges))]
        span = self.calculate_span(sequences[-1])
        edge_index = train_predict(sequences, self.get_edge_number_index)
        same_index = train_predict(sequences, self.get_edge_number_index)
        kills.update({
            abs(sequences[-1][zone_ratio[0]] - sequences[-1][zone_ratio[-1]]),
            (sequences[-1][zone_ratio[0]] + sequences[-1][zone_ratio[-1]]) % 35,
            abs(sequences[-1][-zone_ratio[0]] - sequences[-1][-zone_ratio[-1]]),
            (sequences[-1][-zone_ratio[0]] + sequences[-1][-zone_ratio[-1]]) % 35,
            abs(sequences[-1][0] - span),
            (sequences[-1][-1] + span) % 35,
            span
        })
        if edge_index:
            kills.update(sequences[-1][edge - 1] + i for edge in edge_index if edge - 1 in range(5) for i in [-1, 1])

        if same_index:
            kills.update(sequences[-1][same - 1] for same in same_index if same - 1 in range(5))

        return kills

    def calculate_back_kills(self, sequences: List[List[int]], next_weekday: int) -> Set[int]:
        """Helper function to calculate back kill numbers based on the last sequence."""

        def train_predict(chunk, func_name, chunk_size=1):
            train_data = [result
                          for c, n in self.get_chunks_with_next(chunk, chunk_size)
                          for result in func_name(c[-1], n)]
            return (
                {self.exponential_moving_average_next_value(train_data),
                 self.linear_regression_next_value_by_index(train_data),
                 self.harmonic_regression_next_value_by_index(train_data)}
                if len(train_data) > 2 else {}
            )

        last_sequence = sequences[-1]
        b1, b2 = last_sequence
        bb = abs(b1 - b2)
        kills = {bb + t for t in [0, 1, 3, 6] if abs(t) != next_weekday}
        kills.update(sequences[-2])
        if bb == 0:
            kills.update({b1, b2})
        kills.update({sum(last_sequence) // self.back_size})

        # odd_even_ratio = [n - 1 if n != 0 else n for n in set(self.calculate_odd_even_ratio(sequences[-1]))]
        zone_ratio = [n - 1 if n != 0 else n for n in set(self.calculate_zone_ratio(sequences[-1],
                                                                                    self.back_zone_ranges))]
        span = self.calculate_span(sequences[-1])
        edge_index = train_predict(sequences, self.get_edge_number_index)
        same_index = train_predict(sequences, self.get_edge_number_index)
        kills.update({
            abs(sequences[-1][zone_ratio[0]] - sequences[-1][zone_ratio[-1]]),
            (sequences[-1][zone_ratio[0]] + sequences[-1][zone_ratio[-1]]) % 35,
            abs(sequences[-1][-zone_ratio[0]] - sequences[-1][-zone_ratio[-1]]),
            (sequences[-1][-zone_ratio[0]] + sequences[-1][-zone_ratio[-1]]) % 35,
            abs(sequences[-1][0] - span),
            (sequences[-1][-1] + span) % 35,
            span
        })
        if edge_index:
            kills.update(sequences[-1][edge - 1] + i for edge in edge_index if edge - 1 in range(5) for i in [-1, 1])

        if same_index:
            kills.update(sequences[-1][same - 1] for same in same_index if same - 1 in range(5))
        return kills

    def get_banker_numbers(self, data: List[Any], next_period: int = None, next_weekday: int = None) -> Tuple[
        Set[int], Set[int]]:
        """
        Calculate and return sets of 'banker numbers' for both front and back sequences based on provided data.

        Parameters:
            data (List[Any]): The data to process.
            next_period (int, optional): The next period number. If None, it's calculated.
            next_weekday (int, optional): The next weekday number. If None, it's calculated.

        Returns:
            Tuple[Set[int], Set[int]]: A tuple containing two sets of banker numbers for front and back sequences.
        """
        front_sequences = [self.calculate_front(d) for d in data]
        back_sequences = [self.calculate_back(d) for d in data]
        next_weekday = next_weekday or self.get_next_weekday()
        next_period = next_period or self.get_next_period()

        front_banker_numbers = self.calculate_front_bankers(front_sequences, next_period, next_weekday)
        back_backer_numbers = self.calculate_back_bankers(back_sequences, next_weekday)

        # Ensure numbers are within the valid range
        front_banker_numbers = {num for num in front_banker_numbers if 1 <= num <= self.front_vocab_size}
        back_banker_numbers = {num for num in back_backer_numbers if 1 <= num <= self.back_vocab_size}

        return front_banker_numbers, back_banker_numbers

    @staticmethod
    def calculate_front_bankers(sequences: List[List[int]], next_period: int, next_weekday: int) -> Set[int]:
        """Helper function to calculate front banker numbers based on the last sequence."""
        last_sequence = sequences[-1]
        a1, a2, a3, a4, a5 = last_sequence
        bankers = {a1, a2, a3, a4, a5}
        for i in last_sequence:
            bankers.update({i - 1, i + 1})
        return bankers

    @staticmethod
    def calculate_back_bankers(sequences: List[List[int]], next_weekday: int) -> Set[int]:
        """Helper function to calculate back banker numbers based on the last sequence."""
        last_sequence = sequences[-1]
        b1, b2 = last_sequence
        bankers = {b1, b2}
        for i in last_sequence:
            bankers.update({i - 1, i + 1})
        return bankers

    def get_previous_history_data(self, next_period: int = None):
        history_data = self.read_csv_data_from_file(self.history_record_path, app_log=self.app_log)
        if next_period is None:
            history_data = history_data[:]
        else:
            index = next((i for i, sublist in enumerate(history_data) if sublist[0] == str(next_period)), -1)
            history_data = history_data[:index] if index != -1 else history_data[:]
        return history_data

    def get_previous_period_data(self, next_period: int = None):
        period_data = self.read_json_data_from_file(self.period_record_path, app_log=self.app_log)
        if next_period is None:
            period_data = period_data.get(str(self.get_next_period()).zfill(3))
        else:
            period_data = period_data.get(str(next_period % 100).zfill(3))
            index = next((i for i, sublist in enumerate(period_data) if sublist[0] == str(next_period)), -1)
            period_data = period_data[:index] if index != -1 else period_data[:]
        return period_data

    def get_previous_weekday_data(self, next_weekday: int = None, next_period: int = None):
        weekday_data = self.read_json_data_from_file(self.weekday_record_path, app_log=self.app_log)
        if next_weekday is None:
            weekday_data = weekday_data.get(str(self.get_next_weekday()))
        else:
            weekday_data = weekday_data.get(str(next_weekday))
            if next_period is not None:
                index = next((i for i, sublist in enumerate(weekday_data) if sublist[0] == str(next_period)), -1)
                weekday_data = weekday_data[:index] if index != -1 else weekday_data[:]
        return weekday_data

    def convert_lottery_data(self, data: List[Any]) -> Lottery:
        """
        Creates a Lottery named tuple from the provided data.

        :param data: A list containing t data.
        :return: A Lottery named tuple with the processed data.
        """
        try:
            return self.Lottery(
                period=data[0],
                date=data[1],
                weekday=self.calculate_weekday(data[1]),
                front=self.calculate_front(data),
                back=self.calculate_back(data)
            )
        except Exception as ex:
            # self.app_log.info(ex)
            # If there is an error, create a Lottery with the raw data
            # Ensure that 'data' can be unpacked into the Lottery named tuple
            return self.Lottery(*data)

    def calculate_front(self, data: Iterable[Any]) -> List[int]:
        """
        Calculate the 'front' portion of the data based on predefined size settings.

        :param data: The input data list whose 'front' part is to be calculated.
        :return: A list representing the 'front' portion of the data.
        :raises IndexError: If the length of data does not match any expected size.
        """
        length = len(list(data))

        # If data length is equal to the origin size, return the middle part of the data.
        if isinstance(data, self.Lottery):
            return data.front

        elif length == self.origin_size:
            return list(map(int, data[self.back_size:-self.back_size]))

        # If data length is equal to the normal size, return the front part of the data.
        elif length == self.normal_size:
            return list(map(int, data[:self.front_size]))

        # If data length is equal to the front size, return the data as is.
        elif length == self.front_size:
            return list(map(int, data))

        # If data length is equal to the back size, return an empty list.
        elif length == self.back_size:
            return []

        # If none of the above conditions are met, raise an IndexError.
        raise IndexError(f'length:{length} does not match any expected size')

    def calculate_back(self, data: Iterable[int]) -> List[int]:
        """
        Calculate the 'back' portion of the data based on predefined size settings.

        :param data: The input data list whose 'back' part is to be calculated.
        :return: A list representing the 'back' portion of the data.
        :raises IndexError: If the length of data does not match any expected size.
        """
        length = len(list(data))

        # If data length matches one of the expected sizes, return the 'back' part of the data.
        if isinstance(data, self.Lottery):
            return data.back
        elif length in (self.origin_size, self.normal_size):
            return list(map(int, data[-self.back_size:]))
        elif length == self.back_size:
            return list(map(int, data))
        elif length == self.front_size:
            return []

        # If none of the above conditions are met, raise an IndexError.
        raise IndexError(f'length:{length} does not match any expected size')

    def revised_features(self, last_window_period_datas: Dict[str, Any]) -> Dict[str, Any]:
        """
        Prepares the features data structure for the prediction algorithm.
        """

        def _feature_reviser(predictions: Counter, delta_size: int, feature_key: str) -> Counter:
            """
            Filters predictions based on the feature key and delta size.

            If the feature key includes 'ratio', only predictions where the sum equals the delta size are returned.
            Otherwise, all predictions are returned.

            Parameters:
            predictions (List[Tuple[Any, ...]]): A list of prediction tuples.
            delta_size (int): The target sum of the predictions if the feature key includes 'ratio'.
            feature_key (str): The key of the feature which determines the filtering logic.

            Returns:
            List[Tuple[Any, ...]]: A list of filtered prediction tuples.
            """
            if 'ratio' in feature_key:
                # If the feature key includes "ratio", only keep predictions where the sum equals delta_size
                return Counter({k: v for k, v in predictions.items() if sum(k) == delta_size})
            else:
                # If the feature key does not include "ratio", keep all predictions
                return predictions

        return {
            feature: {
                region: _feature_reviser(
                    predicts,
                    self.front_size if region == 'front' else self.back_size,
                    feature
                )
                for region, predicts in item.get('predictions', {}).items()
            }
            for feature, item in last_window_period_datas.items()
        }

    def calculate_features(self, lottery_datas: List[Lottery], region: int = 3) -> Dict[str, Dict[str, List]]:
        """
        Calculate and return various features for both the front and back t data.

        This method iterates over a predefined set of feature keys, retrieves the corresponding
        to compute method, and applies it to the front and back data of the t. It supports
        additional parameters for certain compute methods. The results are stored in a new dictionary
        and returned.

        :param lottery_datas: A list of Lottery objects containing the front and back data.
        :param region: Integer to select the compute region, 1: front, 2: back, 3: all.
        :return: A dictionary with computed feature results.
        """

        def _calculate_parser(caller: Callable, data: List[int], param: Optional[List] = None, ) -> List[int]:
            return caller(data, param) if param is not None else compute_method(data)

        features = {}
        add_ranges_params: Dict[str, Tuple[List, List]] = {
            'zone_ratio': (self.front_zone_ranges, self.back_zone_ranges),
            'big_small_ratio': (self.front_big_small_ranges, self.back_big_small_ranges),
            'road_012_ratio': (self.front_road_012_ranges, self.back_road_012_ranges),
        }

        special_method_list = ['calculate_span', 'calculate_sum_total', 'calculate_sum_tail', 'calculate_ac']
        for lottery_data in lottery_datas:
            for feature in self.feature_keys:
                compute_method: Callable = getattr(self, f'calculate_{feature}')
                params = add_ranges_params.get(feature)
                region_mapping = {
                    1: (lottery_data.front, params[0] if params else None),
                    2: (lottery_data.back, params[1] if params else None)
                }

                if 1 & region:
                    front_feature = _calculate_parser(compute_method, *region_mapping[1])
                    features.setdefault(feature, {}).setdefault('front', []).append(
                        [front_feature] if compute_method.__name__ in special_method_list
                        else [len(front_feature)] if compute_method.__name__ == 'calculate_consecutive_numbers'
                        else front_feature
                    )

                if 2 & region:
                    back_feature = _calculate_parser(compute_method, *region_mapping[2])
                    features.setdefault(feature, {}).setdefault('back', []).append(
                        [back_feature] if compute_method.__name__ in special_method_list
                        else [len(back_feature)] if compute_method.__name__ == 'calculate_consecutive_numbers'
                        else back_feature
                    )

        add_append_params: Dict[str, Tuple] = {
            'cold_hot_numbers': (range(1, self.front_vocab_size + 1), range(1, self.back_vocab_size + 1)),
            'omitted_numbers': (range(1, self.front_vocab_size + 1), range(1, self.back_vocab_size + 1)),
        }

        # if you have appended feature
        for feature, chunk_size in self.append_feature_mapping.items():
            compute_method: Callable = getattr(self, f'calculate_{feature}')
            params = add_append_params.get(feature)
            for chunk, next_element in self.get_chunks_with_next(lottery_datas, chunk_size=chunk_size):
                region_mapping = {
                    1: ([c.front for c in chunk] + [next_element.front], params[0] if params else None),
                    2: ([c.back for c in chunk] + [next_element.back], params[1] if params else None)
                }
                if 1 & region:
                    front_feature = _calculate_parser(compute_method, *region_mapping[1])
                    features.setdefault(feature, {}).setdefault('front', []).append([len(front_feature)])
                if 2 & region:
                    back_feature = _calculate_parser(compute_method, *region_mapping[2])
                    features.setdefault(feature, {}).setdefault('back', []).append([len(back_feature)])
        return features

    def calculate_predictions(self, feature_results: Dict[str, Dict[str, List[List]]]) -> Dict[str, Dict[str, any]]:
        """
        Calculate predictions for each feature and region using different prediction methods.

        This method iterates over computed feature results and applies various prediction
        algorithms to each sequence of data. It handles features containing 'ratio' differently
        by storing predictions in a tuple. The predictions are stored in a new dictionary that is
        constructed and returned.

        :param feature_results: A dictionary containing computed features with their results.
                                The structure is {feature_key: {'front': [...], 'back': [...]}}.
        :return: A dictionary with the prediction results. The structure is
                 {feature_key: {'front': set(), 'back': set()}}.
        """
        predictions = {}

        for feature, item in feature_results.items():
            for region, matrix in item.items():
                # Transpose the matrix to iterate over columns (sequences)
                # matrix_flip = list(map(list, zip(*matrix)))
                matrix_flip = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

                for predictor in [
                    self.exponential_moving_average_next_value,
                    self.linear_regression_next_value_by_index,
                    self.random_forest_regressor_next_value_by_index
                ]:
                    # Initialize the nested sets for each feature and region if not already present
                    region_predictions = predictions.setdefault(feature, {}).setdefault(region, Counter())

                    # Apply each predictor to each sequence and store the results
                    if 'ratio' in feature:
                        # For 'ratio' features, store results as tuples in a set
                        region_predictions.update([tuple([predictor(seq) for seq in matrix_flip])])
                    else:
                        # For other features, store results directly in the set
                        region_predictions.update(predictor(seq) for seq in matrix_flip)

        return predictions

    def handle_last_window_data(self, data: Optional[List[List[Any]]], window: int = 10) -> Dict[str, Any]:
        """
        Processes the last 'window' data of historical t to compute zone ratios
        and make predictions for the next period.

        :param data: A list of lists containing historical data. If None, data will be read from file.
        :param window: The number of recent periods to process.
        :return: A dictionary containing processed data and predictions.
        """
        if not data:
            raise ValueError("No data provided and no file reading implemented.")

        last_window_data = [self.convert_lottery_data(d) for d in data[-window:]]
        features = self.calculate_features(last_window_data)
        predictions = self.calculate_predictions(features)

        result_mapping = {
            feature: {
                'features': features.get(feature),
                'predictions': predictions.get(feature)
            }
            for feature in set(list(features.keys()) + list(predictions.keys()))
        }
        handle_result = self.revised_features(result_mapping)

        return handle_result

    def predict_by_last_window_data(self, data: Optional[List[List[Any]]], window: int = 10) -> List[Lottery]:
        """
        Predict t numbers based on the data from the last window.

        :param data: A two-dimensional list containing historical t data.
        :param window: The size of the window to consider, default is 10.
        :return: A list of predicted Lottery objects.
        """
        if not data:
            raise ValueError("No data provided and no file reading implemented.")

        # Convert to Lottery data objects
        last_window_data = [self.convert_lottery_data(d) for d in data[-window:]]

        # Create a matrix of front and back area numbers
        matrix = [d.front + d.back for d in last_window_data]

        # Transpose the matrix
        matrix_flip = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

        # Apply the transposed matrix to each predictor and generate predictions
        predictions = [
            tuple(predictor(seq) for seq in matrix_flip) for predictor in [
                self.exponential_moving_average_next_value,
                self.linear_regression_next_value_by_index,
                self.random_forest_regressor_next_value_by_index,
            ]
        ]

        # Create a list of Lottery objects based on the predictions
        return [
            self.Lottery('', '', '', self.calculate_front(d), self.calculate_back(d))
            for d in predictions
        ]

    def predict_by_last_period(
            self,
            next_period: int = None,
            show_details: bool = False,
            window_size: int = 15
    ) -> List[List[int]]:
        """
        Predicts features by the last period window of historical data and prints the results.
        Skips predictions where the sum of 'ratio' features does not match the expected size.
        :param next_period: int eg: 24001
        :param show_details: boolean flag to output details about the prediction
        :param window_size: int, default is 15
        """
        history_data = self.get_previous_history_data(next_period=next_period)

        maybe_combinations = self.predict_by_last_window_data(history_data, window=window_size)
        predict_data = [mc.front + mc.back for mc in maybe_combinations]
        self.app_log.info(predict_data) if show_details is True else None

        handle_result = self.handle_last_window_data(data=history_data, window=window_size)
        self.app_log.info(handle_result) if show_details is True else None

        return predict_data

    def predict_by_same_period(
            self,
            next_period: int = None,
            show_details: bool = False,
            window_size: int = 15
    ) -> List[List[int]]:
        """
        Predicts features by the last period window of historical data and prints the results.
        Skips predictions where the sum of 'ratio' features does not match the expected size.
        :param next_period: int eg: 24001
        :param show_details: boolean flag to output details about the prediction
        :param window_size: int, default is 15
        """
        period_data = self.get_previous_period_data(next_period=next_period)

        maybe_combinations = self.predict_by_last_window_data(period_data, window=window_size)
        predict_data = [mc.front + mc.back for mc in maybe_combinations]
        self.app_log.info(predict_data) if show_details is True else None

        handle_result = self.handle_last_window_data(data=period_data, window=window_size)
        self.app_log.info(handle_result) if show_details is True else None

        return predict_data

    def predict_by_last_weekday(
            self,
            next_weekday: int = None,
            next_period: int = None,
            show_details: bool = False,
            window_size: int = 15
    ) -> List[List[int]]:
        """
        Predicts features by the last weekday window of historical data and prints the results.
        Skips predictions where the sum of 'ratio' features does not match the expected size.
        :param next_weekday: int eg: [1 | 3 | 6]
        :param next_period: int eg: 24001
        :param show_details: boolean flag to output details about the prediction
        :param window_size: int, default is 15
        """
        weekday_data = self.get_previous_weekday_data(next_weekday=next_weekday, next_period=next_period)

        maybe_combinations = self.predict_by_last_window_data(weekday_data, window=window_size)
        predict_data = [mc.front + mc.back for mc in maybe_combinations]
        self.app_log.info(predict_data) if show_details is True else None

        handle_result = self.handle_last_window_data(data=weekday_data, window=window_size)
        self.app_log.info(handle_result) if show_details is True else None

        return predict_data

    def model_predict(
            self,
            next_period: int = None,
            next_weekday: int = None,
            show_details: bool = False,
            window_size: int = 15
    ) -> List[List[int]]:
        """
        :param next_period: int eg: 24001
        :param next_weekday: int eg: [1 | 3 | 6]
        :param show_details: boolean flag to output details about the prediction
        :param window_size: int, the default is 15
        """
        predictions = []
        predictions.extend(self.predict_by_last_period(next_period=next_period,
                                                       show_details=show_details,
                                                       window_size=window_size))
        predictions.extend(self.predict_by_same_period(next_period=next_period,
                                                       show_details=show_details,
                                                       window_size=window_size))
        predictions.extend(self.predict_by_last_weekday(next_weekday=next_weekday,
                                                        next_period=next_period,
                                                        show_details=show_details,
                                                        window_size=window_size))

        if show_details is True:
            self.app_log.info("The following is a preliminary forecast of the data analysis : ")
            # Splitting the data into first 5 and last 2 numbers
            front_zone = [num for row in predictions for num in row[:5]]
            back_zone = [num for row in predictions for num in row[5:]]

            # Counting occurrences
            front_zone_frequency = Counter(front_zone)
            back_zone_frequency = Counter(back_zone)

            # Sorting the counts
            sorted_front_zone_frequency = sorted(front_zone_frequency.items(), key=lambda x: x[1], reverse=True)
            sorted_back_zone_frequency = sorted(back_zone_frequency.items(), key=lambda x: x[1], reverse=True)

            # Printing the results
            self.app_log.info("Counts of the front zone numbers in each row sorted by frequency:")
            for number, count in sorted_front_zone_frequency:
                self.app_log.info(f"Number {number}: {count} times")
            self.app_log.info(f"Total count of the front zone numbers in each row: {len(sorted_front_zone_frequency)}")

            self.app_log.info("\nCounts of the back zone numbers in each row sorted by frequency:")
            for number, count in sorted_back_zone_frequency:
                self.app_log.info(f"Number {number}: {count} times")
            self.app_log.info(f"Total count of the back zone numbers in each row: {len(sorted_back_zone_frequency)}")

            self.app_log.info("\nHere are the preliminary predictions: ")
            for data in predictions:
                self.app_log.info(', '.join(map(str, data)))
        return predictions

    def calculate_predictions_and_intervals(
            self,
            data: List[Union[float, int]],
            sd_threshold: float,
            rolling_size: int,
            warm_start: bool = False,
            random_state: int = 12,
            param_distributions: Optional[Dict] = None,
            param_overrides: Optional[Dict] = None
    ) -> Tuple[Union[float, int], int, int]:
        """
        Calculate prediction intervals based on historical data and a specified rolling size.

        Args:
            data (List[float]): The list of historical data points.
            sd_threshold (float): The threshold for standard deviation calculations.
            rolling_size (int): The number of recent data points to consider for rolling calculations.
            warm_start (bool, optional): Whether to use the previous model state for training. Defaults to False.
            random_state (int, optional): A seed used by the random number generator for reproducibility. Defaults to 12.
            param_distributions (Optional[Dict]): The distribution of parameters to try in randomized search.
            param_overrides (Optional[Dict]): Additional parameters for the RandomizedSearchCV.

        Returns:
            Tuple[float, int, int]: A tuple containing the predicted value, and the minimum and maximum values of the prediction interval.
        """
        # Calculate standard deviation and tendency using a Welford's method based implementation
        sd = self.calculate_standard_deviation_welford(data[-rolling_size:])
        tendency = 0
        rsi = self.relative_strength_index(data[-rolling_size:], period=rolling_size // 2)
        if data[-1] >= math.floor(0.75 * sd_threshold) or rsi > 69:
            tendency = -1
        elif data[-1] <= math.ceil(0.12 * sd_threshold) or rsi < 31:
            tendency = 1
        param_overrides = param_overrides or {
            'n_iter': 100,
            'cv': 3,
            'scoring': 'neg_mean_squared_error',
            'verbose': 0,
            'random_state': 12,
            'n_jobs': -1
        }
        # Predict the next value using a random forest regressor
        pred = self.random_forest_regressor_next_value(data, rolling_size=rolling_size,
                                                       warm_start=warm_start,
                                                       random_state=random_state,
                                                       param_distributions=param_distributions,
                                                       param_overrides=param_overrides)

        # Set default interval values based on zero tendency
        min_val = math.floor(pred - sd)
        max_val = math.ceil(pred + sd)

        # Adjust interval based on the tendency
        if tendency < 0:
            max_val = math.ceil(pred + sd)
        elif tendency > 0:
            min_val = math.floor(pred - sd)

        return pred, min_val, max_val

    def analyze_predict(
            self,
            next_period: int = None,
            next_weekday: int = None,
            show_details: bool = False,
            window_size: int = 15
    ) -> List[List[int]]:
        """
        :param next_period: int eg: 24001
        :param next_weekday: int eg: [1 | 3 | 6]
        :param show_details: boolean flag to output details about the prediction
        :param window_size: int, the default is 15
        """
        # use model predict combinations and handle number set
        predict_data = self.model_predict(next_period=next_period, next_weekday=next_weekday,
                                          show_details=False, window_size=window_size)
        predict_front_set, predict_back_set = set(), set()
        for data in predict_data:
            predict_front_set.update(self.calculate_front(data))
            predict_back_set.update(self.calculate_back(data))
        exclude_front_set = set(range(1, self.front_vocab_size + 1)).difference(predict_front_set)
        exclude_back_set = set(range(1, self.back_vocab_size + 1)).difference(predict_back_set)

        # generate kill and banker numbers
        history_data = self.get_previous_history_data(next_period=next_period)
        period_data = self.get_previous_period_data(next_period=next_period)
        weekday_data = self.get_previous_weekday_data(next_period=next_period, next_weekday=next_weekday)
        front_kill_numbers, back_kill_numbers = self.get_kill_numbers(history_data, next_period=next_period,
                                                                      next_weekday=next_weekday)
        front_banker_numbers, back_banker_numbers = self.get_banker_numbers(history_data, next_period=next_period,
                                                                            next_weekday=next_weekday)

        self.app_log.info("Now, Will analyze the predictions..., Then adjust data")
        # Calculate available numbers avoiding both kill and banker numbers for the front
        available_front_numbers = set(range(1, self.front_vocab_size + 1)) - front_kill_numbers - front_banker_numbers
        # Calculate intersection of kill and banker numbers for the back
        available_back_numbers = back_kill_numbers & back_banker_numbers

        # Convert sets to lists for sampling
        available_front_numbers = list(available_front_numbers)
        available_back_numbers = list(available_back_numbers)

        predictions = []
        random.seed(self.calculate_sum_total(self.calculate_front(history_data[-1])))
        # Generate a prediction if there are enough numbers to sample from
        if len(available_front_numbers) >= 5 and len(available_back_numbers) >= 2:
            fd = sorted(available_front_numbers) if len(available_front_numbers) == 5 else sorted(
                random.sample(list(available_front_numbers), 5))
            bd = sorted(available_back_numbers) if len(available_back_numbers) == 2 else sorted(
                random.sample(list(available_back_numbers), 2))
            predictions.append(fd + bd)

        # Generate prediction from kill numbers if there are enough
        if len(front_kill_numbers) >= 5 and len(available_back_numbers) >= 2:
            fd = sorted(front_kill_numbers) if len(front_kill_numbers) == 5 else sorted(
                random.sample(list(front_kill_numbers), 5))
            bd = sorted(available_back_numbers) if len(available_back_numbers) == 2 else sorted(
                random.sample(list(available_back_numbers), 2))
            predictions.append(fd + bd)

        # Generate prediction from banker numbers if there are enough
        if len(front_banker_numbers) >= 5 and len(available_back_numbers) >= 2:
            fd = sorted(front_banker_numbers) if len(front_banker_numbers) == 5 else sorted(
                random.sample(list(front_banker_numbers), 5))
            bd = sorted(available_back_numbers) if len(available_back_numbers) == 2 else sorted(
                random.sample(list(available_back_numbers), 2))
            predictions.append(fd + bd)

        # Combine front and back combinations
        if show_details is True:
            self.app_log.info("The following is a preliminary forecast of the data analysis : ")
            self.app_log.info(f"available front numbers: {available_front_numbers}")
            self.app_log.info(f"available back numbers: {available_back_numbers}")
            self.app_log.info(f"front kill numbers: {front_kill_numbers}")
            self.app_log.info(f"back kill numbers: {back_kill_numbers}")
            self.app_log.info(f"front banker numbers: {front_banker_numbers}")
            self.app_log.info(f"back banker numbers: {back_banker_numbers}")

            self.app_log.info(f"last combination: {history_data[-1]}")
            self.app_log.info(f"model predict front: {sorted(predict_front_set)}")
            self.app_log.info(f"model predict back: {sorted(predict_back_set)}")
            self.app_log.info(f"exclude model predict front: {sorted(exclude_front_set)}")
            self.app_log.info(f"exclude model predict back: {sorted(exclude_back_set)}")

            # Splitting the data into first 5 and last 2 numbers
            front_zone = [num for row in predictions for num in row[:5]]
            back_zone = [num for row in predictions for num in row[5:]]

            # Counting occurrences
            front_zone_frequency = Counter(front_zone)
            back_zone_frequency = Counter(back_zone)

            # Sorting the counts
            sorted_front_zone_frequency = sorted(front_zone_frequency.items(), key=lambda x: x[1], reverse=True)
            sorted_back_zone_frequency = sorted(back_zone_frequency.items(), key=lambda x: x[1], reverse=True)

            # Printing the results
            self.app_log.info("Counts of the front zone numbers in each row sorted by frequency:")
            for number, count in sorted_front_zone_frequency:
                self.app_log.info(f"Number {number}: {count} times")
            self.app_log.info(f"Total count of the front zone numbers in each row: {len(sorted_front_zone_frequency)}")

            self.app_log.info("\nCounts of the back zone numbers in each row sorted by frequency:")
            for number, count in sorted_back_zone_frequency:
                self.app_log.info(f"Number {number}: {count} times")
            self.app_log.info(f"Total count of the back zone numbers in each row: {len(sorted_back_zone_frequency)}")

            self.app_log.info("\nHere are the preliminary predictions: ")
            for data in predictions:
                self.app_log.info(', '.join(map(str, data)))
        return predictions

    def predict(
            self,
            next_period: int = None,
            next_weekday: int = None,
            show_details: bool = False,
            window_size: int = 15,
            predict_type: str = 'model'
    ) -> List[List[int]]:
        """
        Generates predictions based on the specified prediction type.

        Parameters:
        next_period (int, optional): The next period to predict, defaults to None.
        next_weekday (int, optional): The next weekday to predict, defaults to None.
        show_details (bool): Whether to show detailed predictions, defaults to False.
        window_size (int): The window size used for predictions, defaults to 15.
        predict_type (str): The type of prediction, can be 'model', 'analyze', or 'train', defaults to 'model'.

        Returns:
        List[List[int]]: A list of prediction results based on the prediction type.

        Raises:
        KeyError: If the provided prediction type is not in the supported types list.
        """
        # Define supported prediction types and their corresponding functions
        types: Dict[str, Callable] = {
            'model': self.model_predict,
            'analyze': self.analyze_predict,
        }

        # Select the appropriate function based on the provided prediction type and execute prediction
        if predict_type not in types:
            raise KeyError(f"Predict type '{predict_type}' is not supported.")
        predictions = types[predict_type](
            next_period=next_period,
            next_weekday=next_weekday,
            show_details=show_details,
            window_size=window_size
        )

        return predictions

    def test(self):
        pass
