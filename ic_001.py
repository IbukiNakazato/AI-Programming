def menu():
  while True:
    print("【ウチダ電鉄 交通系 IC カード検証システム】\n")

    print("1: 乗車駅選択")
    print("2: チャージ機能\n")

    try:
        function = int(input("使用する機能を入力してください（終了する場合は99を入力）"))
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
  #ここに処理の中身を書く。()カッコ内の引数はある場合は書く。
  pass #このpassは処理を書いた後消してよい。


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