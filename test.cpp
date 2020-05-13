#include <iostream>
#include <cmath>
#include <iomanip>
#include <string>
#include <iterator>
#include <cctype>
#include <algorithm>

using namespace std;

const int TAX_RATE1 = 25;
const int TAX_RATE2 = 50;
string income;
float inc;
float interest, deduction, paid_tax, tax_amount, final_amount, due, refund;
bool isDue = false, isRefund = false;

bool validate_input(string str) {
		if (str.end() != find_if_not(str.begin(), str.end(), ::isdigit)) {
			return false;
		}
		else if (str.empty())
			return false;
		else
			return true;
}

void getTaxInfo() {
    cout << "Lets gather some information on your finances this year.\n";
    while(true) {
        cout << "Please enter the amount from W2 form: ";
		getline(cin, income);
		while (!validate_input(income)){
			cout << "Please enter the amount from W2 form: ";
			getline(cin, income);
		}
		if (income.empty())
			continue;
		//inc = atoi(income.c_str());
		inc = stof(income);
        if (inc < 0) {
            cout << "Invalid amount. Income cannot be negative.\n";
            continue;
        }
        else
            break;
    }

    while(true) {
        cout << "Please enter the Interest income: ";
        cin >> interest;
        if (interest < 0) {
            cout << "Invalid amount. Interest income cannot be negative.\n";
            continue;
        }
        else
            break;
    }

    while(true){
        cout << "Please enter the Paid tax amount: ";
        cin >> paid_tax;
        if (paid_tax > inc) {
            cout << "Invalid amount. Paid tax cannot be greater than your total income.\n";
            continue;
        }
        else if (paid_tax < 0){
            cout << "Invalid amount. Paid tax cannot be negative.\n";
            continue;
        }
        else
            break;
    }

    while(true){
        cout << "Please enter the amount for deduction: ";
        cin >> deduction;
        if (deduction < 0) {
            cout << "Invalid amount. Deduction cannot be negative.\n";
            continue;
        }
        else
            break;
    }
}

void calcTax(float TAX_RATE) {
    tax_amount = (inc + interest - deduction) * TAX_RATE/100;
    final_amount = (tax_amount - paid_tax);
    if (final_amount < 0) {
        due = fabs(final_amount);
        isDue = true;
     }
    else {
        refund = final_amount;
        isRefund = true;
    }
}

void taxResult() {
    cout << "Tax Report\n";
    cout << "------------------------\n";
    cout << "Income: $" << fixed << setprecision(2) << inc << endl;
    cout << "Interest: $" << fixed << setprecision(2) << interest << endl;
    cout << "Deduction: $" << fixed << setprecision(2) << deduction << endl;
    cout << "Paid Tax: $" << fixed << setprecision(2) << paid_tax << endl;
    cout << "Tax Amount: $" << fixed << setprecision(2) << tax_amount << endl;
    cout << "------------------------\n";
    if (isDue)
        cout << "Due: $" << fixed << setprecision(2) << due << endl;
    else if (isRefund)
        cout << "Refund: $" << fixed << setprecision(2) << refund << endl;
}

void processTax() {
    char tax_again;
    while(true){
        getTaxInfo();
        if (inc <= 10000)
            calcTax(TAX_RATE1);
        else
            calcTax(TAX_RATE2);
        taxResult();
        cout << "Do you want to calculate tax for another income (y/n)?";
        cin >> tax_again;
        cout << endl;
        if (tax_again == 'y' or tax_again == 'Y'){
            continue;
        }
        else if (tax_again == 'n' or tax_again == 'N'){
            break;
        }
        else {
            cout << "Not a valid input, please try again";
            continue;
        }
    }
}
int main(){
    int pin;
    const int MAX_ATTEMPTS = 3;
    int attempts_left = MAX_ATTEMPTS;

    cout << "Welcome to my tax calculation program.\n";
    cout << "-------------------------------------- \n";
	processTax();
	cout << "Thank you for using my program.";
	return 0;
}
