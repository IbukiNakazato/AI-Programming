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

    if function == 1:
      select_station()
      break
    elif function == 2:
      charge( balance=0 )
      break
    elif function == 99:
      print("システムを終了します．")
      break
    else:
      print("正しい数値を入力して下さい．")


def select_station():
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
        break
      elif station == 2:
        print(f"乗車駅は山梨で運賃は {yamanashi_fare} 円です")
        break
      elif station == 3:
        print(f"乗車駅は長野で運賃は {nagano_fare} 円です")
        break
      elif station == 99:
        print("駅の選択をキャンセルしました．")
        break
      else:
        print("正しい数値を入力して下さい．")


def pay():
  #ここに処理の中身を書く。()カッコ内の引数はある場合は書く。
  pass #このpassは処理を書いた後消してよい。


def charge( balance ):

  print("【チャージ機能】")
  print("チャージ残高は", balance, "円です．")
  #print("チャージ残高は{balance}円です．")
  #ここに処理の中身を書く。()カッコ内の引数はある場合は書く。
  pass #このpassは処理を書いた後消してよい。


def main():
  #ここに処理の中身を書く。()カッコ内の引数はある場合は書く。
  pass #このpassは処理を書いた後消してよい。


if __name__ == "__main__":
    main()

print(menu())