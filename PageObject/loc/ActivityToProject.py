# -*- coding: utf-8 -*-
# from PageObject.ActivityItemHelp.Base import build_activities
from ActivityItemHelp import build_activities


Activities = {
    # activities of u"2015CyberMARS產品研發專案"
    u"管理事務_如時程,資源規劃與管理等 <<1.2.3>>" : u"2015CyberMARS產品研發專案",
    u"專案進度會議 <<1.2.4>>"                   : u"2015CyberMARS產品研發專案",
    u"測試環境建置 <<1.5.1>>"                   : u"2015CyberMARS產品研發專案",
    u"測試系統設定 <<1.5.2>>"                   : u"2015CyberMARS產品研發專案",
    u"測試文件撰寫 <<1.5.3>>"                   : u"2015CyberMARS產品研發專案",
    u"測試案例撰寫 <<1.5.4>>"                   : u"2015CyberMARS產品研發專案",
    u"測試案例執行 <<1.5.5>>"                   : u"2015CyberMARS產品研發專案",
    u"自動化測試程式或工具準備與撰寫 <<1.5.6>>"   : u"2015CyberMARS產品研發專案",
    u"Bug重現 <<1.5.7>>"                       : u"2015CyberMARS產品研發專案",
    u"測試報告撰寫 <<1.5.8>>"                   : u"2015CyberMARS產品研發專案",
    u"Bug驗證 <<1.5.9>>"                       : u"2015CyberMARS產品研發專案",
    u"產品文件與相關資料收集 <<1.5.10>>"         : u"2015CyberMARS產品研發專案",

    # activities of '2016Y_SDD'
    u"差旅 <<1.1.1>>"                                     : '2016Y_SDD',
    u"學習成長(自我研讀、參加敎育訓練, <<1.1.2>>"            : '2016Y_SDD',
    u"服務支援(同事間備援、跨部門/處支援, <<1.1.3>>"         : '2016Y_SDD',
    u"會議(內/外部會議, <<1.1.4>>"                         : '2016Y_SDD',
    u"休假 <<1.1.5>>"                                     : '2016Y_SDD',
    u"公司活動(參加員工大會等公司活動, <<1.1.6>>"            : '2016Y_SDD',
    u"行政庶務(準備及撰寫文件、 一般行政或庶務, <<1.1.7>>"    : '2016Y_SDD',
    u"溝通協調(部門或跨部門溝通協調, <<1.1.8>>"              : '2016Y_SDD'
}

_activity1_options = [
    u"差旅 <<1.1.1>>",
    u"學習成長(自我研讀、參加敎育訓練, <<1.1.2>>",
    u"服務支援(同事間備援、跨部門/處支援, <<1.1.3>>",
    u"會議(內/外部會議, <<1.1.4>>",
    u"休假 <<1.1.5>>",
    u"公司活動(參加員工大會等公司活動, <<1.1.6>>",
    u"行政庶務(準備及撰寫文件、 一般行政或庶務, <<1.1.7>>",
    u"溝通協調(部門或跨部門溝通協調, <<1.1.8>>"
]

proj_loc_map = {
    # proj_name                  proj loc     mapped activity loc   activity options list
    u"2015CyberMARS產品研發專案": ("project2", "activity0",          _activity0_options),
    '2016Y_SDD'                : ("project3", "activity1",          _activity1_options)
}


activities = build_activities(proj_loc_map)


if __name__ == '__main__':
    print activities.get(u"管理事務_如時程,資源規劃與管理等 <<1.2.3>>").loc_activity
    print activities.get(u"管理事務_如時程,資源規劃與管理等 <<1.2.3>>").loc_project

    print activities.get(u"差旅 <<1.1.1>>").loc_activity
    print activities.get(u"差旅 <<1.1.1>>").loc_project