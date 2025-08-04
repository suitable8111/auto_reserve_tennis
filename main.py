import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui_mainWindow import Ui_AutoTennis  # Import the generated UI file
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os
import time
from selenium.webdriver.common.keys import Keys
from data import time_title
from PySide6.QtCore import QDate, QStringListModel, QCoreApplication
from datetime import datetime, date
import multiprocessing
from multiprocessing import Process, Manager

path = os.path.dirname(os.path.abspath(__file__))

# Helper function for personal data input (Global scope for multiprocessing)
def _input_personal_data(driver):
    try:
        name = driver.find_element(By.ID, 'name1')  # 신청자명
        tel_info = driver.find_element(By.ID, 'tel1')  # 연락처
        return_account = driver.find_element(By.ID, 'ext5')  # 환불계좌
        return_account_com = driver.find_element(By.ID, 'ext8')  # 환불은행
        gilud = driver.find_element(By.ID, 'com1')  # 단체명
        num_of_people = driver.find_element(By.ID, 'area2')  # 이용인원
        match_name = driver.find_element(By.ID, 'subject1')  # 경기(행사)명
        match_propose = driver.find_element(By.ID, 'content1')  # 이용목적

        name.send_keys('유형민')
        tel_info.send_keys('010-5363-3809')
        return_account.send_keys('3520395979943')
        return_account_com.send_keys('농협')
        gilud.send_keys('하이랠리')
        match_name.send_keys('하이랠리 경기')
        match_propose.send_keys('친목도모')

        time.sleep(1.0)
        # "신청하기" 버튼 클릭
        # "신청하기" 버튼 클릭
        driver.find_elements(By.CLASS_NAME,'page-btn')[0].click()
        time.sleep(1)
        alert = driver.switch_to.alert
        alert.accept()
        time.sleep(1)
        
    except Exception as e:
        print(f"개인 정보 입력 중 오류 발생: {e}")


