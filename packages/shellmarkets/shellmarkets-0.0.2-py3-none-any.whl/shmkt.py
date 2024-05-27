from click import command, argument, option, Path, echo
from os import path
from yfinance import Ticker
from modules.views import *

VERSION = "SHELLMARKETS v0.0.2 - by Croketillo\n"

@command()
@argument('tickers', nargs=-1, required=False)
@option('-e', '--extended', is_flag=True, help='Extended info for ticker.')
@option('-i', '--info', is_flag=True, help='Info about company')
@option('-n', '--news', is_flag=True, help='News about company')
@option('-p', '--portfolio', type=Path(exists=True), help='Show portfolio tickers.')
@option('-c', '--create-portfolio', type=Path(), help='Create a new portfolio file with provided tickers. Usage: -c <portfolio_file> <ticker_optional_list>')
@option('-a', '--add-ticker', nargs=2, type=str, help='Add a ticker to the specified portfolio file. Usage: -a <ticker> <portfolio_file>')
@option('-d', '--delete-ticker', nargs=2, type=str, help='Delete a ticker from the specified portfolio file. Usage: -d <ticker> <portfolio_file>')
@option('-v', '--version', is_flag=True, help='Show shellmarkets version')
def main(tickers, extended, info, news, portfolio, create_portfolio, add_ticker, delete_ticker, version):
    if version:
        echo(VERSION)
        return

    if create_portfolio:
        create_portfolio_file(create_portfolio, tickers)
        return

    if add_ticker:
        add_ticker_to_portfolio(*add_ticker)
        return

    if delete_ticker:
        delete_ticker_from_portfolio(*delete_ticker)
        return

    if portfolio:
        tickers_from_file = read_tickers_from_config(portfolio)
        tickers = list(tickers) + tickers_from_file

    if not tickers:
        echo("[❌] Error: Tickers are required. (--help for more information)")
        return

    if extended or info or news:
        for ticker in tickers:
            try:
                info_dict = Ticker(ticker).info
                show_header(info_dict)
                if extended:
                    show_extended(info_dict)
                if info:
                    show_info_company(info_dict)
                if news:
                    show_news(Ticker(ticker).news)
            except Exception:
                echo(f'❌ [{ticker}]\t - Ticker no válido.')
                echo("-" * 48)
    else:
        get_info(tickers)


def read_tickers_from_config(config_file):
    if not path.exists(config_file):
        echo(f"[❌] Portfolio file '{config_file}' does not exist. You need to create it first.")
        return []
    with open(config_file, 'r') as file:
        return file.read().splitlines()


def create_portfolio_file(file_path, tickers):
    with open(file_path, 'w') as file:
        file.write('\n'.join(tickers) + '\n')
    echo(f"[✅] Portfolio file '{file_path}' created with tickers: {', '.join(tickers)}")


def add_ticker_to_portfolio(ticker, portfolio_file):
    if not path.exists(portfolio_file):
        echo(f"[❌] Portfolio file '{portfolio_file}' does not exist. You need to create it first.")
        return
    tickers = read_tickers_from_config(portfolio_file)
    if ticker not in tickers:
        with open(portfolio_file, 'a') as file:
            file.write(ticker + '\n')
        echo(f"[✅] Ticker '{ticker}' added to the portfolio file '{portfolio_file}'")
    else:
        echo(f"[✅] Ticker '{ticker}' is already in the portfolio file '{portfolio_file}'")


def delete_ticker_from_portfolio(ticker, portfolio_file):
    tickers = read_tickers_from_config(portfolio_file)
    if ticker in tickers:
        tickers.remove(ticker)
        with open(portfolio_file, 'w') as file:
            file.write('\n'.join(tickers) + '\n')
        echo(f"[✅] Ticker '{ticker}' deleted from the portfolio file '{portfolio_file}'")
    else:
        echo(f"[❌] Ticker '{ticker}' not found in the portfolio file '{portfolio_file}'")


def get_info(tickers):
    for ticker in tickers:
        try:
            info_dict = Ticker(ticker).info
            show_price(info_dict)
        except Exception:
            echo(f'❌ [{ticker}]\t - Ticker no válido.')
            echo("-" * 48)


if __name__ == "__main__":
    main()
