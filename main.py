import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui_mainWindow import Ui_Auto  # Import the generated UI file
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os
import time
from selenium.webdriver.common.keys import Keys
from data import time_title
from PySide6.QtCore import QDate, QStringListModel
from datetime import datetime, date
path = os.path.dirname(os.path.abspath(__file__))

class MyApp(QMainWindow, Ui_Auto):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.jungu_list = [
            "정구1",
            "정구2",
            "정구3",
            "정구4",
        ]
        self.day_kor_list = [
            "일요일",
            "월요일",
            "화요일",
            "수요일",
            "목요일",
            "금요일",
            "토요일",
        ]
        #현재날짜를 출력
        self.day_list = [
            "월요일",
            "화요일",
            "수요일",
            "목요일",
            "금요일",
            "토요일",
            "일요일",
        ]
        self.check_box_list = [
            self.sun_chk_box,
            self.mon_chk_box,
            self.tue_chk_box,
            self.wed_chk_box,
            self.thu_chk_box,
            self.fri_chk_box,
            self.sat_chk_box
        ]
        self.jungu_box_list = [
            self.jungu1_chk_box,
            self.jungu2_chk_box,
            self.jungu3_chk_box,
            self.jungu4_chk_box
        ]
        chrome_options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service= Service(ChromeDriverManager().install()), options=chrome_options)
        
    
        self.actionButton.clicked.connect(self.on_clicked_auto_reservce)
        self.time_combo_box.addItems(time_title)
        #set number default 
        self.fail_model = QStringListModel()
        self.fail_list_view.setModel(self.fail_model)
        
        self.pass_model = QStringListModel()
        self.pass_list_view.setModel(self.pass_model)
        
        self.fail_list = []
        self.pass_list = []
        
        self.update_item_list()
        #self.fail_list_view.clicked.connect(self.on_item_clicked)
        
    def what_day_is_it(self,date):
        day = date.weekday()
        return self.day_list[day]
        
    def update_item_list(self):
        self.fail_model.setStringList(self.fail_list)
        self.pass_model.setStringList(self.pass_list)
        
        
    def on_clicked_auto_reservce(self):
        # 정구1 :https://wjpsc.or.kr/%EC%8B%9C%EC%84%A4%EC%98%A8%EB%9D%BC%EC%9D%B8%EC%98%88%EC%95%BD/%EC%8B%9C%EC%84%A4%EB%AC%BC%EC%98%A8%EB%9D%BC%EC%9D%B8%EC%98%88%EC%95%BD/%EB%82%A8%EA%B0%80%EB%9E%8C%ED%85%8C%EB%8B%88%EC%8A%A4%EC%9E%A5/%EC%A0%95%EA%B5%AC1/
        # 정구2 :https://wjpsc.or.kr/%EC%8B%9C%EC%84%A4%EC%98%A8%EB%9D%BC%EC%9D%B8%EC%98%88%EC%95%BD/%EC%8B%9C%EC%84%A4%EB%AC%BC%EC%98%A8%EB%9D%BC%EC%9D%B8%EC%98%88%EC%95%BD/%EB%82%A8%EA%B0%80%EB%9E%8C%ED%85%8C%EB%8B%88%EC%8A%A4%EC%9E%A5/%EC%A0%95%EA%B5%AC2/
        # 정구3 :https://wjpsc.or.kr/%EC%8B%9C%EC%84%A4%EC%98%A8%EB%9D%BC%EC%9D%B8%EC%98%88%EC%95%BD/%EC%8B%9C%EC%84%A4%EB%AC%BC%EC%98%A8%EB%9D%BC%EC%9D%B8%EC%98%88%EC%95%BD/%EB%82%A8%EA%B0%80%EB%9E%8C%ED%85%8C%EB%8B%88%EC%8A%A4%EC%9E%A5/%EC%A0%95%EA%B5%AC3/
        # 정구4 :https://wjpsc.or.kr/%EC%8B%9C%EC%84%A4%EC%98%A8%EB%9D%BC%EC%9D%B8%EC%98%88%EC%95%BD/%EC%8B%9C%EC%84%A4%EB%AC%BC%EC%98%A8%EB%9D%BC%EC%9D%B8%EC%98%88%EC%95%BD/%EB%82%A8%EA%B0%80%EB%9E%8C%ED%85%8C%EB%8B%88%EC%8A%A4%EC%9E%A5/%EC%A0%95%EA%B5%AC4/

        self.fail_list = []
        self.pass_list = []
        for i_jg, idx_jg in enumerate(self.jungu_box_list):
            if (self.jungu_box_list[i_jg].isChecked()): 
                jungu1_url = "https://wjpsc.or.kr/%EC%8B%9C%EC%84%A4%EC%98%A8%EB%9D%BC%EC%9D%B8%EC%98%88%EC%95%BD/%EC%8B%9C%EC%84%A4%EB%AC%BC%EC%98%A8%EB%9D%BC%EC%9D%B8%EC%98%88%EC%95%BD/%EB%82%A8%EA%B0%80%EB%9E%8C%ED%85%8C%EB%8B%88%EC%8A%A4%EC%9E%A5/%EC%A0%95%EA%B5%AC"+str(i_jg+1)+"/" #로그인 관련
                self.driver.get(jungu1_url)
                time.sleep(1)
                
                table_tr = self.driver.find_elements(By.TAG_NAME,'tr')
                table_tr.pop(0)
                table_tr.pop(5)
                
                current_date = self.driver.find_element(By.CLASS_NAME,'calendar').text
                current_year = int(current_date.split(' ')[0].replace('년',''))
                current_month = int(current_date.split(' ')[1].replace('월',''))
                
                
                day_enable_obj = {}
                day_count = 1
                
                for tr_idx in table_tr :
                    item = tr_idx.text.split('\n')
                    for j,jdx in enumerate(item):
                        if(j % 2 == 1):
                            what_day = self.what_day_is_it(date(current_year,current_month,day_count))
                            enable_flag = True if (jdx.find('예약가능') >= 0) else False
                            day_enable_obj[day_count] = [what_day,enable_flag]
                            day_count += 1  
                            
                for i_day, day_idx in enumerate(self.day_kor_list):
                    if (self.check_box_list[i_day].isChecked()):
                        time.sleep(1)
                        target_time = time_title[self.time_combo_box.currentIndex()]
                        target_time_pos = self.time_combo_box.currentIndex()
                        week_count = 0
                        for i_obj, obj_idx in enumerate(day_enable_obj):
                            if day_enable_obj[obj_idx][0] == self.day_kor_list[i_day]:
                                print(str(obj_idx+1),'(',day_idx,')일 ',time_title[self.time_combo_box.currentIndex()],' 시간대 예약하기')
                                #print(str(i_obj+1)+'일 월요일 확인..')
                                if day_enable_obj[obj_idx][1] == False:
                                    print('예약 불가 : 해당 요일 불가능 지났거나 꽉찼음')
                                    fail_msg = self.jungu_list[i_jg]+', '+str(current_month)+'/'+str(i_obj+1)+'('+day_idx+')'+target_time+' 사유 : 해당 요일 불가능 지났거나 꽉찼음'
                                    self.fail_list.append(fail_msg)
                                else:
                                    #print('예약가능 해당 요일 예약하기')
                                    #send 예약
                                    #click 예약하기, 1 is monday
                                    
                                    #weekcount = 0
                                    #7 일 월 화 수 목 금 토
                                    #6 월 화 수 목 금 토
                                    #5 화 수 목 금 토
                                    #4 수 목 금 토
                                    #3 목 금 토
                                    #2 금 토
                                    #1 토
                                    
                                    #weekcount = 5 or 6
                                    #7 일 월 화 수 목 금 토
                                    #6 일 월 화 수 목 금 
                                    #5 일 월 화 수 목 
                                    #4 일 월 화 수 
                                    #3 일 월 화 
                                    #2 일 월 
                                    #1 일 
                                    
                                    size_tr_a = len(table_tr[week_count].find_elements(By.TAG_NAME,'a'))
                                    if(week_count == 0):
                                        diff = 7-size_tr_a
                                        if(diff >= 0):
                                            table_tr[week_count].find_elements(By.TAG_NAME,'a')[i_day-diff].click()
                                        else:
                                            continue
                                    elif(week_count == len(table_tr)-1):
                                        if(size_tr_a > i_day):
                                            table_tr[week_count].find_elements(By.TAG_NAME,'a')[i_day].click()
                                        else:
                                            continue
                                    else:
                                        table_tr[week_count].find_elements(By.TAG_NAME,'a')[i_day].click()
                                    #잠시 쉬어주고
                                    time.sleep(1)
                                    #못하는 시간대 체크
                                    disable_time_list = self.driver.find_elements(By.ID,'layer-select-time')[0].find_elements(By.CLASS_NAME,'disabled')
                                    enable_time_reserved_flag = True
                                    if (len(disable_time_list) > 0):
                                        #print('불가능한 시간 확인 해당 시간이 우리가 찾는 시간인지 확인')
                                        for item in disable_time_list:
                                            if(item.text[0:2] == target_time[0:2]):
                                                print('예약 불가 : 해당시간()',target_time,') 대 예약자가 있음 ',item.text)
                                                # 불가한 경우 Fail 처리
                                                fail_msg = self.jungu_list[i_jg]+', '+str(current_month)+'/'+str(i_obj+1)+'('+day_idx+')'+target_time+' 사유 : 해당시간 예약자가 있음'
                                                self.fail_list.append(fail_msg)
                                                enable_time_reserved_flag = False
                                                
                                    if (len(disable_time_list) >= 15):
                                        print('예약 불가 : 모든 시간 대 예약자가 있음 ',item.text)
                                        # 불가한 경우 Fail 처리
                                        fail_msg = self.jungu_list[i_jg]+', '+str(current_month)+'/'+str(i_obj+1)+'('+day_idx+')'+target_time+' 사유 : 모든 시간대 예약자가 있음'
                                        self.fail_list.append(fail_msg)
                                        enable_time_reserved_flag = False
                                        
                                    #가능한시간대로 확인되면
                                    if (enable_time_reserved_flag):
                                        #해당 시간대 체크
                                        self.driver.find_elements(By.ID,'layer-select-time')[0].find_elements(By.CLASS_NAME,'check-wrap')[target_time_pos].click()
                                        time.sleep(1)
                                        #해당 시간대 클릭
                                        self.driver.find_elements(By.ID,'layer-select-time')[0].find_elements(By.ID,'btn-order')[0].click()
                                        #또 쉬어주고
                                        time.sleep(1)
                                        self.input_personal_data()
                                        print('예약 성공')
                                        pass_msg = self.jungu_list[i_jg]+', '+str(current_month)+'/'+str(i_obj+1)+'('+day_idx+')'+target_time+' 성공'
                                        self.pass_list.append(pass_msg)
                                        self.driver.back()
                                        time.sleep(1)
                                        self.driver.back()    
                                        time.sleep(1)        
                                    else:
                                        self.driver.back()
                                        time.sleep(1)        
                                week_count += 1 #한주 넘기기
        
        self.update_item_list()            
        
    def input_personal_data(self):
        #print('사용자 정보 입력창 진입')
        name = self.driver.find_elements(By.ID,'name1')[0] #신청자명
        tel_info = self.driver.find_elements(By.ID,'tel1')[0] #연락처
        return_account = self.driver.find_elements(By.ID,'ext5')[0] #환불계좌
        return_account_com = self.driver.find_elements(By.ID,'ext8')[0] #환불은행
        gilud = self.driver.find_elements(By.ID,'com1')[0] #단체명
        num_of_people = self.driver.find_elements(By.ID,'area2')[0] #이용인원 #디폴트는 2
        match_name = self.driver.find_elements(By.ID,'subject1')[0] #경기(행사)명
        match_propose = self.driver.find_elements(By.ID,'content1')[0] #이용목적
        
        name.send_keys('유형민')
        tel_info.send_keys('010-5363-3809')
        return_account.send_keys('3520395979943')
        return_account_com.send_keys('농협')
        gilud.send_keys('하이랠리')
        match_name.send_keys('하이랠리 경기')
        match_propose.send_keys('친목도모')
        
        time.sleep(1.0)
        self.driver.find_elements(By.CLASS_NAME,'page-btn')[0].click()
        time.sleep(1)
        alert = self.driver.switch_to.alert
        alert.accept()
        time.sleep(1)
        self.driver.back() 
        #self.driver.back() 
        #신청자명 유형민
        #연락처 010-5363-3809
        #환불계좌 3520395979943 농협 
        #모임명 하이랠리 
        # data-weekday = 0(일)~6(토)
        # data-weeks = 0(첫주)~
        # tr의 data-tr-idx 과 동일
        # btn btn-primary ez-layer-btn 예약버튼

        # check-wrap 체크박스 클래스
        # value 21 --> 21:00
        # btn btn-info btn-xs btn-check 예약하는 버튼
        
        #<input type="submit" id="btn-order" value="예약하기" class="page-btn btn-blue"> 최종 예약하는 버튼


        #<input label="신청자명" type="text" id="name1" name="name1" class="ez_required uk-input uk-form-small" style="width:100%;max-width:300px" placeholder="신청자명">
        #<input label="연락처" type="text" id="tel1" name="tel1" class="ez_required uk-input uk-form-small inline-block phone-number" style="width:100%;max-width:150px" maxlength="13" placeholder="010-1234-5678">
        #<input label="환불계좌" type="text" id="ext5" name="ext5" class="ez_required form-control inline-block" style="width:100%;max-width:200px" placeholder="환불계좌"> / <input label="은행" type="text" id="ext8" name="ext8" class="ez_required form-control inline-block" style="width:100%;max-width:100px" placeholder="은행">
        #<input label="단체명" type="text" id="com1" name="com1" class="uk-input uk-form-small" style="width:100%;max-width:300px" placeholder="단체명">
        #<input label="이용인원" type="text" id="area2" name="area2" value="2" class="ez_required uk-input uk-form-small number-only inline-block" style="width:100%;max-width:50px" maxlength="2" placeholder="">
        #<input label="경기(행사)명" type="text" id="subject1" name="subject1" class="uk-input uk-form-small" style="width:100%;max-width:300px" placeholder="경기(행사)명">
        #<textarea label="이용목적" id="content1" name="content1" class="uk-input" style="width:100%;height:60px" placeholder="이용목적"></textarea>

        #<input type="submit" value="저장" class="page-btn btn-blue">
        
def main():
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()