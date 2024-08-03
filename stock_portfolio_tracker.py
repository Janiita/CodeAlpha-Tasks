import yfinance as yf

class StockPortfolio:
    def __init__(self):
        self.portfolio = {}

    def add_stock(self, symbol, shares):
        if symbol in self.portfolio:
            self.portfolio[symbol]['shares'] += shares
        else:
            self.portfolio[symbol] = {'shares': shares, 'cost_basis': 0.0}
        print(f"Added {shares} shares of {symbol} to the portfolio.")

    def remove_stock(self, symbol, shares):
        if symbol in self.portfolio and self.portfolio[symbol]['shares'] >= shares:
            self.portfolio[symbol]['shares'] -= shares
            if self.portfolio[symbol]['shares'] == 0:
                del self.portfolio[symbol]
            print(f"Removed {shares} shares of {symbol} from the portfolio.")
        else:
            print(f"Unable to remove {shares} shares of {symbol}. Check if you have enough shares.")

    def update_cost_basis(self, symbol, cost_basis):
        if symbol in self.portfolio:
            self.portfolio[symbol]['cost_basis'] = cost_basis
            print(f"Updated cost basis of {symbol} to {cost_basis}.")
        else:
            print(f"{symbol} is not in the portfolio.")

    def get_stock_data(self, symbol):
        stock = yf.Ticker(symbol)
        return stock.history(period='1d')['Close'].iloc[-1]

    def get_portfolio_value(self):
        total_value = 0.0
        for symbol in self.portfolio:
            current_price = self.get_stock_data(symbol)
            total_value += current_price * self.portfolio[symbol]['shares']
        return total_value

    def display_portfolio(self):
        print("\nCurrent Portfolio:")
        for symbol in self.portfolio:
            shares = self.portfolio[symbol]['shares']
            cost_basis = self.portfolio[symbol]['cost_basis']
            current_price = self.get_stock_data(symbol)
            current_value = current_price * shares
            print(f"{symbol}: {shares} shares, Cost Basis: ${cost_basis:.2f}, Current Price: ${current_price:.2f}, Current Value: ${current_value:.2f}")
        total_value = self.get_portfolio_value()
        print(f"\nTotal Portfolio Value: ${total_value:.2f}\n")


if __name__ == "__main__":
    portfolio = StockPortfolio()

    while True:
        print("Stock Portfolio Tracker")
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. Update Cost Basis")
        print("4. Display Portfolio")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            symbol = input("Enter stock symbol: ").upper()
            shares = int(input("Enter number of shares: "))
            portfolio.add_stock(symbol, shares)
        elif choice == '2':
            symbol = input("Enter stock symbol: ").upper()
            shares = int(input("Enter number of shares to remove: "))
            portfolio.remove_stock(symbol, shares)
        elif choice == '3':
            symbol = input("Enter stock symbol: ").upper()
            cost_basis = float(input("Enter cost basis per share: "))
            portfolio.update_cost_basis(symbol, cost_basis)
        elif choice == '4':
            portfolio.display_portfolio()
        elif choice == '5':
            print("Exiting the tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
