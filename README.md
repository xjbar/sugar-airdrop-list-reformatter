# sugar-airdrop-list-reformatter
*Reformats your holders list json to work with sugar airdrop from metaplex.*

## PREREQUISITES:
- python 3

## WHAT IS SUGAR

Sugar airdrop is a tool from the sugar program from metaplex that allows you to mint nfts directly to a list of public wallet addresses. It also allows you to choose the amount of NFTs each public wallet address gets.

## WHATS THE PROBLEM?

Your airdrop list needs to be in a specific json format for the program to run correctly.

## HOW TO DO THIS

**1.** Get the mint hash list of all the nfts you want to airdrop to the owners of. Use this tool to get this list. (https://magiceden.io/mintlist-tool)

**2.** Copy the mint hash list and paste it into this site. (https://cryptostraps.tools/holder-snapshot)

*It will take awhile to download it all. Once its done it will output a json file of all of the holders for you. This is cool but the format wont work with sugar airdrop tool.*

**3.** Move the file to the same directory as your `cache.json` from your ongoing sugar mint. Rename your newly downloaded file to `airdrop_list.json`

**4.** Download the `sugar_airdrop_reformatter.py` and move it to the same directory as the `cache.json` and `airdrop_list.json` file.

**5.** Double click the `sugar_airdrop_reformatter.py`, it will briefly open a CLI window and then automatically close. 

*If you open and check your `airdrop_list.json` file now you will see that its properly formatted for the sugar airdrop tool.*

**6.** Now in the CLI run `sugar airdrop --airdrop-list airdrop_list.json`

**7.** It will mint to all the addresses from the `airdrop_list.json` file

Message xjbar#3020 on discord or @xjbarnft on twitter if you have questions.
