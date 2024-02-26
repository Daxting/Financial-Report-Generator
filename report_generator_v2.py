def define_item_number():
    data = [
        ['代號', '項目名稱'],
        ['1112', '銀行存款'],
        ['111200', '銀行存款-台幣'],
        ['111201', '銀行存款-外幣'],
        ['113', '存貨'],
        ['1131', '商品存貨'],
        ['1132', '製成品存貨'],
        ['1133', '在製品存貨'],
        ['1134', '原料存貨'],
        ['1135', '物料存貨'],
        ['1410', '土地'],
        ['1431', '房屋及建築'],
        ['1432', '累計折舊-房屋及建築'],
        ['1903', '預付設備款'],
        ['2112', '銀行借款'],
        ['2192', '股東往來'],
        ['2220', '長期借款'],
        ['3110', '股本(登記)'],
        ['41', '營業收入總額'], #calculated item        41 total
        ['4', '營業收入淨額'],  #calculated item        4 total
        ['5', '營業成本'],      #calculated item        5 total
        ['50', '進銷成本'],     #calculated item        50 total
        ['51', '直接原料'],     #calculated item        51 total
        ['52', '間接材料'],     #calculated item        52 total
        ['54', '製造費用'],     #calculated item        54 total
        ['5550', '製造成本'],   #calculated item         51+5300+54
        ['5560', '製成品成本'], #calculated item         5550
        ['5570', '產銷成本'],   #calculated item         5560+5561+5562+5566
        ['0045', '營業毛利'],    #calculated item         4+5
        ['6', '營業費用及損失總額'],#calculated item     6 total * -1
        ['00456', '營業淨利'],  #calculated item         4+5+6
        ['7', '非營業收入總額'],#calculated item         7 total 
        ['8', '非營業損失及費用總額'],#calculated item   8 total * -1
        ['0045678', '本期損益'],#calculated item      4+5+6+7+8
        ['9999', '所得稅費用'],
        ['3440', '本期損益(稅後)'],#calculated item      4+5+6+7+8-9999
        ['4101', '營業收入'],
        ['4102', '模具收入'],
        ['4201', '銷貨退回'],
        ['4202', '銷貨折讓'],
        ['5010', '期初存貨'],
        ['5021', '進貨'],
        ['5022', '進貨退出'],
        ['5023', '進貨折讓'],
        ['5030', '期末存貨'],
        ['5040', '進貨-其他(加項)'],
        ['5050', '進貨-其他(減項)'],
        ['5110', '期初存料-原料'],
        ['5121', '原料'],
        ['5122', '原料退出'],
        ['5123', '原料折讓'],
        ['5130', '期末存貨-原料'],
        ['5140', '直接原料-其他(加項)'],
        ['5150', '直接原料-其他(減項)'],
        ['5210', '期初存料-物料'],
        ['5221', '物料'],
        ['5222', '物料退出'],
        ['5223', '物料折讓'],
        ['5230', '期末存貨-物料'],
        ['5240', '間接材料-其他(加項)'],
        ['5250', '間接材料-其他(減項)'],
        ['5300', '直接人工'],
        ['5401', '間接人工-(製)'],
        ['5402', '租金支出-(製)'],
        ['5403', '文具用品-(製)'],
        ['5404', '旅費-(製)'],
        ['5405', '運費-(製)'],
        ['5406', '郵電費-(製)'],
        ['5407', '修繕費-(製)'],
        ['5408', '包裝費-(製)'],
        ['5409', '水電瓦斯費-(製)'],
        ['5410', '保險費-(製)'],
        ['5411', '加工費-(製)'],
        ['5412', '稅捐-(製)'],
        ['5413', '折舊-(製)'],
        ['5414', '各項耗竭及攤提-(製)'],
        ['5415', '伙食費-(製)'],
        ['5416', '職工福利-(製)'],
        ['5490', '其他製造費用'],
        ['5498', '其他製造費用剔除數'],
        ['5550', '製造成本'],
        ['5551', '期初在製品盤存'],
        ['5552', '期末在製品盤存'],
        ['5553', '在製品-其他(加項)'],
        ['5554', '在製品-其他(減項)'],
        ['5560', '製成品成本'],
        ['5561', '期初製成品盤存'],
        ['5562', '期末製成品盤存'],
        ['5563', '製成品-其他(加項)'],
        ['5564', '製成品-其他(減項)'],
        ['5565', '外銷退稅款'],
        ['5566', '產銷成本減項'],
        ['5570', '產銷成本'],
        ['5600', '勞務成本'],
        ['5700', '修理成本'],
        ['5800', '加工成本'],
        ['5810', '業務成本'],
        ['5900', '其他營業成本'],
        ['6110', '薪資支出'],
        ['6111', '租金支出'],
        ['6112', '文具用品'],
        ['6113', '旅費'],
        ['6114', '運費'],
        ['6115', '郵電費'],
        ['6116', '修繕費'],
        ['6117', '廣告費'],
        ['6118', '水電瓦斯費'],
        ['6119', '保險費'],
        ['6120', '交際費'],
        ['6121', '捐贈'],
        ['6122', '稅捐'],
        ['6123', '呆帳損失'],
        ['6124', '折舊'],
        ['6125', '各項耗竭及攤提'],
        ['6126', '外銷損失'],
        ['6127', '伙食費'],
        ['6128', '職工福利'],
        ['6129', '研究費'],
        ['6130', '佣金支出'],
        ['6131', '訓練費'],
        ['6132', '其他費用'],
        ['6133', '商譽攤銷'],       #b102 的 107 無此項
        ['7035', '一般股息與紅利'],
        ['7036', '特殊股利'],
        ['7037', '特殊股票'],
        ['7038', '利息收入'],
        ['7039', '租賃收入'],
        ['7040', '出售資產盈餘'],
        ['7041', '佣金收入'],
        ['7042', '商品盤盈'],
        ['7043', '兌換盈益'],
        ['7044', '其他收入'],
        ['7097', '退稅收入'],
        ['7098', '國外投資收益'],   #b102 的 107 無此項
        ['8046', '利息支出'],
        ['8047', '投資損失'],
        ['8048', '出售資產損失'],
        ['8049', '災害損失'],
        ['8050', '商品盤損'],
        ['8051', '兌換虧損'],
        ['8052', '其他損失'],
    ]
    # Convert the list of lists directly into a dictionary in {key: value} form
    my_dict = {item[0]: item[1] for item in data[1:]}
    # Print the resulting dictionary
    print(my_dict)
    return my_dict

