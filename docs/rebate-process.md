# Rebating Transaction Costs

Rebating a transaction is determined by:

- Is the function that is called in the transaction eligible?

  - By tracking contract function calls we are better able to provide
    observability in the rebating process, we can also coordinate with teams
    wishing to provide more incentives for specific actions and behaviors

- If yes, what is the percentage that can be rebated?

  - This percentage value is a protocol value that can be adjusted

- What is the transaction cost for the eligible transaction?

  - Thi s the value that the end user utilized in submitting their transaction.

- Calculate the Gas Reporting Index value

  - This uses the gas pricing information from api.txprice.com to calculate the
    gas pricing information to be used in calculating the rebate amount for your
    transaction

- Calculate the rebate amount from the bundle profit surplus
  - We take how much profit the arbitrage made and split it among all eligible
    trades within that bundle

## Rebate Mechanism

1. Eligible transactions are rebated based on the 80th confidence interval for
   gas estimation pricing.

2. This is proportionally distributed based on transactional weight. _Note: a
   naive formula would consider pairings, then slippage tolerance and finally
   transactional amount_

3. The amount of compensation is the remainderless fees to miners and network
   operational transactional costs.

4. Compensation payouts occur no later than a half hour

## Rebate Calculations

_Note_: naive implementation, expect changes

bundleCost = mev bribe + bundleTxs[1,2,...]

gasAllowance = mev bribe - bundleTxs[1,2,...]

BundleTransactionGas[1,2,...] = Individual Gas Cost

BundleId = The Block Number (or hash?) in which the bundle was included

max_gasRebate = (BundleId(BundleTransactionGas[1,2,...]))

```json
{
  "confidence": 80,
  "price": 150,
  "maxPriorityFeePerGas": 1.75,
  "maxFeePerGas": 100
}
```

## Transactions

Type0 and Type2 Transactions

Type0 transactions (Pre EIP-1559) should utilize the Price number under each
confidence level.

Type2 transactions (EIP-1559) should utilize the values for maxPriorityFeePerGas
(also known as the "tip") and maxFeePerGas .

## List of Transactions by Contract Function

*Note*: Function calls listed at 0 are not eligible at this time, however we fully plan on expanding coverage to additional functions in the future

|                    **$function_calls**                    | **%eligible** |
| :-------------------------------------------------------: | :-----------: |
|                 swapExactTokensForTokens                  |      100      |
|                   swapExactTokensForETH                   |      100      |
|                   swapExactETHForTokens                   |      100      |
|                   swapETHForExactTokens                   |      100      |
|                       getAmountsOut                       |      0        |
|                      addLiquidityETH                      |      0        |
|                       addLiquidity                        |      0        |
|                 swapTokensForExactTokens                  |      100      |
|                       getAmountOut                        |      0        |
|               removeLiquidityETHWithPermit                |      100      |
|                   swapTokensForExactETH                   |      100      |
|                 removeLiquidityWithPermit                 |      0        |
|                    removeLiquidityETH                     |      0        |
|                      removeLiquidity                      |      0        |
|                          factory                          |      0        |
|    swapExactTokensForETHSupportingFeeOnTransferTokens     |      0        |
|   swapExactTokensForTokensSupportingFeeOnTransferTokens   |      0        |
|                       getAmountsIn                        |      0        |
|                           WETH                            |      0        |
|    swapExactETHForTokensSupportingFeeOnTransferTokens     |      0        |
|                        getAmountIn                        |      0        |
| removeLiquidityETHWithPermitSupportingFeeOnTransferTokens |      0        |
|      removeLiquidityETHSupportingFeeOnTransferTokens      |      0        |



### Transaction Pricing

**maxPrice** Highest priced transaction in the mempool

**currentBlockNumber** Block number at the time of prediction

**msSinceLastBlock** Milliseconds since the last block was mined relative to
when data was computed

**blockNumber** Block this prediction is for

**baseFeePerGas** Base fee per gas for current block in gwei. (Only type2
transactions Post EIP-1559 have this value and it's burned by the network upon
transaction success). estimatedTransactionCount Number of items we estimate will
be included in next block based on mempool snapshot

**confidence** 0-99 likelihood the next block will contain a transaction with a
gas price >= to the listed price

**Price** Price in Gwei (used for type0 transactions: Pre EIP-1559)

**maxPriorityFeePerGas** Max priority fee per gas in gwei also known as the
"tip" (used for type2 transactions: EIP-1559)

**maxFeePerGas** Max fee per gas in gwei (used for type2 transactions:
EIP-1559). Our current max fee heuristic is Base Fee \* 2 + Priority Fee. This
is to protect against a 'rapid' rise in the base fee while your transaction fee
is pending. In most cases, the actual transaction fee will approximate Base
Fee + Priority Fee.
