# sugar-airdrop-list-reformatter
reformats your holders list json to work with sugar airdrop from metaplex.

sugar airdrop is a tool from the sugar program from metaplex that allows you to mint nfts directly to a list of public wallet addresses. it also allows you to choose the amount each public wallet address gets.

it requires a specific json format for the program to run correctly. if you are pulling a lot of public wallet addresses, it would be annoying to format it all manually so this guide will save you time.

**Step 1.** Get the mint hash list of all the nfts you want to airdrop to the owners of. I use Magic Edens Hash List tool found under their creator portal. Most mint hash list tools just require you to input the first creator address of the nft collection.

**Step 2.** Copy the mint hash list and paste it into this site.
https://cryptostraps.tools/holder-snapshot

It will take awhile to download it all. onces its done it will output a json file of all of the holders for you. this is cool but the format wont work with sugar airdrop tool.

**Step 3.** Move the file to the same directory as your 'cache.json' from your ongoing sugar mint. Rename your newly downloaded file to 'airdrop_list.json'

**Step 4.** Take the script i made and move it to the same directory as the 'cache.json' and 'airdrop_list.json' file.

**Step 5.** Double click the script file, it will briefly open a CLI window and then automatically close. If you check your 'airdrop_list.json' file now you will see that its properly formatted for the sugar airdrop tool.

**Step 6.** Now in the CLI run 'sugar airdrop --airdrop-list airdrop_list.json'

**Step 7.** It will mint to all the addresses from the 'airdrop_list.json' file

*Thats it! The script can be modified to do alot more functions and be more modular but this is the most basic way for me to do it so anyone can follow the steps.

Message xjbar#3020 on discord or @xjbarnft on twitter if you have questions.