def process_keys_in_place(input_dict):
    import re
    updated_dict = {}
    for key, value in input_dict.items():
        # 使用正则表达式删除中文字符
        processed_key = re.sub(r'[\u4e00-\u9fff]', '', key)
        
        # 如果键发生变化，将其添加到更新字典中
        if processed_key != key:
            updated_dict[processed_key] = value
        else:
            updated_dict[key] = value

    # 更新原始字典
    input_dict.clear()
    input_dict.update(updated_dict)
              
def read_customer_portfolio_file(file_path):
    import pandas as pd
    try:
        df = pd.read_excel(file_path)
        #turn df into dictionary, each columns stand for different pairs, use first row as keys, other rows as value
        df_dict = df.to_dict('list')
        # if the key contains chinese, then remove the chinese and keep the english and number
        try:
            process_keys_in_place(df_dict)
        except Exception as e:
            pass
        #if the value contains nan, then remove it
        for key in df_dict:
            df_dict[key] = [value for value in df_dict[key] if str(value) != 'nan']
        print(df_dict)
        return df_dict
    except Exception as e:
        pass
        return None

#使用者輸入(函防呆機制)
def user_input(my_dict, customer_dict):
    # 使用者輸入"單一項目代號"or"ALL"
    while True:
        item_number = input("請輸入項目代號(全項目輸入'all'): ")
        # 檢查項目代號的格式是否正確，這裡可以加入更多的檢查邏輯
        if item_number in my_dict.keys() or item_number == 'ALL' or item_number == 'all':
            break  # 輸入正確，跳出迴圈
        else:
            print("項目代號輸入不支援，請重新輸入")
    # 若小寫自動轉大寫
    item_number = item_number.upper()
    # 使用者輸入"單一客戶代號"or"客戶清單編號CP"
    while True:
        customer_number = input("請輸入客戶代號: ")
        # 若小寫自動轉大寫
        customer_number = customer_number.upper()
        #if the first character is not english, then ask user to re-enter or if the customer_number is in customer_dict's key, then break the loop 
        if customer_number[0].isalpha() or customer_number in customer_dict.keys():
            break
        else:
            print("客戶代號第一碼必須為英文，請重新輸入")
    # 使用者輸入年分
    while True:
        year_start = input("請輸入起始年度(民國): ")
        year_end = input("請輸入結束年度(民國): ")
        # 檢查年度的格式是否正確，這裡可以加入更多的檢查邏輯
        if year_start.isdigit() and year_end.isdigit() and int(year_start) <= int(year_end):
            break  # 輸入正確，跳出迴圈
        else:
            print("年度輸入錯誤，請重新輸入")

    year_start = int(year_start)
    year_end = int(year_end)
    year_list = [str(year) for year in range(year_start, year_end + 1)]


    # print the user input for confirmation
    # if the item_number is in my_dict's key, then print the value of the key
    print('')
    print("輸入資訊如下:")
    if item_number in my_dict.keys():
        print(f"項目代號: {item_number}, {my_dict[item_number]}")
    else:
        print(f"項目代號: {item_number}")
    # if the customer_number is in customer_dict's key, then print the value of the key
    if customer_number in customer_dict.keys():
        print(f"客戶代號: {customer_number}, {customer_dict[customer_number]}")
    else:
        print(f"客戶代號: {customer_number}")   
    if year_start == year_end:
        print(f"單年度: {year_start}")
    else:
        print(f"多年度: {year_list}")

    return item_number, customer_number, year_list

