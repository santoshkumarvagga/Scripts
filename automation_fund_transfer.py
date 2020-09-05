from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC

# sender net banking login details(ICICI bank)
USER_ID = 'SANTOSHVAGGA'
PASSWORD = 'Vagga@95'
debit_card_back_letters = {'A': '60', 'B': '94', 'C': '34', 'D': '16', 'E': '82', 'F': '27', 'G': '05', 'H': '44', 'I': '27', 'J': '69', 'K': '70', 'L': '48', 'M': '42', 'N': '12','O': '71', 'P': '15'}

# receiver acc details
ACC_NUM = 72258982420
NAME = 'BHAVANA J'
IFSC_CODE = "SBIN002085"

# amount to be transfered
AMOUNT = 1

# reciver bank type(True if ICICI or Fasle)
to_icici_bank = False

id = {'1' :'pp_1', '2' :'pp_5', '3' :'pp_0', '4' :'pp_16', '5' :'pp_27', '6':'pp_26', '7' :'pp_15', '8' :'pp_4', '9':'pp_2', '0':'pp_3'}

# Code Implemanrtation

browser = webdriver.Chrome()

login_screen = browser.get('https://infinity.icicibank.com/corp/AuthenticationController?FORMSGROUP_ID__=AuthenticationFG&__START_TRAN_FLAG__=Y&FG_BUTTONS__=LOAD&ACTION.LOAD=Y&AuthenticationFG.LOGIN_FLAG=1&BANK_ID=ICI&ITM=nli_personalb_personal_login_btn&_ga=2.4342899.1587489014.1599273028-932039528.1599273028')

using_user_id = browser.find_element_by_xpath('//*[@id="DUMMY1"]').click()

username = browser.find_element_by_xpath('//*[@id="AuthenticationFG.USER_PRINCIPAL"]').send_keys(USER_ID)
password = browser.find_element_by_xpath('//*[@id="AuthenticationFG.ACCESS_CODE"]').send_keys(PASSWORD)

Login_button = browser.find_element_by_xpath('//*[@id="VALIDATE_CREDENTIALS1"]')
Login_button.click()

print("Login Successfull..!!")

send_money_tab = browser.find_element_by_xpath('//*[@id="RetailUserDashboard_DRSCW__1:WidgetForm.Rowset9"]/ul/li[3]/div/a')
send_money_tab.click()

quick_fund_transfer_tab = browser.find_element_by_xpath('//*[@id="Fund-Transfer_Quick-Fund-Transfer"]')
quick_fund_transfer_tab.click()

def acc_details():
    acc_num = browser.find_element_by_xpath('//*[@id="CustomQuickPayFundsTransferFG.TO_ACCOUNT"]').send_keys(ACC_NUM)
    confirm_acc_num = browser.find_element_by_xpath('//*[@id="CustomQuickPayFundsTransferFG.PAYEE_ACCT_NUMBER"]').send_keys(ACC_NUM)
    payee_name = browser.find_element_by_xpath('//*[@id="CustomQuickPayFundsTransferFG.PAYEE_NAME"]').send_keys(NAME)
    amount = browser.find_element_by_xpath('//*[@id="CustomQuickPayFundsTransferFG.ENTRY_AMT"]').send_keys(AMOUNT)
    ifsc_field = browser.find_element_by_xpath('//*[@id="CustomQuickPayFundsTransferFG.PAYEE_BANK_IFSC"]').send_keys(str(IFSC_CODE))
    ifsc_verify_submit = browser.find_element_by_xpath('//*[@id="GET_PAYEE_BANK_DETAILS"]').click()
    proceed = browser.find_element_by_xpath('//*[@id="VALIDATE_FT_DETAILS"]').click()
    # confirmation details
    OTP_VIRTUAL = browser.find_element_by_xpath('//*[@id="virtual_keyboard"]').click()
    otp_received = input('PLEASE ENTER OTP RECEIVED')
    # browser.find_element_by_xpath('//*[@id="CustomQuickPayFundsTransferFG.ONE_TIME_PASSWORD__"]').send_keys(otp_received)
    otp = ''
    for i in otp_received:
        otp = otp+i+' '
    temp_list = []

    print("OTP input string is:", otp)
    for i in otp.split(' '):
        print("now entering :", i)
        temp_list.append(i)

    def get_id(digit):
        print("retrieving id for digit {}".format(digit))
        return id[str(digit)]

    input_list = temp_list[:-1]
    print('Final OTP list input', input_list)
    for i in input_list:
        browser.find_element_by_id(get_id(i)).click()
        print("entered the digit {} in Virtual keyboard".format(i))

    print("Finished entering OTP in virtual keyboard")
    Ok_virtual_keyboard = browser.find_element_by_xpath('//*[@id="done"]').click()

    print("Entering values for Alphabets on debit card..")

if to_icici_bank:
    Send_within_ICICI = browser.find_element_by_xpath('//*[@id="CustomQuickPayFundsTransferFG.TO_BANK_ACC_TYPE1"]').click()
    acc_details()
else:
    send_to_other_bank = browser.find_element_by_xpath('//*[@id="CustomQuickPayFundsTransferFG.TO_BANK_ACC_TYPE2"]').click()
    acc_details()