def _reserve_court_worker(jungu_url, jungu_name, target_time_list, target_time_pos_list, next_month_checked, selected_day_indices, day_kor_list, day_list, check_box_list, fail_list, pass_list):
    """
    하나의 코트 종류에 대한 예약을 처리하는 워커 함수 (멀티프로세싱용)
    """
    def what_day_is_it(dt, day_list_arg):
        return day_list_arg[dt.weekday()]

    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument("--headless")
    # chrome_options.add_argument("--disable-gpu")
    # chrome_options.add_argument("--no-sandbox")
    driver = None
    try:
        # 각 워커가 직접 드라이버를 설치하고 서비스 시작
        if sys.platform == "win32":
            service = ChromeDriverManager().install()
            correct_driver_path = os.path.join(os.path.dirname(service), "chromedriver.exe")
            driver = webdriver.Chrome(service=Service(executable_path=correct_driver_path), options=chrome_options)
        elif sys.platform == "darwin":
            service = Service(ChromeDriverManager().install())
            driver = webdriver.Chrome(service=service, options=chrome_options)
        driver.get(jungu_url)
        time.sleep(1)

        current_date_text = driver.find_element(By.CLASS_NAME, 'calendar').text
        current_year = int(current_date_text.split(' ')[0].replace('년', ''))
        current_month = int(current_date_text.split(' ')[1].replace('월', ''))

        reserve_year, reserve_month = current_year, current_month
        if next_month_checked:
            if current_month == 12:
                reserve_year += 1
                reserve_month = 1
            else:
                reserve_month += 1
            next_text = f"?indate={reserve_year}/{reserve_month}/1"
            driver.get(jungu_url + next_text)
            time.sleep(2)

        table_tr = driver.find_elements(By.TAG_NAME,'tr')
        table_tr.pop(0)
        table_tr.pop(5)
        
        day_enable_obj = {}
        day_count = 1
        
        for tr_idx in table_tr:
            item = tr_idx.text.split('\n')
            for j,jdx in enumerate(item):
                if(j % 2 == 1):
                    current_day_to_check = date(reserve_year, reserve_month, day_count) if next_month_checked else date(current_year, current_month, day_count)
                    what_day = what_day_is_it(current_day_to_check, day_list)
                    enable_flag = '예약가능' in jdx
                    day_enable_obj[day_count] = [what_day, enable_flag]
                    day_count += 1  
                    
        for i_day, day_kor_name in enumerate(day_kor_list):
            if check_box_list[i_day]:
                time.sleep(1)
                
                week_count = 0
                for i_obj, obj_idx in enumerate(day_enable_obj):
                    if day_enable_obj[obj_idx][0] == day_kor_name:
                        
                        if not day_enable_obj[obj_idx][1]:
                            print('예약 불가 : 해당 요일 불가능 지났거나 꽉찼음')
                            month_str = reserve_month if next_month_checked else current_month
                            fail_msg = f"{jungu_name}, {month_str}/{i_obj+1}({day_kor_name}) 사유 : 해당 요일 불가능 지났거나 꽉찼음"
                            fail_list.append(fail_msg)
                        else:
                            size_tr_a = len(table_tr[week_count].find_elements(By.TAG_NAME,'a'))
                            
                            clicked = False
                            if week_count == 0:
                                diff = 7 - size_tr_a
                                if diff >= 0 and (i_day - diff) >= 0 and (i_day-diff) < size_tr_a:
                                    table_tr[week_count].find_elements(By.TAG_NAME,'a')[i_day-diff].click()
                                    clicked = True
                            elif i_day < size_tr_a:
                                table_tr[week_count].find_elements(By.TAG_NAME,'a')[i_day].click()
                                clicked = True

                            if not clicked:
                                week_count += 1
                                continue

                            time.sleep(1)
                            disable_time_list = driver.find_elements(By.ID,'layer-select-time')[0].find_elements(By.CLASS_NAME,'disabled')
                            enable_time_reserved_flag_list = [pos != 0 for pos in target_time_pos_list]

                            month_str = reserve_month if next_month_checked else current_month
                            day_str = f"{month_str}/{i_obj+1}({day_kor_name})"

                            if len(disable_time_list) >= 15:
                                fail_msg = f"{jungu_name}, {day_str} 사유 : 모든 시간대 예약자가 있음"
                                fail_list.append(fail_msg)
                                enable_time_reserved_flag_list = [False, False, False]
                            else:
                                for item in disable_time_list:
                                    for tidx, time_pos in enumerate(target_time_pos_list):
                                        if time_pos != 0 and item.text.startswith(time_title[time_pos][0:2]):
                                            fail_msg = f"{jungu_name}, {day_str}{time_title[time_pos]} 사유 : 해당시간 예약자가 있음"
                                            fail_list.append(fail_msg)
                                            enable_time_reserved_flag_list[tidx] = False
                                
                            if any(enable_time_reserved_flag_list):
                                for idx, is_enabled in enumerate(enable_time_reserved_flag_list):
                                    if is_enabled:
                                        driver.find_elements(By.ID,'layer-select-time')[0].find_elements(By.CLASS_NAME,'check-wrap')[target_time_pos_list[idx]-1].click()
                                        time.sleep(0.5)
                                driver.find_element(By.ID,'layer-select-time').find_element(By.ID,'btn-order').click()
                                time.sleep(1)
                                _input_personal_data(driver)
                                print('예약 성공')
                                for idx, is_enabled in enumerate(enable_time_reserved_flag_list):
                                    if is_enabled:
                                        pass_msg = f"{jungu_name}, {day_str}{target_time_list[idx]} 성공"
                                        pass_list.append(pass_msg)
                                driver.back()
                                time.sleep(1)
                                driver.back()
                                time.sleep(1)
                            else:
                                driver.back()
                                time.sleep(1)                                                   
                                            
                        week_count += 1
    except Exception as e:
        print(f"Worker error for {jungu_name}: {e}")
    finally:
        if driver:
            driver.quit()