#解壓縮檔案
def extract_file(source_file_path, extract_to_path, file_to_extract):
    import zipfile
    with zipfile.ZipFile(source_file_path , 'r') as zip_ref:
        fixed_path = file_to_extract.split('\\')
        try:
            zip_ref.extract(fixed_path[-1], extract_to_path)
        except Exception as e:
            pass
    # if the extract_to_path exists and is not empty return True
    import os
    if os.path.exists(extract_to_path) and os.listdir(extract_to_path):
        return True
    else:
        return False
        
#抓公司名稱
def get_company_name(extract_to_path, company_number):
    import pandas as pd
    file_path = f'{extract_to_path}\\{company_number}_.TXT'
    company_name = ''
    #read the first line of the file
    try:
        with open(file_path, 'r', encoding='big5') as f:
            company_name = f.readline()
            pass
    except FileNotFoundError:
        pass
    except Exception as e:
        pass
    return company_name

#轉檔dbf to csv
def dbf_to_csv(dbf_table_path):
    import os
    import glob
    from dbfread import DBF
    import csv
    csv_fn = dbf_table_path[:-4] + ".csv"  # Set the csv file name
    table = DBF(dbf_table_path)  # table variable is a DBF object
    with open(csv_fn, 'w', newline='', encoding='Big5') as f:  # create a csv file, fill it with dbf content
        writer = csv.writer(f)
        writer.writerow(table.field_names)  # write the column name
        for record in table:  # write the rows
            writer.writerow(list(record.values()))
    return csv_fn  # return the csv name

