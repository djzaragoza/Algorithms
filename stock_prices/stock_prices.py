#!/usr/bin/python

import argparse

def find_max_profit(prices):
      profit prices[1] - prices[0]
      for i in range(0, len(prices)):
            lowest_value = prices[i]
            for j in range(i+1, len(prices)):
                    if prices[j] - lowest_value > profit:
                          profit = prices[j] - lowest_value
      return profit


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(
    description='Find max profit from pricecs.')
  parser.add_argument('integers', metavar='N', type=int,
                      nargs='+', help=an integer price')
  args = parser.parse_args()
  
  print("A profit of ${profit} can be made from the stock prices {prices}.".format(
    profit=find_max_profit(args.integers), prices=args.integers))
