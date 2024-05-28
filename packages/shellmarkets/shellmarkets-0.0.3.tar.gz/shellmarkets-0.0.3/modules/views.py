from datetime import datetime
from colorama import Fore, Style

def show_header(info_dict):
    name = info_dict["symbol"].upper()
    ext_name=info_dict["shortName"]
    print(Style.BRIGHT+"["+name+" - "+ext_name+"]"+Style.RESET_ALL)

def show_price(info_dict):
    show_header(info_dict)
    """Show the current price."""
    price = float(info_dict["currentPrice"])
    div = info_dict["currency"]
    past_price = float(info_dict["previousClose"])

    if price >= past_price:
        i = "+"
    else:
        i = ""

    var = round(float(price) - float(past_price), 2)
    percent = round(var / float(past_price) * 100, 2)


    if var > 0:
        color = Fore.GREEN
    if var < 0:
        color = Fore.LIGHTRED_EX
    if var == 0:
        color = Fore.WHITE

    print("{}PRICE:{} {:<5} {:<5} {}\t[{}{}] [{}{}%] {}{}".format(
        Style.NORMAL,
        Style.BRIGHT,
        price,
        div,
        color,
        i,
        var,
        i,
        percent,
        Style.RESET_ALL,
        Fore.RESET))
    print(Style.DIM+"-"*48+Style.RESET_ALL)

def show_extended(info_dict):
    """Show the current price."""
    price = float(info_dict["currentPrice"])
    div = info_dict["currency"]
    volume = int(info_dict["volume"])
    average_volume = int(info_dict["averageVolume"])
    past_price = float(info_dict["previousClose"])
    max_day = info_dict["dayHigh"]
    min_day = info_dict["dayLow"]

    if price >= past_price:
        i = "+"
    else:
        i = ""

    var = round(float(price) - float(past_price), 2)
    percent = round(var / float(past_price) * 100, 2)
    volume_percent = (volume / average_volume) - 1

    if 0 < volume_percent <= 0.1:
        v_code = "~"
        color_v = Fore.WHITE
    elif 0.1 < volume_percent <= 0.25:
        v_code = "+"
        color_v = Fore.GREEN
    elif 0.25 < volume_percent <= 0.5:
        v_code = "++"
        color_v = Fore.GREEN
    elif volume_percent > 0.5:
        v_code = "+++"
        color_v = Fore.GREEN
    elif 0 > volume_percent >= -0.1:
        v_code = "~"
        color_v = Fore.RED
    elif -0.1 > volume_percent >= -0.25:
        v_code = "-"
        color_v = Fore.RED
    elif -0.25 > volume_percent >= -0.5:
        v_code = "--"
        color_v = Fore.RED
    elif volume_percent < -0.5:
        v_code = "---"
        color_v = Fore.RED

    if var > 0:
        color = Fore.GREEN
    if var < 0:
        color = Fore.RED
    if var == 0:
        color = Fore.WHITE

    print(Style.RESET_ALL
        +"PRICE:"
        + Style.BRIGHT
        + f" {price} {div}\t\t"
        + color
        + f"[{i}{var}] [{i}{percent}%]"
        + Style.RESET_ALL
        + Fore.RESET
        + "\t Volume:"
        + Style.BRIGHT
        + f" {volume}"
        + Style.RESET_ALL
        + " ["
        + color_v
        + f"{v_code}"
        + Fore.RESET
        + "]"
    )
    print(Style.DIM + f"Day high: {max_day}{div}\t Day Low:{min_day}{div}")
    print(
        f"Previous session: {past_price} {div}\t\t\t\t Average Volume: {average_volume}"
    )
    print("-"*80+Style.RESET_ALL)

def show_info_company(info_dict):
    summary = info_dict["longBusinessSummary"]
    print(Style.RESET_ALL+Style.DIM+summary)
    print("-"*80+Style.RESET_ALL)
    
def show_news(news):
    try:
        for new in news:
            date = datetime.fromtimestamp(new["providerPublishTime"])
            date_format = datetime.strftime(date, "%d / %b / %Y")
           
            print(Style.RESET_ALL+Style.DIM+
                "NEWS:\t" + Style.NORMAL + f"{new['title'].upper()}" + Style.RESET_ALL
            )
            print(Style.DIM+"LINK:\t"+Style.NORMAL+f"{new['link']}")
            print(Style.DIM+"DATE:\t"+Style.NORMAL+f"{date_format}\n")
    except:
        print(f"No NEWS for:{news}")