#加入計算項目
def add_calculated_item(df):
        # ['41', '營業收入總額'], #calculated item        41 total
        # ['4', '營業收入淨額'],  #calculated item        4 total
        # ['50', '進銷成本'],     #calculated item        50 total
        # ['51', '直接原料'],     #calculated item        51 total
        # ['52', '間接材料'],     #calculated item        52 total
        # ['54', '製造費用'],     #calculated item        54 total
        # ['5550', '製造成本'],   #calculated item         51+5300+54
        # ['5560', '製成品成本'], #calculated item         5550
        # ['5570', '產銷成本'],   #calculated item         5560+5561+5562+5566
        # ['5', '營業成本'],      #calculated item         5 total * -1
        # ['0045', '營業毛利'],    #calculated item         4+5
        # ['6', '營業費用及損失總額'],#calculated item     6 total * -1
        # ['00456', '營業淨利'],  #calculated item         4+5+6
        # ['7', '非營業收入總額'],#calculated item         7 total 
        # ['8', '非營業損失及費用總額'],#calculated item   8 total * -1
        # ['0045678', '本期損益'],#calculated item      4+5+6+7+8
        # ['9999', '所得稅費用'],
        # ['3440', '本期損益(稅後)']#calculated item      4+5+6+7+8-9999
    df['41'] = df['4101'] + df['4102']
    df['4'] = df['41'] + df['4201'] + df['4202']
    df['50'] = df['5010'] + df['5021'] + df['5022'] + df['5023'] + df['5030'] + df['5040'] + df['5050']
    df['51'] = df['5110'] + df['5121'] + df['5122'] + df['5123'] + df['5130'] + df['5140'] + df['5150']
    df['52'] = df['5210'] + df['5221'] + df['5222'] + df['5223'] + df['5230'] + df['5240'] + df['5250']
    df['54'] = df['5401'] + df['5402'] + df['5403'] + df['5404'] + df['5405'] + df['5406'] + df['5407'] + df['5408'] + df['5409'] + df['5410'] + df['5411'] + df['5412'] + df['5413'] + df['5414'] + df['5415'] + df['5416'] + df['5490'] + df['5498']
    df['5550'] = df['51'] + df['52'] + df['5300'] + df['54']
    df['5560'] = df['5550'] + df['5551'] + df['5552'] + df['5553'] + df['5554']
    df['5570'] = df['5560'] + df['5561'] + df['5562'] + df['5563'] + df['5564'] + df['5565'] + df['5566']
    df['5'] = df['50'] + df['5570'] + df['5600'] + df['5700'] + df['5800'] + df['5900']
    df['5'] = df['5'] * -1
    df['0045'] = df['4'] + df['5']
    # 因為107年的資料沒有6133，所以要先判斷6133是否存在
    if '6133' not in df:
        df['6133'] = 0
    df['6'] = df['6110'] + df['6111'] + df['6112'] + df['6113'] + df['6114'] + df['6115'] + df['6116'] + df['6117'] + df['6118'] + df['6119'] + df['6120'] + df['6121'] + df['6122'] + df['6123'] + df['6124'] + df['6125'] + df['6126'] + df['6127'] + df['6128'] + df['6129'] + df['6130'] + df['6131'] + df['6132'] + df['6133']
    df['6'] = df['6'] * -1
    df['00456'] = df['0045'] + df['6']
    # 因為107年的資料沒有7098，所以要先判斷7098是否存在
    if '7098' not in df:
        df['7098'] = 0
    df['7'] = df['7035'] + df['7036'] + df['7037'] + df['7038'] + df['7039'] + df['7040'] + df['7041'] + df['7042'] + df['7043'] + df['7044'] + df['7097'] + df['7098']
    df['8'] = df['8046'] + df['8047'] + df['8048'] + df['8049'] + df['8050'] + df['8051'] + df['8052']
    df['8'] = df['8'] * -1
    df['0045678'] = df['00456'] + df['7'] + df['8']
    df['3440'] = df['0045678'] + df['9999']

    return df

