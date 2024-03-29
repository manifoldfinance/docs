# Comparison to other MEV solutions


!!! warning

  This is for informational purposes only and may be incomplete


## Comparison

|         **Name**          |  **OpenMEV**   |   **Flashbots**   | **EdenNetwork** |   **Mist X**   |  **CowSwap**   |
| :-----------------------: | :------------: | :---------------: | :-------------: | :------------: | :------------: |
|       **Category**        |   Aggregator   |     Platform      |    Platform     |      AMM       |      AMM       |
|     **Direct Relay**      |      Yes       |        Yes        |       Yes       | Uses Flashbots | Uses Flashbots |
|     **Custom Client**     |                |                   |                 |                |                |
|      \- Go Ethereum       | uses Flashbots |     MEV Geth      | uses Flashbots  |       No       |       No       |
|       \- Nethermind       | uses Flashbots | Nethermind Plugin | uses Flashbots  |       No       |       No       |
|         \- Erigon         |      N/A       |        N/A        |       N/A       |      N/A       |      N/A       |
|          \- Besu          |       No       |        No         |       No        |      N/A       |      N/A       |
| External Searcher support |      Yes       |        Yes        |       Yes       |    Partial     |    Partial     |
|          **API**          |                |                   |                 |                |                |
|        \- API Spec        |      Yes       |        No         |       No        |       No       |       No       |
|        \- JSON RPC        |      Yes       |        Yes        |       Yes       |       No       |       No       |
|         \- HTTP/S         |      Yes       |        Yes        |       Yes       |      Yes       |      Yes       |
|       \- Websocket        |      Yes       |        No         |       No        |                |                |
|    \-MQ \(Kafka, etc\)    |      Yes       |        No         |       No        |       No       |       No       |
| Direct Miner Integrations |      Yes       |        Yes        |       Yes       |       No       |       No       |
|    **Infrastructure**     |                |                   |                 |                |                |
|          \- AWS           |    Partial     |        Yes        |       Yes       |       No       |       No       |
|      \- Google Cloud      |       No       |        No         |       No        |       No       |       No       |
| \-Bare Metal \(OVH, etc\) |      Yes       |        No         |       No        |       \-       |       \-       |
|  \-PaaS \(Heroku, etc\)   |       No       |        No         |       No        |      Yes       |       \-       |
|          **SDK**          |      Yes       |      Partial      |     Partial     |      Yes       |       \-       |
