#include <iostream>

using namespace std;

int main()
{
	int num;
	cout << "Enter Number" << endl;
	cin >> num;
	int mul = 1;

	for (int i = 0; i < num; ++i) {
		for (int j = i + 1; j >= i + 2; j++) {
			cout << j * mul << " " ;
			mul++;
		}
		cout << "\n";
	}
	return 0;
}