#獲取關鍵訊息
def get_key_dict(data, xmaster_csv, invent_csv):
    #把xmaster.csv轉成字典
    # 指定要保留的ACCNO值
    values_in_invent = ['113', '1131', '1132', '1133', '1134', '1135', '5010', '5030', '5110', '5130', '5210', '5230', '5551', '5552', '5561', '5562']
    # 进行筛选
    import pandas as pd
    # 读取CSV文件
    try:
        df = pd.read_csv(xmaster_csv, encoding='big5')  
    except Exception as e:
        df = pd.read_csv(xmaster_csv, encoding='utf-8')

    
    # filter the dataframe
    # if the ACCNO is in data.keys, then keep the row
    filtered_df = df[df['ACCNO'].astype(str).isin(data.keys())]
    # if the ACCNO is in values_in_invent, then remove the row
    filtered_df = filtered_df[~filtered_df['ACCNO'].astype(str).isin(values_in_invent)]
    # if the filter_df contains empty value, then fill the empty value with 0
    filtered_df.fillna(float(0.0), inplace=True)
    # add a new column 'result' to the filtered_df
    filtered_df['result']=filtered_df['LDAMOUNT']+filtered_df['DAMOUNT1']+filtered_df['DAMOUNT2']+filtered_df['DAMOUNT3']+filtered_df['DAMOUNT4']+filtered_df['DAMOUNT5']+filtered_df['DAMOUNT6']+filtered_df['DAMOUNT7']+filtered_df['DAMOUNT8']+filtered_df['DAMOUNT9']+filtered_df['DAMOUNT10']+filtered_df['DAMOUNT11']+filtered_df['DAMOUNT12']-filtered_df['LCAMOUNT']-filtered_df['CAMOUNT1']-filtered_df['CAMOUNT2']-filtered_df['CAMOUNT3']-filtered_df['CAMOUNT4']-filtered_df['CAMOUNT5']-filtered_df['CAMOUNT6']-filtered_df['CAMOUNT7']-filtered_df['CAMOUNT8']-filtered_df['CAMOUNT9']-filtered_df['CAMOUNT10']-filtered_df['CAMOUNT11']-filtered_df['CAMOUNT12']
    result_dict = filtered_df[['ACCNO', 'result']].set_index('ACCNO').to_dict()['result']
    # to ensure the value is float, to ensure the key is string
    result_dict = {str(key): float(value) for key, value in result_dict.items()}
    # to ensure the value is positive
    result_dict['2112']*=-1#銀行借款
    result_dict['2192']*=-1#業主(股東)往來
    result_dict['2220']*=-1#長期借款
    result_dict['3110']*=-1#股本(登記)
    result_dict['4101']*=-1#營業收入
    result_dict['4102']*=-1#模具收入
    result_dict['4201']*=-1#銷貨退回
    result_dict['4202']*=-1#銷貨折讓
    result_dict['7038']*=-1#利息收入
    result_dict['7043']*=-1#兌換盈益
    result_dict['7044']*=-1#其他收入
    result_dict['9999']*=-1#所得稅費用

    #把invent.csv轉成字典
    import csv
    try:
        with open(invent_csv, 'r', encoding='big5') as csvfile:
            reader = csv.DictReader(csvfile)
            # 获取列名
            fieldnames = reader.fieldnames
            eamt_sum = 0
            # 遍历每一行数据
            for row in reader:
                # 获取 ACCNAME 和 EAMT 列的值
                ACCNO = row.get('ACCNO')
                ACCNO1 = row.get('ACCNO1')
                ACCNO2 = row.get('ACCNO2')
                eamt = float(row.get('EAMT'))
                bamt = float(row.get('BAMT'))
                eamt_sum += eamt
                result_dict.update({ACCNO:eamt}) # 将 ACCNO 和 EAMT 添加到字典中
                result_dict.update({ACCNO1:bamt})
                result_dict.update({ACCNO2:(eamt*-1)})
            result_dict.update({'113':eamt_sum})# 将 存貨 和 EAMT 添加到字典中
    except FileNotFoundError:
        pass
    except Exception as e:
        pass
    
    return add_calculated_item(result_dict)

