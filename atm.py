class atm:
    def __init__(self,bankbalance,pin,cashwidrawn,cardno):
        self.pin=pin
        self.cardno=cardno
        self.cashwidrawn=cashwidrawn
        self.bankbalance=bankbalance

    def AccountDeatail(self):
        print("Card number",self.cardno)
        print("pin",self.pin)
        
    def CashDetails(self):
        print("Cash Widrawn",self.cashwidrawn)

    def Balance(self):
        print("Bank Balance",self.bankbalance)


