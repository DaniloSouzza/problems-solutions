/* 
    [03-2021]
    A simple function inspired by the problem that I found on CodeSignal website. The function proceeds with 
    some commons bank transactions (deposit, withdraw and transfer) for account balances inserted into the 
    'balances' args.

    The 'chatbot' will interpret a command line and proceed with each operation. Some things could be better
    like a function to handle errors or a withdraw function and deposit function being recalled for the transfers
    but the intention was to make the flow clear for beginners :)
   
    Hope you enjoy it,
   
    Dan
*/

function bankTransaction(balances, requests){
	for(let i = 0; i < requests.length;i ++){
  	    transaction = requests[i].split(" ");
		switch(transaction[0]){
			case "withdraw":
				if(transaction[1] - 1 < balances.length){
					withdrawAmount = parseInt(transaction[2]);
					balances[transaction[1] - 1] -= withdrawAmount;
				}else{
					console.log("Error on transaction " + (i+1) + ", please check your accounts and try again");
				}
				break;

			case "transfer":
				if(transaction[1] - 1 < balances.length && transaction[2] - 1 < balances.length){
					transferAmount = parseInt(transaction[3]);
					balances[transaction[1] - 1] -= parseInt(transferAmount);
					balances[transaction[2] - 1] +=parseInt(transferAmount);
				}else{
					console.log("Error on transaction " + (i+1) + ", please check your accounts and try again");
				}
				break;

			case "deposit":
				if(transaction[1] - 1 < balances.length){
					depositAmount = parseInt(transaction[2]);
					balances[transaction[1] - 1] += depositAmount;
				}else{
					console.log("Error on transaction " + (i+1) + ", please check your accounts and try again");
				}
				break;
			default:
				console.log("Error on transaction " + (i+1) + ".You only can withdraw, transfer or deposit.");
				break;
		}
	console.log(balances);
	}
}

/* Example of use */
bankTransaction([100,25,66,89,1000], ["donate 5 2 1500","deposit 6 500","withdraw 3 1500"]);