#加入年度資訊
def append_to_xlsx(df, year, result_dict, extract_to_path):
    import locale
    import numpy as np
    # create a new column '小計('+year+')'
    year_str = 'Amount_'+year
    df[year_str] = 0
    # if result_dict contains key, update value in df
    # 确保 '代號' 列和 result_dict 的键具有相同的数据类型
    df['代號'] = df['代號'].astype(str)
    # 清理数据，确保一致性
    df['代號'] = df['代號'].str.strip()
    # 检查 '代號' 列和 result_dict 的索引匹配
    common_indices = set(df['代號']).intersection(result_dict.keys())
    # 更新 DataFrame
    for common_index in common_indices:
        df.loc[df['代號'] == common_index, year_str] = result_dict[common_index]
    # 将所有的 inf 和 -inf 替换为 nan
    if df[year_str].any():
        df[year_str] = df[year_str].replace([np.inf, -np.inf], np.nan)
    else:
        #set all the value to None
        df[year_str] = np.nan
    # 使用ExcelWriter写入多个工作表

    # delete the result_dict
    del result_dict
    # 删除源文件夹
    import os
    import shutil
    # 删除文件夹
    try:    
        shutil.rmtree(extract_to_path)
       
    except OSError as e:
        pass

def add_info(df, form_name, sheet_name, writer, isCompany):
    
    # turn the value from the third column and the second row to the following format
    # the value in df into integer from the third column and the second row
    # if the value is nan, then skip it, otherwise turn the value from float into integer
    import numpy as np
    if isCompany:
        df.iloc[:, 2:] = df.iloc[:, 2:].applymap(lambda x: int(x) if not np.isnan(x) else x)
        # turn the '代號' column into integer
        df['代號'] = df['代號'].astype(int)
    
    # Additional information
    import openpyxl
    from datetime import datetime
    # 获取当前日期 year-month-day, hour:minute:second 例如 2021-01-01 00:00:00
    current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    # 修改輸出時間格式 year-month-day, hour:minute:second 例如 110-01-01 00:00:00
    current_date = str(int(current_date[:4]) - 1911) + current_date[4:]
    # Additional information
    header_info = ['版權所有: 利品事務所', '', '']
    date_info = ['製表日期: ' + current_date, '', '']
    form_info = ''
    if isCompany:
        if form_name:
            form_info = ['公司名稱: ' + form_name, '', '']
        else:
            form_info = ['公司名稱: 無資料', '', '']
    else:
        form_info = ['項目代號: ' + form_name, '', '']

    # create a new sheet named sheet_name
    writer.sheets[sheet_name] = writer.book.add_worksheet(sheet_name)
    # Write the header information, date information and company name information and info, only info use number_format
    for row_num, info in enumerate([header_info, date_info, form_info]):
        writer.sheets[sheet_name].write_row(row_num, 0, info)
    # 設置每一列的數字格式, no float point and add comma every 3 digits from the 2 column and the fifth row
    number_format = writer.book.add_format({'num_format': '#,##0'})
    if isCompany:
        writer.sheets[sheet_name].set_column('C:ZZ', None, number_format)
    else:
        writer.sheets[sheet_name].set_column('B:ZZ', None, number_format)
    # Write the DataFrame to the Excel file
    if isCompany:
        df.to_excel(writer, sheet_name=sheet_name, index=False, startrow=3, na_rep='Nan')
    else:
        df.to_excel(writer, sheet_name=sheet_name, index=True, startrow=3, na_rep='Nan')