class MyApp(QMainWindow, Ui_AutoTennis):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.jungu_list = [
            "실내1", "실내2", "야외3", "야외4", "야외7",
            "정구1", "정구2", "정구3", "정구4",
        ]
        self.day_kor_list = ["일요일", "월요일", "화요일", "수요일", "목요일", "금요일", "토요일"]
        self.day_list = ["월요일", "화요일", "수요일", "목요일", "금요일", "토요일", "일요일"]
        self.check_box_list = [
            self.sun_chk_box, self.mon_chk_box, self.tue_chk_box, self.wed_chk_box,
            self.thu_chk_box, self.fri_chk_box, self.sat_chk_box
        ]
        self.url_list = [
            "https://wjpsc.or.kr/%EC%8B%9C%EC%84%A4%EC%98%A8%EB%9D%BC%EC%9D%B8%EC%98%88%EC%95%BD/%EC%8B%9C%EC%84%A4%EB%AC%BC%EC%98%A8%EB%9D%BC%EC%9D%B8%EC%98%88%EC%95%BD/%EB%82%A8%EA%B0%80%EB%9E%8C%ED%85%8C%EB%8B%88%EC%8A%A4%EC%9E%A5/%EC%8B%A4%EB%82%B41/",
            "https://wjpsc.or.kr/%EC%8B%9C%EC%84%A4%EC%98%A8%EB%9D%BC%EC%9D%B8%EC%98%88%EC%95%BD/%EC%8B%9C%EC%84%A4%EB%AC%BC%EC%98%A8%EB%9D%BC%EC%9D%B8%EC%98%88%EC%95%BD/%EB%82%A8%EA%B0%80%EB%9E%8C%ED%85%8C%EB%8B%88%EC%8A%A4%EC%9E%A5/%EC%8B%A4%EB%82%B42/",
            "https://wjpsc.or.kr/%EC%8B%9C%EC%84%A4%EC%98%A8%EB%9D%BC%EC%9D%B8%EC%98%88%EC%95%BD/%EC%8B%9C%EC%84%A4%EB%AC%BC%EC%98%A8%EB%9D%BC%EC%9D%B8%EC%98%88%EC%95%BD/%EB%82%A8%EA%B0%80%EB%9E%8C%ED%85%8C%EB%8B%88%EC%8A%A4%EC%9E%A5/%EC%95%BC%EC%99%B83/",
            "https://wjpsc.or.kr/%EC%8B%9C%EC%84%A4%EC%98%A8%EB%9D%BC%EC%9D%B8%EC%98%88%EC%95%BD/%EC%8B%9C%EC%84%A4%EB%AC%BC%EC%98%A8%EB%9D%BC%EC%9D%B8%EC%98%88%EC%95%BD/%EB%82%A8%EA%B0%80%EB%9E%8C%ED%85%8C%EB%8B%88%EC%8A%A4%EC%9E%A5/%EC%95%BC%EC%99%B84/",
            "https://wjpsc.or.kr/%EC%8B%9C%EC%84%A4%EC%98%A8%EB%9D%BC%EC%9D%B8%EC%98%88%EC%95%BD/%EC%8B%9C%EC%84%A4%EB%AC%BC%EC%98%A8%EB%9D%BC%EC%9D%B8%EC%98%88%EC%95%BD/%EB%82%A8%EA%B0%80%EB%9E%8C%ED%85%8C%EB%8B%88%EC%8A%A4%EC%9E%A5/%EC%95%BC%EC%99%B87/",
            "https://wjpsc.or.kr/%EC%8B%9C%EC%84%A4%EC%98%A8%EB%9D%BC%EC%9D%B8%EC%98%88%EC%95%BD/%EC%8B%9C%EC%84%A4%EB%AC%BC%EC%98%A8%EB%9D%BC%EC%9D%B8%EC%98%88%EC%95%BD/%EB%82%A8%EA%B0%80%EB%9E%8C%ED%85%8C%EB%8B%88%EC%8A%A4%EC%9E%A5/%EC%A0%95%EA%B5%AC1/",
            "https://wjpsc.or.kr/%EC%8B%9C%EC%84%A4%EC%98%A8%EB%9D%BC%EC%9D%B8%EC%98%88%EC%95%BD/%EC%8B%9C%EC%84%A4%EB%AC%BC%EC%98%A8%EB%9D%BC%EC%9D%B8%EC%98%88%EC%95%BD/%EB%82%A8%EA%B0%80%EB%9E%8C%ED%85%8C%EB%8B%88%EC%8A%A4%EC%9E%A5/%EC%A0%95%EA%B5%AC2/",
            "https://wjpsc.or.kr/%EC%8B%9C%EC%84%A4%EC%98%A8%EB%9D%BC%EC%9D%B8%EC%98%88%EC%95%BD/%EC%8B%9C%EC%84%A4%EB%AC%BC%EC%98%A8%EB%9D%BC%EC%9D%B8%EC%98%88%EC%95%BD/%EB%82%A8%EA%B0%80%EB%9E%8C%ED%85%8C%EB%8B%88%EC%8A%A4%EC%9E%A5/%EC%A0%95%EA%B5%AC3/",
            "https://wjpsc.or.kr/%EC%8B%9C%EC%84%A4%EC%98%A8%EB%9D%BC%EC%9D%B8%EC%98%88%EC%95%BD/%EC%8B%9C%EC%84%A4%EB%AC%BC%EC%98%A8%EB%9D%BC%EC%9D%B8%EC%98%88%EC%95%BD/%EB%82%A8%EA%B0%80%EB%9E%8C%ED%85%8C%EB%8B%88%EC%8A%A4%EC%9E%A5/%EC%A0%95%EA%B5%AC4/"
        ]
        self.jungu_box_list = [
            self.sinea1_chk_box, self.sinea2_chk_box, self.yaw3_chk_box, self.yaw4_chk_box,
            self.yaw7_chk_box, self.jungu1_chk_box, self.jungu2_chk_box,
            self.jungu3_chk_box, self.jungu4_chk_box
        ]
        self.time_combo_box_list = [
            self.time_combo_box, self.time2_combo_box, self.time3_combo_box
        ]
        for item in self.time_combo_box_list:
            item.addItems(time_title)

        self.actionButton.clicked.connect(self.on_clicked_auto_reservce)

        self.fail_model = QStringListModel()
        self.fail_list_view.setModel(self.fail_model)
        self.pass_model = QStringListModel()
        self.pass_list_view.setModel(self.pass_model)
        self.fail_list = []
        self.pass_list = []

        # Set default values
        self.next_month_chk_box.setChecked(True)
        self.time_combo_box.setCurrentIndex(14) # 19:00~20:00
        self.time2_combo_box.setCurrentIndex(15) # 20:00~21:00
        self.time3_combo_box.setCurrentIndex(16) # 21:00~21:30
        self.yaw3_chk_box.setChecked(True)
        self.yaw4_chk_box.setChecked(True)
        self.yaw7_chk_box.setChecked(True)
        self.jungu1_chk_box.setChecked(True)
        self.jungu2_chk_box.setChecked(True)
        self.jungu3_chk_box.setChecked(True)
        self.jungu4_chk_box.setChecked(True)

        self.update_item_list()

    def what_day_is_it(self, date):
        return self.day_list[date.weekday()]

    def update_item_list(self):
        self.fail_model.setStringList(self.fail_list)
        self.pass_model.setStringList(self.pass_list)
        QCoreApplication.processEvents() # Update UI

    def on_clicked_auto_reservce(self):
        target_time_list = [item.currentText() for item in self.time_combo_box_list]
        target_time_pos_list = [item.currentIndex() for item in self.time_combo_box_list]

        if all(pos == 0 for pos in target_time_pos_list):
            QMessageBox.warning(self, "경고", "하나 이상의 시간대를 선택해야 합니다.")
            return

        self.fail_list = []
        self.pass_list = []
        self.update_item_list()

        selected_courts_info = []
        for i, box in enumerate(self.jungu_box_list):
            if box.isChecked():
                selected_courts_info.append({'url': self.url_list[i], 'name': self.jungu_list[i]})

        if not selected_courts_info:
            QMessageBox.warning(self, "경고", "하나 이상의 코트를 선택해야 합니다.")
            return

        selected_day_indices = [i for i, box in enumerate(self.check_box_list) if box.isChecked()]
        if not selected_day_indices:
            QMessageBox.warning(self, "경고", "하나 이상의 요일을 선택해야 합니다.")
            return
            
        manager = Manager()
        fail_list = manager.list()
        pass_list = manager.list()
        processes = []

        checked_days_list = [box.isChecked() for box in self.check_box_list]
        next_month_checked = self.next_month_chk_box.isChecked()

        for court_info in selected_courts_info:
            p = Process(
                target=_reserve_court_worker,
                args=(
                    court_info['url'], court_info['name'], target_time_list,
                    target_time_pos_list, next_month_checked,
                    selected_day_indices, self.day_kor_list, self.day_list,
                    checked_days_list, fail_list, pass_list
                )
            )
            processes.append(p)
            p.start()

        # 모든 프로세스가 끝날 때까지 기다리면서 GUI가 멈추지 않도록 처리
        for p in processes:
            while p.is_alive():
                QCoreApplication.processEvents()
                p.join(timeout=0.1)

        self.fail_list.extend(list(fail_list))
        self.pass_list.extend(list(pass_list))

        self.update_item_list()
        QMessageBox.information(self, "완료", "예약 시도가 모두 완료되었습니다.")
        
def main():
    # Pyinstaller와 multiprocessing을 함께 사용할 때 필요
    multiprocessing.freeze_support()
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
