from datetime import date
import requests

class Currency_Converter:
    def __init__(self):
        self.cn = []     # Country Names
        self.cv = []     # Currency values from USD to that country
        self.usv = []    # Currency values from that country to USD
        self.T = False   # Flag for online success

    def All_list_append(self):
        """Reads and appends data from 'main_info.txt' into cn, cv, usv lists."""
        try:
            with open('main_info.txt', 'r', encoding='utf-8') as f:
                lines = f.readlines()
                for line in lines:
                    parts = line.strip().split('\t')
                    if len(parts) >= 3:
                        self.cn.append(parts[0])
                        self.cv.append(parts[1])
                        self.usv.append(parts[2])
        except FileNotFoundError:
            print("[ERROR] 'main_info.txt' not found. Please ensure the file exists.")
            exit()

    def Root(self):
        """Fetches currency table from online and writes it to 'string_info.txt'."""
        today = date.today()
        print("📅 Date:", today.strftime("%d/%m/%Y"))
        try:
            response = requests.get("https://www.x-rates.com/table/?from=USD&amount=1")
            if response.status_code == 200:
                with open('string_info.txt', 'wb') as f:
                    f.write(response.content)
                print("[INFO] Online currency data fetched successfully.\n")
                self.T = True
            else:
                print("[WARNING] Failed to fetch live data. Status Code:", response.status_code)
        except requests.RequestException:
            print("[WARNING] No network. Working with offline data.")
            self.T = False

    def Online_process(self):
          """Fetch currency data from HTML source and write to main_info.txt."""
          if not self.T:
               return

          try:
               with open('string_info.txt', 'r', encoding='utf-8') as f:
                    lines = f.readlines()

               cn, cv, usv = [], [], []
               for i in range(len(lines)):
                    line = lines[i].strip()
                    if line.startswith('<td>') and '</td>' in line:
                         try:
                              country = line.split('<td>')[1].split('</td>')[0]
                              val1 = lines[i + 1].strip().split('>')[2].split('<')[0]
                              val2 = lines[i + 2].strip().split('>')[2].split('<')[0]
                              
                              cn.append(country)
                              cv.append(val1)
                              usv.append(val2)
                         except (IndexError, ValueError):
                              continue

               with open('main_info.txt', 'w', encoding='utf-8') as f:
                    for i in range(len(cn)):
                         line = f"{cn[i]}\t{cv[i]}\t{usv[i]}\n"
                         f.write(line)

               print("[INFO] 'main_info.txt' updated with fresh data.")
               self.cn, self.cv, self.usv = cn, cv, usv  # Fill class lists for use in Main()

          except FileNotFoundError:
               print("[ERROR] 'string_info.txt' not found.")

    def Main(self):
        """Handles user interaction for converting currency."""
        print('\n' + '💱 Available Countries'.center(50, '-'))
        for i, country in enumerate(self.cn):
            print(f"{i + 1}) {country}")
        try:
            amount = float(input("\n💰 Enter amount: "))
            from_country = input("🔁 From country: ").strip().title()
            to_country = input(f"➡️ Convert {from_country} to: ").strip().title()

            if from_country not in self.cn and from_country != "Us Dollar":
                print("[ERROR] From country not supported.")
                return

            if to_country not in self.cn and to_country != "Us Dollar":
                print("[ERROR] To country not supported.")
                return

            # Perform conversion logic
            if from_country == "Us Dollar":
                idx = self.cn.index(to_country)
                result = amount * float(self.cv[idx])
            elif to_country == "Us Dollar":
                idx = self.cn.index(from_country)
                result = amount * float(self.usv[idx])
            else:
                idx_from = self.cn.index(from_country)
                idx_to = self.cn.index(to_country)
                result = amount * float(self.usv[idx_from]) * float(self.cv[idx_to])

            print(f"\n✅ {amount} {from_country} = {result:.2f} {to_country}\n")

        except ValueError:
            print("[ERROR] Invalid amount entered.")

def Run():
    while True:
        app = Currency_Converter()
        app.Root()
        app.Online_process()
        app.All_list_append()
        app.Main()

        again = input("🔄 Do you want to convert again? (y/n): ").strip().lower()
        if again != 'y':
            print("👋 Thank you for using Currency Converter!")
            break

if __name__ == '__main__':
    Run()


# old code for reference, not used in the current implementation
# # currency converter ...
# from datetime import date
# import requests