def auto_fit_width(excel_file_path):
    import openpyxl
    wb = openpyxl.load_workbook(excel_file_path)
    
    for sheet_name in wb.sheetnames:
        ws = wb[sheet_name]
        # Iterate over all columns and adjust their widths
        for column in ws.columns:
            max_length = 0
            column_letter = column[0].column_letter
            for cell in column[3:]:
                try:
                    cell_value = str(cell.value)
                    cell_length = len(cell_value.encode('big5')) + (cell_value.count('\n') * 2)  # Adjust for Chinese characters
                    if cell_length > max_length:
                        max_length = cell_length
                except:
                    pass
            adjusted_width = (max_length + 2) * 1.2
            ws.column_dimensions[column_letter].width = adjusted_width
    
    wb.save(excel_file_path)
    wb.close()

def dataframe_trim(df):
    # delete the rows(from the second row) with all the value (from the third colume) is pure digit and is 0 
    for index, row in df.iterrows():
        if  row[2:].astype(str).str.isdigit().all() and row[2:].astype(float).eq(0).all():
            df.drop(index, inplace=True)
    return

def create_all_item_csv(item_dict, customer_list, year_list, destination_file_path, extract_to_path):
    import pandas as pd
    dbf_files = [f'{extract_to_path}\\invent.dbf', f'{extract_to_path}\\xmaster.dbf']
    # 创建 ExcelWriter 对象
    writer = pd.ExcelWriter(destination_file_path, engine='xlsxwriter')
    for customer in customer_list:
        # 将字典转换为DataFrame
        df = pd.DataFrame(list(item_dict.items()), columns=['代號', '項目名稱'])
        company_name=''
        for year in year_list:
            source_file_path = f'.\\{year}\\{customer}.{str(year)[-2:]}a' 
            # detect if file exists
            import os.path
            result_dict = {}
            if not os.path.isfile(source_file_path):
                pass
            else:
                # extract file
                if extract_file(source_file_path, extract_to_path, dbf_files[0]) and extract_file(source_file_path, extract_to_path, dbf_files[1]) and extract_file(source_file_path, extract_to_path, f'{customer}_.TXT'):
                    # get company name
                    if not company_name:
                        company_name = get_company_name(extract_to_path, customer)
                    # convert dbf to csv
                    for dbf_file in dbf_files:
                        try:
                            dbf_to_csv(dbf_file)
                        except Exception as e:
                            pass
                    input1_csv = f'{extract_to_path}\\xmaster.csv'
                    input2_csv = f'{extract_to_path}\\invent.csv'
                    result_dict = get_key_dict(item_dict, input1_csv, input2_csv)
            append_to_xlsx(df, year, result_dict, extract_to_path)
        # delete the zero rows in the dataframe, and add some information to the dataframe
        dataframe_trim(df)
        # 使用 rename 方法更改指定的行索引
        sheet_name = ''
        if company_name:
            sheet_name = f"{customer}{company_name[company_name.find(',') + 1 : company_name.find(',') + 3]}"
        else:
            sheet_name = f"{customer}無資料"
        add_info(df, company_name, sheet_name, writer, True)
    writer.close()
    auto_fit_width(destination_file_path)
    return None

