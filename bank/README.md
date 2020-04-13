# Extra Careful Bank

In this challenge, we're given a service `nc crypto.bytebandit.it 7003`

the service at first gives you the choice of making 10 transaction, by choosing `amount`, and the `receiver_id`, after making 10 transaction and spending all your money, the service gives you these choices:
```
2. See today's transactions(encrypted)
3. See special transaction(encrypted)
4. Provide encrypted transactions.
5. Get flag.
```

* `today's transactions` shows you 20 encrypted transaction inluding the 10 you made
* `special transaction` shows you an encrypted transaction with the `amount` of `500$`
* `Provide encrypted transactions` gives you the change of making 3 transactions if the ciphertext is valid, when i submitted a wrong ciphertext(1 character), it said the following:
```
Invalid Length
Transaction Format:
sender account number(16 bytes)+receiver account number(16 bytes)+amount(prepended appropraitely to 16 bytes)
'+' represents concatenation
```
and i also noticed that all my 10 transactions have the same ciphertexts, and if i change the `receiver_id`, only the middle `16 bytes` change, which means we're dealing with an `ECB cut and paste` attack.

simply grab the `receiver bytes` and the `amount bytes` from the special transaction and the transactions that you didn't make, and forge transactions where you are the `receiver` i.e grabbing the `sender_bytes` from the transactions you made, you can easily differenciate them from the other ones by making 10 identical transaction, so the transactions will have this pattern:
```
sender_bytes_from_your_transaction + receiver_bytes_from_other_transaction +  amounts_bytes_from_other_transaction
```

```
flag{bank$_sh0uld_n07_us3_ECB}
```