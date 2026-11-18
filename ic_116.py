def menu():
  functions = ["乗車駅選択", "チャージ機能"]
  while True:
    print("\n【ウチダ電鉄　交通系ICカード検証システム】\n")

    for i in range(len(functions)):
      print(f"{i + 1}: {functions[i]}")
    print()

    try:
        function = int(input("使用する機能を入力してください(終了する場合には99を入力)\n"))
    except ValueError:
        print("数字を入力してください。")
        continue
    if 1 <= function <= len(functions) or function == 99:
        return function
    else :
        print("正しい数値を入力してください。")

def select_station():
  stations = ["秋葉原", "山梨", "長野"]
  fares = [133, 4128, 7990]

  while True:
      print("\n【乗車駅選択】\n")

      for i in range(len(stations)):
        print(f"{i + 1}: {stations[i]}駅から {fares[i]}円")
      print()

      try:
          station = int(input("乗車した駅を入力してください(キャンセルする場合には99を入力)\n"))
      except ValueError:
          print("数字を入力してください。")
          continue

      if 1 <= station <= len(stations):
        fare = fares[station - 1]
        print(f"乗車駅は{stations[station - 1]}で運賃は{fare}円です。")
        return fare

      elif station == 99:
        print("駅の選択をキャンセルしました。")
        return 0
      else:
        print("正しい数値を入力してください。")

def charge( balance ):
  charges = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]

  print("\n【チャージ機能】\n")
  print(f"チャージ残高は{balance}円です。\n")

  for i in range(len(charges)):
    print(f"{i + 1}: {charges[i]}円")
  print()

  while True:
    try:
        charge_amount = int(input("チャージする金額を選択してください(キャンセルする場合には99を入力)\n"))
    except ValueError:
        print("数字を入力してください。")
        continue

    if 1 <= charge_amount <= len(charges):
      charge = charges[charge_amount - 1]
      print(f"{charge}円チャージします。")
      balance += charges[charge_amount - 1]
      print(f"チャージ残高は{balance}円です。")
      return balance

    elif charge_amount == 99:
      print("チャージをキャンセルしました。")
      return balance
    else:
      print("正しい数値を入力してください。")  

def pay(balance, fare):

  print(f"チャージ残高は{balance}円です。")

  if balance < fare:
     print("残高不足です。")
     while fare > balance:
      balance += 3000
      print("3000円自動チャージします。")
  balance -= fare
  print(f"精算後のチャージ残高は{balance}円です。")
  
  if balance < 500:
     balance += 3000
     print("残高が500円未満のため3000円自動チャージします。")
     print(f"チャージ残高は{balance}円です。")
  return balance

def main():
  balance = 500
  while True:
    function = menu()
    if function == 1:
      fare = select_station()
      if fare > 0:
        balance = pay(balance, fare)
    elif function == 2:
      balance = charge(balance)
    elif function == 99:
      print("システムを終了します")
      break

if __name__ == "__main__":
    main()
