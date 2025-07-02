/*
BOJ22937 - Professor, calculator is wrong! (https://www.acmicpc.net/problem/22937)

Multiply two decimal numbers with 9 digits.
*/

// TIME COMPLEXITY : O(1)

#include <iostream>
#include <iomanip>
#include <string>

using namespace std;

int main() {

    ios::sync_with_stdio(false);
    cin.tie(NULL);


    // 1. TO GET THE INPUT

    int test_count;
    cin >> test_count;

    for (int test_num = 0; test_num < test_count; test_num++) {
        
        string A, B;
        cin >> A >> B;
        

        // 2. PARSING
        
        bool A_minus, B_minus;
        int A_digits[10], B_digits[10];

        if (A.length() == 11) {
            A_minus = false;
            A_digits[0] = (int) A[0] - 48;
            for (int idx = 2; idx < 11; idx++) {
                A_digits[idx - 1] = (int) A[idx] - 48;
            }
        } else {
            A_minus = true;
            A_digits[0] = (int) A[1] - 48;
            for (int idx = 3; idx < 12; idx++) {
                A_digits[idx - 2] = (int) A[idx] - 48;
            }
        }

        if (B.length() == 11) {
            B_minus = false;
            B_digits[0] = (int) B[0] - 48;
            for (int idx = 2; idx < 11; idx++) {
                B_digits[idx - 1] = (int) B[idx] - 48;
            }
        } else {
            B_minus = true;
            B_digits[0] = (int) B[1] - 48;
            for (int idx = 3; idx < 12; idx++) {
                B_digits[idx - 2] = (int) B[idx] - 48;
            }
        }


        // 3. MULTIPLICATION

        int result[19] = {};

        for (int i = 0; i < 10; i++) {
            for (int j = 0; j < 10; j++) {
                result[i + j] += A_digits[i] * B_digits[j];
            }
        }

        for (int idx = 18; 0 < idx; idx--) {
            if (result[idx] >= 10) {
                result[idx - 1] += result[idx] / 10;
                result[idx] = result[idx] % 10;
            }
        }
        
        
        // 4. TO SOLVE THE PROBLEM
        
        for (int i = 0; i < 19; i++) {
            if (i == 0) {
                if ((A_minus && B_minus) || (!A_minus && !B_minus)) {
                    cout << result[i] << ".";
                } else {
                    cout << "-" << result[i] << ".";
                }
            } else if (i == 18) {
                cout << result[i] << "\n";
            } else {
                cout << result[i];
            }
        }
    }

    return 0;

}