def create_single_item_csv(item_dict, item_number, customer_list, year_list, destination_file_path, extract_to_path):
    import pandas as pd
    import os
    import shutil
    dbf_files = [f'{extract_to_path}\\invent.dbf', f'{extract_to_path}\\xmaster.dbf']
    # 创建 ExcelWriter 对象
    writer = pd.ExcelWriter(destination_file_path, engine='xlsxwriter')
    df = pd.DataFrame(index=customer_list, columns=year_list)
    index_mapping = {}
    column_mapping = {year_list[i]: f'Amount_{year_list[i]}' for i in range(len(year_list))}

    for customer in customer_list:
        # 将字典转换为DataFrame
        company_name=''
        for year in year_list:
            source_file_path = f'.\\{year}\\{customer}.{str(year)[-2:]}a' 
            # detect if file exists
            import os.path
            result_dict = {}
            if not os.path.isfile(source_file_path):
                pass
            else:
                # extract file
                if extract_file(source_file_path, extract_to_path, dbf_files[0]) and extract_file(source_file_path, extract_to_path, dbf_files[1]) and extract_file(source_file_path, extract_to_path, f'{customer}_.TXT'):
                    # get company name
                    if not company_name:
                        company_name = get_company_name(extract_to_path, customer)
                    # convert dbf to csv
                    for dbf_file in dbf_files:
                        try:
                            dbf_to_csv(dbf_file)
                        except Exception as e:
                            pass
                    input1_csv = f'{extract_to_path}\\xmaster.csv'
                    input2_csv = f'{extract_to_path}\\invent.csv'
                    result_dict = get_key_dict(item_dict, input1_csv, input2_csv)
                    # turn the value of item_number in the result_dict into integer if the value is not nan
                    if item_number in result_dict:
                        result_dict[item_number] = int(result_dict[item_number])
                    # append to index_mapping
                    df.loc[customer, year] = result_dict[item_number]
                    # delete the result_dict
                    del result_dict
                    # 删除文件夹
                    try:    
                        shutil.rmtree(extract_to_path)
                    except OSError as e:
                        pass
        # append to index_mapping
        if company_name:
            index_mapping[customer] = f"{customer}{company_name[company_name.find(',') + 1 : company_name.find(',') + 3]}"
        else:
            index_mapping[customer] = f"{customer}無資料"

    # 使用 rename 方法更改指定的行索引
    df = df.rename(index=index_mapping, columns=column_mapping)
    sheet_name = f'{item_number}{item_dict[item_number]}'
    item_name=f'{item_number}, {item_dict[item_number]}'
    add_info(df, item_name, sheet_name, writer, False)
    writer.close()
    auto_fit_width(destination_file_path)
    return None

def main():    
    import warnings
    warnings.simplefilter(action='ignore', category=FutureWarning)
    item_dict = define_item_number()
    customer_portfolio_file_path = f'.\\公司組合cp.xlsx'
    customer_dict = read_customer_portfolio_file(customer_portfolio_file_path)
    item_number, customer_number, year_list = user_input(item_dict, customer_dict)

    # create folder if not exist
    import os
    if not os.path.exists('.\\產出報表'):
        os.makedirs('.\\產出報表')
    # destination file path according to user input
    destination_file_path = ''
    if item_number == 'ALL':
        if(year_list[0]==year_list[-1]):
            destination_file_path = f'.\\產出報表\\全項目_{customer_number}_{str(year_list[0])}.xlsx'
        else:
            destination_file_path = f'.\\產出報表\\全項目_{customer_number}_{str(year_list[0])}_{str(year_list[-1])}.xlsx'
    else:
        if(year_list[0]==year_list[-1]):
            destination_file_path = f'.\\產出報表\\{item_number}{item_dict[item_number]}_{customer_number}_{str(year_list[0])}.xlsx'
        else:
            destination_file_path = f'.\\產出報表\\{item_number}{item_dict[item_number]}_{customer_number}_{str(year_list[0])}_{str(year_list[-1])}.xlsx'
    print("destination_file_path: ", destination_file_path)
    extract_to_path = f'.\\產出報表\\extracted_folder'
    # create the customer_list according to customer_number and customer_dict
    customer_list = []
    if customer_number in customer_dict.keys():
        customer_list = customer_dict[customer_number]
    else:
        customer_list.append(customer_number)
    # turn the customer_list into upper case
    customer_list = [customer.upper() for customer in customer_list]

    if item_number == 'ALL':
        # create the item_list according to item_number and item_dict
        create_all_item_csv(item_dict, customer_list, year_list, destination_file_path, extract_to_path)
    else:
        create_single_item_csv(item_dict, item_number, customer_list, year_list, destination_file_path, extract_to_path)

    print("finished")

if __name__ == '__main__':
    main()