# class Currency_Converter:
#      def __init__(self):
#           self.cn = [] # country name
#           self.cv = [] # country value ...
#           self.usv = [] # US value
#           self.all_list = [self.cn,self.cv,self.usv]
#      def All_list_append(self): # this function is compulsory one time run
#           ''' self.cn , self.cv , self.usv list la append panra '''
          
#           for index in range(len(self.all_list)):
#                with open('main_info.txt','r+') as f:
#                     al = f.readlines()
#                     for i in al:
#                          if index == 2:
#                               self.all_list[index].append(i.split('\t')[index][:-1])
#                          else:
#                               self.all_list[index].append(i.split('\t')[index])
#      def Root(self):
#           ''' online la iruntha, "online la irukura US table data va" string_info.txt the write panra '''
#           today = date.today()
#           d1 = today.strftime("%d/%m/%Y")
#           print("date/ month / year :", d1)
#           try:
#                respond = requests.get("https://www.x-rates.com/table/?from=USD&amount=1")
#                if respond.status_code == 200:   
#                     with open('string_info.txt','wb') as f:
#                           f.write(respond.content)
#                     print('update the currency converter and also online\n'.upper())
#                     self.T = True
#                elif respond.status_code == 400:
#                     print('This website is not found')
#           except:
#                self.T = False
#                print('Your Network is not connected, this is old data currency converter')
               
#      def Main(self):
#           ''' print all country and proccess the data '''
#           print('Country and currency name'.center(50,'~'))
#           [print(i + 1,')',self.cn[i]) for i in range(len(self.cn))]
#           print('54 ) US Dollar')
#           print('\ncurrency converter'.upper())
#           try:
#                amount = float(input('Enter your Amount :'))
#                fcn = str(input('Enter your country "from" name :')).strip().title()
#                if fcn in self.cn or fcn == 'Us Dollar':
#                     scn = str(input(f'{fcn} to Enter another country name :')).strip().title()
#                     if (scn in self.cn) or scn == 'Us Dollar':
#                          if fcn == 'Us Dollar':
#                               in_val2 = self.cn.index(scn)
#                               amounts = amount  * float(self.cv[in_val2])
#                          elif scn == 'Us Dollar':
#                               in_val1 = self.cn.index(fcn)
#                               amounts = amount  * float(self.usv[in_val1])
#                          else:
#                               in_val1 = self.cn.index(fcn)
#                               in_val2 = self.cn.index(scn)
#                               amounts = amount  * float(self.usv[in_val1]) * float(self.cv[in_val2])
#                          print(f'{amount} {fcn} is equal to' + ' {:.2f} {}'.format(amounts,scn))
#                     else:
#                          print('your country is not in the list'.upper())
#                else:
#                     print('your country is not in the list'.upper())
#           except ValueError:
#           	print('This is not a number !')
#      def Online_process(self):
#           ''' online la iruntha: html souce code da read panni, main_info.txt la append panra  '''
#           if self.T:
#                cn = self.cn[:]
#                cv = []
#                usv = []
#                with open('string_info.txt','r') as f:
#                     al = f.readlines()
#                     count = 1
#                     for i in self.cn:
#                          for j in range(len(al)):
#                               if f'<td>{i.strip()}</td>' == al[j].strip() and  j + 1 >= 191:
#                                                        #print(als)
#                                                        #print([j + 1,')' ,al[j].strip()],count)
#                                                        cv.append(al[j + 1].strip()[81:-9])
#                                                        #print(al[j + 1].strip()[81:-9])
#                                                        usv.append(al[j + 2].strip()[81:-9])
#                                                        #print(al[j + 2].strip()[81:-9])
#                                                        count += 1
#                with open('main_info.txt','r+') as nf:
#                     for index in range(53):
#                          print(f'{index + 1}) {cn[index]}')
#                          formate = cn[index] +'\t'  + cv[index] + '\t' + usv[index] + '\n'  
#                          nf.write(formate)
                    
# def Run():
#      t = True
#      while t:
#           start = Currency_Converter()
#           start.Root()
#           start.All_list_append()
#           start.Online_process()
#           start.Main()
#           print()
#           while True:
#                requests = str(input('If your want Restart the currency converter, Enter (y/n):')).strip().lower()
#                if requests == 'y':
#                     break
#                elif requests == 'n':
#                     t = False
#                     break

# if __name__ == '__main__':
#      Run()

