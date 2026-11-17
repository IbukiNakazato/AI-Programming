def menu():
  while True:
    print("【ウチダ電鉄 交通系 IC カード検証システム】\n")

    print("1: 乗車駅選択")
    print("2: チャージ機能\n")

    try:
        function = int(input("使用する機能を入力してください（終了する場合は99を入力）\n"))
    except ValueError:
        print("数字を入力してください．")
        continue

    if function == 1 or function == 2 or function == 99:
      #if function in [1, 2, 99]
      return function
    else:
      print("正しい数値を入力して下さい．")
      continue


def select_station(fare):
#各駅の運賃一覧
  akibahara_fare = 133
  yamanashi_fare = 4128
  nagano_fare = 7990

  while True:
      print("【乗車駅選択】\n")

      print(f"1: 秋葉原駅から　{akibahara_fare}円")
      print(f"2: 山梨駅から　{yamanashi_fare}円")
      print(f"3: 長野駅から　{nagano_fare}円\n")

      try:
          station = int(input("乗車した駅を入力してください(キャンセルする場合には 99 を入力)\n"))
      except ValueError:
          print("数字を入力してください．")
          continue

      if station == 1:
        print(f"乗車駅は秋葉原で運賃は {akibahara_fare} 円です")
        fare = akibahara_fare
        return fare
        
      elif station == 2:
        print(f"乗車駅は山梨で運賃は {yamanashi_fare} 円です")
        fare = yamanashi_fare
        return fare

      elif station == 3:
        print(f"乗車駅は長野で運賃は {nagano_fare} 円です")
        fare = nagano_fare
        return fare 

      elif station == 99:
        print("駅の選択をキャンセルしました．")
        return 0
      else:
        print("正しい数値を入力して下さい．")



def pay(balance, fare):
   new_balance = balance - fare 
  #balance:今のチャージ残高，fare:運賃
   print(f"チャージ残高は{balance}円です．")

   if fare > balance:
      print("残高不足です．")
      while fare >= balance:
         print("3000円自動チャージします．")
         balance += 3000
         new_balance = balance - fare 
      print(f"精算後のチャージ残高は{new_balance}円です．")

   elif fare <= balance:
      print(f"精算後のチャージ残高は{new_balance}円です．")

   if new_balance < 500:#1回だけ
      print("残高が500円未満のため3000円自動チャージします．")
      new_balance += 3000
      print(f"チャージ残高は{new_balance}円です．")

   return new_balance





def charge( balance ):
  #current_balance = 500
  print("【チャージ機能】")
  print("チャージ残高は", balance, "円です．")
  #print("チャージ残高は{balance}円です．")
  for i in range(1,11):
     print(f"{i}:{i}000円")
     #i += 1
  while True:
    try:
      charge_balance = int(input("チャージする金額を選択して下さい（キャンセルする場合には99を入力）\n"))
      if 1 <= charge_balance <= 10: 
        print(f"{charge_balance}000円チャージします．")
        balance += charge_balance * 1000
        print(f"チャージ残高は{balance}円です．")

        if balance >= 20000:
           print("チャージ残高が20000円を超えたため，システムを終了します．")
           exit()
        

      elif charge_balance == 99:
        print("チャージをキャンセルしました．")
        print(f"チャージ残高は{balance}円です．")
        return balance
      else:
         print("正しい数字を入力して下さい．")   

    except ValueError:
       print("数字を入力して下さい．")
 


def main():
  balance = 500
  fare = 0
  while True:
       number = menu()
       if number == 1:
          fare = select_station(fare)
          balance = pay(balance, fare)

       elif number == 2:
          balance = charge(balance)

       else:
          print("システムを終了します．")
          break

 


if __name__ == "__main__":
    main()

#print(menu())
#print(charge(20))
#print(pay(2106, 7990))